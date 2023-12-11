import os
import magic  # Requires python-magic package
import logging

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/DataValidation/data_validation.log',
                    level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

data_dir = 'MindMatrix/DataOrganizerAI/DataDumps'
valid_data_dir = 'MindMatrix/DataOrganizerAI/ValidData'
invalid_data_dir = 'MindMatrix/DataOrganizerAI/InvalidData'

os.makedirs(valid_data_dir, exist_ok=True)
os.makedirs(invalid_data_dir, exist_ok=True)

def is_valid_file(file_path):
    try:
        file_type = magic.from_file(file_path, mime=True)
        return file_type.startswith('image/') or file_type.startswith('audio/') or \
               file_type.startswith('video/') or file_type.startswith('text/') or \
               file_type == 'application/pdf'
    except Exception as e:
        logging.error(f"Validation failed for {file_path}: {e}")
        return False

def validate_data():
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        if is_valid_file(file_path):
            shutil.move(file_path, valid_data_dir)
        else:
            shutil.move(file_path, invalid_data_dir)

if __name__ == '__main__':
    validate_data()
