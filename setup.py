from setuptools import setup

setup(name='h5',
      version=0.1,
      description='Wrapper for safe usage of pytables object',
      author='Ambrose J. Carr',
      author_email='mail@ambrosejcarr.com',
      package_dir={'': 'src'},
      packages=['h5'],
      install_requires=[
          'numpy',
          'pandas>=0.18.1'],
      )
