"""Sorter script that sorts files in the Downloads folder by type."""
import os
import shutil
import logging
import subprocess
import time
import os


def check_requirements():
    """
    Check if the requirements for the script are met by running the 'check_requirements.py' script.
    If the requirements check fails, print an error message and return.
    """
    result = subprocess.run(
        [
            "python",
            "/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/Scripts/[Other Scripts]/check_requirements.py",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    if result.returncode != 0:
        print("Requirements check failed. Please resolve the issues before continuing.")
        return


# Setup logging
log_path = os.path.join(os.path.dirname(__file__), "Logs/SortingLogs/file_sorting.log")
logging.basicConfig(
    filename=log_path, level=logging.INFO, format="%(asctime)s %(message)s"
)

DOWNLOADS_DIR = (
    "/home/ncacord/Desktop/raphael_core/AI_Core/Datasets/Datasets_to_process"  # Replace with your actual Downloads folder path
)
SORTED_DIR = "DataOrganizerAI/SortedFiles"

sorted_dir = os.path.join(os.path.dirname(__file__), SORTED_DIR)

if not os.path.exists(sorted_dir):
    os.makedirs(sorted_dir)


def handle_file(file):
    """
    Handle each file by moving it to the corresponding directory based on its extension.

    Args:
        file (str): The name of the file to be handled.
    """
    file_path = os.path.join(DOWNLOADS_DIR, file)
    if os.path.isfile(file_path):
        try:
            file_ext = file.split(".")[-1]
            ext_dir = os.path.join(sorted_dir, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.move(file_path, os.path.join(ext_dir, file))
            logging.info("Moved: %s", file)
        except OSError as e:
            logging.error("Error moving file %s: %s", file, e)


def get_folder_size(folder):
    """
    Get the size of a folder in bytes.

    Args:
        folder (str): The path to the folder.

    Returns:
        int: The size of the folder in bytes.
    """
    total_size = 0
    for path, _, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size


def progress_bar(current, total, start_time_param, initial_size_param):
    """
    Display a progress bar with completion percentage and estimated time left.

    Args:
        current (int): The current progress value.
        total (int): The total progress value.
        start_time_param (float): The start time of the process.
        initial_size_param (int): The size of the initial folder in bytes.
    """
    elapsed_time_param = time.time() - start_time_param
    completion_param = current / total
    progress_param = int(completion_param * 50)
    remaining_time_param = (
        (elapsed_time_param / completion_param) * (1 - completion_param)
        if completion_param > 0
        else 0
    )
    time_left_param = time.strftime("%H:%M:%S", time.gmtime(remaining_time_param))
    percentage_param = int(completion_param * 100)
    bar_param = "[" + "#" * progress_param + " " * (50 - progress_param) + "]"
    print(
        f"\r{bar_param} {percentage_param}% Complete | Time Left: {time_left_param} | Initial Folder Size: {initial_size_param} bytes",
        end="",
    )



def scan_additional_directory():
    """
    Prompt the user to scan an additional directory if no files are found in the default directory.
    The user can choose to scan the whole PC or a specific directory.
    List all scannable directories on the device.
    """
    print("No files found in the default directory.")
    print("Do you want to scan an additional directory?")
    print("1. Scan the whole PC")
    print("2. Scan a specific directory")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        # Scan the whole PC
        print("Scanning the whole PC...")
        for root, dirs, files in os.walk('/'):
            for directory in dirs:
                directory_path = os.path.join(root, directory)
                print(f"Scanning directory: {directory_path}")
                # Add your code to scan the specific directory here
    elif choice == "2":
        # Scan a specific directory
        print("List of scannable directories:")
        for root, dirs, files in os.walk('/'):
            for directory in dirs:
                directory_path = os.path.join(root, directory)
                print(directory_path)
        directory = input("Enter the directory path to scan: ")
        print(f"Scanning directory: {directory}")
        # Add your code to scan the specific directory here
    else:
        print("Invalid choice. Please try again.")


# Get initial folder size
initial_size = get_folder_size(DOWNLOADS_DIR)

# Start sorting process
start_time = time.time()
file_count = len(os.listdir(DOWNLOADS_DIR))
CURRENT_FILE = 0

if file_count == 0:
    scan_additional_directory()
else:
    for filename in os.listdir(DOWNLOADS_DIR):
        handle_file(filename)
        CURRENT_FILE += 1
        progress_bar(CURRENT_FILE, file_count, start_time, initial_size)

    print(
        "\nFiles sorted by type. Check '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/Logs/SortingLogs' for the operation log."
    )

    elapsed_time = time.time() - start_time
    completion = CURRENT_FILE / file_count
    progress = int(completion * 50)
    remaining_time = (elapsed_time / completion) * (1 - completion) if completion > 0 else 0
    time_left = time.strftime("%H:%M:%S", time.gmtime(remaining_time))
    percentage = int(completion * 100)
    bar = "[" + "#" * progress + " " * (50 - progress) + "]"
    print(
        f"\r{bar} {percentage}% Complete | Time Left: {time_left} | Initial Folder Size: {initial_size} bytes",
        end="",
    )
