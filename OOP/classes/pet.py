# pet.py

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic sound"

    def show_info(self):
        return f"{self.name} is {self.age} years old."
