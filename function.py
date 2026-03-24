''' FUNCTIONS
  (1) DEFINE VS CALL
  (2) Keyword & default arguments
  (3) Scope
'''

print("===== (1) DEFINE VS CALL =====")
# build in function > print() type()
# Function > reusable block of code!
# Python uses indentation

# DEFINE - build


def greet(a):
    print(f"How do you do?, {a}")


def greeting(b):
    print("greeting has been executed")
    return f"Hi, {b}"


# CALL - execute
result1 = greet('Martin')
print("result1:", result1)

result2 = greeting('Alex')
print("result2:", result2)


print("===== (2) Keyword & default arguments =====")

# DEFINE


def give_greet(name, age):
    print("give_greet has been executed")
    return f"Hi {name}, you are {age} years old!"


def give_greeting(name, age=25):
    print("give_greet has been executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Alex", age=28)
print("result3:", result3)

result4 = give_greeting("Alex")
print("result4:", result4)


print("===== (3) Scope =====")
b = 100  #3

# DEFINE
def calculate(a, b): #2
    c = a * b  #1
    print(f"C equals: {c}")


# CALL
calculate(5, 50)
