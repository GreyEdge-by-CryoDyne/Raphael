import subprocess
import pkg_resources

def check_requirements():
    with open('/home/ncacord/Desktop/DataOrganizerAI/requirements.txt', encoding='utf-8') as f:
        required_packages = [line.strip() for line in f if line.strip()]

    installed_packages = [pkg.key for pkg in list(pkg_resources.working_set)]
    missing_packages = set(required_packages) - set(installed_packages)

    if missing_packages:
        print("Missing packages detected:")
        for package in missing_packages:
            print(f"- {package}")
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    else:
        return False

    return True
