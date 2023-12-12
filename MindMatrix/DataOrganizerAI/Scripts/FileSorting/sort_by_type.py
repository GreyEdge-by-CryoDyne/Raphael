import os
import shutil
import logging
import zipfile
import tarfile
import rarfile  # Requires 'rarfile' package

# Set up logging
logging.basicConfig(
    filename="file_sorting.log",
    level=logging.ERROR,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

# Directories
SORTED_DIR = "Sorted"
UNCOMPRESSIBLE_DIR = "Uncompressible"

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
    ".avi": "Videos",
}

# Supported archive formats
archive_formats = [".zip", ".tar", ".rar", ".gz", ".7z"]


def uncompress_file(file_path, base_destination):
    """
    Uncompresses a file to a dynamically determined destination within the base_destination.

    Args:
        file_path (str): The path of the file to be uncompressed.
        base_destination (str): The base destination directory where the uncompressed files will be placed.

    Returns:
        bool: True if the file was successfully uncompressed, False otherwise.
    """
    try:
        # Create a unique destination folder for each archive
        archive_name = os.path.splitext(os.path.basename(file_path))[0]
        destination = os.path.join(base_destination, archive_name)
        os.makedirs(destination, exist_ok=True)

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
    except Exception as e:
        logging.error("Failed to uncompress %s: %s", file_path, e)
        return False


def find_source_directory(directory_name):
    """
    Searches the file system for a directory with the specified name.

    Args:
        directory_name (str): The name of the directory to search for.

    Returns:
        str: The path to the found directory or None if not found.
    """
    for root, dirs, _ in os.walk("/"):
        if directory_name in dirs:
            return os.path.join(root, directory_name)
    return None


def sort_files():
    """
    Sorts files in a directory based on their file extension.

    This function searches for a directory named 'Dumps' in the file system.
    It then iterates through all the files in this directory, categorizing them
    based on their file extension. Files with recognized extensions are moved
    to their respective destination directories, while unrecognized file types
    are moved to a separate directory.
    """
    source_dir = find_source_directory("Dumps")

    if not source_dir:
        logging.error("Source directory 'Dumps' not found.")
        return

    for file in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file)
        file_extension = os.path.splitext(file)[1].lower()

        # Check if file is an archive and uncompress it
        if file_extension in archive_formats:
            if uncompress_file(file_path, source_dir):
                os.remove(file_path)  # Remove the archive after extraction
            else:
                shutil.move(file_path, UNCOMPRESSIBLE_DIR)
                continue

        # Sort files into categories
        if file_extension in file_types:
            destination_dir = os.path.join(SORTED_DIR, file_types[file_extension])
            os.makedirs(destination_dir, exist_ok=True)
            shutil.move(file_path, destination_dir)
        else:
            # Move unrecognized file types to UNCOMPRESSIBLE_DIR
            shutil.move(file_path, UNCOMPRESSIBLE_DIR)


if __name__ == "__main__":
    sort_files()
