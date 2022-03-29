from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont
import sys

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()


        self.setWindowTitle("My Notepad")
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action24pt.triggered.connect(lambda: self.change_size(24))

        self.actionOpen.triggered.connect(lambda: self.open_file())
        self.actionSave.triggered.connect(lambda: self.save_file())
        self.actionClose.triggered.connect(lambda: self.close_event())

    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))

    def open_file(self):
        options = QFileDialog.Options()
        filename , _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*.*)", options = options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename , _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*.*)", options = options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def close_event(self):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)

        answer = dialog.exec_()

        if answer == 0:
            self.save_file()
        elif answer == 1:
            sys.exit(app.exec_())




def main():
    global app
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()
