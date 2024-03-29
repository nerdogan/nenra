# -*- coding: utf-8 -*-
import sys, subprocess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *

from ui_maliyet import Ui_Dialog4

from mdb.modulemdb import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *



class Maliyet(QDialog , Ui_Dialog4):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        #self.myddb = Myddb()
        self.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(some_date)
        self.dateEdit_2.setDate(some_date)
        self.pushButton.clicked.connect(self.sloturunmaliyet)
        self.pushButton_3.clicked.connect(self.satisrapor)
        self.pushButton_2.clicked.connect(self.sloturunmaliyetpdf)
        self.tableWidget.setColumnWidth(0, 75)
        self.tableWidget.setColumnWidth(1, 270)
        self.tableWidget.setColumnWidth(2, 75)
        self.tableWidget.setColumnWidth(3, 75)
        self.tableWidget.setColumnWidth(4, 75)

    @pyqtSlot()
    def sloturunmaliyet(self):

        myddb1 = Myddb()

        print("urunmaliyet")
        self.tableWidget.clearContents()
        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d%m%Y')
        tar2 = deger2.strftime('%d%m%Y')
        c = canvas.Canvas("maliyet" + tar1 + tar2 + ".pdf")
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 8)

        item = "            ÜRÜN    AÇIKLAMA                                   ADET           TUTAR                MALIYET                     ORAN "
        c.drawString(10, 810, item)
        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')
        sql = "SELECT pluno,hamad,sum(adet),sum(tutar) FROM (select * from bishop.ciro where tarih between %s and %s union all select * from bishop.ciro1 where tarih between %s and %s ) as ciroo inner join test.hammadde on  pluno=hamkod  group by pluno,hamad order by pluno asc "
        bul2 = myddb1.cur.execute(sql, (tar1, tar2, tar1, tar2))
        print(bul2, tar1, tar2)
        bul = myddb1.cur.fetchall()
        i = bul2
        j = 5
        self.tableWidget.setRowCount(i)
        aa = 0
        bb = 0
        toplam = 0.0
        toplam1 = 0.0
        toplam2 = 0.0

        for row1 in bul:
            sql1 = "select hurunkod,sum(hmiktar*hammadde.fiyat1) from harcanan inner join hammadde on " \
                   "hhammaddeid=hamkod where tarih >=%s and tarih<=%s and hurunkod=%s "
            bul1 = myddb1.cur.execute(sql1, (tar1, tar2, row1[0]))
            bul1 = myddb1.cur.fetchall()

            item = str(row1[0])
            self.tableWidget.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            c.drawString(45, 800 - (15 * (bb + 1)), item)
            item = row1[1]
            c.drawString(80, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            item = str(row1[2])

            toplam = toplam + float(row1[2])
            self.tableWidget.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
            c.drawString(230, 800 - (15 * (bb + 1)), item)
            item = str(row1[3])
            c.drawString(270, 800 - (15 * (bb + 1)), item)
            toplam1 = toplam1 + float(row1[3])
            self.tableWidget.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
            item = "0"
            if (bul1[0][1]) is not None:
                toplam2 = toplam2 + float(bul1[0][1])
                item = str("{:06.2f}".format(float(bul1[0][1])))
            c.drawString(350, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 4, QtWidgets.QTableWidgetItem(item))

            if int(row1[3]) == 0:
                item = "% 100"
            else:
                if (bul1[0][1]) is not None:
                    item = "% " + str(int((float(bul1[0][1])) / row1[3] * 100))
                    c.drawString(450, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 5, QtWidgets.QTableWidgetItem(item))

            aa = aa + 1
            bb = bb + 1
            print(aa)

            if (15 * (bb + 1)) >= 760:
                c.setFont("Verdana", 11)
                c.drawString(210, 800 - (15 * (bb + 1)), str(toplam))
                c.drawString(270, 800 - (15 * (bb + 1)), str(int(toplam1)))
                c.drawString(350, 800 - (15 * (bb + 1)), str(int(toplam2)))
                c.showPage()
                c.setFont("Verdana", 8)
                bb = 0

        c.setFont("Verdana", 12)
        c.drawString(210, 800 - (15 * (bb + 1)), str(toplam))
        c.drawString(270, 800 - (15 * (bb + 1)), str(int(toplam1)))
        c.drawString(350, 800 - (15 * (bb + 1)), str(int(toplam2)))
        c.drawString(450, 800 - (15 * (bb + 1)), "% " + str(int(toplam2 / toplam1 * 100)))

        c.save()

    @pyqtSlot()
    def satisrapor(self):
        myddb1 = Myddb()

        print("satisrapor")
        self.tableWidget.clearContents()
        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d%m%Y')
        tar2 = deger2.strftime('%d%m%Y')
        c = canvas.Canvas("maliyet" + tar1 + tar2 + ".pdf")
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 8)

        item = "            ÜRÜN    AÇIKLAMA                                   ADET           TUTAR                 "
        c.drawString(10, 810, item)
        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')

        sql = """SELECT ciroo.departman,pluno,hamad,sum(adet),sum(tutar) FROM (select * from bishop.ciro union all select * from bishop.ciro1) as ciroo  inner join test.hammadde on  pluno=hamkod and
                tarih >= %s and tarih <= %s  group by ciroo.departman,pluno order by ciroo.departman asc """
        bul2 = myddb1.cur.execute(sql, (tar1, tar2))
        print(bul2, tar1, tar2)

        bul = myddb1.cur.fetchall()

        i = bul2
        j = 5
        self.tableWidget.setRowCount(i)
        aa = 0
        bb = 0
        dep=1
        toplam = 0.0
        toplam1 = 0.0
        toplam2 = 0.0
        for row1 in bul:
            sql1 = "select hurunkod,sum(hmiktar*fiyat1),harcanan.tarih from harcanan inner join hammadde on hhammaddeid=hamkod where tarih>=%s and tarih<=%s and hurunkod=%s"
            bul1 = myddb1.cur.execute(sql1, (tar1, tar2, row1[1]))
            bul1 = myddb1.cur.fetchall()


            if dep != int(row1[0]):
                dep = int(row1[0])
                c.setFont("Verdana", 10)
                c.drawString(210, 800 - (15 * (bb + 1)), str(toplam))
                c.drawString(270, 800 - (15 * (bb + 1)), str("{:06.2f}".format(toplam1)))
                c.drawString(350, 800 - (15 * (bb + 1)), str("{:06.2f}".format(toplam2)))
                c.showPage()
                c.setFont("Verdana", 8)
                bb = 0
                toplam = 0.0
                toplam1 = 0.0
                toplam2 = 0.0

            item = str(row1[0])
            self.tableWidget.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            c.drawString(45, 800 - (15 * (bb + 1)), item)
            item = row1[2]
            c.drawString(80, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            item = str(row1[3])

            toplam = toplam + float(row1[3])
            self.tableWidget.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
            c.drawString(230, 800 - (15 * (bb + 1)), item)
            item = str(row1[4])
            c.drawString(270, 800 - (15 * (bb + 1)), item)
            toplam1 = toplam1 + float(row1[4])
            self.tableWidget.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
            item = "0"
            if (bul1[0][1]) is not None:
                toplam2 = toplam2 + float(bul1[0][1])
                item = str("{:06.2f}".format(float(bul1[0][1])))
            c.drawString(350, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 4, QtWidgets.QTableWidgetItem(item))

            if int(row1[4]) == 0:
                item = "% 100"
            else:
                if (bul1[0][1]) is not None:
                    item = "% " + str(int((float(bul1[0][1])) / row1[4] * 100))
                    c.drawString(450, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 5, QtWidgets.QTableWidgetItem(item))

            aa = aa + 1
            bb = bb + 1


            if (15 * (bb + 1)) >= 760:
                c.setFont("Verdana", 10)
                c.drawString(230, 800 - (15 * (bb + 1)), str(toplam))
                c.drawString(270, 800 - (15 * (bb + 1)), str(int(toplam1)))
                c.drawString(350, 800 - (15 * (bb + 1)), str(int(toplam2)))
                c.showPage()
                c.setFont("Verdana", 8)
                bb = 0
        c.setFont("Verdana", 10)
        c.drawString(230, 800 - (15 * (bb + 1)), str(toplam))
        c.drawString(270, 800 - (15 * (bb + 1)), str(int(toplam1)))
        c.drawString(350, 800 - (15 * (bb + 1)), str(int(toplam2)))
        c.drawString(450, 800 - (15 * (bb + 1)), "% " + str(int(toplam2 / toplam1 * 100)))
        #todo genel toplam yazılacak

        c.save()

    @pyqtSlot()
    def sloturunmaliyetpdf(self):
        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d%m%Y')
        tar2 = deger2.strftime('%d%m%Y')

        if sys.platform == "win32":
            os.startfile("maliyet" + tar1 + tar2 + ".pdf")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "maliyet" + tar1 + tar2 + ".pdf"])



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    fatura1=Maliyet()
    fatura1.show()
    fatura1.raise_()
    app.exec_()
    print("maliyet kapandı")








