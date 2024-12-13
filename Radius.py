import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("The radius cannot be negative.")
        self.radius = float(radius)

    def diameter(self):
        return (self.radius * 2)
    
    def circumference(self):
        return (2 * math.pi * self.radius)

    def area(self):
        return (math.pi * self.radius ** 2)