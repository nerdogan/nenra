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
import os, sys, subprocess
import sys
import re
import datetime
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from mainwindow import MainWindow
from mainwindow import Recete
from mainwindow import Recete2
from mainwindow import Fatura
from mainwindow import Maliyet
from modulemdb import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont   


def main():
    app =QApplication(sys.argv)
    app.processEvents()

    mainWindow = MainWindow()
    
    recete=Recete()
    recete2=Recete2()
    fatura=Fatura()
    maliyet=Maliyet()
    myddb=Myddb()
    

   
    bul=myddb.cek("select * from menu")
    
    


    def kontrol(girdi):
        girdi = str(girdi)
        ara = re.search(",", girdi)
        if ara:
            derle = re.compile(",")
            cikti = derle.sub(".",girdi)
            return cikti
        return girdi


    

    @pyqtSlot(int,int)
    def slotrecete2(item,item2):

        
#   recete2 ekranı hazırlanıyor       
        deger0=recete.tableWidget.item(item,0).text()
        recete2.label_3.setText(deger0)
        file = open(deger0+".txt", "w")


        deger=recete.tableWidget.item(item,1).text()
        deger1=deger+" "+recete.tableWidget.item(item,2).text()+"  "
        recete2.label.setText(deger1)   

# veritabanından bilgi çek
        
        bul2=myddb.cek2(deger0,"recete","menuid")
        bul=myddb.cek("select * from menu where menukod>9000")
        recete2.comboBox.clear()
        i=len(bul)
        for xx1 in range(i):
            recete2.comboBox.addItem(str(bul[xx1][1])+" "+bul[xx1][2])



        i=len(bul2)
        j=5
        recete2.tableWidget_2.setRowCount(i)
        aa=0
        toplam=0
        for row1 in bul2:

            item=str(row1[2])
            file.write(item+" ")
            recete2.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            bul3=myddb.cek2(item,"hammadde","hammaddeid")
            item=str(bul3[0][1])
            file.write(item+" ")
            recete2.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=bul3[0][2]
            #file.write(item+" ")
            recete2.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=bul3[0][3]
            file.write(item+" ")
            recete2.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            recete2.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            aa=aa+1
            file.write(item+"\n")

        file.close()
        
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
            deger2=kontrol(deger2)
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
    def slotpuss3(item2):
        print "maliyet arayüzü açıldı"
        maliyet.show()
        maliyet.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        maliyet.dateEdit.setDate(some_date)
        maliyet.dateEdit_2.setDate(some_date)

        StartDate="21/03/14"
        
        EndDate = datetime.datetime.strptime(StartDate, "%d/%m/%y")
        now = datetime.datetime.now()- datetime.timedelta(days=1)
        dt=now-EndDate
        print dt.days
        #mainWindow.plainTextEdit.appendPlainText(str(dt.days))
        for i in range(dt.days):
            EndDate = EndDate + datetime.timedelta(days=1)
            sql= " select * from harcanan where tarih like %s"
            sonuc=myddb.cur.execute(sql,(EndDate.strftime('%Y-%m-%d')+"%"))
            if sonuc==0:
                print " kaydediliyor"
                tar=EndDate.strftime('%d%m%Y')
                
                sql2="SELECT menu.menukod,hammaddeid,miktar,adet FROM SATDATA inner join menu on urunkod=menukod and DATE(tarih)=%s  inner join recete on  menu.menuid=recete.menuid "
                bilgi=myddb.cur.execute(sql2,(EndDate.strftime('%Y-%m-%d')))
                print bilgi
                if bilgi<>0:
                    bilgi2=myddb.cur.fetchall()
                    for row1 in bilgi2:
                        hmikt=row1[2]*row1[3]
                        print hmikt
                        sql1="insert into harcanan (hurunkod,hhammaddeid,hmiktar,fiyat,tarih) values (%s,%s,%s,%s,%s)"
                        myddb.cur.execute(sql1,(row1[0],row1[1],hmikt,"0",EndDate))
                        myddb.conn.commit()
                
            print EndDate.strftime('%d%m%Y')


       

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
    def sloturunmaliyet(item2):
        
        print "urunmaliyet"
        c = canvas.Canvas("maliyet.pdf")
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 8)
        deger1=maliyet.dateEdit.date().toPyDate()
        deger2=maliyet.dateEdit_2.date().toPyDate()
        tar1=deger1.strftime('%Y-%m-%d')
        tar2=deger2.strftime('%Y-%m-%d')

       
        sql="SELECT urunkod,menuad,sum(adet),sum(tutar) FROM SATDATA inner join menu on  urunkod=menukod and DATE(tarih)>=%s and DATE(tarih)<=%s group by urunkod order by urunkod asc"
        bul=myddb.cur.execute(sql,(tar1,tar2))
        bul=myddb.cur.fetchall()


        i=len(bul)
        j=5
        maliyet.tableWidget.setRowCount(i)
        aa=0
        bb=0
        toplam=0
        toplam1=0
        toplam2=0
        item="   ÜRÜN AÇIKLAMA                                              ADET             TUTAR                      MALIYET                     ORAN "
        c.drawString(10,810,item)
        for row1 in bul:
            sql1="select hurunkod,sum(hmiktar*fiyat1),harcanan.tarih from harcanan inner join hammadde on hhammaddeid=hammaddeid where DATE(tarih)>=%s and DATE(tarih)<=%s and hurunkod=%s"
            bul1=myddb.cur.execute(sql1,(tar1,tar2,str(row1[0])))
            bul1=myddb.cur.fetchall()


            item=str(row1[0])
            c.drawString(10,800-(15*(bb+1)),item)
            maliyet.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=row1[1]
            c.drawString(35,800-(15*(bb+1)),item)
            maliyet.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=str(row1[2])
            c.drawString(240,800-(15*(bb+1)),item)
            toplam=toplam+row1[2]
            maliyet.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            c.drawString(320,800-(15*(bb+1)),item)
            toplam1=toplam1+row1[3]
            maliyet.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item=str(bul1[0][1])
            toplam2=toplam2+bul1[0][1]
            c.drawString(400,800-(15*(bb+1)),item)
            maliyet.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            item="% "+str(int((row1[3]-bul1[0][1])/bul1[0][1]*100))
            c.drawString(510,800-(15*(bb+1)),item)
            maliyet.tableWidget.setItem(aa, 5, QtGui.QTableWidgetItem(item))
            
            aa=aa+1
            bb=bb+1
            if (15*(bb+1))>=760:
                c.setFont("Verdana", 11)
                c.drawString(240,800-(15*(bb+1)),str(toplam))
                c.drawString(320,800-(15*(bb+1)),str(toplam1))
                c.drawString(400,800-(15*(bb+1)),str(toplam2))
                c.showPage()
                c.setFont("Verdana", 8)
                bb=0
        c.setFont("Verdana", 12)
        c.drawString(240,800-(15*(bb+1)),str(toplam))
        c.drawString(320,800-(15*(bb+1)),str(toplam1))
        c.drawString(400,800-(15*(bb+1)),str(toplam2))
                
        c.save()
    @pyqtSlot()
    def sloturunmaliyetpdf(item2):
        if sys.platform == "win32":
            os.startfile("maliyet.pdf")
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "maliyet.pdf"])


        
   







    @pyqtSlot()
    def copyFunction():
        print "f10 a bastın"
        abc = QKeyEvent ( QEvent.KeyPress, Qt.Key_Tab, Qt.NoModifier)
        QCoreApplication.postEvent (fatura, abc)


    @pyqtSlot()
    def slotrecete2satirsil():
        bb=recete2.tableWidget_2.currentRow()
        recete2.tableWidget_2.removeRow(bb)




    
    mainWindow.pushButton.setStyleSheet("color: black ;  background-image: url(image.png)")  
    mainWindow.pushButton_2.setStyleSheet("color: black ;  background-image: url(fatura.png)")  
    mainWindow.pushButton_3.setStyleSheet("color: black ;  background-image: url(maliyet.png)")  
    mainWindow.pushButton.clicked.connect(slotpuss)
    mainWindow.pushButton_2.clicked.connect(slotpuss2)
    mainWindow.pushButton_3.clicked.connect(slotpuss3)
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
    recete2.pushButton_3.clicked.connect(slotrecete2satirsil)
    maliyet.pushButton.clicked.connect(sloturunmaliyet)
    maliyet.pushButton_2.clicked.connect(sloturunmaliyetpdf)

    sh = QtGui.QShortcut(fatura)
    sh.setKey(Qt.Key_Enter)
    fatura.connect(sh, QtCore.SIGNAL("activated()"), copyFunction)



    mainWindow.show()



    return app.exec_()

if __name__ == "__main__":
    main()
