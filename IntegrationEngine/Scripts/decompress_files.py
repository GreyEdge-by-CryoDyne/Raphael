import os
import zipfile
import py7zr
import logging
from tqdm import tqdm

# Setup basic logging
logging.basicConfig(
    filename="IntegrationEngine/Logs/decompression.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

input_dir = "IntegrationEngine/Input"
processing_dir = "IntegrationEngine/Processing"


def decompress_zip(file_path, destination, progress_bar):
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        for file in tqdm(
            iterable=zip_ref.namelist(),
            total=len(zip_ref.namelist()),
            desc=f"Decompressing ZIP: {os.path.basename(file_path)}",
            unit="file",
            leave=False,
        ):
            zip_ref.extract(member=file, path=destination)
            progress_bar.update(1)


def decompress_7z(file_path, destination, progress_bar):
    with py7zr.SevenZipFile(file_path, mode="r") as z:
        for file in tqdm(
            iterable=z.getnames(),
            total=len(z.getnames()),
            desc=f"Decompressing 7Z: {os.path.basename(file_path)}",
            unit="file",
            leave=False,
        ):
            z.extract(targets=[file], path=destination)
            progress_bar.update(1)


def decompress_file(file_path, destination):
    try:
        file_extension = os.path.splitext(file_path)[1]
        with tqdm(total=1, desc=f"Processing {os.path.basename(file_path)}") as pbar:
            if file_extension == ".zip":
                decompress_zip(file_path, destination, pbar)
            elif file_extension == ".7z":
                decompress_7z(file_path, destination, pbar)
        logging.info(f"Decompressed: {file_path}")
    except Exception as e:
        logging.error(f"Error decompressing {file_path}: {e}")


def process_input_directory():
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if filename.endswith(".zip") or filename.endswith(".7z"):
            decompress_file(file_path, processing_dir)


if __name__ == "__main__":
    process_input_directory()
