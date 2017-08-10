from setuptools import setup

setup( name='pcreode',
       version='0.1',
       description='p-Creode algorithm for mapping state transitions',
       url='https://github.com/herrinca/pCreode',
       author='Chuck Herring',
       author_email='charles.a.herring@Vanderbilt.edu',
       license='MIT',
       packages=[''],
       install_requires=[
           'numpy>=1.11.0',
           'pandas>=0.17.1',
           'tsne==0.1.3',
           'matplotlib',
           'sklearn',
           'igraph'])

