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
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from mainwindow import MainWindow
from mainwindow import Recete
from mainwindow import Recete2
from fatura import Fatura
from mainwindow import Maliyet
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

class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle(u"NENRA 2016 Kullanıcı Girişi      ")
        self.labelname = QtGui.QLabel(self)
        self.labelpass = QtGui.QLabel(self)
        self.textName = QtGui.QLineEdit(self)
        self.textPass = QtGui.QLineEdit(self)
        self.labelname.setText(u"Kullanıcı Adı")
        self.labelpass.setText(u"Parola")
        self.buttonLogin = QtGui.QPushButton(u'Giriş', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.labelname)
        layout.addWidget(self.textName)
        layout.addWidget(self.labelpass)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        self.elma = 1234
        self.workerthread=WorkerThread()
        self.workerthread.start()

    def handleLogin(self):
        if (self.textName.text() == 'mehmet' and
                    self.textPass.text() == '1234'):
            self.accept()
            self.elma = 123
        elif (self.textName.text() == 'demo' and
            self.textPass.text() == 'demo'):
            self.accept()
            self.elma=1234
        else:
            QtGui.QMessageBox.warning(
                self, 'Hata', u'Kullanıcı adı yada parola yanlış')

class WorkerThread(QThread):
    acac1 = pyqtSignal(int)
    def __init__(self,parent=None):
        super(WorkerThread,self).__init__(parent)





    def run(self):
        with open("ver.png", "r") as dosya:
            elma1 = dosya.read()

        urlpath = urllib2.urlopen('http://nen.duckdns.org:8080/dist/ver.png')
        string = urlpath.read()
        print string, elma1
        if elma1 == string:
            print u"aynı"
        else:
            self.filename = string
            rq = urllib2.urlopen('http://nen.duckdns.org:8080/dist/' + self.filename)
            fSize = int(rq.info()['Content-Length'])
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


def main():
    #app =QApplication(sys.argv)
    app.processEvents()

    mainWindow = MainWindow()


    recete=Recete()
    recete2=Recete2()
    fatura=Fatura()
    maliyet=Maliyet()
    myddb=Myddb()



    bul=myddb.cek("select * from menu")
    logger.info('Program opened 1002 '+str(os.getpid()))





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

        recete2.lineEdit.setText("")
#   recete2 ekranı hazırlanıyor
        deger0=recete.tableWidget.item(item,0).text()
        recete2.label_3.setText(deger0)
        file = open(deger0+".txt", "w")


        deger=recete.tableWidget.item(item,1).text()
        deger1=deger+" "+recete.tableWidget.item(item,2).text()+"  "
        recete2.label.setText(deger1)

# veritabanından bilgi çek

        bul2=myddb.cek2(deger0,"recete","menukod")
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
        QSound(r"horn.wav").play()


    @pyqtSlot()
    def slotrecete2kaydet():
        deger0=recete2.label_3.text()
        myddb.sil(deger0,"recete","menukod")
        i=recete2.tableWidget_2.rowCount()
        for item in range(i):

            deger1=recete2.tableWidget_2.item(item,0).text()
            deger2=recete2.tableWidget_2.item(item,3).text()
            print deger0 , deger1 , deger2
            deger2=kontrol(deger2)
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
            recete.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=row1[2]
            recete.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            proto=QtGui.QTableWidgetItem(item)
            proto.setTextAlignment(Qt.AlignRight)
            recete.tableWidget.setItem(aa, 3, proto)
            item=str(row1[4])
            recete.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            aa=aa+1
        recete.lineEdit.setFocus(True)


    @pyqtSlot()
    def slotfatura2(item2):
        fatura.goster()

    @pyqtSlot()
    def slotpuss3(item2):
        print "maliyet arayüzü açıldı"
        maliyet.show()
        maliyet.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        maliyet.dateEdit.setDate(some_date)
        maliyet.dateEdit_2.setDate(some_date)

        StartDate="01/04/16"

        EndDate = datetime.datetime.strptime(StartDate, "%d/%m/%y")
        now = datetime.datetime.now()- datetime.timedelta(days=1)
        dt=now-EndDate
        print dt.days
        #mainWindow.plainTextEdit.appendPlainText(str(dt.days))
        for i in range(dt.days):
            EndDate = EndDate + datetime.timedelta(days=1)
            sql= " select * from harcanan where tarih like %s"
            sonuc=myddb.cur.execute(sql,[(EndDate.strftime('%Y-%m-%d')+"%")])
            if sonuc==0:
                print " kaydediliyor"
                tar=EndDate.strftime('%d%m%Y')

                sql2="SELECT menu.menukod,hammaddeid,miktar,adet FROM SATDATA inner join menu on urunkod=menukod and DATE(tarih)=%s  inner join recete on  menu.menuid=recete.menuid "
                bilgi=myddb.cur.execute(sql2,[(EndDate.strftime('%Y-%m-%d'))])
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
    def slotpuss4(item2):
        mainWindow.statusbar.showMessage(u"Namık ERDOĞAN © 2016  GÜNCELLENİYOR %"+str(item2)+"       Bishop Restaurant")
        if item2==100:
            os.system('taskkill /PID '+str(os.getpid()))



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
        item="            ÜRÜN    AÇIKLAMA                                   ADET           TUTAR                MALIYET                     ORAN "
        c.drawString(10,810,item)
        for row1 in bul:
            sql1="select hurunkod,sum(hmiktar*fiyat1),harcanan.tarih from harcanan inner join hammadde on hhammaddeid=hammaddeid where DATE(tarih)>=%s and DATE(tarih)<=%s and hurunkod=%s"
            bul1=myddb.cur.execute(sql1,(tar1,tar2,str(row1[0])))
            bul1=myddb.cur.fetchall()


            item=str(row1[0])
            c.drawString(45,800-(15*(bb+1)),item)
            maliyet.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            item=row1[1]
            c.drawString(80,800-(15*(bb+1)),item)
            maliyet.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item=str(row1[2])
            c.drawString(230,800-(15*(bb+1)),item)
            toplam=toplam+row1[2]
            maliyet.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            item=str(row1[3])
            c.drawString(270,800-(15*(bb+1)),item)
            toplam1=toplam1+row1[3]
            maliyet.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item=str(bul1[0][1])
            toplam2=toplam2+bul1[0][1]
            c.drawString(350,800-(15*(bb+1)),item)
            maliyet.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            print row1[3]
            if int(row1[3])==0:
                item="% 100"
            else:
                item="% "+str(int((bul1[0][1])/row1[3]*100))
            c.drawString(450,800-(15*(bb+1)),item)
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
        c.drawString(230,800-(15*(bb+1)),str(toplam))
        c.drawString(270,800-(15*(bb+1)),str(int(toplam1)))
        c.drawString(350,800-(15*(bb+1)),str(int(toplam2)))
        c.drawString(450,800-(15*(bb+1)),"% "+str(int(toplam2/toplam1*100)))

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
    mainWindow.pushButton.setStyleSheet("color: black ;  background-image: url(image.png)")
    mainWindow.pushButton_2.setStyleSheet("color: black ;  background-image: url(fatura.png)")
    mainWindow.pushButton_3.setStyleSheet("color: black ;  background-image: url(maliyet.png)")
    mainWindow.pushButton.clicked.connect(slotpuss)
    mainWindow.pushButton_2.clicked.connect(slotfatura2)
    mainWindow.pushButton_3.clicked.connect(slotpuss3)
    mainWindow.statusbar.showMessage(u"Namık ERDOĞAN © 2016                                             Bishop Restaurant")
    recete.lineEdit.textChanged.connect(slottextch)



    recete.tableWidget.cellClicked.connect(slotrecete2)
    recete2.lineEdit.textChanged.connect(slotrecete2sql)
    recete2.tableWidget.cellClicked.connect(slothamclick)
    recete2.pushButton.clicked.connect(slotrecete2kaydet)
    recete2.pushButton_3.clicked.connect(slotrecete2satirsil)
    maliyet.pushButton.clicked.connect(sloturunmaliyet)
    maliyet.pushButton_2.clicked.connect(sloturunmaliyetpdf)

    recete.setWindowModality(Qt.ApplicationModal)
    recete2.setWindowModality(Qt.ApplicationModal)
    fatura.setWindowModality(Qt.ApplicationModal)
    maliyet.setWindowModality(Qt.ApplicationModal)

    sh = QtGui.QShortcut(fatura)
    sh.setKey("Enter")
    fatura.connect(sh, QtCore.SIGNAL("activated()"), copyFunction)
    mainWindow.connect(login.workerthread,SIGNAL("acac1(int)"),slotpuss4)
    if login.elma ==123:
        mainWindow.statusbar.showMessage(
            u"Namık ERDOĞAN © 2016       Mehmet TUNCER          Bishop Restaurant")
        mainWindow.pushButton.blockSignals(1)

        mainWindow.pushButton_3.blockSignals(1)

    if login.elma == 1234:
        mainWindow.statusbar.showMessage(
                u"Namık ERDOĞAN © 2016              demo                     Bishop Restaurant")


    mainWindow.move(13, 10)
    mainWindow.show()




    return app.exec_()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtGui.QDialog.Accepted:
        main()




