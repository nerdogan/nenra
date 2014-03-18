# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NAMIK ERDOĞAN
#
# Created:     22.01.2014
# Copyright:   (c) NAMIK ERDOĞAN  2014
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
from mainwindow import Fatura
from modulemdb import *


def main():
    app =QApplication(sys.argv)
    app.processEvents()

    mainWindow = MainWindow()
    mmdb=Mmdb()
    recete=Recete()
    recete2=Recete2()
    fatura=Fatura()
    myddb=Myddb()
    



    bilgi=mmdb.cek()
    mmdb.kapat()
    bul=myddb.cek("select * from menu")
    





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
        #toplam=toplam+row1[15]
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
        recete2.lineEdit.setFocus(True)
        

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



    @pyqtSlot(int,int)
    def slothamclick(item,item2):
    #   hammadde listesinden çiftklikle tablewidget_2 ye hammadde bilgisini ekliyor.     
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
        recete2.lineEdit.setFocus(True)

    @pyqtSlot()
    def slotfaturakont(item2):
        
        deger5=fatura.lineEdit.text()
        deger6=fatura.lineEdit_2.text()
        sql="select * from carihar where  serino='"+str(deger5)+"' and sirano='"+str(deger6)+"'"
        sonuc=myddb.cek(sql)
        fatura.label_3.setText("")
        fatura.tableWidget.setRowCount(0)
        fatura.tableWidget_2.setRowCount(0)
        # some_date = QtCore.QDate(2011,4,22)
        some_date = QtCore.QDate.currentDate()
        fatura.dateEdit.setDate(some_date)
        

        if len(sonuc)>0 :
            dt=sonuc[0][4]
            QMessageBox.information(fatura.tableWidget,
                "QTableWidget Cell Click",
                "Text: "+str(dt.year))
            print sonuc
            for item in sonuc:
                fatura.dateEdit.setDate(QtCore.QDate(dt.year,dt.month,dt.day))
                sonuc1=myddb.cek2(item[1],"cari","cariid")
                for item2 in sonuc1:
                    deger0=str(item2[0])+" "+item2[1]+" "+item2[2]
                    fatura.label_3.setText(deger0)
                    bul1=str(item[0])

                bul2=myddb.cek2(item[0],"cariay","chid")
                i=len(bul2)
                j=5
                fatura.tableWidget_2.setRowCount(i)
                aa=0
                toplam=0
                for row1 in bul2:
                    item=str(row1[2])
                    fatura.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
                    bul3=myddb.cek2(item,"hammadde","hammaddeid")
                    item=str(bul3[0][1])
                    fatura.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
                    item=bul3[0][2]
                    fatura.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
                    item=bul3[0][3]
                    fatura.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
                    item=str(row1[3])
                    recete2.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item))
                    aa=aa+1   
            fatura.lineEdit_3.setFocus(True)
            return

       


    @pyqtSlot(int,int)
    def slotfatura(item,item2):
    #   cari listesinden çiftklikle line edite cari firma bilgisini yazıyor
        
        if len(fatura.label_3.text())<12 :
            deger1=fatura.tableWidget.item(item,0).text()
            deger2=fatura.tableWidget.item(item,1).text()
            deger3=fatura.tableWidget.item(item,2).text()
            deger4=fatura.tableWidget.item(item,3).text()
            fatura.label_5.setText(deger1)
            fatura.label_3.setText(deger1+" "+deger2+" "+deger3)
            bul1=str(deger1)
            fatura.lineEdit_3.setText("")
            

            return

        if len(fatura.label_3.text())>12 :
            #   hammadde listesinden çiftklikle tablewidget_2 ye hammadde bilgisini ekliyor.     
            i=fatura.tableWidget_2.rowCount()
            deger1=fatura.tableWidget.item(item,0).text()
            deger2=fatura.tableWidget.item(item,2).text()
            deger3=fatura.tableWidget.item(item,3).text()
            deger4=fatura.tableWidget.item(item,4).text()
        
            i=i+1
            j=5
            fatura.tableWidget_2.setRowCount(i)
            aa=i-1

            item=deger1
            fatura.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=deger2
            fatura.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=deger3 
            fatura.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=deger4
            fatura.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item='0'
            fatura.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item)) 
            fatura.lineEdit_3.setFocus(True)

   
 


       


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
        
    @pyqtSlot()
    def slotfaturakaydet():
        deger0=fatura.label_5.text()
        deger5=fatura.lineEdit.text()
        deger6=fatura.lineEdit_2.text()
        deger7=fatura.dateEdit.date().toPyDate()
        sql="select * from carihar where  serino='"+str(deger5)+"' and sirano='"+str(deger6)+"'"
        sonuc=myddb.cek(sql)
        if len(sonuc)==0:
            print "fatura kaydı yok"
            sql1="insert into carihar (cariid,serino,sirano,tarih) values (%s,%s,%s,%s)"
            print sql1
            myddb.cur.execute(sql1,(deger0,deger5,deger6,deger7))
            myddb.conn.commit()

        else:
            print " fatura kaydı var"
            myddb.sil(sonuc[0][0],"cariay","chid")


       
        
        i=fatura.tableWidget_2.rowCount()
        for item in range(i):
            
            deger1=fatura.tableWidget_2.item(item,0).text()
            deger2=fatura.tableWidget_2.item(item,4).text()
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
        recete.lineEdit.setFocus(True)


    @pyqtSlot()
    def slotpuss2(item2):
        print "fatura arayüzü açıldı"
        fatura.lineEdit.setText("")
        fatura.lineEdit_2.setText("")
        fatura.lineEdit_3.setText("")
        fatura.label_3.setText("")
        fatura.tableWidget.setRowCount(0)
        fatura.tableWidget_2.setRowCount(0)
        # some_date = QtCore.QDate(2011,4,22)
        some_date = QtCore.QDate.currentDate()
        fatura.dateEdit.setDate(some_date)
        fatura.show()
        fatura.lineEdit.setFocus(True)

       

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
            

           
    @pyqtSlot()
    def slottextch2(item2):
        print "fatura"
        a=item2.toUtf8()
        a=str(a)
        print a
        bul=myddb.cek1(a,"cari","cariad")

        if len(fatura.label_3.text())>12 :
            bul=myddb.cek1(a,"hammadde","hamad")


        
        i=len(bul)
        j=5
        fatura.tableWidget.setRowCount(i)
        aa=0
        toplam=0
        for row1 in bul:
            item=str(row1[0])
            fatura.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=str(row1[1])
            fatura.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=row1[2]
            fatura.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            fatura.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item=str(row1[5])
            fatura.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            aa=aa+1


    @pyqtSlot()
    def copyFunction():
        print "f10 a bastın"
        abc = QKeyEvent ( QEvent.KeyPress, Qt.Key_Tab, Qt.NoModifier)
        QCoreApplication.postEvent (fatura, abc)



    
    mainWindow.pushButton.setStyleSheet("color: black ;  background-image: url(image.png)")  
    mainWindow.pushButton_2.setStyleSheet("color: black ;  background-image: url(fatura.png)")  
    mainWindow.tableWidget.cellClicked.connect(slotItemClicked)
    mainWindow.pushButton.clicked.connect(slotpuss)
    mainWindow.pushButton_2.clicked.connect(slotpuss2)
    recete.lineEdit.textChanged.connect(slottextch)
    fatura.lineEdit_3.textChanged.connect(slottextch2)
    fatura.lineEdit_2.textChanged.connect(slotfaturakont)
    fatura.lineEdit.textChanged.connect(slotfaturakont)
    fatura.pushButton.clicked.connect(slotfaturakaydet)
    fatura.tableWidget.cellClicked.connect(slotfatura)
    recete.tableWidget.cellDoubleClicked.connect(slotrecete2)
    recete2.lineEdit.textChanged.connect(slotrecete2sql)
    recete2.tableWidget.cellClicked.connect(slothamclick)
    recete2.pushButton.clicked.connect(slotrecete2kaydet)

    sh = QtGui.QShortcut(fatura)
    sh.setKey(Qt.Key_Enter)
    fatura.connect(sh, QtCore.SIGNAL("activated()"), copyFunction)



    mainWindow.show()



    return app.exec_()

if __name__ == "__main__":
    main()
