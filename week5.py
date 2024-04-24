'''


animals = [
    { "species": "zebra", "name": "Penelope"},
{ "species": "zebra", "name": "Penelope"},
{ "species": "zebra", "name": "Penelope"},
{ "species": "zebra", "name": "Penelope"}
]

for animal in animals:
    print(`animal["species"]`)

'''


'''
# WRITE
with open('file.txt', 'w') as file:
    file.write("content to write")
'''

'''
# READ
with open('content.txt', 'r') as file:
    content = file.read()

print(content)

'''
# READ And WRITE
'''
with open('content.txt', 'w+') as file:
    people = file.read()

print(content)
'''


'''
# EXAMPLE: 
new_item = input("Enter a todo item")
with open('todo.txt', 'w+') as todo_file:
    todo = todo_file.read()

todo = todo + new_item + '/n'
print(todo)

with open("todo.txt", "w+") as todo_file:
    todo_file.write(todo)

'''
'''
# ERIN'S CODE fr the code above  
new_item = input('Enter a to do item:')

with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()

todo = todo + new_item + '\n'

with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)
'''

'''
import csv

field_names = ["name", "age"]

data = [
    {'name': 'Josh', 'age': 22},
    {'name': 'Abby', 'age': 40},
    {'name': 'Grace', 'age': 32},
    {'name': 'Jade', 'age': 16},
]

with open ("team.csv", "w+") as csv_file:
    spreadsheet = csv.DictWriter(csv_file, field_names = field_names)

    spreadsheet.writeheader()
    spreadsheet.writeheader() ### bu satır ve sonrası  sonrası düzeltilecek
'''


# Writing a CSV File
'''

import csv

field_names = ['name', 'age']

data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]

with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data)
'''


# Reading a CSV File
'''

import csv

with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))

'''

# Exercise with trees.csv
'''
import csv

with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    heights = []

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)

'''

# pip is an external package created by other people

pokemon_API = "https://pokeapi.co/"

