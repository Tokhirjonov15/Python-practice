''' CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITANCE
    (3) POLIMORPHISM
'''

print("===== (2) INHERITANCE & (3) POLIMORPHISM =====")
# PARENT > CHILD
# Parent can only provides public and protected properties(state + method) to child element!


class Animal:  # Parent
    # state
    description = "The class is parent for animals"

    # constructor
    def __init__(self, voice):
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you!")
        
    def make_voice(self):
        print(f"the {self.name} says: {self.sound}")


class Cat(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("------")
dog.make_voice()
cat.make_voice()
fish.make_voice()

print("------")
print(Animal.description)
print(Dog.description)


print("====== (3) POLIMORPHISM ======")

dog.make_voice()
fish.make_voice()