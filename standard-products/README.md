# Explanation of sample scripts
All scripts in this folder are using standard products. Your account needs to have been configured (by Telia) to query a given API. You also need to have added your bearer token to the .env-file. See authentication.py on how to retrieve your bearer token.

### simple.py
A simple example, as simple as they come, on how you can download data from the Crowd Insights API as JSON and display a sample of the data in the console.

### fetching_csv.py
An example on how you can download data from any API, retrieve the signed url and download the data as CSV (same logic works for Avro as well).

### using_pagination.py
Example script that requests a larger dataset that requires the use of pagination to download the entire dataset.