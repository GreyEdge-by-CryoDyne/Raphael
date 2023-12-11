import os
import json
from PIL import Image
from tqdm import tqdm
import humanize

def extract_image_metadata(file_path):
    """
    Extracts metadata from an image file.
    Supported formats: JPEG, PNG, etc.
    """
    try:
        with Image.open(file_path) as img:
            metadata = {
                "format": img.format,
                "size": img.size,
                "mode": img.mode,
                "info": img.info  # Additional metadata like EXIF data
            }
            return metadata
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def save_metadata(metadata, save_path):
    """
    Saves the extracted metadata to a file in JSON format.
    """
    with open(save_path, 'w') as f:
        json.dump(metadata, f, indent=4)

def process_image_files(image_dir, metadata_dir):
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))] # Add more formats if needed

    with tqdm(total=len(image_files), unit='file', desc="Processing Image Files") as pbar:
        for file in image_files:
            file_path = os.path.join(image_dir, file)
            file_size = os.path.getsize(file_path)
            print(f"Processing {file} (Size: {humanize.naturalsize(file_size)})")

            metadata = extract_image_metadata(file_path)
            if metadata:
                save_path = os.path.join(metadata_dir, os.path.basename(file) + '.json')
                save_metadata(metadata, save_path)
            
            pbar.update(1)
            pbar.set_postfix_str(f"{pbar.n}/{pbar.total} files processed")

def main():
    image_dir = 'path/to/image/files'
    metadata_dir = 'path/to/ParsedData/ImageMetadata'
    process_image_files(image_dir, metadata_dir)

if __name__ == '__main__':
    main()
