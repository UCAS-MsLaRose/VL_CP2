# VL Classes Notes

# example 1
class Dog:
    def __init__(self, name, breed, age):
        self.name = name.capitalize()
        self.breed = breed.title()
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}\n"
    
    def speak(self):
        return f'{self.name}: "Bark"'


doug = Dog("Doug", "Golden Retreiver", 3)
pongo = Dog("Pongo", "Dalmation", 8)

# example 2
class ClassSubject:
    def __init__(self, name, room = None, teacher = "Ms.LaRose"):
        self.name = name.title()
        self.room = room
        self.teacher = teacher

    def __str__(self):
        return f"Name: {self.name}\nRoom: {self.room}\nTeacher: {self.teacher}\n"
    