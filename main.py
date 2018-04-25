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
    brand = input("Please enter the brand of the vehicle: ")
    model = input("Please enter the model of the vehicle: ")
    km_done = input("Please enter the current mileage of the vehicle: ")
    service_date = input("Please enter the last service date: ")
    new = Vehicle(brand=brand, model=model, km_done=km_done, service_date=service_date)
    cars.append(new)

# Edit a car's record
def editCar(cars):
    print("Please select the ID of the vehicle that you want to edit from the list below.")
    for index_number, car in enumerate(cars): #Print a list of all vehicles in DB
        print(str(index_number) + " " + car.getCarNameModel())
    selected_id = input("Please enter the ID of the vehicle for which you want to edit data: ")
    selected_vehicle = cars[int(selected_id)] #convert selected ID to an integer for the editCar argument

    new_mileage = input("Please enter the new mileage number for %s " % selected_vehicle.getCarNameModel())
    selected_vehicle.km_done = new_mileage

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

        #User chooses an action
        selection = input("Enter your selection" + color.BOLD + "(a, b, c, d, e)" + color.END +": ")
        print(" ") # empty line

        if selection.lower() == "a":
            listAllCars(cars)
            print("") #print empty line
            input("Press any key to choose another action...")
        if selection.lower() == "b":
            addNewCar(cars)
        if selection.lower() == "c":
            editCar(cars)
        if selection.lower() == "d":
            deleteCar(cars)
main()


