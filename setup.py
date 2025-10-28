## setup.py is responsible for creating my Machine Learning Appliaction as a Package and that Package can be 
# deployed in Python pipy where  anybody can install the package and use it.
## in requirements.txt in the end we have placed '-e .' , which basically is used to redirect to setup.py and  install all libraries

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements 

setup(
    name='mlproject',
    version='0.0.1',
    author='Keshav Saini',
    author_email='keshavsaini1005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)