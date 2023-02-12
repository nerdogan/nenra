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
# pyinstaller --clean --win-private-assemblies -F masa.py   --distpath="C:\Users\NAMIK\Desktop\masa" -w
# pyinstaller --clean --win-private-assemblies -F  nenra.py   --distpath="C:\Users\bisho\Desktop\nenra" -w
import sys, os
import datetime
import logging
import decimal
# import urllib2
import time
from threading import Thread
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import *

from mainwindow import MainWindow
from recete import Recete
from fatura import Fatura
from maliyet import Maliyet
from cari import Cari
from stok import Stok
from login import Login
from rapor import Rapor
from masraf import Masraf
from mdb.modulemdb import Myddb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('hello.log', encoding="UTF-8")
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


myddb = Myddb()


class WorkerThread(QThread):

    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)
        # self.myddb = Myddb()
        # your code

    def run1(self, EndDate):
        print(EndDate.strftime('%d%m%Y'))
        sql = " select * from harcanan where tarih= %s"
        sonuc = myddb.cur.execute(sql, [(EndDate.strftime('%Y-%m-%d'))])
        valnen = []
        if sonuc == 0:
            print(" kaydediliyor")
            tar = EndDate.strftime('%d%m%Y')

            sql2 = "SELECT hammadde.hamkod,recete.hamkod,miktar,adet " \
                   "FROM (select * from bishop.ciro where tarih=%s union all select * from bishop.ciro1 where tarih=%s) as ciroo  inner join hammadde on pluno=hamkod " \
                   "and tarih=%s  inner join recete on " \
                   " hammadde.hamkod=recete.menukod"
            bilgi = myddb.cur.execute(sql2, [(EndDate.strftime('%Y-%m-%d')), (EndDate.strftime('%Y-%m-%d')),
                                             (EndDate.strftime('%Y-%m-%d'))])
            print(bilgi)
            valnen = []
            if bilgi != 0:
                bilgi2 = myddb.cur.fetchall()
                for row1 in bilgi2:
                    hmikt = row1[2] * decimal.Decimal(row1[3])

                    sql1 = "insert into harcanan " \
                           "(hurunkod,hhammaddeid,hmiktar,fiyat,tarih) " \
                           "values (%s,%s,%s,%s,%s)"
                    valnen.append((row1[0], row1[1], hmikt, "0", EndDate))
                    # myddb.cur.execute(sql1, (row1[0],
                    # row1[1], hmikt, "0", EndDate))

                myddb.cur.executemany(sql1, valnen)
                myddb.conn.commit()
                print(valnen)

    def run(self):
        selfstart_time = time.time()
        StartDate = "01/01/22"
        EndDate = datetime.datetime.strptime(StartDate, "%d/%m/%y")
        now = datetime.datetime.now() - datetime.timedelta(days=1)
        dt = now - EndDate
        print(dt.days)
        # mainWindow.plainTextEdit.appendPlainText(str(dt.days))
        dum = []
        for i in range(dt.days + 1):
            dum.append(Thread(target=self.run1, args=[EndDate]))
            EndDate = EndDate + datetime.timedelta(days=1)
            dum[i].start()
            # time.sleep(0.02)
            dum[i].join()

        elapsed_time = time.time() - selfstart_time
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

            rq = urllib2.urlopen('http://nen.duckdns.org:8080/dist/' 
            + self.filename)
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
    app = QApplication(sys.argv)
    app.processEvents()

    sound = QSound("./images/ses.wav")
    sound.play()

    mainWindow = MainWindow()
    login = Login()


    recete = Recete()
    fatura = Fatura()
    maliyet = Maliyet()
    cari = Cari()
    stok = Stok()
    rapor = Rapor()
    masraf = Masraf()
    workerthread = WorkerThread()
    workerthread.start()

    logger.info('Program opened  ' + str(os.getpid()))

    @pyqtSlot()
    def slotpuss(item2):
        myddb = Myddb()
        print("reçete arayüzü açıldı")
        bul = myddb.cek("select * from hammadde where kategori=2 or"
                        " kategori=3 order by hamkod")

        mainWindow.statusbar.showMessage(
            u"Namık ERDOĞAN © 2016         Reçete 2020.03"
            u"                        Bishop Restaurant")
        recete.move(13, 10)
        recete.show()
        recete.setFixedSize(recete.size())
        # dialog penceresi boyutu sabit (fixed)
        i = len(bul)
        recete.tableWidget.setRowCount(i)
        recete.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        recete.tableWidget.setColumnWidth(0, 50)
        recete.tableWidget.setColumnWidth(1, 50)
        recete.tableWidget.setColumnWidth(2, 220)
        recete.tableWidget.setColumnWidth(3, 100)
        # TODO: Sutün genişlikleri ayarlanacak

        aa = 0
        toplam = 0
        for row1 in bul:
            item = str(row1[0])
            recete.tableWidget.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            item = str(row1[1])
            bul2 = myddb.cek2(item, "recete", "menukod")
            recete.tableWidget.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            item = row1[2]
            recete.tableWidget.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
            item = str(row1[3])
            proto = QtWidgets.QTableWidgetItem(item)
            proto.setTextAlignment(Qt.AlignRight)
            recete.tableWidget.setItem(aa, 3, proto)
            item = str(row1[4])
            recete.tableWidget.setItem(aa, 4, QtWidgets.QTableWidgetItem(item))
            if len(bul2) == 0:
                recete.tableWidget.item(aa, 2).setBackground(
                    QtGui.QColor('red'))

            aa = aa + 1
        recete.lineEdit.setFocus(True)

    @pyqtSlot()
    def slotfatura(item2):
        fatura.goster()
        fatura.lineEdit.setText(item2)

    @pyqtSlot()
    def slottediye(item2):
        if item2 == "VADE":
            cari.show()
         #   cari.slotcarivade()

    @pyqtSlot()
    def slotmaliyet(item2):
        print("maliyet arayüzü açıldı")
        maliyet.show()

    @pyqtSlot()
    def slotcari(item2):
        print("cari arayüzü açıldı")
        cari.show()

    @pyqtSlot()
    def slotstok(item2):
        print("stok arayüzü açıldı")
        stok.show()
        stok.raise_()

    @pyqtSlot()
    def slotkasa(item2):
        print("kasa arayüzü açıldı")
        rapor.show()

    @pyqtSlot()
    def slotmasraf(item2):
        print("masraf arayüzü açıldı")
        masraf.show()
        masraf.raise_()

    @pyqtSlot()
    def slotpuss4(item2):
        print(item2)
        mainWindow.show()
        mainWindow.raise_()
        if item2 == 100:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016   Kullanıcı adı girilmedi !!! "
                u"   Bishop Restaurant")
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
                u"Namık ERDOĞAN © 2016       Mutfak Şef   "
                u"       Bishop Restaurant")
            mainWindow.pushButton_2.blockSignals(0)
        if item2 == 123456:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016       Kasiyer      "
                u"    Bishop Restaurant")
            mainWindow.pushButton_5.blockSignals(0)

        if item2 == 101:
            mainWindow.close()

        if item2 == 1234:
            mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016  26122022  Yönetici "
                u"                 Bishop Restaurant")
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
        logger.info(item2 + " nolu fişi göster")

        fatura.goster()
        fatura.lineEdit_5.setText(item2)
        fatura.fisgetir(item2)

    @pyqtSlot()
    def copyFunction(e):
        print("f10 a bastın")
        print(e.key())
        '''

            if fatura.tableWidget_2.currentColumn()==5:
                if elma1 == elma + 1:
                    fatura.pushButton.setFocus()
                else:
                    fatura.tableWidget_2.setCurrentCell(elma + 1, 2)
                print elma '''

    # dosya açmak için dialog
    # fileName =(QtGui.QFileDialog.getOpenFileName(mainWindow,
    # u"Düzenlenecek dosyayı seçin", ".", u"Metin dosyaları (*.txt)"))
    app.setWindowIcon(QtGui.QIcon('nenra.png'))
    mainWindow.pushButton_8.setStyleSheet("border-image: url(images/newyork.png) 0 0 0 0 stretch stretch;")
    mainWindow.pushButton.setStyleSheet("color: black ;  background-image: url(images/image.png)")
    mainWindow.pushButton_2.setStyleSheet("color: black ;  background-image: url(images/fatura.png)")
    mainWindow.pushButton_3.setStyleSheet("color: black ;  background-image: url(images/maliyet.png)")
    mainWindow.pushButton_4.setStyleSheet("color: black ;  background-image: url(images/nenra.png)")
    mainWindow.pushButton_5.setStyleSheet("color: black ;  background-image: url(images/nenra.png)")
    mainWindow.pushButton_6.setStyleSheet("color: black ;  background-image: url(images/maliyet.png)")
    mainWindow.pushButton_7.setStyleSheet("color: black ;  background-image: url(images/masraf.png)")

    mainWindow.pushButton.clicked.connect(slotpuss)
    mainWindow.pushButton_2.clicked.connect(lambda: slotfatura(""))
    mainWindow.pushButton_3.clicked.connect(slotmaliyet)
    mainWindow.pushButton_4.clicked.connect(slotcari)
    mainWindow.pushButton_5.clicked.connect(slotstok)
    mainWindow.pushButton_6.clicked.connect(slotkasa)
    mainWindow.pushButton_7.clicked.connect(slotmasraf)

    mainWindow.actionTediye_Fi_i.triggered.connect(lambda: slotfatura("TED"))
    mainWindow.actionSay_m_Fi_i.triggered.connect(lambda: slotfatura("SAY"))
    mainWindow.actionStok_Tan_mlama.triggered.connect(lambda: slottediye("VADE"))
    mainWindow.actionGelir_Tablosu_Ayl_k.triggered.connect(lambda: slotfatura("ZZ"))
    mainWindow.statusbar.showMessage(
        u"Namık ERDOĞAN © 2016 2022 v2.99  "
        u"                                  Bishop Restaurant")

    # recete.setWindowModality(Qt.ApplicationModal)
    fatura.setWindowModality(Qt.ApplicationModal)
    maliyet.setWindowModality(Qt.ApplicationModal)
    login.setWindowModality(Qt.ApplicationModal)
    rapor.setWindowModality(Qt.ApplicationModal)
    stok.setWindowModality(Qt.ApplicationModal)
    cari.setWindowModality(Qt.ApplicationModal)
 #   fatura.keyPressEvent=copyFunction


 #   fatura.connect(QtGui.QShortcut(QtGui.QKeySequence(Qt.Key_Enter),  fatura), QtCore.SIGNAL('activated()'), copyFunction)

#    mainWindow.connect(login, QtCore.SIGNAL("acac1(int)"), slotpuss4)
    login.acac1.connect(slotpuss4)
#    mainWindow.connect(fatura, QtCore.SIGNAL("acac"), slotpuss5)
    fatura.acac.connect(slotpuss5)
#    mainWindow.connect(cari, QtCore.SIGNAL("fisac"), slotpuss6)
    cari.my_signal.connect(slotpuss6)
   # mainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    mainWindow.move(13, 10)

    # mainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # mainWindow.raise_()

    mainWindow.show()
    mainWindow.menubar.setStyleSheet(
        "    QMenuBar {    background-color: orange;   } "
        "QMenuBar::item {    background-color: orange;   } ")
    mainWindow.setStyleSheet(" background-color: orange;")

    # mainWindow.setWindowState(mainWindow.windowState() &
    # ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)

    # mainWindow.activateWindow()
    login.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    login.setStyleSheet("color:red ; background-color: orange;")
    login.show()
    login.raise_()

    return app.exec_()


if __name__ == "__main__":
    main()
