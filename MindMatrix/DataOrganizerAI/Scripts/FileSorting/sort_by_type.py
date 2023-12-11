import os
import shutil
import subprocess
import logging
import time
import sys

def install_requirements(requirements_file):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
        logging.info("Successfully installed requirements from {}".format(requirements_file))
    except subprocess.CalledProcessError as e:
        logging.error("Failed to install requirements: {}".format(e))
        sys.exit(1)

def find_requirements_file(start_path):
    for root, dirs, files in os.walk(start_path):
        if 'requirements.txt' in files:
            return os.path.join(root, 'requirements.txt')
    return None

def find_data_dumps_dir(start_path):
    for root, dirs, files in os.walk(start_path):
        if 'DataDumps' in dirs:
            return os.path.join(root, 'DataDumps')
    return None

def categorize_file(file):
    # Define your file categorization logic here
    file_ext = file.split(".")[-1].lower()
    if file_ext in ['mp3', 'wav', 'aac']:
        return "Audio"
    elif file_ext in ['doc', 'docx', 'txt']:
        return "Documents"
    elif file_ext in ['jpg', 'jpeg', 'png', 'gif']:
        return "Images"
    elif file_ext == 'pdf':
        return "PDFs"
    elif file_ext in ['mp4', 'avi', 'mov']:
        return "Videos"
    else:
        return "Other Types"

def handle_file(file, sorted_dir, data_dumps_dir):
    file_path = os.path.join(data_dumps_dir, file)
    if os.path.isfile(file_path):
        try:
            category = categorize_file(file)
            category_dir = os.path.join(sorted_dir, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)
            shutil.move(file_path, os.path.join(category_dir, file))
            logging.info("Moved: %s to %s", file, category)
        except OSError as e:
            logging.error("Error moving file %s: %s", file, e)


def get_folder_size(folder):
    total_size = 0
    for path, _, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    return total_size

def progress_bar(current, total, start_time, initial_size):
    elapsed_time = time.time() - start_time
    completion = current / total
    progress = int(completion * 50)
    remaining_time = (elapsed_time / completion) * (1 - completion) if completion > 0 else 0
    time_left = time.strftime("%H:%M:%S", time.gmtime(remaining_time))
    percentage = int(completion * 100)
    bar = "[" + "#" * progress + " " * (50 - progress) + "]"
    print(f"\r{bar} {percentage}% Complete | Time Left: {time_left} | Initial Folder Size: {initial_size} bytes", end="")

# Script start
# Setup logging
log_path = "file_sorting.log"
logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s %(message)s")

# Check for requirements.txt and install requirements
requirements_file = find_requirements_file(os.path.expanduser("~"))
if requirements_file:
    install_requirements(requirements_file)

# Find DataDumps directory
data_dumps_dir = find_data_dumps_dir(os.path.expanduser("~"))
if not data_dumps_dir:
    logging.error("DataDumps directory not found.")
    sys.exit(1)

# Sorting files in DataDumps
SORTED_DIR = "SortedFiles"
sorted_dir = os.path.join(data_dumps_dir, SORTED_DIR)
if not os.path.exists(sorted_dir):
    os.makedirs(sorted_dir)

initial_size = get_folder_size(data_dumps_dir)
start_time = time.time()
file_count = len(os.listdir(data_dumps_dir))
current_file = 0

for filename in os.listdir(data_dumps_dir):
    handle_file(filename, sorted_dir, data_dumps_dir)
    current_file += 1
    progress_bar(current_file, file_count, start_time, initial_size)

logging.info("Files sorted by type. Check sorting logs for details.")
# Script end
