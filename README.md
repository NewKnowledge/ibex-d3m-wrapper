# Ibex D3M Wrapper

Wrapper of Ibex into D3M infrastructure. All code is written in Python 3.5 and must be run in 3.5 or greater. 

This service is a wrapper for the spaCy named entity recognition tool. Given a text document, ibex.get_entites(text, language='english') will return a list of the named entities detected. A key weakness of spaCy's NER is that it may not recognize proper nouns that are not properly capitalized.

## Install

pip3 install -e git+https://github.com/NewKnowledge/ibex-d3m-wrapper.git#egg=IBEXd3mWrapper --process-dependency-links

## Input
A pandas dataframe where a column is a pd.Series of text documents.

## Output
A dataframe with the sets of named entities extracted from the columns of the input dataframe.

## Available Functions

#### produce
Perform named entity recognition based on the input data provided. The output is described above.
