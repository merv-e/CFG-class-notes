'''
price = input("How much does a burger cost?")
is_enough = float(price) <= 10.0

# print("Burger is within budget: {}".format(is_enough))

veg_option = input("Does the restaurant have a vegetarian option? y/n")
veg_friendly = veg_option == "y"
meets_criteria = veg_friendly and is_enough

# print("Restaurant meets criteria {}".format(meets_criteria))


if veg_friendly and is_enough:
    print("Great choice!")

if not veg_friendly or not is_enough:
    print("Not the best idea ever :/ ")


meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'


if meal_price > 20:
    print("Discount applied.")
else:
    print("Discount can not be applied.")


price_to_be_paid = meal_price *


mars_choice = input('Would you like to visit Mars? y/n ')
is_willing = mars_choice == 'y'

affordable = input('Can you afford to visit Mars? y/n ')
can_afford = affordable == 'y'

should_visit_mars = is_willing and can_afford
print('You should visit Mars: {}'.format(should_visit_mars))
'''

'''
admin = input("What is your name?")
name = admin == "Merve"

password = input('password: ')
is_password_correct =

if password == 'jumanji':
    print('Success!')

if not password:
    print("Nope! Try again!")
'''

'''
name = input("name:")
if name == "Merve":
    print("Success!")
else:
    print("Try again!")
'''


'''
temp = float(input("What is the temperature in Celcius?"))
if temp > 200:
    print("The oven is too hot")
elif temp == 180:
    print("The oven is at the perfect temperature")
elif temp < 150:
    print("The oven is too cold")
else:
    print("The temperature is close enough")
'''



# flip a coin

import random
def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side


choice = input('heads or tails: ')
result = flip_coin()
print('The coin landed on {}'.format(result))