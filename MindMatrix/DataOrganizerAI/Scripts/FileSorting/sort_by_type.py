"""
This script sorts files in a directory based on their file extension.
It categorizes files with recognized extensions into their respective destination directories,
while unrecognized file types are moved to a separate directory.

The script also includes a function to uncompress files in supported archive formats.

Functions:
- uncompress_file(file_path, destination): Uncompresses a file to the specified destination.
- sort_files(): Sorts files in a directory based on their file extension.
"""
"""_summary_Returns:_type_: _description_"""
import os
import shutil
import logging
import zipfile
import tarfile
import rarfile  # Requires 'rarfile' package

# Set up logging
logging.basicConfig(
    filename="/home/ncacord/Desktop/Raphael/MindMatrix/DataOrganizerAI/Logs/SortingLogs/file_sorting.log",
    level=logging.ERROR,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

# Directories
UNCOMPRESSIBLE_DIR = "MindMatrix/DataOrganizerAI/Uncompressible"
SORTED_DIR = "MindMatrix/DataOrganizerAI/Sorted"  # Define the SORTED_DIR variable

# Ensure existence of necessary directories
os.makedirs(SORTED_DIR, exist_ok=True)
os.makedirs(UNCOMPRESSIBLE_DIR, exist_ok=True)

# Supported file types for sorting
file_types = {
    ".txt": "Documents",
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Videos",
    ".avi": "Videos"
    # Add other file types as needed
}

# Supported archive formats
archive_formats = [".zip", ".tar", ".rar"]


import logging
import os
import rarfile
import shutil
import tarfile
import zipfile
import os

def uncompress_file(file_path, destination): # type: ignore
    """
    Uncompresses a file to the specified destination.

    Args:
        file_path (str): The path of the file to be uncompressed.
        destination (str): The destination directory where the uncompressed files will be placed.

    Returns:
        bool: True if the file was successfully uncompressed, False otherwise.
    """
    try:
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(destination)
        elif file_path.endswith(".tar"):
            with tarfile.open(file_path, "r") as tar_ref:
                tar_ref.extractall(destination)
        elif file_path.endswith(".rar"):
            with rarfile.RarFile(file_path, "r") as rar_ref:
                rar_ref.extractall(destination)
        return True
    except zipfile.BadZipFile as e:
        logging.error("Failed to uncompress %s: %s", file_path, e)
        return False
    except tarfile.TarError as e:
        logging.error("Failed to uncompress %s: %s", file_path, e)
        return False
    except rarfile.RarCannotExec as e:
        logging.error("Failed to uncompress %s: %s", file_path, e)
        return False


def sort_files_new():
    """
    Sorts files in a directory based on their file extension.

    This function iterates through all the files in the source directory and
    categorizes them based on their file extension. Files with recognized
    extensions are moved to their respective destination directories, while
    unrecognized file types are moved to a separate directory.

    Parameters:
        None

    Returns:
        None
    """
    source_dir = "MindMatrix/DataOrganizerAI/Source"  # Define the source_dir variable

    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        file_extension = os.path.splitext(file)[1].lower()

        # Check if file is an archive and uncompress it
        uncompressible_dir = "MindMatrix/DataOrganizerAI/Uncompressible"  # Define the uncompressible_dir variable

        if file_extension in archive_formats:
            if uncompress_file(file_path, source_dir):
                os.remove(file_path)  # Remove the archive after extraction
            else:
                shutil.move(file_path, uncompressible_dir)
                continue

        # Sort files into categories
        if file_extension in file_types:
            destination_dir = os.path.join(
                SORTED_DIR, file_types[file_extension]
            )  # Replace 'sorted_dir' with 'SORTED_DIR'
            os.makedirs(destination_dir, exist_ok=True)
            shutil.move(file_path, destination_dir)
        else:
            # Move unrecognized file types to uncompressible
            shutil.move(file_path, uncompressible_dir)
# Ensure existence of necessary directories
os.makedirs(SORTED_DIR, exist_ok=True)
# Ensure existence of necessary directories
os.makedirs(UNCOMPRESSIBLE_DIR, exist_ok=True)

# Supported file types for sorting
file_types = {
    ".txt": "Documents",
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".mp4": "Videos",
    ".avi": "Videos"
    # Add other file types as needed
}

# Supported archive formats
archive_formats = [".zip", ".tar", ".rar"]


def uncompress_file(file_path, destination):
    """
    Uncompresses a file to the specified destination.

    Args:
        file_path (str): The path of the file to be uncompressed.
        destination (str): The destination directory where the uncompressed files will be placed.

    Returns:
        bool: True if the file was successfully uncompressed, False otherwise.
    """
    try:
        if file_path.endswith(".zip"):
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(destination)
        elif file_path.endswith(".tar"):
            with tarfile.open(file_path, "r") as tar_ref:
                tar_ref.extractall(destination)
        elif file_path.endswith(".rar"):
            with rarfile.RarFile(file_path, "r") as rar_ref:
                rar_ref.extractall(destination)
        return True
    except zipfile.BadZipFile as e:
        logging.error("Failed to uncompress %s: %s", file_path, e)
        return False
    except tarfile.TarError as e:
        logging.error("Failed to uncompress %s: %s", file_path, e)
        return False
    except rarfile.RarCannotExec as e:
        logging.error("Failed to uncompress %s: %s", file_path, e)
        return False


def sort_files():
    """
    Sorts files in a directory based on their file extension.

    This function iterates through all the files in the source directory and
    categorizes them based on their file extension. Files with recognized
    extensions are moved to their respective destination directories, while
    unrecognized file types are moved to a separate directory.

    Parameters:
        None

    Returns:
        None
    """
    source_dir = "Dumps"
    for root, dirs, _ in os.walk("/"):
        if "Dumps" in dirs:
            source_dir = os.path.join(root, "Dumps")
            break

    if not source_dir:
        print("Source directory not found.")
        exit()

    SORTED_DIR = "MindMatrix/DataOrganizerAI/Sorted"  # Define the SORTED_DIR variable
    UNCOMPRESSIBLE_DIR = "MindMatrix/DataOrganizerAI/Uncompressible"  # Define the UNCOMPRESSIBLE_DIR variable

    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        file_extension = os.path.splitext(file)[1].lower()

        # Check if file is an archive and uncompress it
        if file_extension in archive_formats:
            if uncompress_file(file_path, source_dir):
                os.remove(file_path)  # Remove the archive after extraction
            else:
                shutil.move(file_path, UNCOMPRESSIBLE_DIR)  # Replace 'uncompressible_dir' with 'UNCOMPRESSIBLE_DIR'
                continue

        # Sort files into categories
        if file_extension in file_types:
            destination_dir = os.path.join(
                SORTED_DIR, file_types[file_extension]
            )  # Replace 'sorted_dir' with 'SORTED_DIR'
            os.makedirs(destination_dir, exist_ok=True)
            shutil.move(file_path, destination_dir)
        else:
            # Move unrecognized file types to UNCOMPRESSIBLE_DIR
            shutil.move(file_path, UNCOMPRESSIBLE_DIR)


if __name__ == "__main__":
    sort_files()    
