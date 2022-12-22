# Driver:    Christian Taylor          U-Number: U75799592       Participation percentage: 50%
# Navigator: Anshul Raghuvanshi        U-Number: U69656337       Participation percentage: 50%
# This program allows us to update the attributes of a pet object given the user-inputted name, type and age.

class Pet:
    def __init__(self):
        self.__name = "Not provided"
        self.__type = "Not provided"
        self.__age = 0

    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__type
    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name
    def set_type(self, type):
        self.__type = type
    def set_age(self, age):
        self.__age = age

    def pricePerHour(self):
        return self.ticketPrice / self.hoursOpen

def main():
    # creating an instance of Pet class
    p = Pet()
    print("A pet object has been created. \nHere is the initial information about the pet:")
    print("Name of pet:", p.get_name())
    print("Type of pet:", p.get_type())
    print("Age of pet:", p.get_age())
    print("\nLet's update the information for a pet!")
    name = input("Enter the pet's name: ")
    p.set_name(name)
    type = input("Enter the type of animal: ")
    p.set_type(type)
    age = int(input("Enter the pet's age: "))
    p.set_age(age)
    print("\nHere is the updated information about the pet:")
    print("Name of pet:", p.get_name())
    print("Type of pet:", p.get_type())
    print("Age of pet:", p.get_age())

    # creating an instance of Pet class
    p = Pet()
    print("\nAnother pet object has been created. \nHere is the initial information about the pet:")
    print("Name of pet:", p.get_name())
    print("Type of pet:", p.get_type())
    print("Age of pet:", p.get_age())
    print("\nLet's update the information for a pet!")
    name = input("Enter the pet's name: ")
    p.set_name(name)
    type = input("Enter the type of animal: ")
    p.set_type(type)
    age = int(input("Enter the pet's age: "))
    p.set_age(age)
    print("\nHere is the updated information about the pet:")
    print("Name of pet:", p.get_name())
    print("Type of pet:", p.get_type())
    print("Age of pet:", p.get_age())

main()