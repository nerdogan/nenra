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
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui

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
        print "Row: "+str(item)+" |Column: "+QString.number(item2)
        QMessageBox.information(recete2.tableWidget,
                "QTableWidget Cell Click",
                "Text: "+str(item)) 

#   recete2 ekranı hazırlanıyor       
        deger=recete.tableWidget.item(item,item2-1).text()
        deger=deger+" "+recete.tableWidget.item(item,item2).text()+"  "
        recete2.label.setText(deger)   

# veritabanından bilgi çek



        recete2.show()
        recete.close()

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

    mainWindow.show()

    return app.exec_()

if __name__ == "__main__":
    main()
