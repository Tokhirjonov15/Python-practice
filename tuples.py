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


print("===== Unpacking arguments =====")
groups = ["MIT", "FLEXY", "PYTHON", "STACK"]
(x, y, *z) = groups
print(f"the x: {x} and the y: {y}")
print("z:", z)  # list


# *args > tuple
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


calculate(1, 4, 5, 8)
calculate(1, 5, 8)
calculate(1, 4, 5)

print("-------")

# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} yeard old!")


introduce(name="Alex", age=25)
