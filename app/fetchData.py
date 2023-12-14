import requests
from bs4 import BeautifulSoup
import json
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

json_file_path = os.path.join(current_directory, 'data.json')

# Set the URL and headers
url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request to the website
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
json_data = soup.find('p').text

# Save the JSON data to a file named 'data.json'
with open(json_file_path, 'w') as json_file:
    json.dump(json.loads(json_data), json_file, indent=2)

print('Data saved to data.json')