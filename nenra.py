# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      NAMIK ERDOĞAN
#
# Created:     22.01.2014
# Copyright:   (c) NAMIK ERDOĞAN  2014
# Licence:     <your licence>
# -------------------------------------------------------------------------------
# pyinstaller --clean --win-private-assemblies -F masa.py --distpath="C:\Users\NAMIK\Desktop\masa" -w
import subprocess
import sys
import re
import datetime
import logging
#import urllib2
import os
import time
from threading import Thread

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
from stok import Stok
from login import Login
from rapor import Rapor
from masraf import Masraf
from modulemdb import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('hello.log',encoding = "UTF-8")
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
def run1(EndDate):
    myddb = Myddb()

    print (EndDate.strftime('%d%m%Y'))
    sql = " select * from harcanan where tarih= %s"
    sonuc = myddb.cur.execute(sql, [(EndDate.strftime('%Y-%m-%d'))])
    valnen = []
    if sonuc == 0:
        print (" kaydediliyor")
        tar = EndDate.strftime('%d%m%Y')

        sql2 = "SELECT hammadde.hamkod,recete.hamkod,miktar,adet FROM bishop.ciro inner join hammadde on pluno=hamkod and DATE(tarih)=%s  inner join recete on  hammadde.hamkod=recete.menukod"
        bilgi = myddb.cur.execute(sql2, [(EndDate.strftime('%Y-%m-%d'))])  # type: object
        print (bilgi)
        valnen = []
        if bilgi != 0:
            bilgi2 = myddb.cur.fetchall()
            for row1 in bilgi2:
                hmikt = row1[2] * row1[3]

                sql1 = "insert into harcanan (hurunkod,hhammaddeid,hmiktar,fiyat,tarih) values (%s,%s,%s,%s,%s)"
                valnen.append((row1[0], row1[1], hmikt, "0", EndDate))
                # myddb.cur.execute(sql1, (row1[0], row1[1], hmikt, "0", EndDate))

            myddb.cur.executemany(sql1, valnen)
            myddb.conn.commit()
            print(valnen)


selfstart_time = time.time()

StartDate = "01/01/20"

EndDate = datetime.datetime.strptime(StartDate, "%d/%m/%y")
now = datetime.datetime.now() - datetime.timedelta(days=1)
dt = now - EndDate
print(dt.days)
# mainWindow.plainTextEdit.appendPlainText(str(dt.days))
dum=[]
for i in range(dt.days + 1):
    dum.append( Thread(target=run1, args=[EndDate]))
    EndDate = EndDate + datetime.timedelta(days=1)
    dum[i].start()
    if i % 30 == 0:
        time.sleep(1)

for i in range(dt.days + 1):
    dum[i].join()
elapsed_time = time.time() - selfstart_time
print(elapsed_time)



class WorkerThread(QThread):


    def __init__(self,parent=None):
        super(WorkerThread,self).__init__(parent)
        self.myddb = Myddb()
        self.start_time = time.time()
        # your code

    def run(self):


        StartDate = "01/01/20"

        EndDate = datetime.datetime.strptime(StartDate, "%d/%m/%y")
        now = datetime.datetime.now() - datetime.timedelta(days=1)
        dt = now - EndDate
        print (dt.days)
        # mainWindow.plainTextEdit.appendPlainText(str(dt.days))
        for i in range(dt.days + 1):
            print (EndDate.strftime('%d%m%Y'))
            sql = " select * from harcanan where tarih= %s"
            sonuc = self.myddb.cur.execute(sql, [(EndDate.strftime('%Y-%m-%d'))])
            valnen = []
            if sonuc == 0:
                print (" kaydediliyor")
                tar = EndDate.strftime('%d%m%Y')

                sql2 = "SELECT hammadde.hamkod,recete.hamkod,miktar,adet FROM bishop.ciro inner join hammadde on pluno=hamkod and DATE(tarih)=%s  inner join recete on  hammadde.hamkod=recete.menukod"
                bilgi = self.myddb.cur.execute(sql2, [(EndDate.strftime('%Y-%m-%d'))])  # type: object
                print (bilgi)
                valnen = []
                if bilgi != 0:
                    bilgi2 = self.myddb.cur.fetchall()
                    for row1 in bilgi2:
                        hmikt = row1[2] * row1[3]

                        sql1 = "insert into harcanan (hurunkod,hhammaddeid,hmiktar,fiyat,tarih) values (%s,%s,%s,%s,%s)"
                        valnen.append((row1[0], row1[1], hmikt, "0", EndDate))
                        # self.myddb.cur.execute(sql1, (row1[0], row1[1], hmikt, "0", EndDate))

                    self.myddb.cur.executemany(sql1, valnen)
                    self.myddb.conn.commit()
                    print(valnen)

            EndDate = EndDate + datetime.timedelta(days=1)
        elapsed_time = time.time() - self.start_time
        print(elapsed_time)

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
    stok = Stok()
    rapor = Rapor()
    masraf = Masraf()
#    workerthread = WorkerThread()
 #   workerthread.start()

    logger.info('Program opened  '+str(os.getpid()))



    @pyqtSlot(int,int)
    def slotrecete2(item,item2):

        recete2.lineEdit.setText("")
#   recete2 ekranı hazırlanıyor
        recete2.label_2.setText(str(item))



        deger0=recete.tableWidget.item(item,1).text()
        recete2.label_3.setText(deger0)
        file = open(deger0+".txt", "w")


        deger0=recete.tableWidget.item(item,1).text()
        deger1=deger0+" "+recete.tableWidget.item(item,2).text()+"  "
        recete2.label.setText(deger1)

# veritabanından bilgi çek

        bul2=myddb.cek2(deger0,"recete","menukod")
        bul=myddb.cek("select * from hammadde where kategori=2")
        myddb.conn.commit()
        recete2.comboBox.clear()
        i=len(bul)
        for xx1 in range(i):
            recete2.comboBox.addItem(str(bul[xx1][1])+" "+bul[xx1][2])



        i=len(bul2)
        j=5
        recete2.tableWidget_2.setRowCount(i)
        aa=0
        toplam=0
        topelma=0

        for row1 in bul2:

            item=str(row1[2])


            bul3=myddb.cek2(item,"hammadde","hamkod")
            myddb.conn.commit()


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
            file.write(item + " ")

            item = str(bul3[0][6])
            file.write(item + "\n")
            recete2.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item))

            elma=(bul3[0][6])*(row1[3])*(100+(bul3[0][4]))/100
            topelma=topelma+elma
            item =  str(elma)
            file.write(item + "\n")
            item = str("{:.2f}".format(elma))
            item = QtGui.QTableWidgetItem(item)
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

            recete2.tableWidget_2.setItem(aa, 5, QtGui.QTableWidgetItem(item))

            aa=aa+1

        recete2.label_4.setText(str("{:.2f}".format(topelma)))

        file.close()

        recete2.tableWidget.setColumnWidth(0, 50)
        recete2.tableWidget.setColumnWidth(1, 250)
        recete2.tableWidget.setColumnWidth(2, 50)
        recete2.tableWidget.setColumnWidth(3, 50)
        recete2.tableWidget_2.setColumnWidth(0, 50)
        recete2.tableWidget_2.setColumnWidth(1, 150)
        recete2.tableWidget_2.setColumnWidth(2, 50)
        recete2.tableWidget_2.setColumnWidth(3, 75)
        recete2.tableWidget_2.setColumnWidth(4, 75)
        recete2.tableWidget_2.setColumnWidth(5, 60)


        recete2.show()
        recete2.lineEdit.setFocus(True)



    @pyqtSlot()
    def slotrecete2sql(item2):

        a=item2
        a=str(a)


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
        QtGui.QSound(r"horn.wav").play()


    @pyqtSlot()
    def slotrecete2kaydet():
        deger0=recete2.label_3.text()
        myddb.sil(deger0,"recete","menukod")
        i=recete2.tableWidget_2.rowCount()
        for item in range(i):

            deger1=recete2.tableWidget_2.item(item,0).text()
            deger2=recete2.tableWidget_2.item(item,3).text()
            print (deger0 , deger1 , deger2)
            deger2=fatura.kontrol(deger2)
            myddb.kaydet(deger0,deger1,deger2)
        myddb.conn.commit()
        recete2.close()
        slotrecete2(int(recete2.label_2.text()),0)



# veritabanından bilgi çek

    @pyqtSlot()
    def slotpuss(item2):
        print ("reçete arayüzü açıldı")
        bul = myddb.cek("select * from hammadde where kategori=2 or kategori=3 order by hamkod")

        mainWindow.statusbar.showMessage(
            u"Namık ERDOĞAN © 2016         Reçete 1.20                         Bishop Restaurant")
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
        fatura.lineEdit.setText(item2)

    @pyqtSlot()
    def slottediye(item2):
        if item2=="VADE":
            cari.show()
            cari.slotcarivade()





    @pyqtSlot()
    def slotmaliyet(item2):
        print ("maliyet arayüzü açıldı")
        maliyet.show()

    @pyqtSlot()
    def slotcari(item2):
        print ("cari arayüzü açıldı")
        cari.show()

    @pyqtSlot()
    def slotstok(item2):
        print ("stok arayüzü açıldı")
        stok.show()
        stok.raise_()

    @pyqtSlot()
    def slotkasa(item2):
        print ("kasa arayüzü açıldı")
        rapor.show()

    @pyqtSlot()
    def slotmasraf(item2):
        print ("masraf arayüzü açıldı")
        masraf.show()

    @pyqtSlot()
    def slotpuss4(item2):
        print (item2)
        if item2 == 100:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016    Kullanıcı adı girilmedi !!!    Bishop Restaurant")
            mainWindow.pushButton.blockSignals(1)
            mainWindow.pushButton_2.blockSignals(1)
            mainWindow.pushButton_3.blockSignals(1)
            mainWindow.pushButton_4.blockSignals(1)
            mainWindow.pushButton_5.blockSignals(1)
            mainWindow.pushButton_6.blockSignals(1)

            mainWindow.actionTediye_Fi_i.setEnabled(0)
            mainWindow.actionSay_m_Fi_i.setEnabled(0)
            mainWindow.actionStok_Tan_mlama.setEnabled(0)

        if item2 == 12345:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016       Mutfak Şef          Bishop Restaurant")
            mainWindow.pushButton_2.blockSignals(0)
        if item2 == 123456:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016       Kasiyer          Bishop Restaurant")
            mainWindow.pushButton_5.blockSignals(0)

        if item2 == 101:
            mainWindow.close()




        if item2 == 1234:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016  02062019   Yönetici                  Bishop Restaurant")
            mainWindow.pushButton.blockSignals(0)
            mainWindow.pushButton_2.blockSignals(0)
            mainWindow.pushButton_3.blockSignals(0)
            mainWindow.pushButton_4.blockSignals(0)
            mainWindow.pushButton_5.blockSignals(0)
            mainWindow.pushButton_6.blockSignals(0)

            mainWindow.actionTediye_Fi_i.setEnabled(1)
            mainWindow.actionSay_m_Fi_i.setEnabled(1)
            mainWindow.actionStok_Tan_mlama.setEnabled(1)

    @pyqtSlot()
    def slotpuss5(item2):
        logger.info(item2)

    @pyqtSlot()
    def slotpuss6(item2):
        logger.info(item2+" nolu fişi göster")

        fatura.goster()
        fatura.lineEdit_5.setText(item2)
        fatura.fisgetir(item2)

    @pyqtSlot()
    def slottextch(item2):

        a=item2
        a='%'+str(a)+'%'



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
        print ("f10 a bastın")

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
    mainWindow.verticalLayoutWidget_2.setStyleSheet("background-image: url(images/newyork.png);")
    mainWindow.pushButton.setStyleSheet("color: black ;  background-image: url(images/image.png)")
    mainWindow.pushButton_2.setStyleSheet("color: black ;  background-image: url(images/fatura.png)")
    mainWindow.pushButton_3.setStyleSheet("color: black ;  background-image: url(images/maliyet.png)")
    mainWindow.pushButton_4.setStyleSheet("color: black ;  background-image: url(images/nenra.png)")
    mainWindow.pushButton_5.setStyleSheet("color: black ;  background-image: url(images/nenra.png)")
    mainWindow.pushButton_6.setStyleSheet("color: black ;  background-image: url(images/maliyet.png)")
    mainWindow.pushButton_7.setStyleSheet("color: black ;  background-image: url(images/masraf.png)")


    mainWindow.pushButton.clicked.connect(slotpuss)
    mainWindow.pushButton_2.clicked.connect(slotfatura)
    mainWindow.pushButton_3.clicked.connect(slotmaliyet)
    mainWindow.pushButton_4.clicked.connect(slotcari)
    mainWindow.pushButton_5.clicked.connect(slotstok)
    mainWindow.pushButton_6.clicked.connect(slotkasa)
    mainWindow.pushButton_7.clicked.connect(slotmasraf)

    mainWindow.actionTediye_Fi_i.triggered.connect(lambda:slotfatura("TED"))
    mainWindow.actionSay_m_Fi_i.triggered.connect(lambda: slotfatura("SAY"))
    mainWindow.actionStok_Tan_mlama.triggered.connect(lambda:slottediye("VADE"))
    mainWindow.statusbar.showMessage(u"Namık ERDOĞAN © 2016 v 1.513                                   Bishop Restaurant")
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
    rapor.setWindowModality(Qt.ApplicationModal)
    stok.setWindowModality(Qt.ApplicationModal)
    cari.setWindowModality(Qt.ApplicationModal)


    fatura.connect(QtGui.QShortcut(QtGui.QKeySequence(Qt.Key_Enter), fatura), QtCore.SIGNAL('activated()'), copyFunction)

    mainWindow.connect(login, QtCore.SIGNAL("acac1(int)"), slotpuss4)
    slotpuss4(100)
    mainWindow.connect(fatura, QtCore.SIGNAL("acac"), slotpuss5)
    mainWindow.connect(cari, QtCore.SIGNAL("fisac"), slotpuss6)


    mainWindow.move(13, 10)

    #mainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #mainWindow.raise_()


    mainWindow.show()
    mainWindow.menubar.setStyleSheet("    QMenuBar {    background-color: orange;   } QMenuBar::item {    background-color: orange;   } ")
    mainWindow.setStyleSheet(" background-color: orange;")




    #mainWindow.setWindowState(mainWindow.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
    #mainWindow.activateWindow()
    login.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    login.setStyleSheet("color:red ; background-color: orange;")
    login.show()
    login.raise_()




    return app.exec_()

if __name__ == "__main__":
    main()
