# Function to create python class called circle with constructor

import math

class Circle:
    def __init__(self, list):
        self.radius = list

    def area(self):
        return [math.pi * r**2 for r in self.radius]

    def circumference(self):
        return [2 * math.pi * r for r in self.radius]


list = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(list)

areas = circle.area()
circumferences = circle.circumference()

print("List of radii:", list)
print("Areas:", areas)
print("Circumferences:", circumferences)
