class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.make}, {self.model}, {self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, value):
        super().__init__(make, model, year)
        self.value = value

    def car_info(self):
        return f"{super().car_info()} , £{self.value}"

car1 = Car("Mercedes", "Sprinter", 2022, 23000)
print(car1.car_info())
car2 = Car("Range Rover", "Sport", 2019, 48990)
print(car2.car_info())


