import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from newmain import *

class VentanaPrincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec_()