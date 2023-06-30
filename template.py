import os
from pathlib import Path
import logging

# log the basic info with a message
logging.basicConfig(level=logging.INFO, format='[%(astime)s]:%(message)s:')

project_name = 'cnnClassifier'

list_of_files = [
    './github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    filedir, filename = os.path.split(filePath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    if(not os.path.exists(filename)) or (os.path.getSize(filename)==0):
        with open(filePath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filePath}")
    
    else:
        logging.inf(f"{filename} already exists")












