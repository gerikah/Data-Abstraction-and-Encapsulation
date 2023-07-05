# import Pet from pet_class.py
from pet_class import Pet

# object of the Pet class
pet = Pet()

# prompts the user to enter the name, type, and age of his or her pet
name = input ("Enter the name of your pet: ")
animal_type = input ("Enter the type of animal your pet is: ")
age = int(input("Enter the age of your pet: "))

# setting the attributes
pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)

# display the informations
print("Pet Details")
print("Pet's Name:", pet.get_name())
print("Animal Type:", pet.get_animal_type())
print("Age:", pet.get_age())