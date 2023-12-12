import os
import zipfile
import py7zr
import logging

# Setup basic logging
logging.basicConfig(filename='IntegrationEngine/Logs/decompression.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

input_dir = 'IntegrationEngine/Input'
processed_dir = 'IntegrationEngine/ProcessedData'

def decompress_file(file_path, extension):
    """
    Decompresses a file based on its extension.
    """
    try:
        if extension == '.zip':
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(processed_dir)
        elif extension == '.7z':
            with py7zr.SevenZipFile(file_path, mode='r') as z:
                z.extractall(processed_dir)
        logging.info(f"Decompressed: {file_path}")
    except Exception as e:
        logging.error(f"Error decompressing {file_path}: {e}")

def main():
    """
    Main function to decompress all .zip and .7z files in the input directory.
    """
    for file in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file)
        if file.endswith('.zip') or file.endswith('.7z'):
            decompress_file(file_path, os.path.splitext(file)[1])

if __name__ == "__main__":
    main()
