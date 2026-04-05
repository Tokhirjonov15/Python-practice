''' OPERATORS & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''

print("===== (1) Operators =====")

a = 19
b = 5

print(a / b)
result = a // b  # bo'lingandagi butun son
left = a % b    # bo'lingandagi qoldiq son
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a:", a)

print("Bning kvadrati:", b**2)
print("Bning kubi:", b**3)


print("===== (2) Condition =====")
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("===== (3) Logical Operators =====")

age = 25
# person = None
# if age > 18:
#     person = "adult"
# else:
#     person = "child"


# Ternary Operator
person = "adult" if age > 18 else "minor"
print("person:", person)

print("--------------")

is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:
    print("Welcome here, do you want to be student?")
elif is_admin:
    print("Please go to this office")
elif is_guest or is_parent:
    print("Waiting room is over there!")