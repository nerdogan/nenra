# -*- coding: utf-8 -*-

import sys
from PyQt5 import  QtCore, QtWidgets
from PyQt5.QtCore import *


class Login(QtWidgets.QDialog):
    acac1 = pyqtSignal(int)

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle(u"NENRA 2016 20210301 Kullanıcı Girişi ")
        self.labelname = QtWidgets.QLabel(self)
        self.labelpass = QtWidgets.QLabel(self)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.labelname.setText(u"Kullanıcı Adı")
        self.labelpass.setText(u"Parola")
        self.buttonLogin = QtWidgets.QPushButton(u'Giriş', self)
        self.buttonLogin.clicked.connect(self.handleLogin)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.labelname)
        layout.addWidget(self.textName)
        layout.addWidget(self.labelpass)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
       # self.acac1 = pyqtSignal(int) böyle olmuyor
 #todo: veritabanından yada api den yap
    def handleLogin(self):
        if (self.textName.text() == 'mutfak' and
                self.textPass.text() == '1234'):
            self.accept()
            self.acac1.emit(12345)

        elif (self.textName.text() == 'kasa' and
              self.textPass.text() == '1234'):
            self.accept()
            self.acac1.emit(123456)


        elif ((self.textName.text() == 'n' or self.textName.text() == 'N') and self.textPass.text() == ''):
            self.accept()

            self.acac1.emit(1234)

        else:
            QtWidgets.QMessageBox.warning(
                self, 'Hata', u'Kullanıcı adı yada parola yanlış')

    def elmaa(self):
        self.acac1.emit(101)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            print("Program kapanıyor")
            self.elmaa()
            self.close()
        super(Login, self).keyPressEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.setStyleSheet("color:red ; background-color: orange;")
    login.show()
    app.exec_()
