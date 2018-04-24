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

#Main program logic
def main():
    print(color.BOLD + "Welcome!" + color.END)
    print(color.BOLD + "---------------------------------------------------------------------------------" + color.END)

    #Cars
    mercedes = Vehicle("Mercedes", "SLK", 100000, 2010)
    bmw = Vehicle("BMW", "Z4", 200000, 2009)
    audi = Vehicle("Audi", "A4", 300000, 2008)
    cars = [mercedes, bmw, audi]


    #Show options
    while True:
        print(" ")  # empty line
        print("Please choose one of these options: ")
        print("a) View all your cars")
        print("b) Add a new car record")
        print("c) Edit a car's record")
        print("d) Delete a car's record")
        print("e) Quit the program.")
        print(" ")  # empty line

        #User chooses an action
        selection = input("Enter your selection (a, b, c, d, e): ")
        print(" ") # empty line

        if selection.lower() == "a":
            listAllCars(cars)
            input("Press any key to choose another action...")
main()


