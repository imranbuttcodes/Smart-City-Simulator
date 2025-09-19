#this is the base Building class
class Building:
    def __init__(self,name,type,power = 0):
        self.name = name
        self.type = type
        self.power = power
    def supply_power(self,amount):
        self.power += amount
    def consume_energy(self,amount):
        self.power -= amount
    def __str__(self):
        return f"------ Info ------\nName: {self.name}\nBuilding Type:{self.type}\Current Power:{self.power}"
    def __eq__(self, value):
        return self.type == value.type
    