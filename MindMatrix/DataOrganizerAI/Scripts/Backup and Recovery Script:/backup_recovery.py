import os
import shutil
import logging
from datetime import datetime

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/BackupRecovery/backup.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

data_dir = 'MindMatrix/DataOrganizerAI'
backup_dir = 'MindMatrix/DataOrganizerAI/Backups'

os.makedirs(backup_dir, exist_ok=True)

def backup_data():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}')
    try:
        shutil.copytree(data_dir, backup_path)
        logging.info(f"Backup created successfully at {backup_path}")
    except Exception as e:
        logging.error(f"Backup failed: {e}")

if __name__ == '__main__':
    backup_data()
