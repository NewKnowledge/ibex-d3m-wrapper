import os
import sys
import typing
from json import loads
import numpy as np
import pandas as pd

from ibex import *

from d3m.primitive_interfaces.base import PrimitiveBase, CallResult

from d3m import container, utils
from d3m.metadata import hyperparams, base as metadata_base, params

__author__ = 'Distil'
__version__ = '1.0.0'

Inputs = container.pandas.DataFrame
Outputs = container.pandas.DataFrame


class Params(params.Params):
    pass


class Hyperparams(hyperparams.Hyperparams):
    target_columns = hyperparams.Set(
        elements=hyperparams.Hyperparameter[str](''),
        default=(),
        max_size=sys.maxsize,
        min_size=0,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description='names of columns with input text values'
    )

    output_labels = hyperparams.Set(
        elements=hyperparams.Hyperparameter[str](''),
        default=(),
        max_size=sys.maxsize,
        min_size=0,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description='names of columns with output sets of named entities'
    )


class ibex(PrimitiveBase[Inputs, Outputs, Params, Hyperparams]):
    """
    This D3M wrapper invokes the d3m_ibex primitive, which calls the spaCy named entity recognition tool 
    (https://spacy.io/usage/linguistic-features). Given a set of input text documents, the wrapper will 
    return a list of the named entities detected. A key weakness of spaCy's NER is that it might not 
    recognize proper nouns that are not properly capitalized.

    Parameters
    ----------
    inputs : pandas dataframe where a column is a pd.Series of text documents

    Returns
    -------
    output : A dataframe with the sets of named entities extracted from the columns of the input dataframe.

    """
    metadata = metadata_base.PrimitiveMetadata({
        # Simply an UUID generated once and fixed forever. Generated using "uuid.uuid4()".
        'id': 'd822d93e-60fa-4634-983b-99a3ad852999',
        'version': __version__,
        'name': "ibex",
        # Keywords do not have a controlled vocabulary. Authors can put here whatever they find suitable.
        'keywords': ['entity extraction'],
        'source': {
            'name': __author__,
            'uris': [
                # Unstructured URIs.
                "https://github.com/NewKnowledge/ibex-d3m-wrapper",
            ],
        },
        # A list of dependencies in order. These can be Python packages, system packages, or Docker images.
        # Of course Python packages can also have their own dependencies, but sometimes it is necessary to
        # install a Python package first to be even able to run setup.py of another package. Or you have
        # a dependency which is not on PyPi.
        "installation": [
              {
                  "type": "PIP",
                  "package_uri": "git+https://github.com/NewKnowledge/d3m_ibex@7519b2a0ae7220fc04aa616cd65c4592d3ea8b2f#egg=d3m_ibex-1.0.0"
              },
              {
                  "type": "PIP",
                  "package_uri": "git+https://github.com/NewKnowledge/ibex-d3m-wrapper.git@{git_commit}#egg=IBEXd3mWrapper".format(
                        git_commit=utils.current_git_commit(os.path.dirname(__file__))
                        ),
              }
        ],
        # The same path the primitive is registered with entry points in setup.py.
        'python_path': 'd3m.primitives.feature_extraction.ibex.Ibex',
        # Choose these from a controlled vocabulary in the schema. If anything is missing which would
        # best describe the primitive, make a merge request.
        "algorithm_types": [
            metadata_base.PrimitiveAlgorithmType.DATA_CONVERSION
            ],
        'primitive_family': metadata_base.PrimitiveFamily.FEATURE_EXTRACTION,
    })

    def __init__(self, *, hyperparams: Hyperparams)-> None:
        super().__init__(hyperparams=hyperparams)

    def fit(self) -> None:
        pass

    def get_params(self) -> Params:
        return self._params

    def set_params(self, *, params: Params) -> None:
        self.params = params

    def set_training_data(self, *, inputs: Inputs, outputs: Outputs) -> None:
        pass

    def produce(self, *, inputs: Inputs) -> CallResult[Outputs]:
        """

        Parameters
        ----------
        inputs : pandas dataframe where a column is a pd.Series of text documents

        Returns
        -------
        output : A dataframe with the sets of named entities extracted from the columns of the input dataframe.

        """

        target_columns = self.hyperparams['target_columns']
        output_labels = self.hyperparams['output_labels']

        input_df = inputs

        for i, ith_column in enumerate(target_columns):
            # initialize an empty dataframe
            result_df = pd.DataFrame()
            output_label = output_labels[i]

            for doc in input_df.loc[:, ith_column]:
                jth_result = get_entities(doc)

                result_df = result_df.append(
                    {
                        output_label + 'entities': jth_result
                    },
                    ignore_index=True)

            output_df = pd.concat(
                [input_df.reset_index(drop=True), result_df], axis=1)

        return output_df


if __name__ == '__main__':
    client = ibex(hyperparams={'target_columns': ['test_column'], 'output_labels': ['test_column_prefix_']})

    text = ['The Trump administration struggled on Monday to defend its policy of separating parents from their sons and daughters at the southern US border amid growing national outrage and the release of of sobbing children.']

    input_df = pd.DataFrame(pd.Series([text, text]))
    input_df.columns = ['test_column']
    result = client.produce(inputs=input_df)
    print(result.head)
