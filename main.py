import sys
import serial
import os
from ui.current_time import Ui_MainWindow as CurentTime
from PyQt5 import QtWidgets, QtCore

# list_coms = ['COM1', 'COM2']


import serial.tools.list_ports


class MyApp(QtWidgets.QMainWindow, CurentTime):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.list_coms = []
        self.ButtonConnect.clicked.connect(self.show_comports)

    def show_comports(self):
        self.listCOMports.clear()
        for com_name in self.list_coms:  # для каждого файла в директории
            self.listCOMports.addItem(com_name)   # добавить файл в listWidget

    def refresh_comports(self):
        self.listCOMports.clear()
        self.list_coms = list(serial.tools.list_ports.comports())




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MyApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение




if __name__ == "__main__":
    main()
