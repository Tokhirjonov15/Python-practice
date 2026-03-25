print("===== Iterable objects & RANGE =====")
# Iterable objects > string dict tuple list range map filter

range_obj = range(3)
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")
for ele in range_obj:
    print(f"the element: {ele}")


print("===== DICTIONARY =====")
# DICTIONARY is JSON object!
person = {"name": "Alex", "age": 25, "status": "married"}
person_obj = dict(name="Alex", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# name = person_obj["name"]
# print("name:", name)
# hobby = person_obj["hobby"] # It causes error not "none", bcz there is no hobby state
# print("hobby:", hobby)

name = person_obj.get("name")
hobby = person_obj.get("hobby") # It doesn't cause error but "none", bcz we used get method
balance = person_obj.get("balance", 0) # 0 is gonna be default value if there is no state balance
print(f"Your name is {name}, your hobby is {hobby}, your balance is {balance}") 

del person_obj["single"] # It deletes given value in array
for key in person_obj:
    print(f"the key: {key} => value is {person_obj.get(key)}")