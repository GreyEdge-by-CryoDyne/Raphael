import os
import logging

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/ParsingLogs/text_parsing.log',
                    level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

text_dir = 'MindMatrix/DataOrganizerAI/SortedFiles/Documents'
parsed_dir = 'MindMatrix/DataOrganizerAI/ParsedData/TextData'

os.makedirs(parsed_dir, exist_ok=True)

def parse_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Text parsing failed for {file_path}: {e}")
        return None

def process_text_files():
    for file in os.listdir(text_dir):
        if file.lower().endswith(('.txt', '.docx')):  # Add other text formats as needed
            file_path = os.path.join(text_dir, file)
            text = parse_text_file(file_path)
            if text:
                parsed_file = os.path.join(parsed_dir, f"{os.path.splitext(file)[0]}_parsed.txt")
                with open(parsed_file, 'w') as f:
                    f.write(text)

if __name__ == '__main__':
    process_text_files()
