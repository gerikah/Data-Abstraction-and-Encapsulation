from car_class import Car

# car object
car = Car(2022, "Example Make")

# then calls the accelerate method five times. 
print("Accelerating: ")
for i in range(5):
    car.accelerate()
    print(f"Current Speed: {car.get_speed()}")

# after each call to the accelerate method, get the current speed of the car and display it. 
# then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.
