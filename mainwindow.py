from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):#Clase Mainwindow que hereda desde QMainWindow
    def __init__(self):
        #Llama al constructor de QMainWindow(Le reserva memoria para poder crear una ventana)
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)

        ui.pushButton.clicked.connect(self.click_agregar)

    @Slot()
    def click_agregar(self):
        print('CLICK')