import os.path
import sys
import yaml
import base64

from imgSegmentation.exception import AppException
from imgSegmentation.logger import logging

def read_yaml_file(file_path: str):
    """
    Read the yaml file from the given path.

    Args:
    file_path (str): The path of the yaml file.

    Returns:
    dict: The dictionary containing the yaml file content.
    """
    try:
        with open(file_path, 'r') as file:
            logging.info(f'Reading the yaml file successfully from the path: {file_path}')
            return yaml.safe_load(file)
        
    except Exception as e:
        raise AppException(e, sys) from e
    
def write_yaml_file(file_path: str, content: object, replace: bool = False):
    """
    Write the content to the yaml file.

    Args:
    file_path (str): The path of the yaml file.
    content (object): The content to be written to the yaml file.
    replace (bool): If True, the content will be replaced with the existing content in the file. 
    If False, the content will be appended to the existing content in the file.

    Returns:
    None
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
                logging.info(f'File removed successfully at the path: {file_path}')
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
            logging.info(f'Content written to the yaml file successfully at the path: {file_path}')
        
    except Exception as e:
        raise AppException(e, sys) from e
    
def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open('./data/'+filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as image_file:
        return base64.b64encode(image_file.read())
        