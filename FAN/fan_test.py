# import modules
from colorama import init, Fore
from pyfiglet import Figlet

# import Fan from fan_class.py 
from fan_class import Fan

init() # initialize colorama

# create a test program with class namednTestFan
class TestFan:
    def run_test(self):

        # two Fan objects
        Fan_1 = Fan(Fan.FAST, 10, "Yellow", True)
        Fan_2 = Fan(Fan.MEDIUM, 5, "Blue", False)

        # for fan 1
        print(Fore.CYAN + "Fan 1")
        print("Speed: ", Fan_1.get_fan_speed())
        print("Radius:", Fan_1.get_fan_radius())
        print("Color:", Fan_1.get_fan_color())
        print("Status (On):", Fan_1.get_fan_status())

        # for fan 2
        print(Fore.MAGENTA + "\nFan 2")
        print("Speed:", Fan_2.get_fan_speed())
        print("Radius:", Fan_2.get_fan_radius())
        print("Color:", Fan_2.get_fan_color())
        print("Status (On):", Fan_2.get_fan_status())   

# run the test 
test = TestFan()
test.run_test()