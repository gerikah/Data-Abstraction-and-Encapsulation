from car_class import Car

# car object
car = Car(2022, "Example Make")

# call the accelerate method five times. 
print("Accelerating: ")
for i in range(5):
    car.accelerate()
    print(f"Current Speed: {car.get_speed()}")

# then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.
print("Braking: ")
for i in range(5):
    car.brake()
    print(f"Current Speed: {car.get_speed()}")