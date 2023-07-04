# Write a test program named TestFan that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object’s speed, radius, color, and on properties.
from fan_class import Fan
# create a test program with class namednTestFan
class TestFan:
    def test(self):

        Fan_1 = Fan(Fan.FAST, 10, "Yellow", True)
        Fan_2 = Fan(Fan.MEDIUM, 5, "Blue", False)