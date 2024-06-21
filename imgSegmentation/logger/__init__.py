import logging
import os
from datetime import datetime
from from_root import from_root

LOG_FILE = f'{datetime.now().strftime("%Y-%m-%d_%H_%M_%S")}.log'

log_path = os.path.join(from_root(),'log', LOG_FILE)

os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s'
    )