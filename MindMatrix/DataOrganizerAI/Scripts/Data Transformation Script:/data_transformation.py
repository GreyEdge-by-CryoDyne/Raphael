import os
import logging

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/DataTransformation/transformation.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

source_dir = 'MindMatrix/DataOrganizerAI/ParsedData'
transformed_dir = 'MindMatrix/DataOrganizerAI/TransformedData'

os.makedirs(transformed_dir, exist_ok=True)

def transform_data(file_path):
    # Example transformation logic
    # Modify this function based on specific transformation needs
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            # Apply some transformation to the data
            transformed_data = data.upper()  # Example: converting text to uppercase

        transformed_file_path = os.path.join(transformed_dir, os.path.basename(file_path))
        with open(transformed_file_path, 'w') as file:
            file.write(transformed_data)

        logging.info(f"Data transformed for {file_path}")
    except Exception as e:
        logging.error(f"Transformation failed for {file_path}: {e}")

def process_files():
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        transform_data(file_path)

if __name__ == '__main__':
    process_files()
