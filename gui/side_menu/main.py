import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QStackedWidget, QLineEdit
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont
import icons_rc
import os

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("interface.ui", self)
        self.show()

        self.setWindowTitle("My App")

        




app = QApplication(sys.argv)
welcome = WelcomeScreen()
try:
    sys.exit(app.exec_())
except:
    print("Exit")
