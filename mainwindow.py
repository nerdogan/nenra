# -*- coding: utf-8 -*-
import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_mainwindow import Ui_MainWindow
from ui_recete import Ui_Dialog
from ui_recete2 import Ui_Dialog2


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)


class Recete(QtGui.QDialog , Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)



class Recete2(QtGui.QDialog , Ui_Dialog2):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)