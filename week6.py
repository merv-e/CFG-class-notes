import requests

def recipe_search(ingredient):
    # Register to get an APP ID and key https://developer.edamam.com/

    app_id = '9a01e4df'
    app_key = 'f55aa716d20221d7c0b1a7bd7d721c8c'

    result = requests.get(
    'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    data = result.json()
    print(data)
    return data['hits']
def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']

        print(recipe['label'])
        print(recipe['uri'])
       # print("calories :", round(recipe['calories'], 2))
        # print(recipe['totalNutrients'])
        print(recipe["cuisineType"])
        print("dish Type:", recipe["dishType"])
        print("meal Type:", recipe["mealType"])
print()
run()


