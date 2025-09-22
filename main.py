# this is the base Building class
from building import Building
from traffic_light import Traffic
from citizen import Citizen
from city1 import City
from vahical import Vahical


def main():
    # Create city
    city = City("Smartville")

    # Add buildings
    b1 = Building("Central Hospital", "hospital")
    b2 = Building("Green Apartments", "residential")
    city.add_entity(b1)
    city.add_entity(b2)

    # Add citizens
    c1 = Citizen("Ali", 25, "Engineer", b2)
    c2 = Citizen("Sara", 30, "Doctor", b1)
    city.add_entity(c1)
    city.add_entity(c2)

    # Add vehicles
    v1 = Vahical("Car", fuel=100, speed=60)
    v2 = Vahical("Bus", fuel=200, speed=40)
    city.add_entity(v1)
    city.add_entity(v2)

    # Simulation
    c1.go_to_work(v1)  # Ali drives car
    c2.go_to_work(v2)  # Sara takes bus
    print(len(c1))  # Age of citizen
    print(v1 - 20)  # Fuel reduced
    print(v1 + v2)  # Carpooling

    # Traffic light
    light = Traffic("Main Road")
    print(light)  # Red
    light.change_state()
    print(light)  # Green


main()
