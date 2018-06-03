import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.setGeometry(300, 300, 350, 300)
        self.second = SecondWindow()
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
        self.sw.show()


class SecondWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.setGeometry(300, 300, 350, 300)
        #GRID layout
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(20)
        list_all_cars_q = QLabel('Press this button to view all your cars')
        grid.addWidget(list_all_cars_q, 1, 0)
        self.show()


app = QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())


