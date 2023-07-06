# import modules for design
from colorama import init, Fore
from pyfiglet import Figlet

# import Car from car_class.py
from car_class import Car

# car object
car = Car(2022, "Example Make")

# call the accelerate method five times. 
print("Accelerating: ")
for i in range(5):
    car.accelerate()
    print(f"Current Speed: {car.get_speed()}")

# call the brake method five times. 
print("Braking: ")
for i in range(5):
    car.brake()
    print(f"Current Speed: {car.get_speed()}")