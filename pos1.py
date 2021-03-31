from PyQt5 import Qt, QtCore,  QtWidgets
from PyQt5.QtCore import *
import fdb
from modulemdb import *
from datetime import datetime,timedelta
import time as ttim
from socket import *
import sys
import atexit
import nenraconfig



dizi=0
satir={}


con = fdb.connect(
    dsn='nen.duckdns.org/30500:D:\RESTO_2015\DATA\DATABASE.GDB',
    user='sysdba', password='masterkey',
    charset='UTF8' # specify a character set for the connection #
     )
cur = con.cursor()


class Pos1(QtWidgets.QWidget):

    def __init__(self):
        super(Pos1, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(10,20,1024,668)

        self.b = QtWidgets.QPushButton(self)
        self.b.setText(u"GİRİŞ SALON")
        self.b.move(2, 72)
        self.b.setFixedSize(110, 64)

        b1 = QtWidgets.QPushButton(self)
        b1.setText(u"ÖN BAHÇE")
        b1.move(2, 136)
        b1.setFixedSize(110, 64)

        b2 = QtWidgets.QPushButton(self)
        b2.setText(u"ARKA BAHÇE")
        b2.move(2, 200)
        b2.setFixedSize(110, 64)

        b3 = QtWidgets.QPushButton(self)
        b3.setText(u"1. KAT")
        b3.move(2, 264)
        b3.setFixedSize(110, 64)

        b4 = QtWidgets.QPushButton(self)
        b4.setText(u"2. KAT")
        b4.move(2, 328)
        b4.setFixedSize(110, 64)

        b5 = QtWidgets.QPushButton(self)
        b5.setText(u"KULE")
        b5.move(2, 392)
        b5.setFixedSize(110, 64)

        b6 = QtWidgets.QPushButton(self)
        b6.setText(u"Kapat")
        b6.move(720, 512)
        b6.setFixedSize(110, 64)

        self.e = QtWidgets.QTableWidget(self)
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
        b6.clicked.connect(self.showdialog)

        self.setWindowTitle("Nenra POS 1.0.0")
        self.masano=""
        self.myddb=Myddb()

    @atexit.register
    def cikis():
        print("çıkıyor")
        con.close()
        pass

    def masanevar(self,masano):
        print(masano)
        self.masano=masano
        self.e.clearContents()
        sql1 = "SELECT plu_no,urun_adi,adet,tutar,masa_no,n_05,kisi_sayisi,tarih,departman,grup3,birim_fiyati FROM DATA WHERE masa_no='" + str(
            masano) + "' and plu_no<1000 and urun_turu > 0"
        cur.execute(sql1)
        bb=cur.fetchall()
        self.e.setRowCount( len(bb) )
        for sira,zz in enumerate(bb):
            self.e.setRowHeight(sira, 16)

            item = str(zz[0])
            self.e.setItem(sira, 0, QtWidgets.QTableWidgetItem(item))
            item = zz[1]
            self.e.setItem(sira, 1, QtWidgets.QTableWidgetItem(item))
            item = str(zz[2])
            self.e.setItem(sira, 2, QtWidgets.QTableWidgetItem(item))
            item = str(zz[3])
            self.e.setItem(sira, 3, QtWidgets.QTableWidgetItem(item))
            item = str(zz[7])
            self.e.setItem(sira, 4, QtWidgets.QTableWidgetItem(item))


    def masagoster(self,katno):
        global dizi
        self.masano=""
        self.e.clearContents()
        sql = "select * from DATA_Y where grup3='" + str(katno) + "' and btn_tipi=4"
        cur.execute(sql)
        aa=cur.fetchall()

        if dizi > 0:
            for kk in range(dizi):
                satir[kk].deleteLater()

        for k, row in enumerate(aa):
            satir[k] = QtWidgets.QPushButton(self)
            satir[k].setText(row[0])
            satir[k].move(row[5], row[4])
            satir[k].setFixedSize(row[7], row[6])
            satir[k].setStyleSheet("QPushButton { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,  stop: 0 blue, stop: 1 white) ; font-size: 9px}")
            satir[k].clicked.connect(lambda checked, tekst=satir[k].text(): self.masanevar(tekst))
            cur.execute("SELECT sum(tutar) FROM DATA WHERE masa_no='" + str(row[0]) + "' and plu_no<1000 and urun_turu > 0")
            bb=cur.fetchall()
            if bb[0][0] is not None:
                satir[k].setText(str(row[0])+"\n\n"+str(bb[0][0]))
                satir[k].setStyleSheet("QPushButton { background-color: rgb(124,197,106) ; font-size: 9px}")

            satir[k].show()
        dizi = k + 1

    def tarihkaydet(self,tarihh):
        self.tarih=self.tar.date().toPyDate()
        print (self.tarih)



    def showdialog(self):

        d = QtWidgets.QDialog()
        d.setFixedSize(200,200)
        self.butt = QtWidgets.QPushButton(self.masano, d)
        self.butt.move(50, 50)

        self.tar=QtWidgets.QDateEdit(d)
        self.tar.setCalendarPopup(True)
        self.tar.setDate(QtCore.QDate.currentDate())
        self.tar.move(10,10)
        self.tar.dateChanged.connect(self.tarihkaydet)
        d.setWindowTitle("Dialog")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

        print(" ")
        selectt1 = "SELECT plu_no,urun_adi,adet,tutar,masa_no,n_05,kisi_sayisi,saat,departman,grup3,birim_fiyati,tarih,islem_kod FROM DATA WHERE  masa_no='" + self.masano + "' and plu_no<1000 and urun_turu > 0 "
        # TARIH='" + tt1 + "' and
        ab = 0
        aa = cur.execute(selectt1)
        for row in aa:
            if row[2] < 0:
                continue
            print (row[11])
            self.myddb.cur.execute(
                "insert into bishop.ciro1  (pluno,urun,adet,tutar,masano,tahkod,acik,tarih,kisi,saat,departman,kategori,tutar1,islem) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (row[0], row[1], row[2], row[3], row[4], row[5], "0", self.tarih, row[6], row[7], row[8], row[9], row[10], row[12]))

            ab = ab + row[3]

        print("toplam       :", str(self.tarih), ab)
  #      sil="delete from data where masano='" + self.masano + "' "
   #     cur.execute()
        self.myddb.cur.execute(
            "insert ignore into bishop.kasa1  (posid,aciklama,tutar,belgeno,muhkod,tarih,kasano,islemid) values (%s,%s,%s,%s,%s,%s,%s,%s)",
            (2000, 'Tahsilat', ab, row[4] , row[5], self.tarih, 99, row[5]))
        cur.execute("delete from DATA where masa_no='" + self.masano+"'")
        self.myddb.conn.commit()
        con.commit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Pos1()
    w.show()
    w.raise_()

    sys.exit(app.exec_())
