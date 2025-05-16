from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath: str) -> List[str]:
    """
    This function returns a list of requirements from the given file.
    """
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DASH in requirements:
            requirements.remove(HYPHEN_E_DASH)
    

    return requirements

setup(
    name="mlproject",
    version="0.1",
    author="Nirmal Raaju",
    author_email="nirmalraaju.mb2023cce@sece.ac.in",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)