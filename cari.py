# -*- coding: utf-8 -*-
import sys
import re
import datetime
import subprocess
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_cari import Ui_Dialog5
import xlwt
from decimal import *

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
        self.kontrol=0
        self.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(QtCore.QDate(2017,01,01))
        self.dateEdit_2.setDate(some_date)
        self.pushButton.clicked.connect(self.sloturunmaliyet)
        self.pushButton_3.clicked.connect(self.sloturunmaliyetxls)
        self.pushButton_2.clicked.connect(self.sloturunmaliyetpdf)
        self.tableWidget.cellClicked.connect(self.slotekstre)
        self.tableWidget.setColumnWidth(0, 75)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 75)
        self.tableWidget.setColumnWidth(3, 25)
        self.tableWidget.setColumnWidth(4, 25)
        getcontext().prec = 12

    @pyqtSlot()
    def sloturunmaliyet(self):

        myddb1 = Myddb()
        self.kontrol=1

        print "caribakiye listesi"
        self.tableWidget.clearContents()
        self.tableWidget.setColumnWidth(0, 75)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 75)
        self.tableWidget.setColumnWidth(3, 25)
        self.tableWidget.setColumnWidth(4, 25)

        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d%m%Y')
        tar2 = deger2.strftime('%d%m%Y')

        self.wb = xlwt.Workbook(encoding="utf-8")
        self.dest_filename = "EKSTRE" + tar1 + tar2 + ".xls"
        date_format = xlwt.XFStyle()
        date_format.num_format_str = u'#,##0.00₺'
        date_xf = xlwt.easyxf(num_format_str='DD-MM-YYYY')
        self.ws1 = self.wb.add_sheet("ekstre")
        self.style1 = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

        c = canvas.Canvas("EKSTRE" + tar1 + tar2 + ".pdf")

        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 8)

        item = "           KOD         FİRMA ADI                                                                            BAKİYE                      "
        c.drawString(10, 810, item)
        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')
        sql = """select `c2`.`cariid` AS `cariid`,`c2`.`cariad` AS `cariad`,sum(`c1`.`tutar`) AS `TUTAR` from (`test`.`cari_har` `c1` join `test`.`cari` `c2`) where ((`c1`.`cariid` = `c2`.`cariid`) and (`c1`.`tarih` >=%s ) and (`c1`.`tarih` <=%s ) and (`c1`.`fistipi`=10 or `c1`.`fistipi`=11)) group by `c2`.`cariad`   order by TUTAR DESC """
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
        toplam2 = 0.0000

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
        self.ws1.write(aa + 1, 2, toplam)

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

    @pyqtSlot()
    def cariekstre(self):
        print "elma"

    @pyqtSlot(int,int)
    def slotekstre(self, item,item2):
        if self.kontrol==0:
            fisno = self.tableWidget.item(item, 0).text()
            self.emit(QtCore.SIGNAL("fisac"), fisno)
            return
        myddb1 = Myddb()
        carikod=self.tableWidget.item(item, 0).text()

        print "ekstrerapor"
        self.tableWidget.clearContents()
        self.tableWidget.setColumnWidth(0, 60)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 75)
        self.tableWidget.setColumnWidth(4, 75)
        self.tableWidget.setColumnWidth(5, 75)

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

        item = "         FİŞ NO       TARİH                AÇIKLAMA                             BORÇ                  ALACAK                    BAKİYE                      "
        c.drawString(10, 810, item)
        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')

        sql = """select `c1`.`fistipi`,`c1`.`tarih` AS `tarih`,`c1`.`fisno` AS `fisno`,concat(`c1`.`serino`,'_',`c1`.`sirano`,' nolu '), `c1`.`tutar` AS `TUTAR` 
        from (`test`.`cari_har` `c1` join `test`.`cari` `c2`) 
        where ((`c1`.`cariid` = `c2`.`cariid`) and (`c1`.`cariid`=%s) 
        and  (`c1`.`tarih` >=%s ) and (`c1`.`tarih` <=%s ) 
        and (`c1`.`fistipi`=10 or `c1`.`fistipi`=11))  order by `c1`.`tarih` asc """

        bul2 = myddb1.cur.execute(sql, (carikod,tar1, tar2))
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
        toplam2 = 0.0000
        for row1 in bul:

            item = str(row1[2])
            self.ws1.write(aa, 0, item)
            self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            c.drawString(45, 800 - (15 * (bb + 1)), item)
            item = (row1[1]).strftime("%d-%m-%Y")
            self.ws1.write(aa, 1, item)
            c.drawString(80, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))

            if row1[0]==10:
                item = str(row1[3])+"Fatura "
                self.ws1.write(aa, 2, item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
                c.drawString(150, 800 - (15 * (bb + 1)), item)

                item = str(row1[4])
                self.ws1.write(aa, 3, float(row1[4]))
                c.drawRightString(310, 800 - (15 * (bb + 1)), item)
                toplam = toplam + float(row1[4])
                toplam2=Decimal(toplam2)+(row1[4])
                self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
                item= ""
                c.drawRightString(390, 800 - (15 * (bb + 1)), item)
                self.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))

            if row1[0]==11:
                item = row1[3]+u" Ödeme"
                self.ws1.write(aa, 2, item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
                c.drawString(150, 800 - (15 * (bb + 1)), item)

                item = str(row1[4])
                self.ws1.write(aa, 4, float(row1[4]))
                c.drawString(350, 800 - (15 * (bb + 1)), item)
                toplam1 = toplam1 + float(row1[4])
                toplam2=Decimal(toplam2)+ (row1[4])
                self.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
                item= ""
                c.drawString(270, 800 - (15 * (bb + 1)), item)
                self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))




            item = str(toplam2)
            self.ws1.write(aa, 5, toplam2)
            self.tableWidget.setItem(aa, 5, QtGui.QTableWidgetItem(item))
            c.drawRightString(470, 800 - (15 * (bb + 1)), str(toplam2))


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

        c.save()
        self.wb.save(self.dest_filename)
        self.kontrol=0

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








