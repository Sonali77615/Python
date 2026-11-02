class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create an object
rect = Rectangle(10, 5)

# Calculate and print area
print("Area of Rectangle:", rect.area())