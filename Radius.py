import math   #This imports the math module that allows us to use pi.

class Circle:
    def __init__(self, radius):   #This initialises the object radius to the class circle.
        if radius < 0:
            raise ValueError("The radius cannot be negative.")   #This raises a value error if the radius is negative and outputs this sentence.
        self.radius = float(radius)   #This converts the radius into a float to allow decimal numbers.

    def diameter(self):    
        return (self.radius * 2)   #This returns the value of the radius multiplied by 2.
    
    def circumference(self):
        return (2 * math.pi * self.radius)   #This returns the value of circumference by using math.pi instead of 3.14.

    def area(self):
        return (math.pi * self.radius ** 2)   #This returns the value of the area.