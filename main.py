import sys
import threading
import time

import serial
import serial.tools.list_ports
import os
from ui.current_time import Ui_MainWindow as CurentTime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox


class MyApp(QtWidgets.QMainWindow, CurentTime):
    dataRefreshed = QtCore.pyqtSignal(str)  # 1 шаг. Создаём свой сигнал

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.com_state = False
        self.ser = None
        self.reading_thread = None
        self.reading_thread2 = None
        self.list_coms = []
        self.refresh_comports()
        self.buttonRefresh.clicked.connect(self.refresh_comports)
        self.buttonConnect.clicked.connect(self.connect_comport)
        # self.buttonWrite.clicked.connect(self.write_com)

        self.dataRefreshed.connect(
            self.refresh_data_slot)  # 3 шаг. Если вызвали сигнал - запускаем функцию обнвления окна

    def refresh_data_slot(self, data):
        self.CurrnetTimeBrowser.clear()  # очищаем окно
        self.data = data  # перезаписываем данные которые мы получили  и обновляем данные в окне
        self.CurrnetTimeBrowser.setHtml(self._translate("MainWindow", self.data))

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
                self.CurrnetTimeBrowser.setHtml(self._translate("MainWindow", self.data_default))  #дефолтный тест
                self.close_port(self.ser)
        else:
            print('COM-port not selected')
            self.buttonConnect.setChecked(False)
            QMessageBox.about(self, "Error", "Please, select COM port")

    def refresh_comports(self):
        if self.com_state is not True:
            self.listCOMports.clear()
            self.list_coms = list(serial.tools.list_ports.comports())
            for com_name in self.list_coms:
                com_name = str(com_name).split()
                self.listCOMports.addItem(com_name[0])  # добавить comport в listWidget

    def open_port(self, com):
        print('Selected COM:', com)
        ser = serial.Serial(port=com, baudrate=115200, timeout=2)

        if ser.is_open:
            self.com_state = True
            return ser

    def close_port(self, ser):
        if self.com_state:
            self.com_state = False
            self.ser.close()

    def read_com(self, ser):
        try:
            while self.com_state:
                ser.flushInput()
                ser.flushOutput()

                data = ser.readline().decode()

                print('\ninput raw data in COM port:', data)

                line = data.split()
                if '165' not in data:
                    self.input_time = str(line[0])
                    self.input_data = str(line[1])
                # Шаг 2 обновляем полученные в переменные временные и запускаем функцию которая посылает сигнал с тектом
                self.time_refresh()

        except(Exception) as e:
            self.close_port(ser)

    def write_com(self):

        from datetime import datetime
        t = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        print('Current os time:', t)
        # self.ser.write(bytes(t))
        # self.ser.write(b'sending string to Arduino')

    def time_refresh(self):

        data = """<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">
                        <html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head>
                        <body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">
                        <p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n
                        <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Time:</span></p>\n
                        <p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n
                        <p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n
                        <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#00ff00;\">     """ + self.input_time + """</span></p>\n
                        <p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; color:#00ff00;\"><br /></p>\n
                        <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffff00;\">Date: """ + self.input_data + """</span></p></body></html>"""
        # print(data)
        self.dataRefreshed.emit(data)  # После обновления функции кидаем сигнал


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MyApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()
