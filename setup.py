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
        'ibex >= 1.0.0'
    ],
    dependency_links=[
        "git+https://github.com/NewKnowledge/d3m_ibex@7519b2a0ae7220fc04aa616cd65c4592d3ea8b2f#egg=d3m_ibex-1.0.0"
    ],
    entry_points={
        'd3m.primitives': [
            'feature_extraction.ibex.Ibex = IBEXd3mWrapper:ibex'
        ],
    }
)
