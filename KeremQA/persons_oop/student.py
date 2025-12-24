from KeremQA.persons_oop.person_parent import Person

class Student(Person):
    def __init__(self, first_name, last_name="Mreeh"):
        self.first_name = first_name
        self.last_name = last_name

    def get_average_score(self, grades):
        sum = 0
        for grade in grades:
            sum += grade
        avg = sum/len(grades)
        print(f"The average score is: {avg}")
        return avg
