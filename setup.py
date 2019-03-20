from distutils.core import setup


setup(
    name='IBEXd3mWrapper',
    version='1.0.1',
    description='Intelligence based entity Xtraction primitive.',
    packages=['IBEXd3mWrapper'],
    keywords=['d3m_primitive'],
    install_requires=[
        'pandas ==0.23.4',
        'numpy >= 1.13.3',
        'spacy==1.7.0',
        'thinc<6.11.0',
        'preshed<2.0.0',
        'cymem<1.32',
        'd3m_ibex >= 1.1.2'
    ],
    dependency_links=[
        "git+https://github.com/NewKnowledge/d3m_ibex@5b5ba8f7c24a07e8b220335d4527ab621d81ee10#egg=d3m_ibex-1.1.2"
    ],
    entry_points={
        'd3m.primitives': [
            'data_cleaning.ibex.Ibex = IBEXd3mWrapper:d3m_Ibex'
        ],
    }
)
