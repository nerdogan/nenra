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
import re
from datetime import datetime,timedelta
import  time
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
        self.pushButton_3.clicked.connect(self.masrafkaydet)


        self.tableWidget.clearContents()
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 400)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 50)



    def kontrol(self,girdi):
        girdi = str(girdi)
        ara = re.search(",", girdi)
        if ara:
            derle = re.compile(",")
            cikti = derle.sub(".", girdi)
            return cikti
        return girdi






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
        self.mydbb.conn.commit()

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


    @pyqtSlot(int, int)
    def masrafkaydet(self, ):
        dur=0.05
        fatura = Fatura()
        fatura.goster()
        fatura.lineEdit.setText('ZZ')
        self.dt = self.dateEdit.date().toPyDate()
        self.dt = QtCore.QDate.fromString(str(self.dt), 'yyyy-MM-dd')
        fatura.dateEdit.setDate(self.dt)
        fatura.dateEdit_2.setDate(self.dt)
        fatura.lineEdit_3.setText("onur")
        time.sleep(dur)
        fatura.slotfatura(0, 0)
        time.sleep(dur)
        satir=0
        onur=0

        i = self.tableWidget_2.rowCount()
        if i == 0:
            return
        for item in range(i):


            deger10 = self.tableWidget_2.item(item, 0).text()
            deger11 = self.led[satir].text()
            deger12 = self.led[satir+1].text()
            deger13 = self.tableWidget_2.item(item, 2).text()
            deger14 = self.tableWidget_2.item(item, 1).text()
            # deger14  = u' '.join((str(deger14))).encode('utf-8').strip()
            deger13 = self.kontrol(deger13)
            if deger12=="17":
                print "onur"
                fatura.lineEdit_3.setText(deger11)
                time.sleep(dur)
                fatura.slotfatura(0, 0)
                time.sleep(dur)
                fatura.tableWidget_2.setItem(onur, 6, QtGui.QTableWidgetItem(str(float(deger13)*(-1))))
                fatura.tableWidget_2.setItem(onur,1,QtGui.QTableWidgetItem((deger14)))
                fatura.tableWidget_2.setItem(onur,3,QtGui.QTableWidgetItem("0"))
                time.sleep(dur)
                onur+=1
                fatura.slotfaturakaydet()
                self.mydbb.cur.execute("""update kasa set muhkod=1 where islemid=%s""",(deger10,))
                self.mydbb.conn.commit()

            else :
                print "başka"

            satir += 2


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    masraf=Masraf()
    masraf.show()
    masraf.raise_()



    app.exec_()



