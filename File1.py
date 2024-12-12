class Vehicle:
    def __init__(self, make, model, year):   #This creates the class Vehicle and stores the attributes make, model and year in the class.
        self.make = make   #This assigns the make of the vehicle to the variable self.make.
        self.model = model   #This assigns the model of the vehicle to the variable self.model.
        self.year = year   #This assigns the year of the vehicle to the variable self.year.

    def car_info(self):   #This defines the method that outputs the vehicles make, model and year from the class vehicle.
        return f"{self.make}, {self.model}, {self.year}"  #This returns the vehicles make, model and year.

class Car(Vehicle):
    def __init__(self, make, model, year, value): #This creates the class Car that inherits the attributes from the vehicle class and also stores the attribute value.
        super().__init__(make, model, year)   #The function super() initialises the attributes of the vehicle class so the car class can inherit them.
        self.value = value   #This assigns the value of the car to the variable self.value.

    def car_info(self):   #This combines the output of the first method with this one to also output the value of the car aswell.
        return f"{super().car_info()} , £{self.value}"   #This returns the inherited info from the vehicle class and the value of the car.

car1 = Car("Mercedes", "Sprinter", 2022, 23000)   #This stores the attributes of the vehicle to the variable car1.
print(car1.car_info())
car2 = Car("Range Rover", "Sport", 2019, 48990)   #This stores the attributes of the vehicle to the variable car2.
print(car2.car_info())


