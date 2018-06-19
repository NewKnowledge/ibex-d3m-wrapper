from distutils.core import setup


setup(name='IBEXd3mWrapper',
      version='1.0.0',
      description='Intelligence based entity Xtraction primitive.',
      packages=['IBEXd3mWrapper'],
      keywords=['d3m_primitive'],
      install_requires=['pandas >= 0.22.0, < 0.23.0',
                        'numpy >= 1.13.3',
                        'ibex >= 1.0.0'],
      dependency_links=[
                       "git+https://github.com/ghonk/ibex@13e0f36cc3acb2a3f405f63a6cf1b398fc36bbee#egg=ibex-1.0.0"
                       ],
      entry_points={
        'd3m.primitives': [
                          'distil.ibex = IBEXd3mWrapper:ibex'
                          ],
                   }
      )
