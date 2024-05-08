import requests
import json

# Replace these with your actual Edamam API credentials
app_id = 'your_app_id'
app_key = 'your_app_key'

# Set up the endpoint and parameters for the request
url = 'https://api.edamam.com/api/nutrition-data'
ingredient = input("Please enter an ingredient ")

# Prepare the parameters for the request
params = {
    'app_id': "795d6ce1",
    'app_key': "2e6b2654d60789304146442b113a1b7e",
    'ingr': ingredient
}

# Make the HTTP GET request to the Edamam API
response = requests.get(url, params)

data = response.json()
print(json.dumps(data, indent=2))


