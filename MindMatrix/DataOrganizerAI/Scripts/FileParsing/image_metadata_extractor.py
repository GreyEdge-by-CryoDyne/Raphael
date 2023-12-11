import os
from PIL import Image
from PIL.ExifTags import TAGS
import logging

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/ParsingLogs/image_metadata.log',
                    level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

image_dir = 'MindMatrix/DataOrganizerAI/SortedFiles/Images'
metadata_dir = 'MindMatrix/DataOrganizerAI/ParsedData/ImageMetadata'

os.makedirs(metadata_dir, exist_ok=True)

def extract_image_metadata(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        return {TAGS.get(key): exif_data[key] for key in exif_data} if exif_data else {}
    except Exception as e:
        logging.error(f"Metadata extraction failed for {file_path}: {e}")
        return None

def process_image_files():
    for file in os.listdir(image_dir):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):  # Add other image formats as needed
            file_path = os.path.join(image_dir, file)
            metadata = extract_image_metadata(file_path)
            if metadata:
                metadata_file = os.path.join(metadata_dir, f"{os.path.splitext(file)[0]}_metadata.txt")
                with open(metadata_file, 'w') as f:
                    for key, value in metadata.items():
                        f.write(f"{key}: {value}\n")

if __name__ == '__main__':
    process_image_files()
