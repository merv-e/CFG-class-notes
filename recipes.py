import requests

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
    return data['hits']  # Ensure this key exists in the response


def run():
    ingredient = input('Enter an ingredient: ')
    results = search_for_a_recipe(ingredient)
    for result in results:
        recipe = result['recipe']

        print(recipe['label'])
        print(recipe['uri'])
        # Ensure these keys exist in the recipe data
        print("Cuisine Type:", recipe.get("cuisineType", "Not specified"))
        print("Dish Type:", recipe.get("dishType", "Not specified"))
        print("Meal Type:", recipe.get("mealType", "Not specified"))


# Activate the run function to start the process
run()