from kerem_qa.vehicle_oop.vehicle import Vehicle

class Train(Vehicle):
    def __init__(self, is_light):
        self.is_light = is_light

    def get_passengers(self, train_cars):
        passengers = train_cars * 50
        print(f"Max amount of passengers on the train is {passengers}")