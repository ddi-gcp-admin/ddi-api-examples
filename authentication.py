from google.oauth2 import service_account
from google.auth.transport.requests import Request
import os
import json
import requests
import google.auth
import google.auth.transport.requests

from dotenv import load_dotenv  # type: ignore

# Load environment variables from .env file
load_dotenv('.env')

# creds.valid is False, and creds.token is None
# Need to refresh credentials to populate those

def application_default_credentials_token():
    credentials, project = google.auth.default()
    auth_req = google.auth.transport.requests.Request()

    credentials.refresh(auth_req)

    if (credentials.token):
        print("> Successfully fetched token")
        return credentials.token
    else:
        print("> Failed to fetch token")


def service_key_credentials_token():
    # Path to your service account key JSON file
    filename = os.path.join(os.path.dirname(__file__), os.environ['SA_JSON_KEY_FILENAME'])

    # Define the scopes for which you need the access token
    scopes = ['https://www.googleapis.com/auth/cloud-platform']

    credentials = service_account.Credentials.from_service_account_file(filename=filename, scopes=scopes)
    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)

    #print(credentials.__dict__)  # Uncomment this to print full response
    if (credentials.token):
        print("\n Copy and paste the following BEARER_TOKEN to your .env file:")
        print("\n", credentials.token)
    else: 
        print("> Bearer token could not be fetched, please contact Telia support!")

    return credentials.token

def validate_access_token(token):
    response = requests.get(
        "https://oauth2.googleapis.com/tokeninfo?access_token=" + token
    )
    if (response.status_code == 200):
        print("> Validation successful. Token is a valid GCP token: ", response.json())
    else:
        print("> Validation failed. Token is invalid! Response: ", response.status_code)

def validate_api_access(token):
    # Example HTTP request using the access token in the Authorization header
    url = 'https://api.insights.teliacompany.com/api/standard/authenticate-test/hello'
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}

    # Make a GET request (you can change it to POST, PUT, etc. as needed)
    response = requests.get(url, headers=headers)

    print("> API Response", response)
    if (response.status_code == 200):
        print("> API access validation SUCCESSFUL!")
        print("> Response: ", response.json()['rows'])
    elif (response.status_code == 401):
        print("> API access validation FAILED")
        print("> The request was successful but the service account does NOT have access to CI API (status: 401). Please contact Telia CI support.")
    elif (response.status_code == 500):
        print("> API access validation FAILED")
        print("> Bad response (500) from the API. This does not mean the Service account is unauthorized, but something went wrong. Please contact Telia CI support.")
    else:
        print("> API access validation FAILED")
        print("> Unknwon issue", response.status_code)

    print("\n--- End of script")

###

print("\n\n--- APPLICATION DEFAULT CREDENTIALS")

print("\n\n- Retrieving token:")
token=application_default_credentials_token()

print("\n\n- Validating token")
validate_access_token(token)

print("\n\n- Validating API access")
validate_api_access(token)

###

print("\n\n--- SERVICE KEY CREDENTIALS")

print("\n\n- Retrieving bearer token:")
sa_token=service_key_credentials_token()

print("\n\n- Validating token")
validate_access_token(sa_token)

print("\n\n- Validating API access")
validate_api_access(sa_token)