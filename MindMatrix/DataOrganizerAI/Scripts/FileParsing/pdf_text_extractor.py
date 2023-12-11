import os
import PyPDF2
import logging

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/ParsingLogs/pdf_text_extraction.log',
                    level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

pdf_dir = 'MindMatrix/DataOrganizerAI/SortedFiles/PDFs'
text_dir = 'MindMatrix/DataOrganizerAI/ParsedData/TextData'

os.makedirs(text_dir, exist_ok=True)

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ''
            for page_num in range(reader.numPages):
                text += reader.getPage(page_num).extractText()
            return text
    except Exception as e:
        logging.error(f"Text extraction failed for {file_path}: {e}")
        return None

def process_pdf_files():
    for file in os.listdir(pdf_dir):
        if file.lower().endswith('.pdf'):
            file_path = os.path.join(pdf_dir, file)
            text = extract_text_from_pdf(file_path)
            if text:
                text_file = os.path.join(text_dir, f"{os.path.splitext(file)[0]}.txt")
                with open(text_file, 'w') as f:
                    f.write(text)

if __name__ == '__main__':
    process_pdf_files()
