import os
import logging
from moviepy.editor import VideoFileClip
import json
import time
from tqdm import tqdm

def extract_video_metadata(video_path, output_dir):
    try:
        with VideoFileClip(video_path) as clip:
            metadata = clip.reader.infos
        output_file_path = os.path.join(output_dir, os.path.basename(video_path) + '.json')
        with open(output_file_path, 'w') as file:
            json.dump(metadata, file)
        logging.info("Metadata extracted for: %s", video_path)
        return True
    except Exception as e:
        logging.error("Failed to extract metadata for: %s. Error: %s", video_path, str(e))
        return False

def main():
    logging.basicConfig(filename='video_metadata_extraction.log', level=logging.INFO)
    sorted_video_dir = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/SortedFiles/Videos'  # Update this path
    metadata_output_dir = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/ParsedData/VideoMetadata'  # Update this path

    if not os.path.exists(metadata_output_dir):
        os.makedirs(metadata_output_dir)

    video_files = [filename for filename in os.listdir(sorted_video_dir) if filename.lower().endswith(('.mp4', '.mkv', '.avi', '.mov'))]
    total_files = len(video_files)
    processed_files = 0

    print("Video metadata extraction in progress:")
    with tqdm(total=total_files) as pbar:
        for filename in video_files:
            video_path = os.path.join(sorted_video_dir, filename)
            if extract_video_metadata(video_path, metadata_output_dir):
                processed_files += 1

            # Update progress bar
            pbar.update(1)
            pbar.set_description(f"Processing: {filename}")

    print("\nVideo metadata extraction complete.")

if __name__ == "__main__":
    start_time = time.time()
    main()
