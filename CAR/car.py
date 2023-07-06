# import modules for design
from colorama import init, Fore
from pyfiglet import Figlet

# import Car from car_class.py
from car_class import Car

init() # initialize colorama
font_style = Figlet(font="standard")

# car object
car = Car(2022, "Example Make")

# call the accelerate method five times. 
print(Fore.GREEN + "Accelerating: ")
for i in range(5):
    car.accelerate()
    print(f"Current Speed: {Fore.GREEN}{car.get_speed()}")

# call the brake method five times. 
print(Fore.RED + "\nBraking: ")
for i in range(5):
    car.brake()
    print(f"Current Speed: {Fore.RED}{car.get_speed()}")