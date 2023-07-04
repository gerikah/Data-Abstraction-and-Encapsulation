# Write a class named Car that has the following data attributes:
class Car:

    def __init__(self, year_model, make):

        # _ _year_model (for the car’s year model)
        self.__year_model = year_model
        # _ _make (for the make of the car)
        self.__make = make
        # _ _speed (for the car’s current speed)
        self.__speed = 0

    # The class should also have the following methods:
    # accelerate()
    def accelerate(self):
        self.__speed += 5
    # The accelerate method should add 5 to the speed data attribute each time it is called.
    
    # brake()
    def brake(self):
        self.__speed -= 5
    # The brake method should subtract 5 from the speed data attribute each time it is called.
    
    # get_speed()
    def get_speed(self):
        return self.__speed
    # The get_speed method should return the current speed.

# Next, design a program that creates a Car object then calls the accelerate method five times. After each call to the accelerate method, get the current speed of the car and display it. Then call the brake method five times. After each call to the brake method, get the current speed of the car and display it.
