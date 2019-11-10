import sys
import threading
import time

import serial
import serial.tools.list_ports
import os
from ui.current_time import Ui_MainWindow as CurentTime, DATA
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

AAA = 'asdas'

class MyApp(QtWidgets.QMainWindow, CurentTime):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.com_state = None
        self.ser = None
        self.reading_thread = None
        self.reading_thread2 = None
        self.list_coms = []
        self.refresh_comports()
        self.buttonRefresh.clicked.connect(self.refresh_comports)
        self.buttonConnect.clicked.connect(self.connect_comport)

    def connect_comport(self):
        if self.listCOMports.currentItem():
            selected_com = self.listCOMports.currentItem().text()
            if self.buttonConnect.isChecked():
                self.buttonConnect.setText("Disconnect")
                self.ser = self.open_port(selected_com)
                self.reading_thread = threading.Thread(target=self.read_com, args=(self.ser,), daemon=True)
                self.reading_thread.start()
            else:
                self.buttonConnect.setText("Connect")
                self.close_port(self.ser)
        else:
            print('COM-port not selected')
            self.buttonConnect.setChecked(False)
            QMessageBox.about(self, "Error", "Please, select COM port")

    def refresh_comports(self):
        self.listCOMports.clear()
        self.list_coms = list(serial.tools.list_ports.comports())
        for com_name in self.list_coms:
            com_name = str(com_name).split()
            self.listCOMports.addItem(com_name[0])  # добавить comport в listWidget

    def open_port(self, com):
        print('Selected COM:', com)
        ser = serial.Serial(port=com, baudrate=9600, timeout=2)
        if ser.is_open:
            self.com_state = True
            return ser

    def read_com(self, ser):
        try:
            while self.com_state:
                ser.flushInput()
                ser.flushOutput()
                data = ser.readline().decode()

                self.reading_thread2 = threading.Thread(target=self.time_refresh, args=(data,), daemon=True)
                self.reading_thread2.start()
                # self.time_refresh(data)

        except(Exception) as e:
            self.close_port(ser)

    def close_port(self, ser):
        self.com_state = None
        self.ser.close()

    def time_refresh(self, line: str):
        line1, line2 = line.split()
        a1 = line1.split(':')
        a2 = line2.split(':')
        tmp = str(a1[1])
        tmp2 = str(a2[1])
        print(tmp, tmp2)




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MyApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()
