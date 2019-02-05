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
        'd3m_ibex >= 1.0.0'
    ],
    dependency_links=[
        "git+https://github.com/NewKnowledge/d3m_ibex@90323d9e6cf9d17e2f3c1f83298475de723ffa7e#egg=d3m_ibex-1.0.0"
    ],
    entry_points={
        'd3m.primitives': [
            'feature_extraction.ibex.Ibex = IBEXd3mWrapper:ibex'
        ],
    }
)
