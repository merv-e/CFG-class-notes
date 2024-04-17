'''

student_names = ["Erin", "Kyle", "Abby", "John"]

student_names[1] = "Tia"

print(student_names[2])
print(student_names[1])




clothes = ["shorts", "shoes", "t-shirt"]

if clothes[0] == "shorts":
    clothes[0] = "warm coat"
print(clothes)
'''
import random

'''
numbers = [10, 44.5, 100, 99, 60, 2.3]

print(len(numbers))
print(max(numbers))
print(min(numbers))
'''



'''
costs = [1.2, 4.3, 2.0, 0.5]

print(sorted(costs))
print(list(reversed(costs)))
'''


'''
scores = [3, 200, 10, 130, 30, 160, 60, 100, 190, 90,]

print(sorted(scores))
print(len(scores))
print(max(scores))

# print(reversed(sorted))


use a for loop for a reversed descending order list ... check slides.
'''



'''
names = input("What name are you looking for?")
student_names = ["Erin", "Kyle", "Abby", "John"]

if name in student_names:
   print("{} is in the class.format(names)")
'''


'''
shopping_list = ["bread", "tomato", "cheese", "jam"]
print(shopping_list)

if "bread" in shopping_list:
    shopping_list.append("butter")
    print(shopping_list)
'''

'''
shopping_list = ["bread", "tomato", "cheese", "jam"]
count = 0

for shopping_list in shopping_list:
    count = count + 1
    # print(count)
    # print(shopping_list) # bu sekilde yapinca cikti string ve [] icinde değil de alt alta geliyor.

print(count)
'''

'''
costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for amount in costs:
    total_cost = total_cost + amount
    print(total_cost)

print(total_cost)

# Instead of doing the method above, we can just use sum method (below)

total = sum(costs)
print(total)
'''

# WHAT ARE TUPPLES // OR TUFFLE ??? They are like lists...

# Dictionaries

'''
person = {"name": "Jessica", "age": 23}

print(person["name"])

place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
    'longitude': 127,
    'latitude': 63,
    }
}

print(place["name"])
print(place["post_code"])
print(place["street_number"])

loc = place["location"]

# print(place["location"]["longitude"])
print(loc["location"]) # you can shorten it but this one here is wrong, find out what is right :) 

# print(place["location"]["latitude"])

'''

'''
people = [
{'name': 'Jessica', 'age': 23},
{'name': 'Trisha', 'age': 24},
]
for person in people:
    print(person['name'])
'''

'''
fruits = [
{'name': 'apple', 'colour': 'red', 'price': 0.12},
{'name': 'banana', 'colour': 'yellow', 'price': 0.2},
{'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruit_name in fruits:
    print("fruit_names:", fruit_name["name"])

for fruit_colour in fruits:
    print("fruit_colours:", fruit_colour["colour"])

for fruit_price in fruits:
    print("fruit_prices:", fruit_price["price"])
'''

'''
import random

colours = ["red", "pink", "white", "blue"]

chosen_colour = random.choice(colours)
print(chosen_colour)
'''

import random

first_names = ["John", "Mary", "Willy", "Elizabeth"]
last_names = ["Love", "Koontz", "White", "Curry"]

chosen_name = random.choice(first_names) + " " +  random.choice(last_names)

print(chosen_name)

# continue doing this exercise.
# Using list of verbs and a list of nouns, create randomised sentences

verbs = ["hug", "love", "smooch", "", "", ""]
nouns = ["glass", "bird", "dough", "", "", "booze"]