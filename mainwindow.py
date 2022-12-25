# -*- coding: utf-8 -*-
import sys

from PyQt6 import QtGui, QtCore, uic, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt6.QtCore import *
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
