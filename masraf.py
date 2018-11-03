# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      NAMIK ERDOĞAN
#
# Created:     17.10.2018
# Copyright:   (c) NAMIK ERDOĞAN  2018
# Licence:
#-------------------------------------------------------------------------------


import sys
from datetime import datetime,timedelta
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_masraf import Ui_Masraf
from fatura import Fatura

from modulemdb import *



class Masraf(QtGui.QDialog , Ui_Masraf):


    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.mydbb=Myddb()
        self.led={}
        self.deger=0
        self.dt = datetime.now() - timedelta(hours=5)
        self.tar1 = (self.dt).strftime('%Y-%m-%d')
        self.dt = QtCore.QDate.fromString(str(self.dt.date()), 'yyyy-MM-dd')

        self.tableWidget.setRowCount(0)
        self.dateEdit.setDate(self.dt)
        self.pushButton.clicked.connect(lambda :self.slotilerigeri("geri"))
        self.pushButton_2.clicked.connect(lambda :self.slotilerigeri("ileri"))
        self.tableWidget.cellClicked.connect(self.slotmasraf)


        self.tableWidget.clearContents()
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 400)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 50)






    @pyqtSlot()
    def slotilerigeri(self,elma):
        if elma=="geri":
            self.dt = self.dateEdit.date().toPyDate() - timedelta(hours=24)
            self.tar1 = (self.dt).strftime('%Y-%m-%d')
        if elma=="ileri":
            self.dt = self.dateEdit.date().toPyDate() + timedelta(hours=24)
            self.tar1 = (self.dt).strftime('%Y-%m-%d')
        self.dt = QtCore.QDate.fromString(str(self.dt), 'yyyy-MM-dd')
        self.dateEdit.setDate(self.dt)

        sql="select islemid,aciklama,tutar from kasa where kasano=111 and tarih= %s"
        bul1=self.mydbb.cur.execute(sql,(self.tar1,))
        bul=self.mydbb.cur.fetchall()

        i=bul1
        aa=0
        aaa=0
        bb=0
        self.tableWidget_2.setRowCount(i )

        for row in bul:
            for col in row:
                if isinstance(col,basestring):
                    item=col
                else:
                    item=str(col)
                self.tableWidget_2.setItem(aa, aaa, QtGui.QTableWidgetItem(item))
                aaa = aaa + 1
            #lineedit ekleniyor
            led=QtGui.QLineEdit()
            led.setObjectName('0%d' % bb)
            self.led[bb]=led
            self.tableWidget_2.setCellWidget(aa,3,self.led[bb])

            self.connect(self.led[bb],QtCore.SIGNAL("textChanged(const QString&)"),self.linechanged)

            led1=QtGui.QLineEdit()
            led1.setObjectName('000%d' % (bb+1))
            self.led[bb+1]=led1
            self.tableWidget_2.setCellWidget(aa,4,self.led[bb+1])

            self.connect(self.led[bb+1], QtCore.SIGNAL("textChanged(const QString&)"), self.linechanged)

            bb=bb+2
            aa=aa+1
            aaa=0

    def linechanged(self):
        a=str(self.sender().text().toUtf8())
        print self.sender().objectName()
        self.deger=int(self.sender().objectName())

        if len(self.sender().objectName()) < 4:
            bul = self.mydbb.cek1(a, "hammadde", "hamad")
            self.tableWidget.setColumnWidth(0, 75)
            self.tableWidget.setColumnWidth(1, 220)
            self.tableWidget.setColumnWidth(2, 50)
            self.tableWidget.setColumnWidth(3, 50)
        else:
            bul = self.mydbb.cek1(a, "cari", "cariad")
            self.tableWidget.setColumnWidth(0, 75)
            self.tableWidget.setColumnWidth(1, 50)
            self.tableWidget.setColumnWidth(2, 220)
            self.tableWidget.setColumnWidth(3, 50)

        i = len(bul)
        j = 5
        self.tableWidget.setRowCount(i)
        aa = 0
        toplam = 0
        for row1 in bul:
            item = str(row1[1])
            self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item = row1[2]
            self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item = row1[3]
            self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item = str(row1[4])
            self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item = str(row1[6])
            self.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            aa = aa + 1

    @pyqtSlot(int, int)
    def slotmasraf(self, item, item2):
        #   cari listesinden çiftklikle line edite cari firma bilgisini yazıyor
        print item, item2
        print self.deger
        self.tableWidget_2.blockSignals(True)
        self.led[self.deger].setText(self.tableWidget.item(item,0).text())

        self.tableWidget_2.blockSignals(False)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    masraf=Masraf()
    masraf.show()
    masraf.raise_()

    fatura = Fatura()
    fatura.goster()


    app.exec_()



