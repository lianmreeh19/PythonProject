from kerem_qa.vehicle_oop.car import Car
from kerem_qa.vehicle_oop.motorcycle import Motorcycle
from kerem_qa.vehicle_oop.train import Train
from kerem_qa.vehicle_oop.vehicle import Vehicle

car_1 = Car(2023, "Nissan")
car_2 = Car(2020, "cherry")
motor_1 = Motorcycle()
train = Train(True)
vehicle = Vehicle()

car_1.car_tax_calculate(3, 120000)
distance_1 = car_2.calc_distance(2, 60)
distance_train = train.calc_distance(4, 140)
motor_1.tax_calculator(4, 45, 80000)
vehicle.ticket_price(distance_1)
vehicle.ticket_price(distance_train)
car_1.get_years(2025)
