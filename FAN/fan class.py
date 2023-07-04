# create a class named Fan to represent a fan
class Fan:

    # constants representing the fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, radius = 5, color = "Blue", on = False):
        # A private int data field named speed that specifies the speed of the fan.
        self.__fan_speed = speed
        # A private bool data field named on that specifies whether the fan is on (the default is False).
        self.__fan_status = on
        # A private float data field named radius that specifies the radius of the fan.
        self.__fan_radius = radius
        # A private string data field named color that specifies the color of the fan.
        self.__fan_color = color

# The accessor(getters)  and mutator(setters)  methods for all four data fields.
# A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
# Write a test program named TestFan that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object’s speed, radius, color, and on properties.
