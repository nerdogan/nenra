# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtGui, QtCore, uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QDialog, QApplication
from PyQt5.QtCore import *
from ui_mainwindow import Ui_MainWindow
from ui_recete import Ui_Dialog
from ui_recete2 import Ui_Dialog2


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


class Recete(QDialog , Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)



class Recete2(QDialog , Ui_Dialog2):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)