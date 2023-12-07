"""PDF extraction script"""
import os
import logging
from tqdm import tqdm
from PyPDF2 import PdfFileReader

def extract_text_from_pdf(input_file, output_file):
    """
    Extracts text from a PDF file and writes it to an output file.

    Args:
        input_file (str): The path to the input PDF file.
        output_file (str): The path to the output file where the extracted text will be written.

    Raises:
        FileNotFoundError: If the input file does not exist.

    """
    try:
        # Check if input file exists
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' not found.")
        
        # Get initial file size
        initial_size = os.path.getsize(input_file)
        
        # Initialize progress bar
        progress_bar = tqdm(total=initial_size, unit='B', unit_scale=True, desc='Processing')
        
        # Open PDF file
        with open(input_file, 'rb') as file:
            pdf = PdfFileReader(file)
            
            # Extract text from each page
            text = ''
            for page_num in range(pdf.getNumPages()):
                page = pdf.getPage(page_num)
                text += page.extractText()
                
                # Update progress bar
                progress_bar.update(file.tell() - progress_bar.n)
        
        # Write extracted text to output file
        with open(output_file, 'w') as file:
            file.write(text)
        
        # Close progress bar
        progress_bar.close()
        
        # Log completion
        logging.info('Text extraction completed successfully.')
        
    except FileNotFoundError as e:
        # Log error
        logging.error(str(e))
        
    except Exception as e:
        # Log error
        logging.error(f'Error occurred during text extraction: {str(e)}')

def main():
    """
    Extracts text from PDF files in a specified directory and saves the extracted text as separate text files.

    Args:
        None

    Returns:
        None
    """
    logging.basicConfig(filename='pdf_extraction.log', level=logging.INFO)
    
    sorted_pdf_dir = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/SortedFiles/PDFs'  # Placeholder for PDFs directory
    parsed_text_dir = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/ParsedData/TextData'  # Placeholder for extracted text directory

    if not os.path.exists(parsed_text_dir):
        os.makedirs(parsed_text_dir)

    for filename in os.listdir(sorted_pdf_dir):
        if filename.lower().endswith('.pdf'):
            input_file_path = os.path.join(sorted_pdf_dir, filename)
            output_file_path = os.path.join(parsed_text_dir, os.path.splitext(filename)[0] + '.txt')
            extract_text_from_pdf(input_file_path, output_file_path)

    print("PDF text extraction complete.")

if __name__ == "__main__":
    main()
