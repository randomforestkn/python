import sys
import bcrypt
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QStackedWidget, QLineEdit
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("login.ui", self)
        self.pushButton_2.clicked.connect(self.go_to_register)
        self.password_field.setEchoMode(QLineEdit.Password)
        self.login_button.clicked.connect(self.login_function)

    def go_to_register(self):
        register = RegisterScreen()
        widget.addWidget(register)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def login_function(self):
        username = self.username_field.text()
        password = self.password_field.text()
        password = password.encode('utf-8')
        if len(username) == 0 or len(password) == 0:
            self.error_label.setText("Please input all fields!")
        else:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            query = 'SELECT password FROM users WHERE username =\''+username+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if bcrypt.checkpw(password, result_pass):
                self.error_label.setText("Successfully logged in!")
            else:
                self.error_label.setText("Wrong Password!")

class RegisterScreen(QDialog):
    def __init__(self):
        super(RegisterScreen, self).__init__()
        loadUi("register.ui", self)
        self.pushButton_2.clicked.connect(self.go_to_login)
        self.password_field.setEchoMode(QLineEdit.Password)
        self.register_button.clicked.connect(self.register_function)

    def go_to_login(self):
        welcome = WelcomeScreen()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def register_function(self):
        username = self.username_field.text()
        password = self.password_field.text()
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        if len(username) == 0 or len(password) == 0:
            self.error_label.setText("Please input all fields!")
        else:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)")
            cur.execute('INSERT INTO users  VALUES (NULL,?,?)', (username, hashed))
            conn.commit()
            conn.close()
            self.error_label.setText("Successfully Registered!")




app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
widget.setWindowTitle("Form")
try:
    sys.exit(app.exec_())
except:
    print("Exit")
