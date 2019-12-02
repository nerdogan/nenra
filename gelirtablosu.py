# -*- coding: utf-8 -*-
import sys
import re
import locale
import datetime
import subprocess
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_gelirtablo import Ui_Dialog4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *
from modulemdb import *

class GelirTablo(QtGui.QDialog, Ui_Dialog4):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        # self.myddb = Myddb()
        locale.setlocale(locale.LC_ALL, 'tr_TR')
        self.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(some_date)

        self.pushButton.clicked.connect(self.sloturunmaliyet)
        self.pushButton_3.clicked.connect(self.satisrapor)
        self.pushButton_2.clicked.connect(self.sloturunmaliyetpdf)
        self.tableWidget.setColumnWidth(0, 240)
        self.tableWidget.setColumnWidth(1, 125)
        self.tableWidget.setColumnWidth(2, 75)
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
        c = canvas.Canvas("GELİRTABLO" + tar1 + tar2 + ".pdf")
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        c.setFont("Verdana", 16)

        item = "   BISHOP RESTAURANT AYRINTILI GELİR TABLOSU  " + self.deger1.strftime('%B %Y')
        c.drawString(10, 810, item)
        c.setFont("Verdana", 10)
        tar1 = self.deger1.strftime('%Y-%m-%d')
        tar2 = self.deger2.strftime('%Y-%m-%d')
        sql = """SELECT  b.muhad ,a.aciklama,a.miktar1 FROM bishop.genelrapor a  JOIN bishop.muhkodt b ON b.muhkod=a.aciklama where tarih=%s """
        bul2 = myddb1.cur.execute(sql, (tar2,))
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

            item = (row1[0])
            self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
            c.drawString(45, 800 - (15 * (bb + 1)), item)
            item = row1[1]
            c.drawString(180, 800 - (15 * (bb + 1)), item)
            self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
            if len(item) < 4:
                c.setFont("Verdana", 12)

            item = str(row1[2])
            toplam = toplam + float(row1[2])
            self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            c.drawRightString(330, 800 - (15 * (bb + 1)), item)
            c.setFont("Verdana", 10)
            item = " ."
            c.drawString(400, 800 - (15 * (bb + 1)), item)
            toplam1 = toplam1
            self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))

            aa = aa + 1
            bb = bb + 1

            if (15 * (bb + 1)) >= 760:
                c.setFont("Verdana", 11)
                c.drawString(210, 800 - (15 * (bb + 1)), str(toplam))
                c.drawString(270, 800 - (15 * (bb + 1)), str(toplam1))
                c.drawString(350, 800 - (15 * (bb + 1)), str(toplam2))
                c.showPage()
                c.setFont("Verdana", 8)
                bb = 0

        c.setFont("Verdana", 12)
        c.drawString(150, 800 - (15 * (bb + 2)), "Kar Zarar")
        c.drawRightString(330, 800 - (15 * (bb + 2)), str((bul[3][2]) - (bul[20][2])))

        #        c.drawString(450, 800 - (15 * (bb + 1)), "% " + str(int(toplam2 / toplam1 * 100)))
        c.setFont("Verdana", 6)
        c.drawRightString(570,20,datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

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
        c = canvas.Canvas("GELİRTABLO" + ".pdf")
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
            self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
            c.drawRightString(290, 800 - (15 * (bb + 1)), item)
            item = " "
            c.drawString(350, 800 - (15 * (bb + 1)), item)
            toplam1 = toplam1
            self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))

            aa = aa + 1
            bb = bb + 1

            if (15 * (bb + 1)) >= 760:
                c.setFont("Verdana", 11)
                c.drawString(210, 800 - (15 * (bb + 1)), str(toplam))
                c.drawString(270, 800 - (15 * (bb + 1)), str(toplam1))
                c.drawString(350, 800 - (15 * (bb + 1)), str(toplam2))
                c.showPage()
                c.setFont("Verdana", 8)
                bb = 0

        c.setFont("Verdana", 12)
        c.drawString(210, 800 - (15 * (bb + 1)), "")
        c.drawRightString(300, 800 - (15 * (bb + 1)), str((bul[3][3]) - (bul[19][3])))

        #        c.drawString(450, 800 - (15 * (bb + 1)), "% " + str(int(toplam2 / toplam1 * 100)))

        c.save()

    @pyqtSlot()
    def sloturunmaliyetpdf(self):

        tar1 = self.deger1.strftime('%d%m%Y')
        tar2 = self.deger2.strftime('%d%m%Y')

        if sys.platform == "win32":
            os.startfile("GELİRTABLO" + tar1 + tar2 + ".pdf")
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "GELİRTABLO" + tar1 + tar2 + ".pdf"])


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    subprocess.Popen('python3 mizan.py', shell=True)
    gelirt = GelirTablo()
    gelirt.show()
    gelirt.raise_()

    app.exec_()
