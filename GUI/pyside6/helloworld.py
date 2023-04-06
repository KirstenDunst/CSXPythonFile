'''
Author: Cao Shixin
Date: 2023-04-04 14:06:50
LastEditors: Cao Shixin
LastEditTime: 2023-04-04 14:34:58
Description: 
'''
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)
        self.alertBtn = QtWidgets.QPushButton("点这里")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.alertBtn)

        self.button.clicked.connect(self.magic)
        self.alertBtn.clicked.connect(self.showMessage)
        
        

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

    @QtCore.Slot()
    def showMessage(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("hello world")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

