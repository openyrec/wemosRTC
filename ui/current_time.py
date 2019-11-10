# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'current_time.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

DATA = ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">Time</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; color:#00ff00;\">13:{}:{}</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; color:#00ff00;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffff00;\">12-04-2020</span></p></body></html>"]

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 410)
        MainWindow.setMinimumSize(QtCore.QSize(360, 410))
        MainWindow.setMaximumSize(QtCore.QSize(360, 410))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(340, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget.setSizeIncrement(QtCore.QSize(50, 50))
        self.centralwidget.setBaseSize(QtCore.QSize(600, 600))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.centralwidget.setObjectName("centralwidget")
        self.lableCOMports = QtWidgets.QLabel(self.centralwidget)
        self.lableCOMports.setGeometry(QtCore.QRect(70, 10, 111, 31))
        self.lableCOMports.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lableCOMports.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lableCOMports.setObjectName("lableCOMports")
        self.buttonConnect = QtWidgets.QPushButton(self.centralwidget)
        self.buttonConnect.setGeometry(QtCore.QRect(230, 100, 93, 31))
        self.buttonConnect.setCheckable(True)
        self.buttonConnect.setObjectName("buttonConnect")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 140, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.CurrnetTimeBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.CurrnetTimeBrowser.setGeometry(QtCore.QRect(30, 170, 300, 220))
        self.CurrnetTimeBrowser.setMinimumSize(QtCore.QSize(300, 220))
        self.CurrnetTimeBrowser.setMaximumSize(QtCore.QSize(300, 220))
        self.CurrnetTimeBrowser.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.CurrnetTimeBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.CurrnetTimeBrowser.setOverwriteMode(True)
        self.CurrnetTimeBrowser.setObjectName("CurrnetTimeBrowser")
        self.listCOMports = QtWidgets.QListWidget(self.centralwidget)
        self.listCOMports.setGeometry(QtCore.QRect(30, 50, 180, 81))
        self.listCOMports.setMinimumSize(QtCore.QSize(180, 51))
        self.listCOMports.setMaximumSize(QtCore.QSize(180, 100))
        self.listCOMports.setFrameShape(QtWidgets.QFrame.Box)
        self.listCOMports.setObjectName("listCOMports")
        self.buttonRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRefresh.setGeometry(QtCore.QRect(230, 50, 93, 31))
        self.buttonRefresh.setObjectName("buttonRefresh")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Current time"))
        self.lableCOMports.setText(self._translate("MainWindow", "<html><head/><body><p align=\"center\">Select COM port</p></body></html>"))
        self.buttonConnect.setText(self._translate("MainWindow", "Connect"))
        self.CurrnetTimeBrowser.setHtml(self._translate("MainWindow", DATA[0]))
        # self.CurrnetTimeBrowser.setHtml(self._translate("MainWindow", " "))
        self.buttonRefresh.setText(self._translate("MainWindow", "Refresh"))
