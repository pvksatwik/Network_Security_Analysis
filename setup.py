from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    try:
        #Open and read the requirements.txt file
        with open('requirements.txt', 'r') as f:
            #read lines from the file
            lines = f.readlines()
            #Process each line
            for line in lines:
                #Strip whitespaces and newline characters
                requirement = line.strip()
                #ignore empty lines and -e
                if requirement and requirement != '-e':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_list

print(get_requirements())
setup(
    name = 'networksecurity',
    version = '0.0.1',
    author = 'SATWIK',
    author_email = 'satwik@example.com',
    packages = find_packages(),
    install_requirements = get_requirements()
)