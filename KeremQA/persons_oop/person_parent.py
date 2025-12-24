class Person:
    def __init__(self, age):
        self.age = age

    def age_calculator(self, age):
        is_young = False
        if age >= 18:
            is_young = False
            print("You are older than 18 years old")
        else:
            print("You are younger than 18 years old")
            is_young = True
        return is_young

