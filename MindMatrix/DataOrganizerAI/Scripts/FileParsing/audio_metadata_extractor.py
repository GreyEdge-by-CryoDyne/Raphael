import os
import logging
from pydub.utils import mediainfo
import json
import time
from tqdm import tqdm

def extract_audio_metadata(audio_path, output_dir):
    try:
        metadata = mediainfo(audio_path)
        output_file_path = os.path.join(output_dir, os.path.basename(audio_path) + '.json')
        with open(output_file_path, 'w') as file:
            json.dump(metadata, file)
        logging.info("Metadata extracted for: %s", audio_path)
        return True
    except Exception as e:
        logging.error("Failed to extract metadata for: %s. Error: %s", audio_path, str(e))
        return False

def main():
    logging.basicConfig(filename='audio_metadata_extraction.log', level=logging.INFO)
    sorted_audio_dir = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/SortedFiles/Audio'  # Update this path
    metadata_output_dir = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/ParsedData/AudioMetadata'  # Update this path

    if not os.path.exists(metadata_output_dir):
        os.makedirs(metadata_output_dir)

    audio_files = [filename for filename in os.listdir(sorted_audio_dir) if filename.lower().endswith(('.mp3', '.wav', '.aac', '.flac'))]
    total_files = len(audio_files)

    print("Audio metadata extraction started.")
    start_time = time.time()

    with tqdm(total=total_files) as pbar:
        for filename in audio_files:
            file_path = os.path.join(sorted_audio_dir, filename)

            if extract_audio_metadata(file_path, metadata_output_dir):
                pbar.set_postfix({"Processing file": filename})
                pbar.update(1)
            else:
                pbar.set_postfix({"Failed file": filename})
                pbar.update(1)

    print("Audio metadata extraction complete.")

if __name__ == "__main__":
    main()
