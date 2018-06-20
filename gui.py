import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from vehicle import Vehicle
from datetime import datetime

def read_from_file(filename):
    try:
        MainWindow.cars = []
        with open(filename, "r", encoding="utf-8") as file_handle:
            lines = file_handle.read().splitlines()
            for line in lines:
                car = Vehicle()  # init empty car object
                car.read_from_file_line(line)  # populate empty object with line data
                MainWindow.cars.append(car)
            return MainWindow.cars
    except IOError:
        return []

def write_to_file(filename):
    cars = MainWindow.cars
    if len(cars) > 0:
        with open(filename, "w+", encoding="utf-8") as file_handle:
            for car in cars:
                line = car.generate_file_line()
                file_handle.write(line)
    return True


class MainWindow(QWidget):
    filename = "list.txt"
    switch_window = QtCore.pyqtSignal()
    add_car_signal = QtCore.pyqtSignal()
    edit_car_toggled = False
    delete_car_toggled = False
    add_car_toggled = False
    cars = []
    del_id = None

    def __init__(self):
        super(QWidget, self).__init__()
        self.setWindowTitle('Vehicle manager')

        def add_car_dialog(self):

            def add_car_submit():
                filename = "list.txt"
                cars = read_from_file(filename)
                brand = self.brand_input.text()
                model = self.model_input.text()
                km_done = self.mileage_input.text()
                service_date = self.date_input.text()

                new_car = Vehicle(brand, model, km_done, service_date)
                cars.append(new_car)

                if len(cars) > 0:
                    with open(filename, "w+", encoding="utf-8") as file_handle:
                        for car in cars:
                            line = car.generate_file_line()
                            file_handle.write(line)
                self.brand_input.setText("")
                self.model_input.setText("")
                self.mileage_input.setText("")
                self.date_input.setText("")

            def check_fields():
                brand_f = self.brand_input.text()
                model_f = self.model_input.text()
                mileage_f = self.mileage_input.text()
                date_f = self.date_input.text()

                if brand_f == "" or model_f == "" or mileage_f == "" or date_f == "":
                    self.submit_btn.setEnabled(False)
                else:
                    try:
                        datetime.strptime(date_f, "%d.%m.%Y")
                        self.submit_btn.setEnabled(True)
                    except ValueError:
                        self.edit_date_label.setToolTip("A valid date is dd.mm.yyyy")
                        self.submit_btn.setEnabled(False)

            self.brand_label = QLabel("Enter brand name: ")
            self.brand_input = QLineEdit()
            self.brand_label.setHidden(True)
            self.brand_input.setHidden(True)
            self.brand_input.textChanged[str].connect(check_fields)

            self.model_label = QLabel("Enter model name: ")
            self.model_input = QLineEdit()
            self.model_label.setHidden(True)
            self.model_input.setHidden(True)
            self.model_input.textChanged[str].connect(check_fields)

            self.mileage_label = QLabel("Enter current mileage: ")
            self.mileage_input = QLineEdit()
            self.mileage_label.setHidden(True)
            self.mileage_input.setHidden(True)
            self.mileage_input.textChanged[str].connect(check_fields)

            self.date_label = QLabel("Enter last service date: ")
            self.date_input = QLineEdit()
            self.date_label.setHidden(True)
            self.date_input.setHidden(True)
            self.date_input.textChanged[str].connect(check_fields)

            self.submit_btn = QPushButton("Submit")
            self.submit_btn.setHidden(True)
            self.submit_btn.setEnabled(False)

            self.sublayout.addWidget(self.brand_label, 1, 0)
            self.sublayout.addWidget(self.brand_input, 1, 1, 1, 5)
            self.sublayout.addWidget(self.model_label, 2, 0)
            self.sublayout.addWidget(self.model_input, 2, 1, 1, 5)
            self.sublayout.addWidget(self.mileage_label, 3, 0)
            self.sublayout.addWidget(self.mileage_input, 3, 1, 1, 5)
            self.sublayout.addWidget(self.date_label, 4, 0)
            self.sublayout.addWidget(self.date_input, 4, 1, 1, 5)
            self.sublayout.addWidget(self.submit_btn, 5, 1, 1, 5)

            # self.brand_input.textChanged[str].connect(lambda: self.submit_btn.setEnabled(self.brand_input.text() != ""))


            self.submit_btn.clicked.connect(add_car_submit)

        def show_add_car_dialog():
            if not MainWindow.add_car_toggled and not MainWindow.edit_car_toggled and not MainWindow.delete_car_toggled:
                self.brand_label.setHidden(False)
                self.brand_input.setHidden(False)
                self.model_label.setHidden(False)
                self.model_input.setHidden(False)
                self.mileage_label.setHidden(False)
                self.mileage_input.setHidden(False)
                self.date_label.setHidden(False)
                self.date_input.setHidden(False)
                self.submit_btn.setHidden(False)
                self.setFixedHeight(550)
                MainWindow.add_car_toggled = not MainWindow.add_car_toggled
            elif MainWindow.add_car_toggled:
                self.brand_label.setHidden(True)
                self.brand_input.setHidden(True)
                self.model_label.setHidden(True)
                self.model_input.setHidden(True)
                self.mileage_label.setHidden(True)
                self.mileage_input.setHidden(True)
                self.date_label.setHidden(True)
                self.date_input.setHidden(True)
                self.submit_btn.setHidden(True)
                self.setFixedHeight(290)
                MainWindow.add_car_toggled = not MainWindow.add_car_toggled

        def delete_car_dialog(self):
            self.delete_car_label = QLabel("Enter the ID of the car you'd like to delete")
            self.val = QIntValidator(1, len(MainWindow.cars))
            self.del_input = QLineEdit()

            self.spinbox = QSpinBox()
            self.spinbox.setMinimum(1)
            self.spinbox.setMaximum(len(MainWindow.cars))
            self.spinbox.setSingleStep(1)
            self.spinbox.setValue(1)

            # self.del_input.setValidator(self.val)
            self.del_btn = QPushButton("Delete", enabled=True)
            self.delete_car_label.setHidden(True)
            # self.del_input.setHidden(True)
            self.spinbox.setHidden(True)
            self.del_btn.setHidden(True)
            self.sublayout.addWidget(self.delete_car_label, 6, 0, 1, 3)
            self.sublayout.addWidget(self.spinbox, 6, 4, 1, 1)
            self.sublayout.addWidget(self.del_btn, 6, 5)

        def show_delete_car_dialog():

            def del_clicked():
                del_id = self.spinbox.value()
                del_id = int(del_id) - 1
                filename = "list.txt"
                read_from_file(filename)
                MainWindow.cars.remove(MainWindow.cars[del_id])
                write_to_file(filename)
                self.spinbox.setValue(1)
                self.spinbox.setMaximum(len(MainWindow.cars))

            if not MainWindow.delete_car_toggled and not MainWindow.add_car_toggled and not MainWindow.edit_car_toggled:
                self.delete_car_label.setHidden(False)
                self.spinbox.setHidden(False)
                self.del_btn.setHidden(False)
                self.setFixedHeight(350)
            elif MainWindow.delete_car_toggled and not MainWindow.add_car_toggled and not MainWindow.edit_car_toggled:
                self.delete_car_label.setHidden(True)
                self.spinbox.setHidden(True)
                self.del_btn.setHidden(True)
                self.setFixedHeight(290)

            MainWindow.delete_car_toggled = not MainWindow.delete_car_toggled
            # Del toggled
            self.del_btn.clicked.connect(del_clicked)

        def edit_car_dialog(self):

            def edit_car_submit():
                filename = "list.txt"
                cars = read_from_file(filename)

                selected_vehicle = MainWindow.cars[self.sel_edit_id]
                selected_vehicle.brand = self.edit_brand_input.text()
                selected_vehicle.model = self.edit_model_input.text()
                selected_vehicle.km_done = self.edit_mileage_input.text()
                selected_vehicle.service_date = self.edit_date_input.text()

                if len(cars) > 0:
                    with open(filename, "w+", encoding="utf-8") as file_handle:
                        for car in cars:
                            line = car.generate_file_line()
                            file_handle.write(line)

            def update_edit_fields():
                self.sel_edit_id = self.edit_id.value() - 1
                self.edit_brand_input.setText(str(MainWindow.cars[self.sel_edit_id].brand))
                self.edit_model_input.setText(str(MainWindow.cars[self.sel_edit_id].model))
                self.edit_mileage_input.setText(str(MainWindow.cars[self.sel_edit_id].km_done))
                self.edit_date_input.setText(str(MainWindow.cars[self.sel_edit_id].service_date))

            def check_fields():
                brand_f = self.edit_brand_input.text()
                model_f = self.edit_model_input.text()
                mileage_f = self.edit_mileage_input.text()
                date_f = self.edit_date_input.text()

                if brand_f == "" or model_f == "" or mileage_f == "" or date_f == "":
                    self.edit_btn.setEnabled(False)
                else:
                    try:
                        datetime.strptime(date_f, "%d.%m.%Y")
                        self.edit_btn.setEnabled(True)
                    except ValueError:
                        self.edit_date_label.setToolTip("A valid date is dd.mm.yyyy")
                        self.edit_btn.setEnabled(False)

            self.edit_id_label = QLabel("Enter the ID of car you want to edit")
            self.edit_id = QSpinBox()
            self.edit_id.setMinimum(1)
            self.edit_id.setMaximum(len(MainWindow.cars))
            self.sel_edit_id = self.edit_id.value() - 1
            self.edit_id_label.setHidden(True)
            self.edit_id.setHidden(True)
            self.edit_id.valueChanged[str].connect(update_edit_fields)

            self.edit_brand_label = QLabel("Edit brand name to: ")
            self.edit_brand_input = QLineEdit()
            self.edit_brand_label.setHidden(True)
            self.edit_brand_input.setHidden(True)
            self.edit_brand_input.textChanged[str].connect(check_fields)

            self.edit_model_label = QLabel("Edit model name to: ")
            self.edit_model_input = QLineEdit()
            self.edit_model_label.setHidden(True)
            self.edit_model_input.setHidden(True)
            self.edit_model_input.textChanged[str].connect(check_fields)

            self.edit_mileage_label = QLabel("Edit current mileage to: ")
            self.edit_mileage_input = QLineEdit()
            self.edit_mileage_label.setHidden(True)
            self.edit_mileage_input.setHidden(True)
            self.edit_mileage_input.textChanged[str].connect(check_fields)

            self.edit_date_label = QLabel("Edit service date to: ")
            self.edit_date_input = QLineEdit()
            self.edit_date_label.setHidden(True)
            self.edit_date_input.setHidden(True)
            self.edit_date_input.textChanged[str].connect(check_fields)

            self.edit_btn = QPushButton("Edit")
            self.edit_btn.setHidden(True)
            self.edit_btn.setEnabled(False)

            self.sublayout.addWidget(self.edit_id_label, 1, 0)
            self.sublayout.addWidget(self.edit_id, 1, 1)
            self.sublayout.addWidget(self.edit_brand_label, 2, 0)
            self.sublayout.addWidget(self.edit_brand_input, 2, 1, 1, 5)
            self.sublayout.addWidget(self.edit_model_label, 3, 0)
            self.sublayout.addWidget(self.edit_model_input, 3, 1, 1, 5)
            self.sublayout.addWidget(self.edit_mileage_label, 4, 0)
            self.sublayout.addWidget(self.edit_mileage_input, 4, 1, 1, 5)
            self.sublayout.addWidget(self.edit_date_label, 5, 0)
            self.sublayout.addWidget(self.edit_date_input, 5, 1, 1, 5)
            self.sublayout.addWidget(self.edit_btn, 6, 1, 1, 5)
            update_edit_fields()
            self.edit_btn.clicked.connect(edit_car_submit)

        def show_edit_car_dialog():

            if not MainWindow.edit_car_toggled and not MainWindow.add_car_toggled and not MainWindow.delete_car_toggled:
                self.edit_id_label.setHidden(False)
                self.edit_id.setHidden(False)
                self.edit_brand_label.setHidden(False)
                self.edit_brand_input.setHidden(False)
                self.edit_model_label.setHidden(False)
                self.edit_model_input.setHidden(False)
                self.edit_mileage_label.setHidden(False)
                self.edit_mileage_input.setHidden(False)
                self.edit_date_label.setHidden(False)
                self.edit_date_input.setHidden(False)
                self.edit_btn.setHidden(False)
                self.setFixedHeight(570)
                MainWindow.edit_car_toggled = not MainWindow.edit_car_toggled
            elif MainWindow.edit_car_toggled:
                self.edit_id_label.setHidden(True)
                self.edit_id.setHidden(True)
                self.edit_brand_label.setHidden(True)
                self.edit_brand_input.setHidden(True)
                self.edit_model_label.setHidden(True)
                self.edit_model_input.setHidden(True)
                self.edit_mileage_label.setHidden(True)
                self.edit_mileage_input.setHidden(True)
                self.edit_date_label.setHidden(True)
                self.edit_date_input.setHidden(True)
                self.edit_btn.setHidden(True)
                self.setFixedHeight(290)
                MainWindow.edit_car_toggled = not MainWindow.edit_car_toggled

        read_from_file(MainWindow.filename)

        # Container frame
        self.main_CW = QWidget()

        # Main layout within container widget
        self.main_CL = QVBoxLayout(self.main_CW)
        self.main_CW.setLayout(self.main_CL)
        self.setFixedWidth(800)
        self.setFixedHeight(300)

        # Set self layout to main container layout
        self.setLayout(self.main_CL)

        #GRID layout
        self.main_grid = QGridLayout()
        self.main_CL.addLayout(self.main_grid) # add grid layout to main_CL
        self.main_grid.setSpacing(20)

        #Buttons
        self.list_all_cars_btn = QPushButton("List cars")
        self.list_all_cars_btn.setStyleSheet('background: rgb(142, 126, 111)')
        # self.list_all_cars_btn.setStyleSheet(')
        self.add_car_btn = QPushButton("Add car")
        self.add_car_btn.setStyleSheet('background: rgb(142, 126, 111)')
        self.edit_car_btn = QPushButton("Edit car")
        self.edit_car_btn.setStyleSheet('background: rgb(142, 126, 111)')
        self.delete_car_btn = QPushButton("Delete a car")
        self.delete_car_btn.setStyleSheet('background: rgb(142, 126, 111)')
        self.quit_btn = QPushButton("Quit")
        self.quit_btn.setStyleSheet('background: rgb(142, 126, 111)')
        self.quit_btn.setStatusTip('Quit the program')

        #List of labels
        self.list_all_cars_q = QLabel('Press this button to view all your cars')
        self.add_car_q = QLabel('Add a car to your database')
        self.edit_car_q = QLabel("Edit a car's record")
        self.delete_car_q = QLabel('Delete a car from database')

        #POSITIONS
        self.main_grid.addWidget(self.list_all_cars_q, 0, 0)
        self.main_grid.addWidget(self.list_all_cars_btn, 0, 2, 1, 1)
        self.main_grid.addWidget(self.add_car_q, 1, 0)
        self.main_grid.addWidget(self.add_car_btn, 1, 2, 1, 1)
        self.main_grid.addWidget(self.edit_car_q, 2, 0)
        self.main_grid.addWidget(self.edit_car_btn, 2, 2, 1, 1)
        self.main_grid.addWidget(self.delete_car_q, 3, 0)
        self.main_grid.addWidget(self.delete_car_btn, 3, 2, 1, 1)
        self.main_grid.addWidget(self.quit_btn, 4, 2, 1, 1)

        # Sublayout (add car & delete car)
        self.sublayout = QGridLayout()
        self.main_CL.addLayout(self.sublayout)

        # Insert car dialog below main window
        add_car_dialog(self)
        edit_car_dialog(self)
        delete_car_dialog(self)


        #BUTTON ACTIONS

        #Quit
        self.quit_btn.clicked.connect(QApplication.instance().quit)

        #List all cars (new window)
        self.list_all_cars_btn.clicked.connect(self.switch)

        #Show add car dialog
        self.add_car_btn.clicked.connect(show_add_car_dialog)

        #Show edit car dialog
        self.edit_car_btn.clicked.connect(show_edit_car_dialog)

        #Show delete car dialog
        self.delete_car_btn.clicked.connect(show_delete_car_dialog)


    def switch(self):
        self.switch_window.emit()


class ViewCars(QWidget):

    switch_window = QtCore.pyqtSignal()
    back_btn_status = True

    def __init__(self):
        super(QWidget, self).__init__()

        self.setWindowTitle("List of cars in file - Vehicle manager")
        self.setGeometry(1360, 30, 450, 800)

        # Scrolling widget
        widget = QWidget()
        # Layout of container widget
        layout = QGridLayout(self)

        # Set layout to widget
        widget.setLayout(layout)

        #Define filename and car list
        filename = "list.txt"
        cars = read_from_file(filename)

        # Generate car lines in window

        for index, car in enumerate(cars):
            id_line = QLabel('ID: {}'.format(str(index + 1)))
            model_brand_line = QLabel('{} {}'.format(car.brand, car.model))
            mileage_line = QLabel('Mileage: {}'.format(car.km_done))
            service_date_line = QLabel('Last service date: {}\n'.format(car.service_date))
            layout.addWidget(id_line)
            layout.addWidget(model_brand_line)
            layout.addWidget(mileage_line)
            layout.addWidget(service_date_line)

        # Scroll area
        self.scrollArea = QScrollArea()  # Def scrollarea
        # self.scrollArea.setGeometry(700, 400, 200, 300)  # Dimensions
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(False)

        #Assign widget to scrollarea
        self.scrollArea.setWidget(widget)

        v_layout = QGridLayout(self)
        v_layout.addWidget(self.scrollArea)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(self.switch)

        v_layout.addWidget(back_btn)
        if not ViewCars.back_btn_status:
            back_btn.setHidden(True)
        self.setLayout(v_layout)

        if not MainWindow.delete_car_toggled:
            MainWindow.edit_car_toggled = False
            MainWindow.add_car_toggled = False

    def switch(self):
        self.switch_window.emit()


class Controller:
    def show_main(self):
        self.window = MainWindow()
        self.window_car_list = ViewCars()
        self.window.switch_window.connect(self.show_car_list)
        self.window_car_list.close()
        self.window.show()
    def show_car_list(self):
        if not MainWindow.delete_car_toggled:
            self.window.close()
            ViewCars.back_btn_status = True
        if MainWindow.delete_car_toggled:
            ViewCars.back_btn_status = False
        self.window_car_list = ViewCars()
        self.window_car_list.switch_window.connect(self.show_main)
        self.window_car_list.show()
    def reopen_car_list(self):
        self.window_car_list = ViewCars()
        self.window_car_list.close()


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont('SansSerif', 20))
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


