import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s')

projectname = 'imgSegmentation'

listOfFiles = [
    '.github/workflows/.gitkeep',
    'data/.gitkeep',
    f'{projectname}/__init__.py',
    f'{projectname}/components/__init__.py',
    f'{projectname}/components/data_ingestion.py',
    f'{projectname}/components/data_validation.py',
    f'{projectname}/components/model_trainer.py',
    f'{projectname}/constant/__init__.py',
    f'{projectname}/constant/training_pipeline/__init__.py',
    f'{projectname}/constant/application.py',
    f'{projectname}/entity/config_entity.py',
    f'{projectname}/entity/artifacts_entity.py',
    f'{projectname}/exception/__init__.py',
    f'{projectname}/logger/__init__.py',
    f'{projectname}/pipeline/__init__.py',
    f'{projectname}/pipeline/training_pipeline.py',
    f'{projectname}/utils/__init__.py',
    f'{projectname}/utils/main_utils.py',
    'reseach/trials.ipynb',
    'templates/index.html',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py'
]

for fp in listOfFiles:
    filepath = Path(fp)

    filedir, filename = os.path.split(filepath)

    if filedir!='':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created directory: {filedir} for the file: {filename}')


    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Created empty file: {filename}')

    else:
        logging.info(f'File already exists: {filename}')