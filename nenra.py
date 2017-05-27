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
# pyinstaller --clean --win-private-assemblies -F masa.py --distpath="C:\Users\NAMIK\Desktop\masa" -w
import subprocess
import sys
reload(sys)
import re
import datetime
import logging
import urllib2
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSlot,pyqtSignal
from PyQt4 import QtGui, QtCore

from mainwindow import MainWindow
from mainwindow import Recete
from mainwindow import Recete2
from fatura import Fatura
from maliyet import Maliyet
from cari import Cari
from login import Login
from modulemdb import *


sys.setdefaultencoding('utf8')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)




class WorkerThread(QThread):
    acac1 = pyqtSignal(int)

    def __init__(self,parent=None):
        super(WorkerThread,self).__init__(parent)
        self.myddb = Myddb()
        self.acac1 = pyqtSignal(int)


    def run(self):
        self.emit(QtCore.SIGNAL("acac1(int)"), 100)
        StartDate = "01/05/17"

        EndDate = datetime.datetime.strptime(StartDate, "%d/%m/%y")
        now = datetime.datetime.now() - datetime.timedelta(days=1)
        dt = now - EndDate
        print dt.days
        # mainWindow.plainTextEdit.appendPlainText(str(dt.days))
        for i in range(dt.days + 1):
            print EndDate.strftime('%d%m%Y')
            sql = " select * from harcanan where tarih like %s"
            sonuc = self.myddb.cur.execute(sql, [(EndDate.strftime('%Y-%m-%d') + "%")])
            valnen = []
            if sonuc == 0:
                print " kaydediliyor"
                tar = EndDate.strftime('%d%m%Y')

                sql2 = "SELECT hammadde.hamkod,recete.hamkod,miktar,adet FROM bishop.ciro inner join test.hammadde on pluno=hamkod and DATE(tarih)=%s  inner join test.recete on  hammadde.hamkod=recete.menukod"
                bilgi = self.myddb.cur.execute(sql2, [(EndDate.strftime('%Y-%m-%d'))])
                print bilgi
                valnen = []
                if bilgi <> 0:
                    bilgi2 = self.myddb.cur.fetchall()
                    for row1 in bilgi2:
                        hmikt = row1[2] * row1[3]

                        sql1 = "insert into harcanan (hurunkod,hhammaddeid,hmiktar,fiyat,tarih) values (%s,%s,%s,%s,%s)"
                        valnen.append((row1[0], row1[1], hmikt, "0", EndDate))
                        # self.myddb.cur.execute(sql1, (row1[0], row1[1], hmikt, "0", EndDate))

                    print self.myddb.cur.executemany(sql1, valnen)
                    self.myddb.conn.commit()
                    print(valnen)

            EndDate = EndDate + datetime.timedelta(days=1)


"""
        with open("ver.png", "r") as dosya:
            elma1 = dosya.read()

        urlpath = urllib2.urlopen('http://nen.duckdns.org:8080/dist/ver.png')
        string = urlpath.read()
        print string, elma1
        if elma1 == string:
            print u"aynı"
        else:
            if sys.platform == "win32":
                self.filename = string
            elif sys.platform == "linux2":
                pass
            else:
                self.filename = 'nenra.dmg'

            rq = urllib2.urlopen('http://nen.duckdns.org:8080/dist/' + self.filename)
            fSize = int(rq.info()['Content-Length'])
            print rq.info()['Last-Modified']
            fileName = self.filename
            downloadedChunk = 0
            blockSize = 2048
            with open(fileName, "wb") as sura:
                while True:
                    chunk = rq.read(blockSize)
                    if not chunk:
                        print("\nDownload Complete.")
                        break
                    downloadedChunk += len(chunk)
                    sura.write(chunk)
                    progress = float(downloadedChunk) / fSize
                    self.acac1.emit(int(progress*100))
            with open("ver.png", "w") as dosya:
                dosya.write(self.filename)
            os.system(self.filename)
"""

def main():
    app =QApplication(sys.argv)
    app.processEvents()

    mainWindow = MainWindow()
    login=Login()




    myddb = Myddb()


    recete=Recete()
    recete2=Recete2()
    fatura=Fatura()
    maliyet=Maliyet()
    cari = Cari()
    workerthread = WorkerThread()
    workerthread.start()

    bul=myddb.cek("select * from hammadde where kategori=2 or kategori=3 order by hamkod")
    logger.info('Program opened 20170518 '+str(os.getpid()))



    @pyqtSlot(int,int)
    def slotrecete2(item,item2):

        recete2.lineEdit.setText("")
#   recete2 ekranı hazırlanıyor
        deger0=recete.tableWidget.item(item,1).text()
        recete2.label_3.setText(deger0)
        file = open(deger0+".txt", "w")


        deger=recete.tableWidget.item(item,1).text()
        deger1=deger+" "+recete.tableWidget.item(item,2).text()+"  "
        recete2.label.setText(deger1)

# veritabanından bilgi çek

        bul2=myddb.cek2(deger0,"recete","menukod")
        bul=myddb.cek("select * from hammadde where hamkod>9000")
        recete2.comboBox.clear()
        i=len(bul)
        for xx1 in range(i):
            recete2.comboBox.addItem(str(bul[xx1][1])+" "+bul[xx1][2])



        i=len(bul2)
        j=5
        recete2.tableWidget_2.setRowCount(i)
        aa=0
        toplam=0
        print bul2
        for row1 in bul2:

            item=str(row1[2])


            bul3=myddb.cek2(item,"hammadde","hamkod")
            print bul3

            item=str(bul3[0][1])
            file.write(item+" ")
            recete2.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=bul3[0][2]
            #file.write(item+" ")
            recete2.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=bul3[0][3]
            file.write(item+" ")
            recete2.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            recete2.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            aa=aa+1
            file.write(item+"\n")

        file.close()

        recete2.tableWidget.setColumnWidth(0, 50)
        recete2.tableWidget.setColumnWidth(1, 250)
        recete2.tableWidget.setColumnWidth(2, 50)
        recete2.tableWidget.setColumnWidth(3, 50)
        recete2.tableWidget_2.setColumnWidth(0, 50)
        recete2.tableWidget_2.setColumnWidth(1, 220)
        recete2.tableWidget_2.setColumnWidth(2, 50)
        recete2.tableWidget_2.setColumnWidth(3, 75)


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
        recete2.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        aa=0
        toplam=0
        for row1 in bul:
            item=str(row1[1])
            recete2.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=row1[2]
            recete2.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=row1[3]
            recete2.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[4])
            recete2.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            aa=aa+1




    @pyqtSlot(int,int)
    def slothamclick(item,item2):
    #   hammadde listesinden çiftklikle tablewidget_2 ye hammadde bilgisini ekliyor.
        i=recete2.tableWidget_2.rowCount()
        deger1=recete2.tableWidget.item(item,0).text()
        deger2=recete2.tableWidget.item(item,1).text()
        deger3=recete2.tableWidget.item(item,2).text()


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
        item = '0'
        recete2.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
        #recete2.lineEdit.setFocus(True)
        recete2.tableWidget_2.setFocus()
        recete2.tableWidget_2.setCurrentCell(aa,3)
        QtCore.QSound(r"horn.wav").play()


    @pyqtSlot()
    def slotrecete2kaydet():
        deger0=recete2.label_3.text()
        myddb.sil(deger0,"recete","menukod")
        i=recete2.tableWidget_2.rowCount()
        for item in range(i):

            deger1=recete2.tableWidget_2.item(item,0).text()
            deger2=recete2.tableWidget_2.item(item,3).text()
            print deger0 , deger1 , deger2
            deger2=fatura.kontrol(deger2)
            myddb.kaydet(deger0,deger1,deger2)
        myddb.conn.commit()


# veritabanından bilgi çek

    @pyqtSlot()
    def slotpuss(item2):
        print "reçete arayüzü açıldı"
        mainWindow.statusbar.showMessage(
            u"Namık ERDOĞAN © 2016         Reçete                            Bishop Restaurant")
        recete.move(13, 10)
        recete.show()
        recete.setFixedSize(recete.size());  # dialog penceresi boyutu sabit (fixed)
        i=len(bul)
        j=5
        recete.tableWidget.setRowCount(i)
        recete.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        recete.tableWidget.setColumnWidth(0,50)
        recete.tableWidget.setColumnWidth(1,50)
        recete.tableWidget.setColumnWidth(2,220)
        recete.tableWidget.setColumnWidth(3,100)
        # TODO: Sutün genişlikleri ayarlanacak

        aa=0
        toplam=0
        for row1 in bul:
            item=str(row1[0])
            recete.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=str(row1[1])
            bul2 = myddb.cek2(item, "recete", "menukod")
            recete.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=row1[2]
            recete.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            proto=QtGui.QTableWidgetItem(item)
            proto.setTextAlignment(Qt.AlignRight)
            recete.tableWidget.setItem(aa, 3, proto)
            item=str(row1[4])
            recete.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            if len(bul2) == 0:

                recete.tableWidget.item(aa, 2).setBackground(QtGui.QColor('red'))

            aa=aa+1
        recete.lineEdit.setFocus(True)


    @pyqtSlot()
    def slotfatura(item2):
        fatura.goster()

    @pyqtSlot()
    def slotmaliyet(item2):
        print "maliyet arayüzü açıldı"
        maliyet.show()

    @pyqtSlot()
    def slotcari(item2):
        print "cari arayüzü açıldı"
        cari.show()

    @pyqtSlot()
    def slotpuss4(item2):
        if item2 == 100:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016    Kullanıcı adı girilmedi !!!    Bishop Restaurant")
            mainWindow.pushButton.blockSignals(1)
            mainWindow.pushButton_2.blockSignals(1)

            mainWindow.pushButton_3.blockSignals(1)

        if item2 == 12345:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016       Mutfak Şef          Bishop Restaurant")
            mainWindow.pushButton_2.blockSignals(0)

        if item2 == 101:
            mainWindow.close()




        if item2 == 1234:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016      Yönetici                  Bishop Restaurant")
            mainWindow.pushButton.blockSignals(0)
            mainWindow.pushButton_2.blockSignals(0)

            mainWindow.pushButton_3.blockSignals(0)

    @pyqtSlot()
    def slotpuss5(item2):
        logger.info(item2)
        print "shdfhdfdjhfg"

    @pyqtSlot()
    def slottextch(item2):
        print "kjkljlk reçete"
        a=item2.toUtf8()
        a='%'+str(a)+'%'
        print a


        sql3 = "select * from hammadde where (kategori=2 or kategori=3) and  ( hamkod like '"+a+"' or hamad like '"+a+"'  ) order by hamkod"

        myddb.cur.execute(sql3)
        bul=myddb.cur.fetchall()


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
    def copyFunction():
        print "f10 a bastın"

        elma=fatura.tableWidget_2.currentRow()
        elma1=fatura.tableWidget_2.rowCount()
        if elma==-1:
            abc = QKeyEvent(QEvent.KeyPress, Qt.Key_Tab, Qt.NoModifier)
            QCoreApplication.postEvent(fatura, abc)

        else:
            fatura.tableWidget_2.focusNextChild()
            '''

            if fatura.tableWidget_2.currentColumn()==5:
                if elma1 == elma + 1:
                    fatura.pushButton.setFocus()
                else:
                    fatura.tableWidget_2.setCurrentCell(elma + 1, 2)
                print elma '''


    @pyqtSlot()
    def slotrecete2satirsil():
        bb=recete2.tableWidget_2.currentRow()
        recete2.tableWidget_2.removeRow(bb)


    # dosya açmak için dialog
    # fileName =(QtGui.QFileDialog.getOpenFileName(mainWindow, u"Düzenlenecek dosyayı seçin", ".", u"Metin dosyaları (*.txt)"))
    app.setWindowIcon(QtGui.QIcon('nenra.png'))
    mainWindow.verticalLayoutWidget_2.setStyleSheet("background-image: url(newyork.png);")
    mainWindow.pushButton.setStyleSheet("color: black ;  background-image: url(images/image.png)")
    mainWindow.pushButton_2.setStyleSheet("color: black ;  background-image: url(images/fatura.png)")
    mainWindow.pushButton_3.setStyleSheet("color: black ;  background-image: url(images/maliyet.png)")
    mainWindow.pushButton_4.setStyleSheet("color: black ;  background-image: url(images/nenra.png)")
    mainWindow.pushButton.clicked.connect(slotpuss)
    mainWindow.pushButton_2.clicked.connect(slotfatura)
    mainWindow.pushButton_3.clicked.connect(slotmaliyet)
    mainWindow.pushButton_4.clicked.connect(slotcari)
    mainWindow.statusbar.showMessage(u"Namık ERDOĞAN © 2016 1.0518                                        Bishop Restaurant")
    recete.lineEdit.textChanged.connect(slottextch)



    recete.tableWidget.cellClicked.connect(slotrecete2)
    recete2.lineEdit.textChanged.connect(slotrecete2sql)
    recete2.tableWidget.cellClicked.connect(slothamclick)
    recete2.pushButton.clicked.connect(slotrecete2kaydet)
    recete2.pushButton_3.clicked.connect(slotrecete2satirsil)


    recete.setWindowModality(Qt.ApplicationModal)
    recete2.setWindowModality(Qt.ApplicationModal)
    fatura.setWindowModality(Qt.ApplicationModal)
    maliyet.setWindowModality(Qt.ApplicationModal)
    login.setWindowModality(Qt.ApplicationModal)

    sh = QtGui.QShortcut(fatura)
    sh.setKey("Enter")
    fatura.connect(sh, QtCore.SIGNAL("activated()"), copyFunction)
    sh1 = QtGui.QShortcut(fatura)
    sh1.setKey(QtCore.Qt.Key_Down)
    fatura.connect(sh1, QtCore.SIGNAL("activated()"), copyFunction)

    mainWindow.connect(login, QtCore.SIGNAL("acac1(int)"), slotpuss4)
    mainWindow.connect(workerthread, QtCore.SIGNAL("acac1(int)"), slotpuss4)
    mainWindow.connect(fatura,QtCore.SIGNAL("acac"),slotpuss5)

    mainWindow.move(13, 10)

    #mainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #mainWindow.raise_()


    mainWindow.show()


    #mainWindow.setWindowState(mainWindow.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
    #mainWindow.activateWindow()
    login.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    login.setStyleSheet("color:red ; background-color: orange;")
    login.show()
    login.raise_()




    return app.exec_()

if __name__ == "__main__":
    main()
