About Dataset
The dataset provided predictive feature like education , employment status , marital status to predict if the salary is greater than $50K

It can be used to practice machine learning problem like classification

-> day 1
1. GitHub repo
2. Clone GitHub repo
3. requ.txt

> Crete a GitHub Repo 
> git colne [GitHub Path]

> cmd: locate to Folder of your project -- write [code .] you will redirected to VSCode

> create conda environment [conda crate -p env python==3.8 -y] ..CMD in VSCode

* Activate Environment
> For CMD [conda activate env/]

> For GitBash [source activate env/]

create a file: 
1. setup.py
2. requirements.txt

Pyhton Setup Script documentation --> https://docs.python.org/3/distutils/setupscript.html

#### Setup.py
```
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
```
#### requirements.txt
```
numpy
pandas
matplotlib
seaborn
Flask
scikit-learn
-e .
```
