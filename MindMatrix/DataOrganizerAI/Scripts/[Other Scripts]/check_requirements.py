import subprocess

def check_and_install(package):
    try:
        subprocess.run(['pip', 'install', package], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

def main():
    requirements = ['mutagen', 'Pillow', 'PyPDF2', 'moviepy']
    for package in requirements:
        check_and_install(package)

if __name__ == '__main__':
    main()
