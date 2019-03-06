from distutils.core import setup


setup(
    name='IBEXd3mWrapper',
    version='1.0.0',
    description='Intelligence based entity Xtraction primitive.',
    packages=['IBEXd3mWrapper'],
    keywords=['d3m_primitive'],
    install_requires=[
        'pandas >= 0.22.0, < 0.23.0',
        'numpy >= 1.13.3',
        'spacy>=2.0.12',
        'd3m_ibex >= 1.1.1'
    ],
    dependency_links=[
        "git+https://github.com/NewKnowledge/d3m_ibex@7301f69b10fc2c627f8845c2b6b4a91ab7339915#egg=d3m_ibex-1.1.1"
    ],
    entry_points={
        'd3m.primitives': [
            'feature_extraction.ibex.Ibex = IBEXd3mWrapper:d3m_Ibex'
        ],
    }
)
