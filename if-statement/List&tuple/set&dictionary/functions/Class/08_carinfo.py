class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
car1 = Car("Honda", "Red")
car2 = Car("BMW", "Black")
        
print("Car 1 Details:")
print("Brand:", car1.brand)
print("Color:", car1.color)

print("\nCar 2 Details:")
print("Brand:", car2.brand)
print("Color:", car2.color)