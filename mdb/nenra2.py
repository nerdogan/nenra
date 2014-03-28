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
import re
import datetime
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from mainwindow import MainWindow

from modulemdb2 import *


def main():
    app =QApplication(sys.argv)
    app.processEvents()

    mainWindow = MainWindow()
    mmdb=Mmdb()
   

    myddb=Myddb()
    



    
   
    





    bilgi=mmdb.cek()

    i=len(bilgi)
    j=56
    mainWindow.tableWidget.setRowCount(i)
    mainWindow.tableWidget.setColumnCount(j)
    mainWindow.tableWidget.setColumnWidth( 0, 200 )
    aa=0
    toplam=0
    
    for row1 in bilgi:
        
        for aaa in range(len(row1)):
            
            try:
                item = row1[aaa]
                mainWindow.tableWidget.setItem(aa, aaa, QtGui.QTableWidgetItem(item))
                
            except TypeError:
                item = " "
                mainWindow.tableWidget.setItem(aa, aaa, QtGui.QTableWidgetItem(item))
            
            
         
        aa=aa+1

    def kontrol(girdi):
        girdi = str(girdi)
        ara = re.search(",", girdi)
        if ara:
            derle = re.compile(",")
            cikti = derle.sub(".",girdi)
            return cikti
        return girdi


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
                print bul2
                i=len(bul2)
                j=6
                fatura.tableWidget_2.setRowCount(i)
                aa=0
                toplam=0
                for row1 in bul2:
                    item=str(row1[2])
                    fatura.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
                    bul3=myddb.cek2(item,"hammadde","hammaddeid")
                    item=str(bul3[0][2])
                    fatura.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
                    item=bul3[0][3]
                    fatura.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
                    item=str(row1[5])                   
                    fatura.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
                    item=str(row1[3])                    
                    fatura.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item))
                    item=str(row1[4])
                    fatura.tableWidget_2.setItem(aa, 5, QtGui.QTableWidgetItem(item))
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
            slotfaturakaydet()
            

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
        print sonuc
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
            deger10=fatura.tableWidget_2.item(item,0).text()
            deger11=fatura.tableWidget_2.item(item,3).text()
            deger12=fatura.tableWidget_2.item(item,4).text()
            deger13=fatura.tableWidget_2.item(item,5).text()
            deger13=kontrol(deger13)
            print deger10
            sql2="insert into cariay (chid,hammaddeid,kdv,miktar,birimfiy) values (%s,%s,%s,%s,%s)"
            myddb.cur.execute(sql2,(sonuc[0][0],deger10,deger11,deger12,deger13))
            
        myddb.conn.commit()
        fatura.lineEdit_3.setFocus(True)




        
# veritabanından bilgi çek


    
    @pyqtSlot()
    def slotpuss(item2):

        StartDate="31/12/13"
        EndDate = datetime.datetime.strptime(StartDate, "%d/%m/%y")
        now = datetime.datetime.now()- datetime.timedelta(days=1)
        dt=now-EndDate
        print dt.days
        mainWindow.plainTextEdit.appendPlainText(str(dt.days))
        for i in range(dt.days):
            EndDate = EndDate + datetime.timedelta(days=1)
            sql= " select * from satdata where tarih like %s"
            sonuc=myddb.cur.execute(sql,(EndDate.strftime('%Y-%m-%d')+"%"))
            if sonuc==0:
                print " kaydediliyor"
                tar=EndDate.strftime('%d%m%Y')
                mainWindow.plainTextEdit.appendPlainText(tar+" kaydediliyor")
                bilgi=mmdb.cekmysql(tar,"satdata")
                if bilgi!=1978:
                    for row1 in bilgi:
                        sql1="insert into satdata (masaad,konumkod,urunkod,urungrup,yiyic,adisyon,kasiyerkod,kasiyerad,kuver,ikram,fixim,konumad,kdv,saat,tarih,adet,fixmenu,tutarx,tutar) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        myddb.cur.execute(sql1,(row1[1],row1[2],row1[3],row1[4],row1[5],row1[6],row1[7],row1[8],row1[10],row1[18],row1[19],row1[29],row1[32],row1[39],row1[40],row1[41],row1[45],row1[46],row1[47]))
                        myddb.conn.commit()
                else:
                    mainWindow.plainTextEdit.appendPlainText(tar+"  DOSYASI MEVCUT DEGIL!!!. GUNSONU ALINMAMIS OLABILIR")
            print EndDate.strftime('%d%m%Y')
            
    
    @pyqtSlot()
    def slotpuss2(item2):

        StartDate="31/12/13"
        EndDate = datetime.datetime.strptime(StartDate, "%d/%m/%y")
        now = datetime.datetime.now()- datetime.timedelta(days=1)
        dt=now-EndDate
        print dt.days
        mainWindow.plainTextEdit.appendPlainText(str(dt.days))
        for i in range(dt.days):
            EndDate = EndDate + datetime.timedelta(days=1)
            sql= " select * from satodeme where odetar like %s"
            sonuc=myddb.cur.execute(sql,(EndDate.strftime('%Y-%m-%d')+"%"))
            if sonuc==0:
                print " kaydediliyor"
                tar=EndDate.strftime('%d%m%Y')
                mainWindow.plainTextEdit.appendPlainText(tar+" kaydediliyor")
                bilgi=mmdb.cekmysql(tar,"satodeme")
                if bilgi!=1978:
                    for row1 in bilgi:
                        sql1="insert into satodeme (odemasaad,odeadisyon,odesekli,odecarikod,odekasiyerkod,odekasiyerad,odead,odecariad,indirimoran,odetip,odetutar,odesaat,odetarih,odetar,odecaritip) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        myddb.cur.execute(sql1,(row1[1],row1[2],row1[4],row1[5],row1[6],row1[7],row1[8],row1[9],row1[13],row1[14],row1[15],row1[17],row1[21],EndDate,row1[23]))
                        myddb.conn.commit()
                else:
                    mainWindow.plainTextEdit.appendPlainText(tar+"  DOSYASI MEVCUT DEGIL!!!. GUNSONU ALINMAMIS OLABILIR")
            print EndDate.strftime('%d%m%Y')

           
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
    

    sh = QtGui.QShortcut(mainWindow)
    sh.setKey(Qt.Key_Enter)
    mainWindow.connect(sh, QtCore.SIGNAL("activated()"), copyFunction)



    mainWindow.show()



    return app.exec_()

if __name__ == "__main__":
    main()
