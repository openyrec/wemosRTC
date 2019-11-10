from ui.test import Ui_MainWindow as test_window
from PyQt5 import QtWidgets
import sys
import random
import time

class MyApp(QtWidgets.QMainWindow, test_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.refresh_browser)



    def refresh_browser(self):
        # pass
        print(self.text)
        self.text = str((random.random()))
        print('\n-------', self.text)

        self.textBrowser.clear()
        self.data = """ <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n
           <html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n
           p, li { white-space: pre-wrap; }\n
           </style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n
           <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Count</span></p>\n
           <p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">""" +self.text+"""</span></p></body></html>"""
        print('\ndata-------', self.data)

        self.textBrowser.setHtml(self._translate("MainWindow", self.data))

        self.textBrowser.reload()

    def refresh_list(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MyApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == "__main__":
    main()

