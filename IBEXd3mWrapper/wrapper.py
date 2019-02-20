import os
import sys
import typing
from json import loads
import numpy as np
import pandas as pd

from d3m_ibex import Ibex

from d3m.primitive_interfaces.base import PrimitiveBase, CallResult

from d3m import container, utils
from d3m.metadata import hyperparams, base as metadata_base, params

__author__ = 'Distil'
__version__ = '1.1.0'
__contact__ = 'mailto:nklabs@newknowledge.io'

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
    language = hyperparams.Enumeration(default = 'english', 
        semantic_types = ['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        values = ['english','spanish'],
        description = 'language to use for the spacy model')
    
    output_labels = hyperparams.Set(
        elements=hyperparams.Hyperparameter[str](''),
        default=(),
        max_size=sys.maxsize,
        min_size=0,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description='names of columns with output sets of named entities'
    )


class d3m_Ibex(PrimitiveBase[Inputs, Outputs, Params, Hyperparams]):
    """
    This D3M wrapper invokes the d3m_ibex primitive, which calls the spaCy named entity recognition tool 
    (https://spacy.io/usage/linguistic-features). Given a set of input text documents, the wrapper will 
    return a list of the named entities detected. A key weakness of spaCy's NER is that it might not 
    recognize proper nouns that are not properly capitalized.

    Parameters
    ----------
    inputs : pandas dataframe where a column is a pd.Series of text documents

    hyperparams:
        target_columns: names of columns with input text values
        output_labels: names of columns with output sets of named entities
        language: language to use for the spacy model ('english' or 'spanish')

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
            'contact': __contact__,
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
                  "package_uri": "git+https://github.com/NewKnowledge/d3m_ibex@96d5122d771a4506454f50106b400984977b894b#egg=d3m_ibex-1.1.1"
              },
              {
                  "type": "PIP",
                  "package_uri": "git+https://github.com/NewKnowledge/ibex-d3m-wrapper.git@{git_commit}#egg=IBEXd3mWrapper".format(
                        git_commit=utils.current_git_commit(os.path.dirname(__file__))
                        ),
              },
              {
                "type": "TGZ",
                "key": "english_spacy_parser",
                "file_uri": "http://public.datadrivendiscovery.org/en_core_web_md-2.1.0a7.tar.gz",
                "file_digest":"f54a6e6a2ff34c1adb1a2eabeb67b170933453ed878125c76813dc2e31c8cf8a"
              }, 
              {
                "type": "TGZ",
                "key": "spanish_spacy_parser",
                "file_uri": "http://public.datadrivendiscovery.org/es_core_news_md-2.1.0a7.tar.gz",
                "file_digest":"06d827f4822d06308b2a8d66d5ac526dec521d041826405cd5ade0f4d587b656"
              }, 
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

    def __init__(self, *, hyperparams: Hyperparams, volumes: typing.Dict[str,str]=None)-> None:
        super().__init__(hyperparams=hyperparams, volumes=volumes)
        self.volumes = volumes

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
        #client = Ibex()
        if self.hyperparams['language'] == 'spanish':
            parser_installation_file = self.volumes["spanish_spacy_parser"]
        else:   
            parser_installation_file = self.volumes["english_spacy_parser"]
        client = Ibex(parser_installation_file=parser_installation_file)
        target_columns = self.hyperparams['target_columns']
        output_labels = self.hyperparams['output_labels']

        input_df = inputs

        for i, ith_column in enumerate(target_columns):
            # initialize an empty dataframe
            result_df = pd.DataFrame()
            output_label = output_labels[i]

            for doc in input_df.loc[:, ith_column]:
                jth_result = client.get_entities(doc)

                result_df = result_df.append(
                    {
                        output_label + 'entities': jth_result
                    },
                    ignore_index=True)

            output_df = pd.concat(
                [input_df.reset_index(drop=True), result_df], axis=1)

        return output_df


if __name__ == '__main__':
    volumes = {} 
    volumes["english_spacy_parser"] = '/tmp/f54a6e6a2ff34c1adb1a2eabeb67b170933453ed878125c76813dc2e31c8cf8a/en_core_web_md-2.1.0a7.tar.gz'
    volumes["spanish_spacy_parser"] = '/tmp/06d827f4822d06308b2a8d66d5ac526dec521d041826405cd5ade0f4d587b656/es_core_news_md-2.1.0a7.tar.gz'
    client = d3m_Ibex(hyperparams={'target_columns': ['test_column'], 'output_labels': ['test_column_prefix_'], 'language' : 'english'}, \
        volumes = volumes)

    text = 'The Trump administration struggled on Monday to defend its policy of separating parents from their sons and daughters at the southern US border amid growing national outrage and the release of of sobbing children.'

    input_df = pd.DataFrame(pd.Series([text, text]))
    input_df.columns = ['test_column']
    result = client.produce(inputs=input_df)
    print(result.head)
    result.to_csv('d3m_Ibex_output.txt', sep='\t', encoding='utf-8', index=False)
