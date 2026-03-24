''' FUNCTIONS
  (1) DEFINE VS CALL
  (2) Keyword & default arguments
  (3) Scope
'''

print("===== DEFINE VS CALL =====")
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
