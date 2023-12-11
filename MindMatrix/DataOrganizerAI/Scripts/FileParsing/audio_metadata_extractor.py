import os
import json
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.wavpack import WavPack
from tqdm import tqdm
import humanize

def extract_audio_metadata(file_path):
    """
    Extracts metadata from an audio file.
    Supports various formats like mp3, flac, wavpack, etc.
    """
    metadata = {}
    try:
        if file_path.endswith('.mp3'):
            audio = MP3(file_path, ID3=EasyID3)
        elif file_path.endswith('.flac'):
            audio = FLAC(file_path)
        elif file_path.endswith('.wv'):
            audio = WavPack(file_path)
        # ... include other formats as necessary

        for key in audio.keys():
            metadata[key] = audio[key]

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

    return metadata

def save_metadata(metadata, save_path):
    """
    Saves the extracted metadata to a file in JSON format.
    """
    with open(save_path, 'w') as f:
        json.dump(metadata, f, indent=4)

def process_audio_files(audio_dir, metadata_dir):
    audio_files = [f for f in os.listdir(audio_dir) if f.endswith(('.mp3', '.flac', '.wv'))] # Extend for other formats

    with tqdm(total=len(audio_files), unit='file', desc="Processing Audio Files") as pbar:
        for file in audio_files:
            file_path = os.path.join(audio_dir, file)
            file_size = os.path.getsize(file_path)
            print(f"Processing {file} (Size: {humanize.naturalsize(file_size)})")

            metadata = extract_audio_metadata(file_path)
            if metadata:
                save_path = os.path.join(metadata_dir, os.path.basename(file) + '.json')
                save_metadata(metadata, save_path)
            
            pbar.update(1)
            pbar.set_postfix_str(f"{pbar.n}/{pbar.total} files processed")

def main():
    audio_dir = 'path/to/audio/files'
    metadata_dir = 'path/to/ParsedData/AudioMetadata'
    process_audio_files(audio_dir, metadata_dir)

if __name__ == '__main__':
    main()
