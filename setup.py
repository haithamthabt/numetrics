from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
 
 
setup(
  name='numetrics',
  version='0.0.5',
  description='Package For Numerai users to check their models performance',
  long_description=long_description + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type="text/markdown",
  url='',  
  author='Tim Thabt',
  author_email='haithamthabt@hotmail.com',
  license='MIT', 
  keywords='numetrics, numerai', 
  packages=find_packages(),
  install_requires=[''] 
)

