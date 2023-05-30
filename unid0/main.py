from car import Car

# Create a new Car object.
car1 = Car("Nissan", "Sunny", "Silver", "1234ABC")

# Test functionality of the methods
print(car1.brand)
print(car1.fuel_indicator)
car1.switch_engine()
car1.fuel_refill(25.0)
print(car1.fuel_indicator)
car1.switch_engine()
car1.move(100)
car1.fuel_refill(50)
car1.move(1000)
car1.fuel_refill(50)
print(car1.fuel_indicator)
