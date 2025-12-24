class Animal:
    def __init__(self):
        pass

    def get_legs_from_db_into_animal_parent(self, legs_amount):
        if legs_amount == 4:
            print("You have 4 legs")
        else:
            legs_amount = 4
            print("legs amount changed to 4")
        return legs_amount

    def make_sound(self, sound):
        print(f"the animal's sound is {sound}")