''' CLASS
    (1) What is Class
    (2) Ordinary vs Static Properties
    (3) Special Methods
'''

print("===== (1) What is Class =====")
# class - blueprint for object creation!
# structure > state constructor method


class Person():
    # state
    message = "Static state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do?")

    def say_age(self):
        print(f"{self.name} says: i am {self.age}!")

    @classmethod
    def explain(cls):
        print("Static Method Property executed!")


person1 = Person("Justin", 23)
person2 = Person("Alex", 24)
person1 = Person("John", 25)

# ordinary state
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("===== (2) Ordinary vs Static Properties =====")
# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()
