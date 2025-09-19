class Citizen:
    def __init__(self,name,age,job,building):
        self.name = name
        self.age = age
        self.job = job
        self.building = building
    def go_to_work(self,vahical):
        if vahical.type.lower() == "bus":
            print(f"{self.name} takes {vahical.type}")
        else:
            print(f"{self.name} drives {vahical.type}")
    def pay_bill(self):
        print(f"{self.name} paying bill")
    def use_transport(self):
        print(f"{self.name}  bill")
    def __len__(self):
        return self.age
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nJob: {self.job}\nBuilding: {self.building.type}"