import os
import psutil
import logging
from datetime import datetime

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/PerformanceMonitoring/performance.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def monitor_performance():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"{timestamp} - CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%")

if __name__ == '__main__':
    monitor_performance()
