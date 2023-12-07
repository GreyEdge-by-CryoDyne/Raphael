import os
import logging
import time
from tqdm import tqdm

BASE_DIR = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI'
sorted_docs_dir = os.path.join(BASE_DIR, 'SortedFiles/Documents')
parsed_output_dir = os.path.join(BASE_DIR, 'ParsedData/TextData')
log_file = os.path.join(BASE_DIR, 'Logs/ParsingLogs/text_parsing.log')

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(message)s')


def parse_text_file(file_path, output_dir):
    """
    Parse a text file and save the content to a new file in the specified output directory.

    Args:
        file_path (str): The path to the input text file.
        output_dir (str): The directory where the parsed file will be saved.

    Raises:
        FileNotFoundError: If the input file is not found.
        IOError: If an IO error occurs while parsing the file.
        UnicodeDecodeError: If a Unicode decode error occurs while parsing the file.
        OSError: If an OS error occurs while parsing the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        output_file_path = os.path.join(output_dir, os.path.basename(file_path))
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        logging.info("Successfully parsed: %s", file_path)
    except (FileNotFoundError, IOError, UnicodeDecodeError, OSError) as e:
        if isinstance(e, FileNotFoundError):
            logging.error("File not found: %s", file_path)
        elif isinstance(e, IOError):
            logging.error("IO error occurred while parsing %s: %s", file_path, e)
        elif isinstance(e, UnicodeDecodeError):
            logging.error("Unicode decode error occurred while parsing %s: %s", file_path, e)
        elif isinstance(e, OSError):
            logging.error("OS error occurred while parsing %s: %s", file_path, e)

def main():
    """
    Main function to parse text files in the sorted_docs_dir and save the parsed files in the parsed_output_dir.
    """
    if not os.path.exists(parsed_output_dir):
        os.makedirs(parsed_output_dir)

    files = [filename for filename in os.listdir(sorted_docs_dir) if filename.endswith('.txt')]
    total_files = len(files)
    start_time = time.time()

    with tqdm(total=total_files, ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        for filename in files:
            parse_text_file(os.path.join(sorted_docs_dir, filename), parsed_output_dir)
            pbar.update(1)
            elapsed_time = time.time() - start_time
            remaining_time = (elapsed_time / pbar.n) * (pbar.total - pbar.n)
            pbar.set_postfix({'Time Remaining': f'{remaining_time:.2f} seconds'})

if __name__ == "__main__":
    main()
