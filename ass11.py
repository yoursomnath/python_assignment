# Write a python program to implement a hybrid inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Mammal(Animal):
    def give_birth(self):
        print(f"{self.name} is giving birth to live young")


class Bird(Animal):
    def lay_eggs(self):
        print(f"{self.name} is laying eggs")


class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} can fly")


class Dog(Mammal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Sparrow(Bird):
    def speak(self):
        print(f"{self.name} says Chirp!")


# Example usage:
bat = Bat("Batman")
dog = Dog("Buddy")
sparrow = Sparrow("Tweetie")

bat.fly()
bat.give_birth()

dog.give_birth()
dog.speak()

sparrow.lay_eggs()
sparrow.speak()
