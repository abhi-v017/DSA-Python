class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius
    
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Different class with same function name

x = Circle(5)
y = Rectangle(4, 6)

print("Area of Circle:", x.area())
print("Area of Rectangle:", y.area())