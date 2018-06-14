import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from main import *
from vehicle import Vehicle


class MainWindow(QWidget):

    switch_window = QtCore.pyqtSignal()
    add_car_signal = QtCore.pyqtSignal()
    delete_car_toggled = False

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

            self.brand_label = QLabel("Enter brand name: ")
            self.brand_input = QLineEdit()
            self.brand_input.setFixedWidth(400)
            self.brand_label.setHidden(True)
            self.brand_input.setHidden(True)

            self.model_label = QLabel("Enter model name: ")
            self.model_input = QLineEdit()
            self.model_input.setFixedWidth(400)
            self.model_label.setHidden(True)
            self.model_input.setHidden(True)

            self.mileage_label = QLabel("Enter current mileage: ")
            self.mileage_input = QLineEdit()
            self.mileage_input.setFixedWidth(400)
            self.mileage_label.setHidden(True)
            self.mileage_input.setHidden(True)

            self.date_label = QLabel("Enter last service date: ")
            self.date_input = QLineEdit()
            self.date_input.setFixedWidth(400)
            self.date_label.setHidden(True)
            self.date_input.setHidden(True)

            self.submit_btn = QPushButton("Submit")
            self.submit_btn.setHidden(True)

            self.sublayout.addWidget(self.brand_label, 1, 0)
            self.sublayout.addWidget(self.brand_input, 1, 1)
            self.sublayout.addWidget(self.model_label, 2, 0)
            self.sublayout.addWidget(self.model_input, 2, 1)
            self.sublayout.addWidget(self.mileage_label, 3, 0)
            self.sublayout.addWidget(self.mileage_input, 3, 1)
            self.sublayout.addWidget(self.date_label, 4, 0)
            self.sublayout.addWidget(self.date_input, 4, 1)
            self.sublayout.addWidget(self.submit_btn, 5, 1)

            self.submit_btn.clicked.connect(add_car_submit)

        def show_add_car_dialog():
            if self.add_car_toggled == False:
                self.brand_label.setHidden(False)
                self.brand_input.setHidden(False)
                self.model_label.setHidden(False)
                self.model_input.setHidden(False)
                self.mileage_label.setHidden(False)
                self.mileage_input.setHidden(False)
                self.date_label.setHidden(False)
                self.date_input.setHidden(False)
                self.submit_btn.setHidden(False)
                self.setFixedHeight(517)
            elif self.add_car_toggled == True:
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
            self.add_car_toggled = not self.add_car_toggled

        def delete_car_dialog(self):
            self.delete_car_label = QLabel("Please enter the ID of the car you'd like to delete")
            self.delete_car_input = QLineEdit()
            self.delete_btn = QPushButton("Delete {}".format(self.delete_car_input.text()))
            self.delete_car_input.setFixedWidth(40)
            self.delete_car_label.setHidden(True)
            self.delete_car_input.setHidden(True)
            self.delete_btn.setHidden(True)

            self.sublayout.addWidget(self.delete_car_label, 6, 0)
            self.sublayout.addWidget(self.delete_car_input, 6, 1)
            self.sublayout.addWidget(self.delete_btn, 6, 3)

        def show_delete_car_dialog():
            if not MainWindow.delete_car_toggled:
                self.delete_car_label.setHidden(False)
                self.delete_car_input.setHidden(False)
                self.delete_btn.setHidden(False)
            if MainWindow.delete_car_toggled:
                self.delete_car_label.setHidden(True)
                self.delete_car_input.setHidden(True)
                self.delete_btn.setHidden(True)
            MainWindow.delete_car_toggled = not MainWindow.delete_car_toggled


        # Global car list
        self.cars = []
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

        #Is add_car toggled?
        self.add_car_toggled = False

        #Buttons
        self.list_all_cars_btn = QPushButton("List cars")
        self.add_car_btn = QPushButton("Add car")
        self.edit_car_btn = QPushButton("Edit car")
        self.delete_car_btn = QPushButton("Delete a car")
        self.quit_btn = QPushButton("Quit")
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
        delete_car_dialog(self)
        #BUTTON ACTIONS

        #Quit
        self.quit_btn.clicked.connect(QApplication.instance().quit)

        #List all cars (new window)
        self.list_all_cars_btn.clicked.connect(self.switch)

        #Show add car dialog
        self.add_car_btn.clicked.connect(show_add_car_dialog)

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
            id_line = QLabel('ID: {}'.format(str(index)))
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

    def switch(self):
        self.switch_window.emit()


# class AddCar(QWidget):
#
#     def __init__(self):
#         super(AddCar, self).__init__()
#         self.setFixedHeight(100)
#
#         # # Container Widget
#         # widget = QWidget()
#         # # Layout of Container Widget
#         # layout = QVBoxLayout(self)
#         #
#         # # for _ in range(20):
#         # #     btn = QPushButton('test')
#         # #     layout.addWidget(btn)
#         #
#         # widget.setLayout(layout)
#         #
#         # self.setLayout(layout)


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


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont('SansSerif', 20))
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


