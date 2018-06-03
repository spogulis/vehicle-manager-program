import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main import *

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

        #Window2
        list_all_cars_btn.clicked.connect(self.button_clicked)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Main menu - Vehicle manager')
        self.show()

    def button_clicked(self):
        self.sw = SecondWindow()
        # self.sw.show()

class SecondWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.scrollArea = QScrollArea()  # Def scrollarea
        self.scrollArea.setGeometry(700, 300, 350, 300) # Dimensions
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setMinimumHeight(280)
        self.scrollArea.setMaximumHeight(300)
        self.scrollArea.setWindowTitle('List of cars in file')

        self.widget = QWidget(self.scrollArea)

        #Print a list of cars
        filename = "list.txt"
        cars = read_from_file(filename)
        layout = QGridLayout(self.widget)
        for index, car in enumerate(cars):
            # empty_line = QLabel('')
            # grid.addWidget(empty_line, index, 1)
            id_line = QLabel('ID: {}'.format(str(index)))
            layout.addWidget(id_line, index, 1)
        self.scrollArea.show()


app = QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())


