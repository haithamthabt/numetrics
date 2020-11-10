from setuptools import setup, find_packages
 
 
setup(
  name='numetrics',
  version='0.0.1',
  description='Package For Numerai users to check their models performance',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Haitham Thabt',
  author_email='haithamthabt@hotmail.com',
  license='MIT', 
  keywords='numetrics, numerai', 
  packages=find_packages(),
  install_requires=[''] 
)

