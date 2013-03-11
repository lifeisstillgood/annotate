from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='minimal',
      version=version,
      description="",
      long_description="""
        Simple app that hashes POST contents and returns content on GET request
      """,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Paul, Ishan',
      license='BSD',
      include_package_data=True,
      packages=['minimal',],
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [paste.filter_factory]
      main = minimal:middleware
      """,
      )
