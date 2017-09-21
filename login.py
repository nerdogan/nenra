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
        self.setWindowTitle(u"NENRA 2016 20170526 Kullanıcı Girişi ")
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
        if (self.textName.text() == 'mutfak' and
                    self.textPass.text() == '1234'):
            self.accept()
            self.emit(QtCore.SIGNAL("acac1(int)"), 12345)

        elif (self.textName.text() == 'kasa' and
                    self.textPass.text() == '1234'):
            self.accept()
            self.emit(QtCore.SIGNAL("acac1(int)"), 123456)


        elif ((self.textName.text() == 'n' or self.textName.text() == 'N') and    self.textPass.text() == ''):
            self.accept()

            self.emit(QtCore.SIGNAL("acac1(int)"),1234 )

        else:
            QtGui.QMessageBox.warning(
                self, 'Hata', u'Kullanıcı adı yada parola yanlış')

    def elmaa(self):
        self.emit(QtCore.SIGNAL("acac1(int)"), 101)

    def keyPressEvent(self, event):
        if  event.key() == QtCore.Qt.Key_Escape:
            print "Program kapanıyor"
            self.elmaa()
            self.close()
        super(Login, self).keyPressEvent(event)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    fatura1=Login()
    fatura1.setStyleSheet("color:red ; background-color: orange;")
    fatura1.show()
    app.exec_()

