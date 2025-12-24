from kerem_qa.animals_oop.cat_child import Cat
from kerem_qa.animals_oop.dog_child import Dog

cat_1 = Cat("sushi", color = "gray")
cat_2 = Cat("honey", color = "white")
dog_1 = Dog("shoko", 3)

print(cat_1.name)
print(cat_2.name)
print(dog_1.name)

cat_1.make_noise_by_cat()
cat_2.make_noise_by_cat()
dog_1.make_sound("haou")
cat_legs = cat_1.get_legs_from_db_into_animal_parent(3)
cat_2.get_legs_from_db_into_animal_parent(4)
dog_legs = dog_1.get_legs_from_db_into_animal_parent(5)
dog_1.get_eyes_color()
cat_2.get_legs_from_db_into_animal_parent(6)

if cat_legs == dog_legs:
    print("legs amount is equal")
