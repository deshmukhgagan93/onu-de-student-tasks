import os
from dotenv import load_dotenv
load_dotenv()
URL = "https://techport.nasa.gov/api/projects?updatedSince="
TOKEN = os.getenv('TOKEN')
headers = {
    'accept': 'application/json'
}

