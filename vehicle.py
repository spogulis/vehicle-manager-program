#Define vehicle class
class Vehicle:
    def __init__(self, brand="", model="", km_done=0, service_date=""):
        self.brand = brand
        self.model = model
        self.km_done = km_done
        self.service_date = service_date

    # Get car brand and model
    def get_car_name_model(self):
        return self.brand + " " + self.model

    #Read from file line (format: Tesla--Roadster--10000--01.01.2018)
    def read_from_file_line(self, line):
        car_data = line.split("--")
        self.brand = car_data[0]
        self.model = car_data[1]
        self.km_done = car_data[2]
        self.service_date = car_data[3]

    #Print car data
    def print_car(self):
        s = ""
        s += "Brand and model: %s %s\n" % (self.brand, self.model)
        s += "Mileage: %s\n" % self.km_done
        s += "Last service date: %s\n" % self.service_date

        return s

    #Generate file line
    def generate_file_line(self):
        car_record_line = "%s--%s--%s--%s\n" % (
            self.brand, self.model, self.km_done, self.service_date)
        return car_record_line

    #Write to file
    def write_to_file(self, filename, cars):
        if len(cars) > 0:
            with open(filename, "w+", encoding="utf-8") as file_handle:
                for car in cars:
                    line = car.generate_file_line()
                    file_handle.write(line)
        return True

