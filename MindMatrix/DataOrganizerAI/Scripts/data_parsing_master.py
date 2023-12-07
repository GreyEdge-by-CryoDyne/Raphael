import os
import subprocess

def run_parsing_script(script_path, file_type_directory):
    subprocess.run(["python", script_path, file_type_directory])

def main():
    base_dir = '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI'
    sorted_dir = os.path.join(base_dir, 'SortedFiles')

    for file_type in os.listdir(sorted_dir):
        file_type_path = os.path.join(sorted_dir, file_type)
        if file_type == 'Documents':
            run_parsing_script(os.path.join(base_dir, '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/Scripts/FileParsing/text_parser.py'), file_type_path)
        elif file_type == 'Images':
            run_parsing_script(os.path.join(base_dir, '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/Scripts/FileParsing/image_metadata_extractor.py'), file_type_path)
        elif file_type == 'Audio':
            run_parsing_script(os.path.join(base_dir, '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/Scripts/FileParsing/audio_metadata_extractor.py'), file_type_path)
        elif file_type == 'Videos':
            run_parsing_script(os.path.join(base_dir, '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/Scripts/FileParsing/video_metadata_extractor.py'), file_type_path)
        elif file_type == 'PDFs':
            run_parsing_script(os.path.join(base_dir, '/home/ncacord/Desktop/raphael_core/AI_Core/DataOrganizerAI/Scripts/FileParsing/pdf_text_extractor.py'), file_type_path)
    #   elif file_type == 'DIR':
    #       run_parsing_script(os.path.join(base_dir, 'parsed data dir'), file_type_path)
        # Extend this pattern for other file types


if __name__ == "__main__":
    main()
