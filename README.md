## Crowd Insights API examples

The intention of this repo is for Telia Crowd Insights customers to get code examples that use the CI API, to help out with your own development of application using Crowd Insights data.

### Requirements
- A Google account
- The Crowd Insights API is a commercial API for CI customers. You will need to be a **registered user**, with your Google account, to use the API. If you are curious on the Crowd Insights data, please contact Telia Crowd Insights.
- A service account JSON key, provided to you by Telia. Please ask, if you have not received any yet.
- A bearer token. You can retrieve a bearer token with the authentication.py script in this repo.

### Necessary preparations
1. Create a .env file in the root, you can use example.env as an example.
1. Add the filename of your JSON key file to the .env as SA_JSON_KEY_FILENAME. Do NOT enter path names here, just the filename including .json. E.g. 'myfilename.json'
1. Run authentication.py to retrieve a bearer token
1. Add the bearer token to your .env-file as BEARER_TOKEN