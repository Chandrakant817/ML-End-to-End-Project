from setuptools import setup, find_packages

REQUIREMENT_FILE_NAME = "requirements.txt"
REMOVE_PACKAGE = "-e ."


def get_requirement_list(requirement_file_name=REQUIREMENT_FILE_NAME) -> list:
    try:
        requirement_list = None
        with open(requirement_file_name) as requirement_file:
            requirement_list = [requirement.replace("\n", "") for requirement in requirement_file]
            requirement_list.remove(REMOVE_PACKAGE)
        return requirement_list
    except Exception as e:
        raise e


setup(
    name="ML_Pipeline_Project",
    version="0.0.1",
    description="Machine Learning Pipeline Project.",
    author="Chandrakant Thakur",
    author_email="chandrakantthakur817@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement_list()
)