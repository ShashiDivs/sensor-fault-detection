from gettext import find, install
from typing import List
from setuptools import find_namespace_packages, find_packages,setup

def get_requirements()->List[str]:

    """
    This function will return list of requirements....

    """
    requirements_list:List[str] = []
    return requirements_list

setup(

    name = "sensor",
    version='0.0.1',
    author = 'shashi',
    author_email = 'shashipolity@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements(),
)



