# dog_cat.py

from .pet import Pet

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def show_info(self):
        return f"{self.name} is a {self.breed} and is {self.age} years old."


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def show_info(self):
        return f"{self.name} is a {self.color} cat and is {self.age} years old."
