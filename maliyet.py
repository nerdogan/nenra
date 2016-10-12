# -*- coding: utf-8 -*-
import sys
import re
import datetime
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_maliyet import Ui_Dialog4

from modulemdb import *


class Maliyet(QtGui.QDialog , Ui_Dialog4):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        #self.myddb = Myddb()
        self.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(some_date)
        self.dateEdit_2.setDate(some_date)




