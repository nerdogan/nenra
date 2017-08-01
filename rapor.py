# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        
# Purpose:
#
# Author:      NAMIK ERDOĞAN
#
# Created:     22.06.2016
# Copyright:   (c) NAMIK ERDOĞAN  2016
# Licence:     
#-------------------------------------------------------------------------------

import sys

import requests

from escpos.printer import Network,Dummy

from datetime import datetime,timedelta
import subprocess
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_rapor import Ui_Dialog7
import xlwt
from decimal import *

from modulemdb import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *



class Rapor(QtGui.QDialog , Ui_Dialog7):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        #self.myddb = Myddb()
        self.kontrol=0
        self.dt = datetime.now() - timedelta(hours=5)
        self.dt = QtCore.QDate.fromString(str(self.dt.date()), 'yyyy-MM-dd')

        self.tableWidget.setRowCount(0)
        self.dateEdit.setDate(self.dt)
        self.dateEdit_2.setDate(self.dt)
        self.pushButton.clicked.connect(self.sloturunmaliyet)
        self.pushButton_3.clicked.connect(self.sloturunmaliyetxls)
        self.pushButton_2.clicked.connect(self.sloturunmaliyetpdf)
        self.pushButton_4.clicked.connect(self.slotekstre)
        self.pushButton_5.clicked.connect(self.cariekstre)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 450)
        self.tableWidget.setColumnWidth(3, 25)
        self.tableWidget.setColumnWidth(4, 25)
        getcontext().prec = 12

    @pyqtSlot()
    def sloturunmaliyet(self):

        myddb1 = Myddb()
        self.d = Dummy()
        self.kontrol=1

        self.d.text(chr(27))
        self.d.text(chr(116))
        self.d.text(chr(61))

        self.d.set(font='a', align='left', height=1, width=1)

        



        print "caribakiye listesi"
        self.tableWidget.clearContents()
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 400)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 50)

        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d_%m_%Y')
        tar2 = deger2.strftime('%d_%m_%Y')
        self.d.text("  "+tar1+ "  " +tar2 +" Urun Rapor"+" \n")

        self.wb = xlwt.Workbook(encoding="utf-8")
        self.dest_filename = "EKSTRE" + tar1 + tar2 + ".xls"
        date_format = xlwt.XFStyle()
        date_format.num_format_str = u'#,##0.00₺'
        date_xf = xlwt.easyxf(num_format_str='DD-MM-YYYY')
        self.ws1 = self.wb.add_sheet("ekstre")
        self.style1 = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

        c = canvas.Canvas("EKSTRE" + tar1 + tar2 + ".pdf")

        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 16)

        item = "            KOD       STOK ADI                                         BİRİM               GİRİŞ                ÇIKIŞ                 BAKİYE                      "
        c.drawString(10, 800, item)
        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')

        myddb1.cur.execute("drop table if exists test.table3 ")

        myddb1.cur.execute(""" CREATE TEMPORARY TABLE  test.table3 AS (SELECT ciro.departman,pluno,hamad,sum(adet),sum(tutar) FROM bishop.ciro  inner join test.hammadde on  pluno=hamkod and
 date(tarih) between %s and %s and hesap IS NULL group by ciro.departman,pluno order by ciro.departman asc)""",(tar1,tar2))

        sql = """select * from table3 ; """

        bul2 = myddb1.cur.execute(sql)
        print bul2, tar1, tar2
        bul = myddb1.cur.fetchall()
        i = bul2
        j = 5
        self.tableWidget.setRowCount(i + 2)
        aa = 0
        bb = 0
        toplam = 0.0
        toplam1 = 0.0
        toplam2 = 0.0000

        for row1 in bul:

            item = str(row1[0])
            self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            c.drawString(5, 800 - (15 * (bb + 1)), item)
            self.ws1.write(aa,0,item)

            item = str(row1[1])
            c.drawString(50, 800 - (15 * (bb + 1)), item)
            self.ws1.write(aa, 1, item)
            self.d.text(item)
            self.d.text(" ")
            self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            item = row1[2]
            c.drawString(400, 800 - (15 * (bb + 1)), item)
            self.ws1.write(aa, 2, item)
            self.d.text(item.ljust(30))
            self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))

            item = str(row1[3])

            toplam = toplam + float(row1[3])
            self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))

            #c.drawRightString( 440, 800 - (15 * (bb + 1)), "{:10.2f}".format(row1[3]))
            self.ws1.write(aa, 3, float(row1[3]))
            self.d.text(item)
            self.d.text("  ")


            item = str(row1[4])

            toplam1 = toplam1 + float(row1[4])
            self.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))

            c.drawRightString(510, 800 - (15 * (bb + 1)), "{:10.2f}".format(row1[4]))
            self.ws1.write(aa, 4, float(row1[4]))
            self.d.text(item.rjust(8)+"\n")


            aa = aa + 1
            bb = bb + 1

            if (15 * (bb + 1)) >= 760:
                c.setFont("Verdana", 11)
                c.drawRightString(330, 800 - (15 * (bb + 1)), str(toplam))
                c.drawRightString(405, 800 - (15 * (bb + 1)), str(toplam1))
                c.drawRightString(480, 800 - (15 * (bb + 1)), str(toplam2))
                c.showPage()
                c.setFont("Verdana", 16)
                bb = 0

        c.setFont("Verdana", 11)
        c.drawRightString(330, 800 - (15 * (bb + 1)), str(toplam))
        c.drawRightString(405, 800 - (15 * (bb + 1)), str(toplam1))
        c.drawRightString(480, 800 - (15 * (bb + 1)), str(toplam2))
        self.ws1.write(aa + 1, 3, toplam)
        self.ws1.write(aa + 1, 4, toplam1)
        self.ws1.write(aa + 1, 5, toplam2)

        c.setFont("Courier", 60)
        # This next setting with make the text of our
        # watermark gray, nice touch for a watermark.
        c.setFillGray(0.3, 0.3)
        # Set up our watermark document. Our watermark
        # will be rotated 45 degrees from the direction
        # of our underlying document.
        c.saveState()
        c.translate(500, 100)
        c.rotate(45)
        c.drawCentredString(0, 0, "BISHOP NEN ©")
        c.drawCentredString(0, 300, "BISHOP NEN ©")
        c.drawCentredString(0, 600, "BISHOP NEN ©")
        c.restoreState()

        c.save()
        self.wb.save(self.dest_filename)

        self.d.text("\n")
        self.d.text("Toplam :      "+(str(toplam)).rjust(20)+(str(toplam1)).rjust(10)+"\n")

        self.d.cut()

    @pyqtSlot()
    def cariekstre(self):
        p = Network("192.168.2.222")
        p._raw(self.d.output)
        print "elma"
        p=None
        print p

 #       z._raw(self.d.output)

    @pyqtSlot(int,int)
    def slotekstre(self, item):
        if self.kontrol==0:
            print " kasa"
        myddb1 = Myddb()
        self.d = Dummy()
        self.d.text(chr(27))
        self.d.text(chr(116))
        self.d.text(chr(61))

        self.kontrol = 1
        self.d.set(font='a', align='left', height=2, width=1)

        print "ekstrerapor"
        self.tableWidget.clearContents()
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 75)
        self.tableWidget.setColumnWidth(3, 75)
        self.tableWidget.setColumnWidth(4, 75)
        self.tableWidget.setColumnWidth(5, 75)

        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d_%m_%Y')
        tar2 = deger2.strftime('%d_%m_%Y')
        self.d.text("  " + tar1 + "  " + tar2 + " Kasa Raporu " + " \n\n")

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

        item = "         FİŞ NO       TARİH                AÇIKLAMA                             BORÇ                  ALACAK                    BAKİYE                      "
        c.drawString(10, 810, item)
        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')

        sql = """select kasano,sum(tutar) from kasa where date(tarih) between %s and %s  group by kasano; """

        bul2 = myddb1.cur.execute(sql, (tar1, tar2))
        print bul2, tar1, tar2

        bul = myddb1.cur.fetchall()
        i = bul2
        j = 5
        self.tableWidget.setRowCount(i+5)
        aa = 0
        bb = 0
        dep=0
        toplam = 0.0
        toplam1 = 0.0
        toplam2 = 0.0000
        for row1 in bul:


            if row1[0]==100:
                item = str(row1[0])+" Nakit "
                self.ws1.write(aa, 0, item)
                self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
                c.drawString(150, 800 - (15 * (bb + 1)), item)
                self.d.text(item.ljust(30) + " ")
                item = str(row1[1])
                self.d.text(item.rjust(10) + " \n")
                self.ws1.write(aa, 3, float(row1[1]))
                c.drawRightString(310, 800 - (15 * (bb + 1)), item)
                toplam = Decimal(toplam) + (row1[1])

                toplam1 = Decimal(toplam1) + (row1[1])
                item=QtGui.QTableWidgetItem(item)
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
                self.tableWidget.setItem(aa, 1, item)

                item= ""
                c.drawRightString(390, 800 - (15 * (bb + 1)), item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))


            if row1[0]==101:
                item = str(row1[0]) + " Indirim "
                self.ws1.write(aa, 0, item)
                self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
                c.drawString(150, 800 - (15 * (bb + 1)), item)
                self.d.text(item.ljust(30) + " ")

                item = str(row1[1])
                self.d.text(item.rjust(10) + " \n")
                self.ws1.write(aa, 3, float(row1[1]))
                c.drawRightString(310, 800 - (15 * (bb + 1)), item)

                self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
                item = ""
                c.drawRightString(390, 800 - (15 * (bb + 1)), item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))

            if row1[0]==102:
                item = str(row1[0])+" Servis "
                self.ws1.write(aa, 0, item)
                self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
                c.drawString(150, 800 - (15 * (bb + 1)), item)
                self.d.text(item.ljust(30) + " ")

                item = str(row1[1])
                self.d.text(item.rjust(10)+ " \n")
                self.ws1.write(aa, 3, float(row1[1]))
                c.drawRightString(310, 800 - (15 * (bb + 1)), item)
                toplam = Decimal(toplam) - (row1[1])
                self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
                item= ""
                c.drawRightString(390, 800 - (15 * (bb + 1)), item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))

            if row1[0]==105:
                item = str(row1[0])+" Denizbank "
                self.ws1.write(aa, 0, item)
                self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
                c.drawString(150, 800 - (15 * (bb + 1)), item)
                self.d.text(item.ljust(30) + " ")

                item = str(row1[1])
                self.ws1.write(aa, 3, float(row1[1]))
                c.drawRightString(310, 800 - (15 * (bb + 1)), item)
                toplam2=Decimal(toplam2)+(row1[1])
                toplam1 = Decimal(toplam1) + (row1[1])
                self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
                self.d.text(item.rjust(10)+ " \n")
                self.tableWidget.item(aa, 1).setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

                item= ""
                c.drawRightString(390, 800 - (15 * (bb + 1)), item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))

            if row1[0]==106:
                item = str(row1[0])+" Yapi Kredi "
                self.ws1.write(aa, 0, item)
                self.d.text(item.ljust(30) + " ")
                self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
                c.drawString(150, 800 - (15 * (bb + 1)), item)

                item = str(row1[1])
                self.d.text(item.rjust(10)+ " \n")
                self.ws1.write(aa, 3, float(row1[1]))
                c.drawRightString(310, 800 - (15 * (bb + 1)), item)
                toplam2=Decimal(toplam2)+(row1[1])
                toplam1 = Decimal(toplam1) + (row1[1])
                self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
                item= ""
                c.drawRightString(390, 800 - (15 * (bb + 1)), item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))

            if row1[0]==111:
                item = str(row1[0])+" Harcamalar "
                self.ws1.write(aa, 0, item)
                self.d.text(item.ljust(30) + " ")
                self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
                c.drawString(150, 800 - (15 * (bb + 1)), item)

                item = str(row1[1])
                self.d.text(item.rjust(10)+ " \n")
                self.ws1.write(aa, 3, float(row1[1]))
                c.drawRightString(310, 800 - (15 * (bb + 1)), item)
                toplam = Decimal(toplam) + (row1[1])
                self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
                item= ""
                c.drawRightString(390, 800 - (15 * (bb + 1)), item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))





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
        self.ws1.write(aa+1, 3, toplam)
        self.ws1.write(aa+1, 4, toplam1)
        self.ws1.write(aa+1, 5, toplam2)
        c.drawString(270, 800 - (15 * (bb + 1)), str(toplam))
        c.drawString(350, 800 - (15 * (bb + 1)), str(toplam1))
        c.drawString(430, 800 - (15 * (bb + 1)), str(toplam2))

        #todo genel toplam yazılacak
        c.setFont("Courier", 60)
        # This next setting with make the text of our
        # watermark gray, nice touch for a watermark.
        c.setFillGray(0.3, 0.3)
        # Set up our watermark document. Our watermark
        # will be rotated 45 degrees from the direction
        # of our underlying document.
        c.saveState()
        c.translate(500, 100)
        c.rotate(45)
        c.drawCentredString(0, 0, "BISHOP NEN ©")
        c.drawCentredString(0, 300, "BISHOP NEN ©")
        c.drawCentredString(0, 600, "BISHOP NEN ©")
        c.restoreState()

        self.kontrol=0
        self.d.text("\n\n")

        item = "Genel Toplam "
        self.d.text(item.ljust(30) + " ")
        self.tableWidget.setItem(aa + 1, 0, QtGui.QTableWidgetItem(item))
        item = str(toplam1)
        self.d.text(item.rjust(10)+ " \n")
        self.tableWidget.setItem(aa + 1, 1, QtGui.QTableWidgetItem(item))

        item = "Kasa Kalan Nakit "
        self.d.text(item.ljust(30) + " ")
        self.tableWidget.setItem(aa + 2, 0, QtGui.QTableWidgetItem(item))
        item = str(toplam)
        self.d.text(item.rjust(10) + " \n")
        self.tableWidget.setItem(aa + 2, 1, QtGui.QTableWidgetItem(item))

        item = "Kredi Kart Toplam "
        self.d.text(item.ljust(30) + " ")
        self.tableWidget.setItem(aa + 3, 0, QtGui.QTableWidgetItem(item))
        item = str(toplam2)
        self.d.text(item.rjust(10)+ " \n")
        self.tableWidget.setItem(aa + 3, 1, QtGui.QTableWidgetItem(item))

        aa=aa+5
        self.d.text(u"\n\n\n Ödemeler \n")

        sql = """select
        aciklama, tutar
        from kasa where
        tutar < 0 and posid = 2000 and tarih
        between %s and %s """

        bul2 = myddb1.cur.execute(sql, (tar1, tar2))
        print bul2, tar1, tar2

        bul = myddb1.cur.fetchall()
        print bul
        i = bul2
        j = 5
        self.tableWidget.setRowCount(i + aa+1)

        bb = 0
        dep = 0
        toplam = 0.0
        toplam1 = 0.0
        toplam2 = 0.0000
        for row1 in bul:


            item = (row1[0])
      #      self.ws1.write(aa, 0, item)
            self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            c.drawString(150, 800 - (15 * (bb + 1)), item)
            self.d.text(item.ljust(30) + " ")
            item = str(row1[1])
            self.d.text(item.rjust(10) + " \n")
       #     self.ws1.write(aa, 3, float(row1[1]))
            c.drawRightString(310, 800 - (15 * (bb + 1)), item)
            toplam = Decimal(toplam) + (row1[1])

            toplam1 = Decimal(toplam1) + (row1[1])
            item = QtGui.QTableWidgetItem(item)
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
            self.tableWidget.setItem(aa, 1, item)

            aa=aa+1


        self.d.barcode(tar1, "CODE39", 80, 3)
        self.d.text(u"\n\n\n İmza : \n")
        self.d.cut()
        c.save()
        self.wb.save(self.dest_filename)

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



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    rapor=Rapor()
    rapor.show()
    app.exec_()





