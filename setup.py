from distutils.core import setup


setup(
    name='IBEXd3mWrapper',
    version='1.0.1',
    description='Intelligence based entity Xtraction primitive.',
    packages=['IBEXd3mWrapper'],
    keywords=['d3m_primitive'],
    install_requires=[
        'pandas==0.23.4',
        'numpy>=1.13.3',
        'spacy==2.1.0',
        'd3m_ibex>=1.1.3'
    ],
    dependency_links=[
        "git+https://github.com/NewKnowledge/d3m_ibex@4086ca1d94c0bd78a4b9aa80b669a050077c3438#egg=d3m_ibex-1.1.3"
    ],
    entry_points={
        'd3m.primitives': [
            'data_cleaning.ibex.Ibex = IBEXd3mWrapper:d3m_Ibex'
        ],
    }
)
