class Vahical:
    def __init__(self, type, fuel, speed):
        self.type = type
        self.fuel = fuel
        self.speed = speed

    def move(self):
        print(f"{self.type} started moving!")

    def refuel(self, amount):
        self.fuel += amount

    def __add__(self, value):
        return "carpooling"

    def __sub__(self, value):
        self.fuel - value
        return f"Fuel reduced to {value}"
