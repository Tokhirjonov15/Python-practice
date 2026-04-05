''' TUPLE
  (1) What is tuple: tuple vs list
  (2) Unpacking arguments
  (3) zip
'''

print("===== What is tuple: tuple vs list =====")
# Java, PHP, NodeJS array => Python list

# literal
numbs = [3, 4, 5, 6]
car_dict = {"brand": "Ferrari", "year": 2025}

# constructor
letters = list("Hello World")
person_dict = dict(name="Alex", age=25)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("Default fruits:", fruits)
fruits[2] = "melon"
print("Updated fruits:", fruits)

# TUPLE (we can't update tuple's value)
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)
print(animals[0])
