from kerem_qa.animals_oop.animal_parent import Animal

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_eyes_color(self, eye_color="blue"):
        print(f"the dog eyes has color {eye_color}")