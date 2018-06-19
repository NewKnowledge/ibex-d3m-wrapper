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
        description='names of columns with image paths'
    )

    output_labels = hyperparams.Set(
        elements=hyperparams.Hyperparameter[str](''),
        default=(),
        max_size=sys.maxsize,
        min_size=0,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description='desired names for croc output columns'
    )


class ibex(PrimitiveBase[Inputs, Outputs, Params, Hyperparams]):
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
                  "package_uri": "git+https://github.com/NewKnowledge/ibex.git@13e0f36cc3acb2a3f405f63a6cf1b398fc36bbee#egg=ibex"
              },
              {
                  "type": "PIP",
                  "package_uri": "git+https://github.com/NewKnowledge/ibex-d3m-wrapper.git@{git_commit}#egg=IBEXd3mWrapper".format(
                        git_commit=utils.current_git_commit(os.path.dirname(__file__))
                        ),
              }
        ],
        # The same path the primitive is registered with entry points in setup.py.
        'python_path': 'd3m.primitives.distil.ibex',
        # Choose these from a controlled vocabulary in the schema. If anything is missing which would
        # best describe the primitive, make a merge request.
        "algorithm_types": [
            metadata_base.PrimitiveAlgorithmType.DATA_CONVERSION
            ],
        "primitive_family": metadata_base.PrimitiveFamily.DATA_TRANSFORMATION
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
            Produce image object classification predictions and OCR for an
            image provided as an URI or filepath

        Parameters
        ----------
        inputs : pandas dataframe where a column is a pd.Series of image paths/URLs

        Returns
        -------
        output : A dataframe with objects, text and tokens, corresponding to the
            detected objects, raw text and tokens predicted to be in the 
            supplied images.
        """

        target_columns = self.hyperparams['target_columns']
        output_labels = self.hyperparams['output_labels']

        input_df = inputs

        for i, ith_column in enumerate(target_columns):
            # initialize an empty dataframe
            result_df = pd.DataFrame()
            output_label = output_labels[i]

            for doc in input_df.loc[:, ith_column]:
                jth_result = get_entities()

                result_df = result_df.append(
                    {
                        output_label + 'entities': jth_result
                    },
                    ignore_index=True)

            output_df = pd.concat(
                [input_df.reset_index(drop=True), result_df], axis=1)

        return output_df


if __name__ == '__main__':
    client = ibex(hyperparams={'target_columns': ['test_column'], 'output_labels': ['test_column_prefix']})

    text = ['Homeland security secretary claims administration is simply enforcing the law as photos and audio of children fuel anger']

    input_df = pd.DataFrame(pd.Series([text, text]))
    imagepath_df.columns = ['test_column']
    result = client.produce(inputs=input_df)
    print(result.head)
