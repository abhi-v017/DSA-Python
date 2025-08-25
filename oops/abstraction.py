from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
# Example usage
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f'The area of the shape is: {shape.area()}')# Demonstrating Abstraction in OOP