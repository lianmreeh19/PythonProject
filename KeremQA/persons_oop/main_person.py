from KeremQA.persons_oop.driver import Driver
from KeremQA.persons_oop.person_parent import Person
from KeremQA.persons_oop.student import Student

student_1 = Student("Lian", "Mreeh")
student_2 = Student("Liraz", "Daxa")
student_3 = Student("Noor")

avg1 = student_1.get_average_score([100, 95, 90, 88, 60])
avg2 = student_2.get_average_score([74, 99, 62, 80, 100])
student_1.get_average_score([92, 87, 70, 66, 90]) # example of using function without getting the return value
if avg1 > avg2:
    print("Avg1 is higher than avg2")
else:
    print("Avg2 is lower higher avg1")

student_1.age_calculator(22)
student_2.age_calculator(16)

person_1 = Person(18)
person_2 = Person(10)

age1 = person_1.age_calculator(18)
age2 = person_2.age_calculator(10)


driver_1 = Driver("B")
driver_2 = Driver("C")

driver_1.get_license_level()
driver_2.get_license_level()


