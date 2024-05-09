import requests
import pandas as pd

url = "https://api.edamam.com/api/recipes/v2"

def search_for_a_recipe(ingredient):
    parameters = {
        "app_id": "9a01e4df",
        "app_key": "f55aa716d20221d7c0b1a7bd7d721c8c",
        "type": "public",
        "q": ingredient
    }
    result = requests.get(url, params=parameters)
    data = result.json()
    hits = data.get('hits', [])  # Extract 'hits' field from the response
    recipes = [hit['recipe'] for hit in hits]  # Extract 'recipe' field from each hit
    df = pd.DataFrame(recipes)  # Convert the list of recipes into a DataFrame
    return df


def run():
    ingredient = input('Enter an ingredient: ')
    df = search_for_a_recipe(ingredient)
    if not df.empty:
        print("Recipes found:")
        for index, recipe in df.iterrows():
            print(recipe['label'])
            print(recipe['uri'])
            print("Cuisine Type:", recipe.get("cuisineType", "Not specified"))
            print("Dish Type:", recipe.get("dishType", "Not specified"))
            print("Meal Type:", recipe.get("mealType", "Not specified"))
            print()  # Add a blank line between recipes


# Activate the run function to start the process
run()
