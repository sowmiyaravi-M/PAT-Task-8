# Function to create proper member variable

class Circle:
    def __init__(self, radius):
        self._radius = radius  # underscore (_) indicates a protected variable
        self._pi = 3.141  # private variable

    def area(self):
        area = self._pi * (self._radius ** 2)
        return area

    def circumference(self):
        circumference = 2 * self._pi * self._radius
        return circumference


circle = Circle(radius=5)
area = circle.area()
circumference = circle.circumference()

print(f"Radius: {circle._radius}")  # Accessing protected variable
print(f"Area: {area}")
print(f"Circumference: {circumference}")



