from PyQt4  import QtGui
from PyQt4 import QtCore
import fdb
import MySQLdb as mdb
from datetime import datetime,timedelta
import time as ttim
from socket import *
import sys
import atexit


dizi=0
satir={}


con = fdb.connect(
    dsn='192.168.2.251/3050:D:\RESTO_2015\DATA\DATABASE.GDB',
    user='sysdba', password='masterkey',

    charset='UTF8' # specify a character set for the connection #
     )
cur=con.cursor()


class Pos1(QtGui.QWidget):

    def __init__(self):
        super(Pos1, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(10,20,1024,668)

        self.b = QtGui.QPushButton(self)
        self.b.setText(u"GİRİŞ SALON")
        self.b.move(2, 72)
        self.b.setFixedSize(110, 64)

        b1 = QtGui.QPushButton(self)
        b1.setText(u"ÖN BAHÇE")
        b1.move(2, 136)
        b1.setFixedSize(110, 64)

        b2 = QtGui.QPushButton(self)
        b2.setText(u"ARKA BAHÇE")
        b2.move(2, 200)
        b2.setFixedSize(110, 64)

        b3 = QtGui.QPushButton(self)
        b3.setText(u"1. KAT")
        b3.move(2, 264)
        b3.setFixedSize(110, 64)

        b4 = QtGui.QPushButton(self)
        b4.setText(u"2. KAT")
        b4.move(2, 328)
        b4.setFixedSize(110, 64)

        b5 = QtGui.QPushButton(self)
        b5.setText(u"KULE")
        b5.move(2, 392)
        b5.setFixedSize(110, 64)

        self.e = QtGui.QTableWidget(self)
        self.e.setGeometry(16, 500, 700, 168)
        self.e.setRowCount(10)
        self.e.setColumnCount(5)

        self.e.setColumnWidth(0,60)
        self.e.setColumnWidth(1,200)
        self.e.setStyleSheet("QTableWidget { background-color: white ; font-size: 12px}")




        self.b.clicked.connect(lambda checked, tekst=self.b.text(): self.masagoster(tekst))
        b1.clicked.connect(lambda checked, tekst=b1.text(): self.masagoster(tekst))
        b2.clicked.connect(lambda checked, tekst=b2.text(): self.masagoster(tekst))
        b3.clicked.connect(lambda checked, tekst=b3.text(): self.masagoster(tekst))
        b4.clicked.connect(lambda checked, tekst=b4.text(): self.masagoster(tekst))
        b5.clicked.connect(lambda checked, tekst=b5.text(): self.masagoster(tekst))

        self.setWindowTitle("Nenra POS 1.0.0")

    @atexit.register
    def cikis():
        print ("çıkıyor")
        con.close()
        pass

    def masanevar(self,masano):
        print(masano)
        self.e.clearContents()
        sql1 = "SELECT plu_no,urun_adi,adet,tutar,masa_no,n_05,kisi_sayisi,saat,departman,grup3,birim_fiyati FROM DATA WHERE masa_no='" + str(
            masano) + "' and plu_no<1000"
        bb = cur.execute(sql1)
        bb=cur.fetchall()
        self.e.setRowCount( len(bb) )
        for sira,zz in enumerate(bb):
            self.e.setRowHeight(sira, 16)

            item = str(zz[0])
            self.e.setItem(sira, 0, QtGui.QTableWidgetItem(item))
            item = zz[1]
            self.e.setItem(sira, 1, QtGui.QTableWidgetItem(item))
            item = str(zz[2])
            self.e.setItem(sira, 2, QtGui.QTableWidgetItem(item))
            item = str(zz[3])
            self.e.setItem(sira, 3, QtGui.QTableWidgetItem(item))
            item = str(zz[7])
            self.e.setItem(sira, 4, QtGui.QTableWidgetItem(item))


    def masagoster(self,katno):
        global dizi
        sql = "select * from DATA_Y where grup3='" + str(katno) + "' and btn_tipi=4"
        aa = cur.execute(sql)

        if dizi > 0:
            for kk in range(dizi):
                satir[kk].deleteLater()

        for k, row in enumerate(aa):
            satir[k] = QtGui.QPushButton(self)
            satir[k].setText(row[0])
            satir[k].move(row[5], row[4])
            satir[k].setFixedSize(row[7], row[6])
            satir[k].setStyleSheet("QPushButton { background-color: white ; font-size: 9px}")
            satir[k].clicked.connect(lambda checked, tekst=satir[k].text(): self.masanevar(tekst))
            #        print(satir[k].text())
            satir[k].show()
        dizi = k + 1

    def showdialog():

        d = QDialog()
        b1 = QPushButton("ok", d)
        b1.move(50, 50)
        d.setWindowTitle("Dialog")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    w = Pos1()
    w.show()
    w.raise_()

    sys.exit(app.exec_())
