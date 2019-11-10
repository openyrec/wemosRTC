import sys

import serial
import serial.tools.list_ports
import os
from ui.current_time import Ui_MainWindow as CurentTime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


def close_port(com):
    ser = serial.Serial(port=com, baudrate=9600, timeout=2)
    ser.close()
    print('Closed: ', com)


def open_port(com):
    print('COM', com)
    ser = serial.Serial(port=com, baudrate=9600, timeout=2)
    if ser.is_open:
        print('is open')
        ser.flushInput()
        ser.flushOutput()
        res = ser.readline()
        print(res)


class MyApp(QtWidgets.QMainWindow, CurentTime):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.list_coms = []
        self.refresh_comports()
        self.buttonRefresh.clicked.connect(self.refresh_comports)
        self.buttonConnect.clicked.connect(self.connect_comport)

    def connect_comport(self):
        if self.listCOMports.currentItem():
            selected_com = self.listCOMports.currentItem().text()
            if self.buttonConnect.isChecked():
                self.buttonConnect.setText("Disconnect")
                print(selected_com)
                open_port(selected_com)
            else:
                self.buttonConnect.setText("Connect")
                print('Run disconnect')
                close_port(selected_com)
        else:
            print('Not selected')
            self.buttonConnect.setChecked(False)
            QMessageBox.about(self, "Error", "Please, select COM port")

    def refresh_comports(self):
        self.listCOMports.clear()
        self.list_coms = list(serial.tools.list_ports.comports())
        for com_name in self.list_coms:
            com_name = str(com_name).split()
            self.listCOMports.addItem(com_name[0])  # добавить comport в listWidget


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MyApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()
