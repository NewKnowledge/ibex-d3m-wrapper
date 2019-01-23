# Ibex D3M Wrapper

Wrapper of Ibex into D3M infrastructure. All code is written in Python 3.5 and must be run in 3.5 or greater. 

This service is a wrapper for the spaCy named entity recognition tool. Given a text document, ibex.get_entites(text, language='english') will return a list of the named entities detected. A key weakness of spaCy's NER is that it may not recognize proper nouns that are not properly capitalized.

## Output
A dataframe with objects, text and tokens, corresponding to the detected objects, raw text and tokens predicted to be in the supplied images.

## Available Functions

#### produce
Produce primitive's best guess for the structural type of each input column. The input is a pandas dataframe. The output is a dataframe with objects, text and tokens, corresponding to the detected objects, raw text and tokens predicted to be in the supplied images.
