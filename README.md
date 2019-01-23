# Ibex D3M Wrapper

Wrapper of Ibex into D3M infrastructure. All code is written in Python 3.5 and must be run in 3.5 or greater. 

This service is a wrapper for the spaCy named entity recognition tool. Given a text document, ibex.get_entites(text, language='english') will return a list of the named entities detected. A key weakness of spaCy's NER is that it may not recognize proper nouns that are not properly capitalized.

## Install

pip3 install -e git+https://github.com/NewKnowledge/ibex-d3m-wrapper.git#egg=IBEXd3mWrapper --process-dependency-links

## Output
A dataframe with objects, text and tokens, corresponding to the detected objects, raw text and tokens predicted to be in the supplied images.

## Available Functions

#### produce
Produce image object classification predictions and OCR for an image provided as an URI or filepath The input is a pandas dataframe. The output is described above.
