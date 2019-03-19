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
        'spacy==2.0.11',
        'd3m_ibex >= 1.1.1'
    ],
    dependency_links=[
        "git+https://github.com/NewKnowledge/d3m_ibex@eb7ee4fb2cb974c35b6b47f71a739a7ad17cf14c#egg=d3m_ibex-1.1.1"
    ],
    entry_points={
        'd3m.primitives': [
            'data_cleaning.ibex.Ibex = IBEXd3mWrapper:d3m_Ibex'
        ],
    }
)
