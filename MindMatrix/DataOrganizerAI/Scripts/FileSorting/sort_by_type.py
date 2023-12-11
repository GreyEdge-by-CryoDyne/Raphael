import os
import shutil
import zipfile
import tarfile
import rarfile  # Requires 'rarfile' package
import logging

# Set up logging
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/CategorizationLogs/file_sorting.log',
                    level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Directories
source_dir = 'DataDumps'
sorted_dir = 'MindMatrix/DataOrganizerAI/SortedFiles'
uncompressible_dir = 'MindMatrix/DataOrganizerAI/Uncompressible'

# Ensure existence of necessary directories
os.makedirs(sorted_dir, exist_ok=True)
os.makedirs(uncompressible_dir, exist_ok=True)

# Supported file types for sorting
file_types = {
    '.txt': 'Documents',
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.mp4': 'Videos',
    '.avi': 'Videos'
    # Add other file types as needed
}

# Supported archive formats
archive_formats = ['.zip', '.tar', '.rar']

def uncompress_file(file_path, destination):
    try:
        if file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(destination)
        elif file_path.endswith('.tar'):
            with tarfile.open(file_path, 'r') as tar_ref:
                tar_ref.extractall(destination)
        elif file_path.endswith('.rar'):
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                rar_ref.extractall(destination)
        return True
    except Exception as e:
        logging.error(f"Failed to uncompress {file_path}: {e}")
        return False

def sort_files():
    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        file_extension = os.path.splitext(file)[1].lower()

        # Check if file is an archive and uncompress it
        if file_extension in archive_formats:
            if uncompress_file(file_path, source_dir):
                os.remove(file_path)  # Remove the archive after extraction
            else:
                shutil.move(file_path, uncompressible_dir)
                continue

        # Sort files into categories
        if file_extension in file_types:
            destination_dir = os.path.join(sorted_dir, file_types[file_extension])
            os.makedirs(destination_dir, exist_ok=True)
            shutil.move(file_path, destination_dir)
        else:
            # Move unrecognised file types to uncompressible
            shutil.move(file_path, uncompressible_dir)

if __name__ == '__main__':
    sort_files()
