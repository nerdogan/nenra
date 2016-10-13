# -*- coding: utf-8 -*-

import sys
import time as ttim
import re
from PyQt4.QtCore import pyqtSlot,pyqtSignal
from PyQt4 import QtGui, QtCore



from modulemdb import *





class Login(QtGui.QDialog):
    acac1 = pyqtSignal(int)
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle(u"NENRA 2016 1053 Kullanıcı Girişi ")
        self.labelname = QtGui.QLabel(self)
        self.labelpass = QtGui.QLabel(self)
        self.textName = QtGui.QLineEdit(self)
        self.textPass = QtGui.QLineEdit(self)
        self.labelname.setText(u"Kullanıcı Adı")
        self.labelpass.setText(u"Parola")
        self.buttonLogin = QtGui.QPushButton(u'Giriş', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.labelname)
        layout.addWidget(self.textName)
        layout.addWidget(self.labelpass)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        self.acac1 = pyqtSignal(int)



    def handleLogin(self):
        if (self.textName.text() == 'mehmet' and
                    self.textPass.text() == '1234'):
            self.accept()
            self.emit(QtCore.SIGNAL("acac1(int)"), 123)


        elif ((self.textName.text() == 'n' or self.textName.text() == 'N') and    self.textPass.text() == ''):
            self.accept()

            self.emit(QtCore.SIGNAL("acac1(int)"),1234 )

        else:
            QtGui.QMessageBox.warning(
                self, 'Hata', u'Kullanıcı adı yada parola yanlış')


