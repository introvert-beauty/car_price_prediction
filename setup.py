from setuptools import setup,find_packages
from typing import List


HYPHEN_E_DOT="-e ."

def get_requirements(file_path:str)->list[str]:
    '''
    this function is responsilble for read the librarys one by one
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n'," ") for req in requirements]
       
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)




setup(
    name='car_price_prediction',
    version='0.0.1',
    author="sharmi",
    author_email="anyumsharmila@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)