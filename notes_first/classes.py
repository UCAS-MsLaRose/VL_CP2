# VL Classes Notes

#example 1
class Animal:
    def __init__(self, name, species, age):
        self.name = name.capitalize()
        self.species = species.capitalize()
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nspecies: {self.species}\nage: {self.age}"
    
    def birthday(self):
        self.age += 1

dog = Animal("Doug", "Dog", 4)
bunny = Animal("Judy", "Rabbit", 20)
print(dog)
print(bunny)
dog.birthday()
print(dog)

# Example 2
class ClassPeriod:
    def __init__(self, subject, teacher = "Ms. LaRose", room = None):
        self.subject = subject.title()
        self.teacher = teacher
        self.room = room
    
    def __str__(self):
        return f"Subject: {self.subject}\nTeacher: {self.teacher}\nRoom: {self.room}\n"
    
