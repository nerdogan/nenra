# -*- coding: utf-8 -*-

import sys
import re

from PyQt5.QtCore import pyqtSignal

import hesapla
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

from ui_hesap import Ui_Dialog


class Hesap(QDialog, Ui_Dialog):
    acac = pyqtSignal(str)

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
        elma = (self.lineEdit.text())
        elma = self.kontrol(elma)
        elma = str(hesapla.calc(str(elma)))

        self.lineEdit_2.setText(elma)

        self.acac.emit(elma)
        self.close()

