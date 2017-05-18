# -*- coding: utf-8 -*-
import sys
import re
import datetime
import subprocess
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_cari import Ui_Dialog5
import xlwt

from modulemdb import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *



class Cari(QtGui.QDialog , Ui_Dialog5):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        #self.myddb = Myddb()
        self.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(QtCore.QDate(2017,01,01))
        self.dateEdit_2.setDate(some_date)
        self.pushButton.clicked.connect(self.sloturunmaliyet)
        self.pushButton_3.clicked.connect(self.sloturunmaliyetxls)
        self.pushButton_2.clicked.connect(self.sloturunmaliyetpdf)
        self.tableWidget.setColumnWidth(0, 75)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 75)
        self.tableWidget.setColumnWidth(3, 75)
        self.tableWidget.setColumnWidth(4, 75)

    @pyqtSlot()
    def sloturunmaliyet(self):

        myddb1 = Myddb()

        print "caribakiye listesi"
        self.tableWidget.clearContents()
        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d%m%Y')
        tar2 = deger2.strftime('%d%m%Y')

        self.wb = xlwt.Workbook(encoding="utf-8")
        self.dest_filename = "EKSTRE" + tar1 + tar2 + ".xls"
        date_format = xlwt.XFStyle()
        date_format.num_format_str = u'#,##0.00₺'
        date_xf = xlwt.easyxf(num_format_str='DD/MM/YYYY')
        self.ws1 = self.wb.add_sheet("ekstre")
        self.style1 = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

        c = canvas.Canvas("EKSTRE" + tar1 + tar2 + ".pdf")
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 8)

        item = "           KOD         FİRMA ADI                                                                         BAKİYE                      "
        c.drawString(10, 810, item)
        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')
        sql = """select `c2`.`cariid` AS `cariid`,`c2`.`cariad` AS `cariad`,sum(`c1`.`tutar`) AS `TUTAR` from (`test`.`cari_har` `c1` join `test`.`cari` `c2`) where ((`c1`.`cariid` = `c2`.`cariid`) and (`c1`.`tarih` >=%s ) and (`c1`.`tarih` <=%s )) group by `c2`.`cariad`   order by TUTAR asc """
        bul2 = myddb1.cur.execute(sql, (tar1, tar2))
        print bul2, tar1, tar2
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

            item = str(row1[0])
            self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            c.drawString(45, 800 - (15 * (bb + 1)), item)
            self.ws1.write(aa,0,item)
            item = row1[1]
            c.drawString(80, 800 - (15 * (bb + 1)), item)
            self.ws1.write(aa, 1, item)
            self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item = str(row1[2])

            toplam = toplam + float(row1[2])
            self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            c.drawRightString( 380, 800 - (15 * (bb + 1)), "{:10.2f}".format(row1[2]))
            self.ws1.write(aa, 2, float(row1[2]))




            aa = aa + 1
            bb = bb + 1

            if (15 * (bb + 1)) >= 760:
                c.setFont("Verdana", 11)
                c.drawString(210, 800 - (15 * (bb + 1)), ".")
                c.drawString(320, 800 - (15 * (bb + 1)), str(toplam))
                c.drawString(550, 800 - (15 * (bb + 1)), ".")
                c.showPage()
                c.setFont("Verdana", 8)
                bb = 0

        c.setFont("Verdana", 11)
        c.drawString(210, 800 - (15 * (bb + 1)), "Genel Toplam")
        c.drawString(320, 800 - (15 * (bb + 1)), str(toplam))
        c.drawString(550, 800 - (15 * (bb + 1)), ".")

        c.save()
        self.wb.save(self.dest_filename)

    @pyqtSlot()
    def cariekstre(self):
        print "elma"

    @pyqtSlot()
    def satisrapor(self):
        myddb1 = Myddb()

        print "satisrapor"
        self.tableWidget.clearContents()
        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d%m%Y')
        tar2 = deger2.strftime('%d%m%Y')
        c = canvas.Canvas("EKSTRE" + tar1 + tar2 + ".pdf")
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 8)

        item = "            ÜRÜN    AÇIKLAMA                                   ADET           TUTAR                 "
        c.drawString(10, 810, item)
        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')

        sql = """SELECT ciro.departman,pluno,hamad,sum(adet),sum(tutar) FROM bishop.ciro  inner join test.hammadde on  pluno=hamkod and
                DATE(tarih) >= %s and DATE(tarih) <= %s  group by ciro.departman,pluno order by ciro.departman asc """
        bul2 = myddb1.cur.execute(sql, (tar1, tar2))
        print bul2, tar1, tar2

        bul = myddb1.cur.fetchall()
        i = bul2
        j = 5
        self.tableWidget.setRowCount(i)
        aa = 0
        bb = 0
        dep=0
        toplam = 0.0
        toplam1 = 0.0
        toplam2 = 0.0
        for row1 in bul:
            sql1 = "select hurunkod,sum(hmiktar*fiyat1),harcanan.tarih from harcanan inner join hammadde on hhammaddeid=hamkod where DATE(tarih)>=%s and DATE(tarih)<=%s and hurunkod=%s"
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
            self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            c.drawString(45, 800 - (15 * (bb + 1)), item)
            item = row1[2]
            c.drawString(80, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item = str(row1[3])

            toplam = toplam + float(row1[3])
            self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            c.drawString(230, 800 - (15 * (bb + 1)), item)
            item = str(row1[4])
            c.drawString(270, 800 - (15 * (bb + 1)), item)
            toplam1 = toplam1 + float(row1[4])
            self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item = "0"
            if (bul1[0][1]) is not None:
                toplam2 = toplam2 + float(bul1[0][1])
                item = str("{:06.2f}".format(float(bul1[0][1])))
            c.drawString(350, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))

            if int(row1[4]) == 0:
                item = "% 100"
            else:
                if (bul1[0][1]) is not None:
                    item = "% " + str(int((float(bul1[0][1])) / row1[4] * 100))
                    c.drawString(450, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 5, QtGui.QTableWidgetItem(item))

            aa = aa + 1
            bb = bb + 1


            if (15 * (bb + 1)) >= 760:
                c.setFont("Verdana", 10)
                c.drawString(210, 800 - (15 * (bb + 1)), str(toplam))
                c.drawString(270, 800 - (15 * (bb + 1)), str(toplam1))
                c.drawString(350, 800 - (15 * (bb + 1)), str(toplam2))
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
            os.startfile("EKSTRE" + tar1 + tar2 + ".pdf")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "EKSTRE" + tar1 + tar2 + ".pdf"])

    def sloturunmaliyetxls(self):
        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d%m%Y')
        tar2 = deger2.strftime('%d%m%Y')

        if sys.platform == "win32":
            os.startfile("EKSTRE" + tar1 + tar2 + ".xls")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "EKSTRE" + tar1 + tar2 + ".xls"])









