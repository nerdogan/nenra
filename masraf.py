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

from modulemdb import *



class Masraf(QtGui.QDialog , Ui_Masraf):


    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.mydbb=Myddb()
        self.led={}
        self.dt = datetime.now() - timedelta(hours=5)
        self.tar1 = (self.dt).strftime('%Y-%m-%d')
        self.dt = QtCore.QDate.fromString(str(self.dt.date()), 'yyyy-MM-dd')

        self.tableWidget.setRowCount(0)
        self.dateEdit.setDate(self.dt)
        self.pushButton.clicked.connect(lambda :self.slotilerigeri("geri"))
        self.pushButton_2.clicked.connect(lambda :self.slotilerigeri("ileri"))
        self.tableWidget_2.itemChanged.connect(self.ara)

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
            led.setObjectName('Line%d 4' % aa)
            self.led[bb]=led
            self.tableWidget_2.setCellWidget(aa,3,self.led[bb])

            self.connect(self.led[bb],QtCore.SIGNAL("textChanged(const QString&)"),self.linechanged)
            led1=QtGui.QLineEdit()
            self.led[bb+1]=led1
            self.tableWidget_2.setCellWidget(aa,4,self.led[bb+1])
            bb=bb+2
            aa=aa+1
            aaa=0

    def linechanged(self):
        elma=str(self.sender().text().toUtf8())
        print self.sender().objectName()
        print len(self.mydbb.cek1(elma,"hammadde","hamad"))


    @pyqtSlot(int,int)
    def ara(self,item):
        if item.column()==3:
            print "hammadde"
        elif item.column()==4:
            print "firma"






if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    masraf=Masraf()
    masraf.show()
    masraf.raise_()


    app.exec_()



