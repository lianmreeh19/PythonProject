from KeremQA.persons_oop.person_parent import Person

class Driver(Person):
    def __init__(self, license_level):
        self.license_level = license_level

    def get_license_level(self):
        print(f"license level is: {self.license_level}")

