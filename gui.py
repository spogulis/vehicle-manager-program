import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main import *
from Vehicle import Vehicle


class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.setGeometry(300, 300, 350, 300)
        #GRID layout
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(20)

        #Buttons
        list_all_cars_btn = QPushButton("List cars")
        add_car_btn = QPushButton("Add car")
        edit_car_btn = QPushButton("Edit car")
        delete_car_btn = QPushButton("Delete a car")
        quit_btn = QPushButton("Quit")
        quit_btn.setStatusTip('Quit the program')

        #List of labels
        list_all_cars_q = QLabel('Press this button to view all your cars')
        add_car_q = QLabel('Add a car to your database')
        edit_car_q = QLabel("Edit a car's record")
        delete_car_q = QLabel('Delete a car from database')

        #POSITIONS
        grid.addWidget(list_all_cars_q, 1, 0)
        grid.addWidget(list_all_cars_btn, 1, 1)
        grid.addWidget(add_car_q, 2, 0)
        grid.addWidget(add_car_btn, 2, 1)
        grid.addWidget(edit_car_q, 3, 0)
        grid.addWidget(edit_car_btn, 3, 1)
        grid.addWidget(delete_car_q, 4, 0)
        grid.addWidget(delete_car_btn, 4, 1)
        grid.addWidget(quit_btn, 5, 2)

        #BUTTON ACTIONS
        #Quit
        quit_btn.clicked.connect(QApplication.instance().quit)

        #List all cars (new window)
        list_all_cars_btn.clicked.connect(self.list_cars_clicked)

        #Add car dialog
        add_car_btn.clicked.connect(self.add_car_clicked)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Main menu - Vehicle manager')
        self.show()

    def list_cars_clicked(self):
        self.sw = ViewCars()
        self.sw.setGeometry(700, 300, 270, 300)
        self.sw.setWindowTitle('List of cars in file')
        self.sw.show()
    def add_car_clicked(self):
        self.tw = AddCar()
        self.tw.show()

class ViewCars(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

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
        self.setLayout(v_layout)


class AddCar(QWidget):

    def __init__(self):
        super(AddCar, self).__init__()
        self.setFixedHeight(200)

        # Container Widget
        widget = QWidget()
        # Layout of Container Widget
        layout = QVBoxLayout(self)
        
        # for _ in range(20):
        #     btn = QPushButton('test')
        #     layout.addWidget(btn)

        widget.setLayout(layout)

        # Scroll Area Properties
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(False)
        scroll.setWidget(widget)

        # Scroll Area Layer add
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)

app = QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())


