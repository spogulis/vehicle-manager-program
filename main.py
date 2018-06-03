#Import datetime library
from datetime import datetime
from Vehicle import Vehicle

def list_all_cars(cars):
    for index, car in enumerate(cars):
        print(" ")
        print("ID: %s" % str(index + 1))
        print(car.print_car())
    if not cars:
        print("You don't have any cars in your database")

def add_new_car(cars):
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
    # new = Vehicle(brand=brand, model=model, km_done=km_done, service_date=service_date)
    new_car = Vehicle(brand, model, km_done, service_date)
    cars.append(new_car)

def edit_car(cars):
    print("Please select the ID of the vehicle that you want to edit from the list below.")
    index = 0
    for car in cars: #Print a list of all vehicles in DB
        print("")
        print("ID: %s" % (index + 1))
        print("Brand and model: %s %s" % (car.brand, car.model))
        print("")
        index += 1

    #Check for selection input
    while True:
        try:
            selected_id = input("Car ID: ")
            selected_id = int(selected_id) - 1
            selected_vehicle = cars[int(selected_id)] #convert selected ID to an integer for the editCar argument
            break
        except ValueError:
            print("")
            print("Sorry, selection can only be a digit from the list above. Please try again!")

    #Ask what data the user wants to edit
    print("What data would you like to edit for vehicle \"%s %s\" with the ID: %s" % (selected_vehicle.brand, selected_vehicle.model, str(selected_id)))
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
                new_mileage = input("Please enter the new mileage number for record with the ID %s " % str(selected_id))
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
    print("") # empty line

def delete_car(cars):
    print("Please select the ID of the vehicle that you want to remove from the list below")
    for index_number, car in enumerate(cars):
        print(str(index_number + 1) + " " + car.get_car_name_model())  # Print a list of all vehicles in DB

    while True:
        try:
            selected_id = input("Delete vehicle with the ID: ")
            if not selected_id:
                print("Sorry, the field cannot be empty.")
            elif selected_id.isdigit() and int(selected_id) <= len(cars):
                break
            else:
                print("Sorry, try again")
        except IOError:
            print("Sorry, an unexpected error occured. Please try again!")
    selected_vehicle = cars[int(selected_id) - 1]  # convert selected ID to an integer for the deleteCar argument

    #Delete car
    cars.remove(selected_vehicle)
    print("") # print empty line
    print("Vehicle with the ID: %s has been deleted from the system" % str(selected_id))
    print("")

def read_from_file(filename):
    try:
        cars = []
        with open(filename, "r", encoding="utf-8") as file_handle:
            lines = file_handle.read().splitlines()
            for line in lines:
                car = Vehicle() #init empty car object
                car.read_from_file_line(line) #populate empty object with line data
                cars.append(car)
            return cars
    except IOError:
        return []

def write_to_file(filename, cars):
    if len(cars) > 0:
        with open(filename, "w+", encoding="utf-8") as file_handle:
            for car in cars:
                line = car.generate_file_line()
                file_handle.write(line)
    return True

#Main program logic


def main():
    print("Welcome!")
    print("---------------------------------------------------------------------------------")
    # Filename variable
    filename = "list.txt"
    # Cars list
    cars = read_from_file(filename)
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
        print("---------------------------------------------------------------------------------")

        #User chooses an action
        selection = input("Enter your selection(a, b, c, d, e): ")
        selection = selection.lower()
        print(" ") # empty line

        if selection == "a":
            list_all_cars(cars)
            print("") #print empty line
            input("Press \"Enter\" to choose another action...")
        if selection == "b":
            add_new_car(cars)
            write_to_file(filename, cars)
        if selection == "c" and len(cars) == 0:
            print("Sorry, there are no cars in your list to edit.")
        elif selection == "c":
            edit_car(cars)
        if selection == "d" and len(cars) == 0:
            print("Sorry, there are no cars in your list to delete.")
        elif selection == "d":
            delete_car(cars)
        if selection == "e":
            print("Thank you for using this software, goodbye!")
            write_to_file(filename, cars)
            break
# main()


