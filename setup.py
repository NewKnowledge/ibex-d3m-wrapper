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
        'ibex >= 1.0.0'
    ],
    dependency_links=[
        "git+https://github.com/NewKnowledge/ibex@455d33e4434d9e75b0d86f43ac9c3d9de2a1ce61#egg=ibex-1.0.0"
    ],
    entry_points={
        'd3m.primitives': [
            'distil.ibex = IBEXd3mWrapper:ibex'
        ],
    }
)
