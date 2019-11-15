import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("my_test.ui", self)

        self.myPushButton.clicked.connect(self.printSomething)

    def printSomething(self):
        self.myTextEdit.append("Why did you press the button?")
        print("test button pressed")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())