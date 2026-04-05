''' LOOP operators
  (1) for
  (2) break/else
  (3) while
'''

print("===== for operator =====")
# Iterable objects > string dict tuple list range map filter
text = "MIT"
numbs = [10, 7, 5, 3]
car_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)

for letter in text:
    print(f"the letter is: {letter}")

print("-------")
for number in numbs:
    print(f"the number is: {number}")

print("-------")
for a in car_obj:
    print(f"the element is: {a} => value is: {car_obj.get(a)}")

print("-------")
for x in range_obj:
    print(f"the element is: {x}")

print("-------")
for key in range(1, 20, 4):  # the third argument(4) is step
    print(f"the key element is: {key}")


print("===== break/else =====")
for b in range(1, 20, 5):
    print(f"the x: {b}")
    if b > 10:
        print("Reached BREAK")
        break
else:
    print("Executed Successfully")


print("===== while operator =====")
numb = 40
while numb > 0:
    numb -= 10
    print(f"the numb equals {numb}")

print("------")
count = 0
while True:
    count += 1
    x = int(input("Find Number "))

    if x == 41:
        print(f"You found a number in {count} steps")
        break
    else:
        print("Wrong, please find again!")
