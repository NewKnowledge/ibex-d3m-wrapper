from distutils.core import setup


setup(
    name='IBEXd3mWrapper',
    version='1.0.4',
    description='Intelligence based entity Xtraction primitive.',
    packages=['IBEXd3mWrapper'],
    keywords=['d3m_primitive'],
    install_requires=[
        'pandas==0.23.4',
        'numpy>=1.13.3',
        'spacy==2.1.0',
        'd3m_ibex @ git+https://github.com/NewKnowledge/d3m_ibex@bdcfdf1669fd356fa30d9512d62bfd8c482b80d0#egg=d3m_ibex-1.1.3'
    ],
    entry_points={
        'd3m.primitives': [
            'data_cleaning.ibex.Ibex = IBEXd3mWrapper:d3m_Ibex'
        ],
    }
)
