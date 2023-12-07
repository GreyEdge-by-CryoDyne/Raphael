import json
import logging
import os
import time
from PIL import Image
from tqdm import tqdm

import PIL


def extract_image_metadata(image_path: str, output_dir: str) -> None:
    """
    Extracts metadata from an image file and saves it as a JSON file.

    Args:
        image_path (str): The path to the image file.
        output_dir (str): The directory to save the JSON file.

    Returns:
        None
    """
    try:
        with Image.open(image_path) as img:
            metadata = img.info

        output_file_path = os.path.join(output_dir, os.path.basename(image_path) + '.json')
        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(metadata, file)

        logging.info("Metadata extracted for: %s", image_path)
    except (FileNotFoundError, PIL.UnidentifiedImageError) as e:
        logging.error("Error extracting metadata from %s: %s", image_path, e)

def main() -> None:
    """
    Main function to extract image metadata from a directory of images.
    """
    sorted_images_dir = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/SortedFiles/Images'  # Update the path
    metadata_output_dir = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/ParsedData/ImageMetadata'  # Update the path

    if not os.path.exists(metadata_output_dir):
        os.makedirs(metadata_output_dir)

    files = os.listdir(sorted_images_dir)
    total_files = len(files)
    processed_files = 0

    start_time = time.time()

    with tqdm(total=total_files, unit='file') as pbar:
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                extract_image_metadata(os.path.join(sorted_images_dir, filename), metadata_output_dir)

            processed_files += 1
            elapsed_time = time.time() - start_time
            remaining_time = (elapsed_time / processed_files) * (total_files - processed_files)

            completion_percentage = (processed_files / total_files) * 100

            pbar.set_description(f"Processing file: {filename}")
            pbar.set_postfix(completion=f"{completion_percentage:.2f}%", remaining_time=f"{remaining_time:.2f} seconds")
            pbar.update(1)

    print("Image metadata extraction complete.")

if __name__ == "__main__":
    main()
