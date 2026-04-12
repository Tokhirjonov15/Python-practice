''' List
    (1) Working with lists
    (2) List methods
    (3) Enum, map and filter
'''

print("===== (1) Working with lists =====")

# literal
person = {"name": "Alex", "age": 25}   # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX"]
for team in groups:
    print(f"the team: {team}")

# constructor
letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")


print("------")
fruits = ["apple", "orange", "lemon", 'kiwi']

a = fruits[0]
b = fruits[0:2]  # first two element
c = fruits[::3]  # first and skip 3 steps
d = fruits[::-1]  # opposite

print("A:", a)
print("B:", b)
print("C:", c)
print("D:", d)


print("===== (2) List methods =====")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "b", "d"]
letters.append("c")  # add behind
print(f"the append result: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letter is: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result1: {result2} and letter is: {letters}")

print("------")
animals = ["fish", "cat", "capybara", "bird", "lion"]
print("Animals:", animals)

animals.remove("lion")
print("Animals Remove:", animals)

del animals[2:4]
print("Animals Delete:", animals)
