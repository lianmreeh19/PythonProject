class Vehicle:
    def __init__(self):
        print("into Vehicle Class")

    def calc_distance(self, time, speed):
        print(f"calculate distance with time {time} and speed {speed}")
        distance = time * speed
        print(f"the distance is {distance}")
        return distance

    def ticket_price(self, distance):
        if distance >= 100:
            print("you should pay the ticket")

