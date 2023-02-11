# -*- coding: utf-8 -*-
# import re
import locale
import datetime
import subprocess
import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from ui_gelirtablo import Ui_Dialog4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *
from mdb.modulemdb import *


class GelirTablo(QtWidgets.QDialog, Ui_Dialog4):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        # self.myddb = Myddb()

        if sys.platform == "win32":
            locale.setlocale(locale.LC_ALL, 'turkish')

        elif sys.platform == "darwin":
            locale.setlocale(locale.LC_ALL, 'tr_TR')

        else:
            locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

        self.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(some_date)

        self.pushButton.clicked.connect(self.sloturunmaliyet)
        self.pushButton_3.clicked.connect(self.satisrapor)
        self.pushButton_2.clicked.connect(self.sloturunmaliyetpdf)
        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setColumnWidth(1, 125)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 75)
        self.tableWidget.setColumnWidth(4, 75)

    def last_day_of_month(self, any_day):
        next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
        return next_month - datetime.timedelta(days=next_month.day)

    @pyqtSlot()
    def sloturunmaliyet(self):

        myddb1 = Myddb()

        print("urunmaliyet")
        self.tableWidget.clearContents()
        deger1 = self.dateEdit.date().toPyDate()
        self.deger1 = deger1.replace(day=1)
        self.deger2 = self.last_day_of_month(deger1)

        tar1 = self.deger1.strftime('%d%m%Y')

        tar2 = self.deger2.strftime('%d%m%Y')
        c = canvas.Canvas("./tempnenra/GELİRTABLO" + tar1 + tar2 + ".pdf")
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 16)

        item = "   BISHOP RESTAURANT AYRINTILI GELİR TABLOSU  " + self.deger1.strftime('%B %Y')
        c.drawString(10, 801, item)
        c.setFont("Verdana", 10)
        tar1 = self.deger1.strftime('%Y-%m-%d')
        tar2 = self.deger2.strftime('%Y-%m-%d')
        sql = """ SELECT  b.muhad ,b.`muhkod`,COALESCE(a.miktar1, 0) FROM bishop.muhkodt b   LEFT JOIN (select * from bishop.genelrapor where tarih=%s)  a ON b.muhkod=a.aciklama  order by b.id """
        bul2 = myddb1.cur.execute(sql, (tar2,))
        print(bul2, tar1, tar2)
        bul = myddb1.cur.fetchall()
        i = bul2
        self.tableWidget.setRowCount(i)
        aa = 0
        bb = 0
        toplam = 0.0
        toplam1 = 0.0
        toplam2 = 0.0

        for row1 in bul:

            item = (row1[0])
            self.tableWidget.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            c.drawString(45, 760 - (15 * (bb + 1)), item)
            item = row1[1]
            c.drawString(180, 760 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            if len(item) < 4:
                c.setFont("Verdana", 12)

            item = str(row1[2])
            if item == 'None':
                item = "0"
            toplam = toplam + float(item)

            item1 = QtWidgets.QTableWidgetItem(locale.currency(float(item), grouping=True, symbol=False))
            item1.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
            self.tableWidget.setItem(aa, 2, item1)

            c.drawRightString(400, 760 - (15 * (bb + 1)), locale.currency(float(item), grouping=True, symbol=False))
            c.setFont("Verdana", 10)
            item = " ."
            c.drawString(470, 760 - (15 * (bb + 1)), item)
            toplam1 = toplam1
            self.tableWidget.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))

            aa = aa + 1
            bb = bb + 1

            if (15 * (bb + 1)) >= 760:
                c.setFont("Verdana", 11)
                c.drawString(210, 760 - (15 * (bb + 1)), str(toplam))
                c.drawString(270, 760 - (15 * (bb + 1)), str(toplam1))
                c.drawString(350, 760 - (15 * (bb + 1)), str(toplam2))
                c.showPage()
                c.setFont("Verdana", 8)
                bb = 0

        c.setFont("Verdana", 12)
        c.drawString(220, 760 - (15 * (bb + 2)), "Kar Zarar")

        try:
            c.drawRightString(400, 760 - (15 * (bb + 2)), str((bul[3][2]) - (bul[23][2])))
        except:
            pass

        #        c.drawString(450, 760 - (15 * (bb + 1)), "% " + str(int(toplam2 / toplam1 * 100)))
        c.setFont("Verdana", 6)
        c.drawRightString(570, 20, datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

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

    @pyqtSlot()
    def satisrapor(self):

        print("satisrapor")
        myddb1 = Myddb()

        # self.tableWidget.clearContents()
        deger1 = self.dateEdit.date().toPyDate()
        self.deger1 = deger1.replace(day=1)
        self.deger2 = self.last_day_of_month(deger1)

        tar1 = self.deger1.strftime('%d%m%Y')

        tar2 = self.deger2.strftime('%d%m%Y')
        c = canvas.Canvas("./tempnenra/GELİRTABLO" + ".pdf")
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 14)

        item = "             BISHOP RESTAURANT AYRINTILI GELİR TABLOSU  "
        c.drawString(10, 810, item)
        c.setFont("Verdana", 8)
        tar1 = self.deger1.strftime('%Y-%m-%d')
        tar2 = self.deger2.strftime('%Y-%m-%d')
        sql = """SELECT   * FROM test.genelrapor order by rkod  """
        bul2 = myddb1.cur.execute(sql)
        print(bul2, tar1, tar2)
        bul = myddb1.cur.fetchall()
        i = bul2
        j = 5
        self.tableWidget.setRowCount(i)
        self.tableWidget.setColumnCount(12)
        aa = 0
        bb = 0
        toplam = 0.0
        toplam1 = 0.0
        toplam2 = 0.0

        for row1 in bul:

            item = str(row1[3])
            toplam = toplam + float(row1[3])
            self.tableWidget.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
            c.drawRightString(290, 760 - (15 * (bb + 1)), item)
            item = " "
            c.drawString(350, 760 - (15 * (bb + 1)), item)
            toplam1 = toplam1
            self.tableWidget.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))

            aa = aa + 1
            bb = bb + 1

            if (15 * (bb + 1)) >= 760:
                c.setFont("Verdana", 11)
                c.drawString(210, 760 - (15 * (bb + 1)), str(toplam))
                c.drawString(270, 760 - (15 * (bb + 1)), str(toplam1))
                c.drawString(350, 760 - (15 * (bb + 1)), str(toplam2))
                c.showPage()
                c.setFont("Verdana", 8)
                bb = 0

        c.setFont("Verdana", 12)
        c.drawString(210, 760 - (15 * (bb + 1)), "")
        c.drawRightString(300, 760 - (15 * (bb + 1)), str((bul[3][3]) - (bul[19][3])))

        #        c.drawString(450, 760 - (15 * (bb + 1)), "% " + str(int(toplam2 / toplam1 * 100)))

        c.save()

    @pyqtSlot()
    def sloturunmaliyetpdf(self):

        tar1 = self.deger1.strftime('%d%m%Y')
        tar2 = self.deger2.strftime('%d%m%Y')

        if sys.platform == "win32":
            os.startfile(r"./tempnenra/GELİRTABLO" + tar1 + tar2 + ".pdf")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "./tempnenra/GELİRTABLO" + tar1 + tar2 + ".pdf"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # subprocess.Popen('python mizan.py', shell=True)
    gelirt = GelirTablo()
    gelirt.show()
    gelirt.raise_()

    app.exec_()
