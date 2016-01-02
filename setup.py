#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 2):
    raise Exception('Only Python 3.2+ is supported')

setup(name='import_from_github_com',
      version='0.1',
      description="Python module finder/loader from github, like in golang",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/import_from_github_com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples',
                                      'tests', 'release']),
      include_package_data=True,
      zip_safe=False)
