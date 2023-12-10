import requests
import os
import json
import logging

# Logging setup
logging.basicConfig(filename='MindMatrix/DataOrganizerAI/Logs/APIIntegration/api_integration.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

api_url = 'https://example.com/api'  # Replace with the actual API URL
data_dir = 'MindMatrix/DataOrganizerAI/TransformedData'

def call_api(file_path):
    with open(file_path, 'rb') as file:
        response = requests.post(api_url, files={'file': file})
        if response.status_code == 200:
            logging.info(f"API call successful for {file_path}")
            return json.loads(response.content)
        else:
            logging.error(f"API call failed for {file_path}: {response.content}")
            return None

def integrate_with_api():
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        api_response = call_api(file_path)
        # Handle the API response as needed

if __name__ == '__main__':
    integrate_with_api()
