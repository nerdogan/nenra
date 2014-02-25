# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NAMIK ERDO?AN
#
# Created:     22.01.2014
# Copyright:   (c) NAMIK ERDO?AN  2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from mainwindow import MainWindow
from mainwindow import Recete
from mainwindow import Recete2
from modulemdb import *

def main():
    app = QtGui.QApplication(sys.argv)

    mainWindow = MainWindow()
    mmdb=Mmdb()
    recete=Recete()
    recete2=Recete2()
    myddb=Myddb()



    bilgi=mmdb.cek()
    mmdb.kapat()
    bul=myddb.cek("menu")
    bul1=()





    i=len(bilgi)
    j=5
    mainWindow.tableWidget.setRowCount(i)
    aa=0
    toplam=0
    for row1 in bilgi:
        item=row1[1]
        mainWindow.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
        item=row1[2]
        mainWindow.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
        item=row1[7]
        mainWindow.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
        item=row1[8]
        mainWindow.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
        item=str(row1[15])
        mainWindow.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
        toplam=toplam+row1[15]
        aa=aa+1


    @pyqtSlot(int,int)
    def slotItemClicked(item,item2):
        print "Row: "+str(item)+" |Column: "+QString.number(item2)
        mainWindow.tableWidget.horizontalHeaderItem(0).setText(str(item)+"  "+str(item2))
        QMessageBox.information(mainWindow.tableWidget,
				"QTableWidget Cell Click",
				"Text: "+str(toplam))

    @pyqtSlot(int,int)
    def slotrecete2(item,item2):

        
#   recete2 ekranı hazırlanıyor       
        deger0=recete.tableWidget.item(item,0).text()
        recete2.label_3.setText(deger0)

        deger=recete.tableWidget.item(item,1).text()
        deger1=deger+" "+recete.tableWidget.item(item,2).text()+"  "
        recete2.label.setText(deger1)   

# veritabanından bilgi çek
        
        bul2=myddb.cek2(deger0,"recete","menuid")


        i=len(bul2)
        j=5
        recete2.tableWidget_2.setRowCount(i)
        aa=0
        toplam=0
        for row1 in bul2:
            item=str(row1[2])
            recete2.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            bul3=myddb.cek2(item,"hammadde","hammaddeid")
            item=str(bul3[0][1])
            recete2.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=bul3[0][2]
            recete2.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=bul3[0][3]
            recete2.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            recete2.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            aa=aa+1


        
        recete2.show()
        

    @pyqtSlot()
    def slotrecete2sql(item2):

        a=item2.toUtf8()
        a=str(a)
        print a

        bul=myddb.cek1(a,"hammadde","hamad")

        
        i=len(bul)
        j=5
        recete2.tableWidget.setRowCount(i)
        aa=0
        toplam=0
        for row1 in bul:
            item=str(row1[0])
            recete2.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=str(row1[1])
            recete2.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=row1[2]
            recete2.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            recete2.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item=str(row1[4])
            recete2.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            aa=aa+1

    
#   recete2 ekranı hazırlanıyor       
   
# veritabanından bilgi çek


    @pyqtSlot(int,int)
    def slothamclick(item,item2):
        
        i=recete2.tableWidget_2.rowCount()
        deger1=recete2.tableWidget.item(item,0).text()
        deger2=recete2.tableWidget.item(item,1).text()
        deger3=recete2.tableWidget.item(item,2).text()
        deger4=recete2.tableWidget.item(item,3).text()
        
        i=i+1
        j=5
        recete2.tableWidget_2.setRowCount(i)
        aa=i-1

        item=deger1
        recete2.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
        item=deger2
        recete2.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
        item=deger3 
        recete2.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
        item=deger4
        recete2.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
        item='0'
        recete2.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item)) 


    @pyqtSlot()
    def slotrecete2kaydet():
        deger0=recete2.label_3.text()
        myddb.sil(deger0,"recete","menuid")
        i=recete2.tableWidget_2.rowCount()
        for item in range(i):
            
            deger1=recete2.tableWidget_2.item(item,0).text()
            deger2=recete2.tableWidget_2.item(item,4).text()
            print deger0 , deger1 , deger2
            myddb.kaydet(deger0,deger1,deger2)
        myddb.conn.commit()
        
        

        
# veritabanından bilgi çek


    
    @pyqtSlot()
    def slotpuss(item2):
        print "reçete arayüzü açıldı"
        recete.show()
        i=len(bul)
        j=5
        recete.tableWidget.setRowCount(i)
        aa=0
        toplam=0
        for row1 in bul:
            item=str(row1[0])
            recete.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=str(row1[1])
            recete.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=row1[2]
            recete.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            recete.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item=str(row1[4])
            recete.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            aa=aa+1

    @pyqtSlot()
    def slottextch(item2):
        print "kjkljlk reçete"
        a=item2.toUtf8()
        a=str(a)
        print a

        bul=myddb.cek1(a,"menu","menuad")

        
        i=len(bul)
        j=5
        recete.tableWidget.setRowCount(i)
        aa=0
        toplam=0
        for row1 in bul:
            item=str(row1[0])
            recete.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=str(row1[1])
            recete.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=row1[2]
            recete.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            recete.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item=str(row1[4])
            recete.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            aa=aa+1



    mainWindow.tableWidget.cellClicked.connect(slotItemClicked)
    mainWindow.pushButton.clicked.connect(slotpuss)
    recete.lineEdit.textChanged.connect(slottextch)
    recete.tableWidget.cellDoubleClicked.connect(slotrecete2)
    recete2.lineEdit.textChanged.connect(slotrecete2sql)
    recete2.tableWidget.cellClicked.connect(slothamclick)
    recete2.pushButton.clicked.connect(slotrecete2kaydet)

    mainWindow.show()

    return app.exec_()

if __name__ == "__main__":
    main()
