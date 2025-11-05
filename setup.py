from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    Reads the requirements from a given file and returns them as a list.'''
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='Vansh Pal',
    author_email='jontypal888@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)