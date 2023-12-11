import os
from mutagen.easyid3 import EasyID3
import logging

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/ParsingLogs/audio_metadata.log',
                    level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

audio_dir = 'MindMatrix/DataOrganizerAI/SortedFiles/Audio'
metadata_dir = 'MindMatrix/DataOrganizerAI/ParsedData/AudioMetadata'

os.makedirs(metadata_dir, exist_ok=True)

def extract_audio_metadata(file_path):
    try:
        audio_metadata = EasyID3(file_path)
        return {key: audio_metadata[key][0] for key in audio_metadata}
    except Exception as e:
        logging.error(f"Metadata extraction failed for {file_path}: {e}")
        return None

def process_audio_files():
    for file in os.listdir(audio_dir):
        if file.lower().endswith(('.mp3', '.wav')):  # Add other audio formats as needed
            file_path = os.path.join(audio_dir, file)
            metadata = extract_audio_metadata(file_path)
            if metadata:
                metadata_file = os.path.join(metadata_dir, f"{os.path.splitext(file)[0]}_metadata.txt")
                with open(metadata_file, 'w') as f:
                    for key, value in metadata.items():
                        f.write(f"{key}: {value}\n")

if __name__ == '__main__':
    process_audio_files()
