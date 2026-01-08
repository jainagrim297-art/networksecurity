from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements.
    """
    requirements_list: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and '-e .'
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_list

print(get_requirements())

setup(
    name='NatworkSecurity',
    version='0.0.1',
    author='Krish Naik',
    author_email='krishnaik@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
