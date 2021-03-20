# -*- coding: utf-8 -*-

import sys
import time as ttim
import math
import re
import hesapla
from PyQt5 import QtGui, QtCore, uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QDialog, QApplication
from PyQt5.QtCore import *

from ui_hesap import Ui_Dialog

from modulemdb import *



class Hesap(QDialog , Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.slothesapla)





    def closeEvent(self, event):
        print ("hesapmak Closing")



    def kontrol(self,girdi):
        girdi = str(girdi)
        ara = re.search(",", girdi)
        if ara:
            derle = re.compile(",")
            cikti = derle.sub(".", girdi)
            return cikti
        return girdi



    def goster(self):
        print ("fatura arayüzü açıldı")
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.show()
        self.raise_()
        self.lineEdit.setFocus(True)




    def slothesapla(self):
        elma=(self.lineEdit.text())
        elma=self.kontrol(elma)
        elma=str(hesapla.calc(str(elma)))

        self.lineEdit_2.setText(elma)
        self.emit(QtCore.SIGNAL("acac"), elma)
        self.close()



if __name__ == "__main__":
    import locale

    for x in locale.windows_locale.values():
        print(x.replace('_', '-'))
    app = QtGui.QApplication(sys.argv)
    hesap=Hesap()
    hesap.goster()
    app.exec_()
    print ("hesap kapandı")
