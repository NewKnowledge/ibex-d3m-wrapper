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
        'spacy>=2.0.11',
        'd3m_ibex >= 1.1.0'
    ],
    dependency_links=[
        "git+https://github.com/NewKnowledge/d3m_ibex@5c7f3718153359e107653e7fb5e5bd32d13e6c95#egg=d3m_ibex-1.1.0"
    ],
    entry_points={
        'd3m.primitives': [
            'feature_extraction.ibex.Ibex = IBEXd3mWrapper:d3m_Ibex'
        ],
    }
)
