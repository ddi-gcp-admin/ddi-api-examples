
import requests
import os
from dotenv import load_dotenv  # type: ignore

# Load environment variables from .env file
load_dotenv('../.env')

def fetch_data(api_url, token, page_token=None, job_id=None):
    # Set up the headers with the bearer token
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'  # Returns the result as json. Other options are CSV or Avro.
    }

    # Make the GET request to the API endpoint
    if (page_token):
        print("Page token exists")
        api_url=api_url + "?page_token=" + page_token + "&job_id=" + job_id
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        response_json = response.json()
        data = response_json['rows']
        print(f"Number of JSON objects in result: {len(data)}")

        # Print a sample of the data
        print(f"Sample data:\n", data[:1])  # Returns the first row of data

        # Check if 'pageToken' exists in the response
        if 'pageToken' in response_json:
            page_token = response_json['pageToken']
            job_id = response_json['jobReference']['jobId']

            if page_token:
                print("\npageToken\n", page_token)
                print("\njobId\n", job_id)
                fetch_data(api_url.split('?')[0], token, page_token=page_token, job_id=job_id)  # Run the script again with new page_token
        else:
            print("No more pages left to fetch.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# EXAMPLE (Activities API)
# This example url does a request on the Activities API filtered by the date 2023-01-01 and by activities in Admin Level 1 = 1 (i.e. Stockholms län), showing down to 
# admin level 2 resolution in the results.
# API_URL: https://api.insights.teliacompany.com/api/standard/activities/v2/activity/swe/2023-01-01/admin-level/al2/daily/?spatial_resolution_filter=al1&area_code=1

API_URL = 'https://api.insights.teliacompany.com/api/standard/activities/v2/activity/swe/2023-01-01/admin-level/al3/hourly/' # '<INSERT API URL>'  # Replace with your actual API endpoint
BEARER_TOKEN = os.environ['BEARER_TOKEN'] # Create (or edit) a .env-file or replace this code with your bearer token. Get a bearer_token using retrieve_bearer_token.py

fetch_data(API_URL, BEARER_TOKEN)
