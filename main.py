import sys
import threading
import time

import serial
import serial.tools.list_ports
import os
from ui.current_time import Ui_MainWindow as CurentTime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random

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
                # self.read_com(self.ser)
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

                # data = ser.readline().decode()

                data = str(input())
                print('\ninput data:', data)

                line = data.split()

                self.input_time = str(line[0])
                self.input_data = str(line[1])

                self.reading_thread2 = threading.Thread(target=self.time_refresh, daemon=True)
                self.reading_thread2.start()
                # self.time_refresh()

        except(Exception) as e:
            self.close_port(ser)

    def close_port(self, ser):
        self.com_state = None
        self.ser.close()

    def time_refresh(self):

        print('\n self.input_time',  self.input_time)
        print('\n self.input_data', self.input_data)

        self.CurrnetTimeBrowser.clear()

        self.data = """<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
                        <html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">
                        p, li { white-space: pre-wrap; }
                        </style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n
                        <p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n
                        <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Time</span></p>\n
                        <p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n
                        <p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n
                        <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#00ff00;\">""" + self.input_time + """ </span></p>\n
                        <p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; color:#00ff00;\"><br /></p>\n
                        <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffff00;\">""" + self.input_data + """ </span></p></body></html>"""

        print('\n data', self.data)

        # self.CurrnetTimeBrowser.setHtml(self._translate("MainWindow", self.data))
        # self.CurrnetTimeBrowser.reload()




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MyApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()
