# create a class named Pet 
class Pet:
    # class attributes
    def __init__(self):
        self.__name = " "
        self.__animal_type = " "
        self__age = 0

    # set and get for __name field
    def set_name (self, name):
        self.__name = name
    def get_name (self):
        return self.__name
    
        # set and get for __animal_type field
    def set_animal_type (self, animal_type):
        self.__animal_type = animal_type
    def get_animal_type (self):
        return self.__animal_type
    
    # set_animal_type()
    # This method assigns a value to the _ _animal_type field.
    # set_age()
    # This method assigns a value to the _ _age field.
    # get_name()
    # This method returns the value of the _ _ name field.
    # get_animal_type()
    # This method returns the value of the _ _animal_type field.
    # get_age()
    # This method returns the value of the _ _age field.

# Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet. This data should be stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.
