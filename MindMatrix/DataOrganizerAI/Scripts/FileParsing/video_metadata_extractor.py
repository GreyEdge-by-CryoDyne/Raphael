import os
from moviepy.editor import VideoFileClip
import logging

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/ParsingLogs/video_metadata.log',
                    level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

video_dir = 'MindMatrix/DataOrganizerAI/SortedFiles/Videos'
metadata_dir = 'MindMatrix/DataOrganizerAI/ParsedData/VideoMetadata'

os.makedirs(metadata_dir, exist_ok=True)

def extract_video_metadata(file_path):
    try:
        clip = VideoFileClip(file_path)
        return {
            "Duration": clip.duration,
            "FPS": clip.fps,
            "Resolution": clip.size
        }
    except Exception as e:
        logging.error(f"Metadata extraction failed for {file_path}: {e}")
        return None

def process_video_files():
    for file in os.listdir(video_dir):
        if file.lower().endswith(('.mp4', '.avi')):  # Add other video formats as needed
            file_path = os.path.join(video_dir, file)
            metadata = extract_video_metadata(file_path)
            if metadata:
                metadata_file = os.path.join(metadata_dir, f"{os.path.splitext(file)[0]}_metadata.txt")
                with open(metadata_file, 'w') as f:
                    for key, value in metadata.items():
                        f.write(f"{key}: {value}\n")

if __name__ == '__main__':
    process_video_files()
