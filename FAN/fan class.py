# create a class named Fan to represent a fan
class Fan:

    # constants representing the fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, radius = 5, color = "Blue", on = False):
        # a private int data field named speed that specifies the speed of the fan.
        self.__fan_speed = speed
        # a private bool data field named on that specifies whether the fan is on (the default is False).
        self.__fan_status = on
        # a private float data field named radius that specifies the radius of the fan.
        self.__fan_radius = radius
        # a private string data field named color that specifies the color of the fan.
        self.__fan_color = color

    # the accessor(getters)  and mutator(setters)  methods for all four data fields.
    # for fan speed
    def get_fan_speed(self):
        return self.__fan_speed
    def set_fan_speed(self, speed):
        self.__fan_speed = speed

    # for fan status
    def get_fan_status(self):
        return self.__fan_status
    def set_fan_status(self, on):
        self.__fan_status = on

    # for fan radius
    def get_fan_radius(self):
        return self.__fan_radius
    def set_fan_radius(self, radius):
        self.__fan_radius = radius
    
    # for fan color
    def get_fan_color(self):
        return self.__fan_color
    def set_fan_color(self, color):
        self.__fan_color = color