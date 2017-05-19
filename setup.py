from setuptools import setup, Extension, find_packages
import platform

setup(name='openeng',
      version='1.0',
      description='Automated design of liquid rocket engines',
      url='http://github.com/cmflannery/openrocketengine',
      author='Cameron Flannery',
      author_email='cmflannery@ucsd.edu',
      license='MIT',
      packages=['openeng'],
      zip_safe=False)
