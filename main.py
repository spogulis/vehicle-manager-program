# Import datetime library
from datetime import datetime

#Define vehicle class
class Vehicle:
    def __init__(self, brand, model, km_done, service_date):
        self.brand = brand
        self.model = model
        self.km_done = km_done
        self.service_date = service_date

    # Get car brand and model
    def getCarNameModel(self):
        return self.brand + " " + self.model
#Text effects
class color:

    BOLD = '\033[1m'
    END = '\033[0m'

# List all cars
def listAllCars(cars):
    for index_number, car in enumerate(cars):
        print(" ")
        print("ID: " + color.BOLD + str(index_number) + color.END)
        print("Brand and model: " + color.BOLD + str(car.getCarNameModel()) + color.END)
        print("Mileage: " + color.BOLD + str(car.km_done) + color.END)
        print("Last service date: " + color.BOLD + str(car.service_date) + color.END)
    if not cars:
        print("You don't have any cars in your database")

# Add new car to the list
def addNewCar(cars):
    #Check if data entered into brand variable is text
    while True:

        try:
            brand = input("Please enter the brand of the vehicle.")
            if brand.isalpha():
                break
            elif not brand:
                print("")
                print("Sorry, the brand field cannot be empty.")
                print("")
            elif brand.isdigit() or brand.isalnum() or float(brand):
                print("")
                print("Sorry, brand names usually don't contain numbers or decimals.")
                print("")
        except ValueError:
            print("")
            print("Sorry, this is not a valid brand name... Please try again!")
            print("")

    #Check if data entered into model is not empty
    while True:
        try:
            model = input("Please enter the model of the vehicle: ")
            if not model:
                print("Sorry, the model field cannot be empty.")
            elif model.isdigit() or model.isalnum() or float(model):
                break
        except ValueError:
            print("")
            print("Sorry, this is not a valid model... Please try again!")
            print("")

    #Check if data entered into mileage variable is a digit
    while True:
        try:
            km_done = input("Please enter the current mileage of the vehicle: ")
            if not km_done:
                print("Sorry, the mileage field cannot be empty.")
            elif km_done.isdigit():
                break
            elif km_done.isalpha() or km_done.isalnum() or float(km_done):
                print("Sorry, mileage cannot contain text, decimals or negative numbers")
        except ValueError:
            print("")
            print("Sorry, this is not a valid mileage... Please try again!")
            print("")

    # Check if data entered into service_date variable is in correct form
    while True:
        try:
            service_date = input("Please enter the last service date (dd.mm.yyyy: ")
            if not service_date:
                print("Sorry, the service date field cannot be empty.")
            if datetime.strptime(service_date, "%d.%m.%Y"):
                break
        except ValueError:
            print("")
            print("Sorry, this is not a valid date... Please try again!")
            print("")

    #Add vehicle to cars list
    new = Vehicle(brand=brand, model=model, km_done=km_done, service_date=service_date)
    cars.append(new)

# Edit a car's record
def editCar(cars):
    print("Please select the ID of the vehicle that you want to edit from the list below.")
    for index_number, car in enumerate(cars): #Print a list of all vehicles in DB
        print(str(index_number) + " " + car.getCarNameModel())

    while True:
        try:
            selected_id = input("Car ID: ")
            selected_vehicle = cars[int(selected_id)] #convert selected ID to an integer for the editCar argument
            break
        except ValueError:
            print("")
            print("Sorry, selection can only be a digit from the list above. Please try again!")

    #Ask if the user wants to edit mileage or last service date
    print("What data would you like to edit for vehicle \"%s\" with the ID: %s" % (cars[int(selected_id)].getCarNameModel(), str(selected_id)))
    print("1) Brand name")
    print("2) Model name")
    print("3) Mileage")
    print("4) Last service date")
    print("")

    #User selection
    while True:
        try:
            user_selection = input("Enter a number for the option you want from the list: ")
            if not user_selection:
                print("")
                print("Sorry, input field cannot be empty")
            elif user_selection == "1":
                new_brand_name = input("Please enter the new brand name for vehicle with the ID: %s" % str(selected_id))
                selected_vehicle.brand = new_brand_name
                break
            elif user_selection == "2":
                new_model_name = input("Please enter the new model name for vehicle with the ID: %s" % str(selected_id))
                selected_vehicle.model = new_model_name
                break
            elif user_selection == "3":
                new_mileage = input("Please enter the new mileage number for %s " % str(selected_id))
                selected_vehicle.km_done = new_mileage
                break
            elif user_selection == "4":
                try:
                    new_date = input("Please enter the newest service date (dd.mm.yyyy: ")
                    datetime.strptime(new_date, "%d.%m.%Y")
                    selected_vehicle.service_date = new_date
                    break
                except ValueError:
                    print("")
                    print("Sorry, this is not a valid date... Please try again!")
                    print("")
            else:
                print("Sorry, try again")
        except ValueError:
            print("")
            print("Sorry, this is not a valid selection... Please try again!")
            print("")


    #Change mileage number
    # new_mileage = input("Please enter the new mileage number for %s " % car.getCarNameModel())
    # selected_vehicle.km_done = new_mileage

    print("") # empty line
    print("New mileage updated!")

# Delete a car's record
def deleteCar(cars):
    print("Please select the ID of the vehicle that you want to remove from the list below")
    for index_number, car in enumerate(cars):
        print(str(index_number) + " " + car.getCarNameModel()) #Print a list of all vehicles in DB
    selected_id = input("Delete vehicle with the ID: ")
    selected_vehicle = cars[int(selected_id)] #convert selected ID to an integer for the deleteCar argument

    #Delete car
    cars.remove(selected_vehicle)
    print("") # print empty line
    print("Vehicle with the ID: %s has been deleted from the system" % str(selected_id))
    print("")

#Main program logic
def main():
    print(color.BOLD + "Welcome!" + color.END)
    print(color.BOLD + "---------------------------------------------------------------------------------" + color.END)

    #Cars
    cars = []

    #Show options
    while True:
        print(" ")  # empty line
        print(color.BOLD + "Please choose one of these options: " + color.END)
        print(color.BOLD + "a)" + color.END + "View all your cars")
        print(color.BOLD + "b)" + color.END + "Add a new car record")
        print(color.BOLD + "c)" + color.END + "Edit a car's record")
        print(color.BOLD + "d)" + color.END + "Delete a car's record")
        print(color.BOLD + "e)" + color.END + "Quit the program.")
        print(" ")  # empty line
        print(color.BOLD + "---------------------------------------------------------------------------------" + color.END)

        #User chooses an action
        selection = input("Enter your selection" + color.BOLD + "(a, b, c, d, e)" + color.END +": ")
        print(" ") # empty line

        if selection.lower() == "a":
            listAllCars(cars)
            print("") #print empty line
            input("Press \"Enter\" to choose another action...")
        if selection.lower() == "b":
            addNewCar(cars)
        if selection.lower() == "c" and len(cars) == 0:
            print("Sorry, there are no cars in your list to edit.")
            input("Please press Enter to choose another action!")
        elif selection.lower() == "c":
            editCar(cars)
        if selection.lower() == "d" and len(cars) == 0:
            print("Sorry, there are no cars in your list to delete.")
            input("Please press Enter to choose another action!")
        elif selection.lower() == "d":
            deleteCar(cars)
        if selection.lower() == "e":
            print("Thank you for using this software, goodbye!")
            break
main()


