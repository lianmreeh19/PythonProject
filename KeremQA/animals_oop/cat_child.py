from kerem_qa.animals_oop.animal_parent import Animal

class Cat(Animal):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_noise_by_cat(self):
        print("meow")