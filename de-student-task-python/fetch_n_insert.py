import requests
import sys
from entry_point import URL
from entry_point import TOKEN
from entry_point import headers
from db_functions import create_table_db, store_in_db


def fetch_nasa_data(date):
    api_key = TOKEN
    get_url = f'{URL}{date}&{api_key}'
    response = requests.get(get_url, headers=headers)
    data = response.json()
    return data

def extract_data(data):
    if data and 'projects' in data:
        projects = data['projects']
        project_details = []
        for project in projects:
            project_id = project.get('projectId')
            last_updated = project.get('lastUpdated')
            project_details.append((project_id, last_updated))
        return project_details
    

data_fetched = fetch_nasa_data(sys.argv[1])
extracted_data = extract_data(data_fetched)
create = create_table_db()
insert_data = store_in_db(extracted_data)