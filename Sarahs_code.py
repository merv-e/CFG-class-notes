import requests

def recipe_search(ingredient):
    # Replace 'YOUR_APP_ID' and 'YOUR_APP_KEY' with your own Edamam API credentials
    app_id = '7a387e12'
    app_key = 'fb3fff780cf9e3c5a27056f66c7aa7ab'
    # Fetching data from Edamam API
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    # Parsing the JSON response
    data = result.json()
    return data['hits']

def save_to_file(recipes):
    with open("recipes.txt", "w") as file:
        for recipe in recipes:
            file.write(recipe['recipe']['label'] + "\n")
            file.write(recipe['recipe']['url'] + "\n\n")