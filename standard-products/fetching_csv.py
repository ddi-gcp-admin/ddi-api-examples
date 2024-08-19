### This is a simple script with a minimum of code needed to make an API request for any of the standard products,
# depending on which API_URL you enter:
# - Trips API
# - Visits API
# - Activities API
# - Maps API
# You choose API by choosing an API_URL.
# This example ignores pagination, and returns some sample data.

import requests
import os
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv('../.env')

def fetch_data_from_signed_url(signed_url):
    print("Fetching CSV data from signed url \n")
    response = requests.get(signed_url)
    print(response)
    output_filename = "activities_20230101.csv"
    if (response.status_code == 200): 
        print("Response ok. Downloading.")
        with open("../" + output_filename, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded and saved as {output_filename}")        
    else:
        print("Could not find file at the signed url.")


def fetch_data(api_url, token):
    # Set up the headers with the bearer token
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'text/csv'  # Returns the result as json. Other options are CSV or Avro.
    }

    # Make the GET request to the API endpoint
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        download_url = data['downloadUrls'][0]
        print("\n\n Download url: ", download_url)
        fetch_data_from_signed_url(download_url)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# EXAMPLE (Activities API)
# This example url does a request on the Activities API filtered by the date 2023-01-01, showing down to 
# admin level 2 resolution in the results.
# API_URL: https://api.insights.teliacompany.com/api/standard/activities/v2/activity/swe/2023-01-01/admin-level/al2/daily/?spatial_resolution_filter=al1&area_code=1

API_URL = 'https://api.insights.teliacompany.com/api/standard/activities/v2/activity/swe/2023-01-01/admin-level/al2/daily/' # '<INSERT API URL>'  # Replace with your actual API endpoint
BEARER_TOKEN = os.environ['BEARER_TOKEN'] # Create (or edit) a .env-file or replace this code with your bearer token. Get a bearer_token using retrieve_bearer_token.py

fetch_data(API_URL, BEARER_TOKEN)
