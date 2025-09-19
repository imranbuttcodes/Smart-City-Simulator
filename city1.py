from building import Building
from citizen import Citizen
from  vahical import Vahical
from  traffic_light import Traffic

class City:
    def __init__(self,name):
        self.name = name
        self.list_buildings = []
        self.list_citizens = []
        self.list_vehicles = []
        self.list_traffic_lights = []
    def add_entity(self,entity):
        if isinstance(entity,Building):
            self.list_buildings.append(entity)
        elif isinstance(entity,Citizen):
            self.list_citizens.append(entity)
        elif isinstance(entity,Vahical):
            self.list_vehicles.append(entity)
        elif isinstance(entity,Traffic):
            self.list_traffic_lights.append(entity)
        else:
            print("Invalid entity entered!")
            return False
    def simulate_day(self):
        pass
    def __contains__(self,entity):
        if entity in self.list_buildings:
            return True
        if entity in self.list_citizens:
            return True
        if entity in self.list_vehicles:
            return True
        if entity in self.list_traffic_lights:
            return True
        return False
    def __len__(self):
        return len(self.list_buildings) + len(self.list_citizens) + len(self.list_traffic_lights) + len(self.list_vehicles)
    def report(self):
        print(f"\t\t\t------- The City {self.name} Report -------")
        print("\t\t\tTotal buildings in City")
        for no,b in enumerate(self.list_buildings):
            print(f"Building {(no+1)}: {b}")
        print("\t\t\tTotal Citizen in City")
        for no,c in enumerate(self.list_citizens):
            print(f"Citizen {(no+1)}: {c}")
        print("\t\t\tTotal Vahicels in City")
        for no,v in enumerate(self.list_vehicles):
            print(f"Vahicels {(no+1)}: {v}")
        print("\t\t\tTotal buildings in City")        
    def get_items(self,entity,idx):
        if isinstance(entity,Building):
            return f"{self.list_buildings[idx]}"
        elif isinstance(entity,Citizen):
            return f"{self.list_citizens[idx]}"
        elif isinstance(entity,Vahical):
            return f"{self.list_vehicles[idx]}"
        elif isinstance(entity,Traffic):
            return f"{self.list_traffic_lights[idx]}"
        else:
            print("Invalid entity entered!")
            return False

