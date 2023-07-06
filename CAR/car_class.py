# Write a class named Car that has the following data attributes:
class Car:

    def __init__(self, year_model, make):

        # _ _year_model (for the car’s year model)
        self.__year_model = year_model
        # _ _make (for the make of the car)
        self.__make = make
        # _ _speed (for the car’s current speed)
        self.__speed = 0

    # accelerateadd -- 5 to the speed data attribute each time it is called
    def accelerate(self):
        self.__speed += 5
    
    # brake -- subtract 5 from the speed data attribute each time it is called
    def brake(self):
        self.__speed -= 5
    
    # get_speed -- return the current speed
    def get_speed(self):
        return self.__speed