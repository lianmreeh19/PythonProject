from kerem_qa.vehicle_oop.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self):
        pass

    def tax_calculator(self, time_on_street, tax_value, price):
        if time_on_street > 5:
            price = price +tax_value
        print(f"motorcycle price is {price}")
        return price
