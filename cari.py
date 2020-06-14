# -*- coding: utf-8 -*-
import sys
import re
import datetime
import locale
import subprocess
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_cari import Ui_Dialog5
import xlwt
from decimal import *
import logging

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

        if sys.platform == "win32":
            locale.setlocale(locale.LC_ALL, 'turkish')

        elif sys.platform == "darwin":
            locale.setlocale(locale.LC_ALL, 'tr_TR')

        else:
            locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

        self.kontrol=0
        self.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(QtCore.QDate(2017, 1, 1))
        self.dateEdit_2.setDate(some_date)
        self.pushButton.clicked.connect(self.sloturunmaliyet)
        self.pushButton_3.clicked.connect(self.sloturunmaliyetxls)
        self.pushButton_2.clicked.connect(self.sloturunmaliyetpdf)
        self.tableWidget.cellClicked.connect(self.slotekstre)
        self.lineEdit.textChanged.connect(self.sloturunmaliyet)
        self.tableWidget.setColumnWidth(0, 75)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 75)
        self.tableWidget.setColumnWidth(3, 25)
        self.tableWidget.setColumnWidth(4, 25)
        getcontext().prec = 12

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        handler = logging.FileHandler('hello.log', encoding="UTF-8")
        handler.setLevel(logging.INFO)

        # create a logging format

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @pyqtSlot()
    def sloturunmaliyet(self):
        firma="%"+self.lineEdit.text()+"%"
        print("firma ", firma)
        myddb1 = Myddb()
        self.kontrol=1

        self.logger.info("caribakiye listesi"+self.lineEdit.text())

        self.tableWidget.clearContents()
        self.tableWidget.setColumnWidth(0, 75)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 25)
        self.tableWidget.setColumnWidth(4, 25)

        deger1 = self.dateEdit.date().toPyDate()
        deger2 = self.dateEdit_2.date().toPyDate()
        tar1 = deger1.strftime('%d%m%Y')
        tar2 = deger2.strftime('%d%m%Y')
        tar3 = deger2.strftime('%B %Y')
      #  if sys.platform=="win32":
      #      tar3=unicode(tar3,'cp1254')
      #  else:
      #      tar3=unicode(tar3,'utf-8')

        self.wb = xlwt.Workbook(encoding="utf-8")
        self.dest_filename = "EKSTRE" + tar1 + tar2 + ".xls"
        date_format = xlwt.XFStyle()
        date_format.num_format_str = u'#,##0.00₺'
        date_xf = xlwt.easyxf(num_format_str='DD-MM-YYYY')
        self.ws1 = self.wb.add_sheet("ekstre")
        self.style1 = xlwt.easyxf('pattern: pattern solid, fore_colour red;')

        c = canvas.Canvas("EKSTRE" + tar1 + tar2 + ".pdf")

        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        print (c.getAvailableFonts())
        c.setFont("Verdana", 12)

        item = u"BISHOP CARİ BAKİYE LİSTESİ     "+ tar3
        c.drawString(55, 815, item)
        c.setFont("Verdana", 8)

        item = "           KOD         FİRMA ADI                                                                            BAKİYE                      "
        c.drawString(10, 800, item)

        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')
        sql = """select c2.cariid ,c2.cariad ,sum(c1.tutar) AS TUTAR from (cari_har c1 join cari c2) 
        where ((c1.cariid = c2.cariid) and (c1.tarih >=%s ) and (c1.tarih <=%s ) and (c1.fistipi=10 or c1.fistipi=11))
         and  c2.cariad like %s group by c2.cariid,c2.cariad order by TUTAR DESC """
        myddb1.conn.commit()
        bul2 = myddb1.cur.execute(sql, (tar1, tar2,firma))
        print(bul2, tar1, tar2)
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
            if row1[2]<10 and self.checkBox.isChecked():
                continue


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
        self.tableWidget.setRowCount(aa+2)
        font = QtGui.QFont("Courier New", 11)
        self.tableWidget.setItem(aa+1,2,QtGui.QTableWidgetItem(str(toplam)))
        self.tableWidget.item(aa + 1, 2).setBackground(QtGui.QColor(255, 128, 128))
        self.tableWidget.item(aa + 1, 2).setFont(font)
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
        print("elma")

    @pyqtSlot()
    def slotcarivade(self):
        firma = "%" + self.lineEdit.text() + "%"
        print("firma ", firma)
        myddb1 = Myddb()
        self.kontrol = 1

        print("cari vade listesi")
        self.tableWidget.clearContents()
        self.tableWidget.setColumnWidth(0, 60)
        self.tableWidget.setColumnWidth(1, 400)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
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

        item = "           KOD         FİRMA ADI                                                                            VADESİ GELEN               TOPLAM"
        c.drawString(10, 810, item)
        tar1 = deger1.strftime('%Y-%m-%d')
        tar2 = deger2.strftime('%Y-%m-%d')
        myddb1.cur.execute("drop table if exists table3 ")
        myddb1.cur.execute("drop table if exists table4 ")
        myddb1.cur.execute(
            """ CREATE TEMPORARY TABLE  table3 AS (select `cariid` AS `cariid`,sum(`tutar`) AS `tutar` from cari_har where ( (tarih > '2016-12-31')) and (fistipi=10 or fistipi=11) group by cariid )""")
        myddb1.cur.execute(""" CREATE TEMPORARY TABLE  table4 AS (select cariid,sum(tutar) as tutar from cari_har where vade < %s and (tarih > '2016-12-31') group by cariid )""",(tar2,))

        sql = """select a.cariid,a.cariad , ifnull( b.tutar,0) as giriş ,ifnull(c.tutar,0) as çıkış, (ifnull( b.tutar,0)-ifnull(c.tutar,0)) as fark from cari a  left join table3 b on a.cariid=b.cariid left join table4 c on a.cariid=c.cariid where b.tutar>0 and a.cariad like %s order by çıkış desc """
        bul2 = myddb1.cur.execute(sql, ( firma,))
        print(bul2, tar1, tar2)
        bul = myddb1.cur.fetchall()
        i = bul2
        j = 5
        self.tableWidget.setRowCount(i)
        aa = 0
        bb = 0
        dep = 0
        toplam = 0.0
        toplam1 = 0.0
        toplam2 = 0.0000
        for row1 in bul:

            item = str(row1[0])
            self.ws1.write(aa, 0, item)
            self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            c.drawString(45, 800 - (15 * (bb + 1)), item)
            item = (row1[1])
            self.ws1.write(aa, 1, item)
            c.drawString(80, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))

            if row1[3] > 0:
                item = str(row1[3])
                self.ws1.write(aa, 2, item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
                c.drawRightString(400, 800 - (15 * (bb + 1)), item)

                item = str(row1[2])
                self.ws1.write(aa, 3, float(row1[4]))
                c.drawRightString(470, 800 - (15 * (bb + 1)), item)
                toplam = toplam + float(row1[3])
                toplam2 = Decimal(toplam2) + (row1[2])
                self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))

            if row1[3] <= 0:
                item = "0"
                self.ws1.write(aa, 2, item)
                self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
                c.drawRightString(400, 800 - (15 * (bb + 1)), item)

                item = str(row1[2])
                self.ws1.write(aa, 3, float(row1[4]))
                c.drawRightString(470, 800 - (15 * (bb + 1)), item)

                toplam2 = Decimal(toplam2) + (row1[2])
                self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))


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
        self.tableWidget.setRowCount(aa + 2)
        font = QtGui.QFont("Courier New", 11)
        self.tableWidget.setItem(aa + 1, 2, QtGui.QTableWidgetItem(str(toplam)))
        self.tableWidget.item(aa + 1, 2).setBackground(QtGui.QColor(255, 128, 128))
        self.tableWidget.item(aa + 1, 2).setFont(font)

        c.setFont("Verdana", 10)
        self.ws1.write(aa + 1, 3, toplam)
        self.ws1.write(aa + 1, 4, toplam1)
        self.ws1.write(aa + 1, 5, toplam2)
        c.drawString(350, 800 - (15 * (bb + 1)), str(toplam))
        c.drawString(420, 800 - (15 * (bb + 1)), str(toplam2))
        #c.drawString(430, 800 - (15 * (bb + 1)), str(toplam2))

        # todo genel toplam yazılacak
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
        self.kontrol = 0

    @pyqtSlot(int,int)
    def slotekstre(self, item,item2):
        if self.kontrol==0:
            fisno = self.tableWidget.item(item, 0).text()
            self.emit(QtCore.SIGNAL("fisac"), fisno)
            return
        myddb1 = Myddb()
        carikod=self.tableWidget.item(item, 0).text()

        print("ekstrerapor")
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
        from (`cari_har` `c1` join `cari` `c2`) 
        where ((`c1`.`cariid` = `c2`.`cariid`) and (`c1`.`cariid`=%s) 
        and  (`c1`.`tarih` >=%s ) and (`c1`.`tarih` <=%s ) 
        and (`c1`.`fistipi`=10 or `c1`.`fistipi`=11))  order by `c1`.`tarih` asc """

        bul2 = myddb1.cur.execute(sql, (carikod,tar1, tar2))
        print(bul2, tar1, tar2)

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



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    fatura1=Cari()
    fatura1.show()
    fatura1.raise_()
    app.exec_()
    print("fatura kapandı")




