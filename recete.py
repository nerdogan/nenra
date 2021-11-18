# -*- coding: utf-8 -*-
import sys
import locale
import subprocess
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import *
import re
import xlwt
from decimal import *
import logging
from mdb.modulemdb import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_settings import *
from ui_recete import Ui_Dialog
from ui_recete2 import Ui_Dialog2


class Recete2(QtWidgets.QDialog, Ui_Dialog2):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.slotrecete2sql)
        self.tableWidget.cellClicked.connect(self.slothamclick)
        self.pushButton.clicked.connect(self.slotrecete2kaydet)
        self.pushButton_3.clicked.connect(self.slotrecete2satirsil)

    def kontrol(self, girdi):
        girdi = str(girdi)
        ara = re.search(",", girdi)
        if ara:
            derle = re.compile(",")
            cikti = derle.sub(".", girdi)
            return cikti
        return girdi

    @pyqtSlot()
    def slotrecete2sql(self, item2):
        myddb = Myddb()

        a = item2
        a = str(a)

        bul = myddb.cek1(a, "hammadde", "hamad")

        i = len(bul)
        self.tableWidget.setRowCount(i)
        self.tableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)

        aa = 0
        toplam = 0
        for row1 in bul:
            item = str(row1[1])
            self.tableWidget.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            item = row1[2]
            self.tableWidget.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            item = row1[3]
            self.tableWidget.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
            item = str(row1[4])
            self.tableWidget.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
            aa = aa + 1

    @pyqtSlot(int, int)
    def slothamclick(self, item, item2):
        #   hammadde listesinden çiftklikle
        #   tablewidget_2 ye hammadde bilgisini ekliyor.
        i = self.tableWidget_2.rowCount()
        deger1 = self.tableWidget.item(item, 0).text()
        deger2 = self.tableWidget.item(item, 1).text()
        deger3 = self.tableWidget.item(item, 2).text()

        i = i + 1
        self.tableWidget_2.setRowCount(i)

        aa = i - 1

        item = deger1
        self.tableWidget_2.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
        item = deger2
        self.tableWidget_2.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
        item = deger3
        self.tableWidget_2.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
        item = '0'
        self.tableWidget_2.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
        # self.lineEdit.setFocus(True)
        self.tableWidget_2.setFocus()
        self.tableWidget_2.setCurrentCell(aa, 3)

    @pyqtSlot()
    def slotrecete2kaydet(self):
        myddb = Myddb()
        deger0 = self.label_3.text()
        myddb.sil(deger0, "recete", "menukod")
        i = self.tableWidget_2.rowCount()
        for item in range(i):
            deger1 = self.tableWidget_2.item(item, 0).text()
            deger2 = self.tableWidget_2.item(item, 3).text()
            print(deger0, deger1, deger2)
            deger2 = self.kontrol(deger2)
            myddb.kaydet(deger0, deger1, deger2)
        myddb.conn.commit()
        self.close()
        # self.slotrecete2(int(self.label_2.text()))

    # veritabanından bilgi çek

    @pyqtSlot()
    def slotrecete2satirsil(self):
        bb = self.tableWidget_2.currentRow()
        self.tableWidget_2.removeRow(bb)

    @pyqtSlot(int, int)
    def slotrecete2(self, item):
        myddb = Myddb()

        self.lineEdit.setText("")
        deger0 = self.tableWidget.item(item, 1).text()

        #   recete2 ekranı hazırlanıyor
        self.label_2.setText(str(item))
        self.label_3.setText(deger0)
        file = open("./tempnenra/" + deger0 + ".txt", "w")

        deger0 = self.tableWidget.item(item, 1).text()
        deger1 = deger0 + " " + self.tableWidget.item(item, 2).text() + "  "
        self.label.setText(deger1)

        # veritabanından bilgi çek

        bul2 = myddb.cek2(deger0, "recete", "menukod")
        bul = myddb.cek("select * from hammadde where kategori=2")
        myddb.conn.commit()
        self.comboBox.clear()
        i = len(bul)
        for xx1 in range(i):
            self.comboBox.addItem(str(bul[xx1][1]) + " " + bul[xx1][2])

        i = len(bul2)
        self.tableWidget_2.setRowCount(i)
        aa = 0
        toplam = 0
        topelma = 0

        for row1 in bul2:
            item = str(row1[2])

            bul3 = myddb.cek2(item, "hammadde", "hamkod")
            myddb.conn.commit()

            item = str(bul3[0][1])
            file.write(item + " ")
            self.tableWidget_2.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            item = bul3[0][2]
            # file.write(item+" ")
            self.tableWidget_2.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            item = bul3[0][3]
            file.write(item + " ")
            self.tableWidget_2.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
            item = str(row1[3])
            self.tableWidget_2.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
            file.write(item + " ")

            item = str(bul3[0][6])
            file.write(item + "\n")
            self.tableWidget_2.setItem(aa, 4, QtWidgets.QTableWidgetItem(item))

            elma = (bul3[0][6]) * (row1[3]) * (100 + (bul3[0][4])) / 100
            topelma = topelma + elma
            item = str(elma)
            file.write(item + "\n")
            item = str("{:.2f}".format(elma))
            item = QtWidgets.QTableWidgetItem(item)
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

            self.tableWidget_2.setItem(aa, 5, QtWidgets.QTableWidgetItem(item))

            aa = aa + 1

        self.label_4.setText(str("{:.2f}".format(topelma)))

        file.close()

        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 50)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget_2.setColumnWidth(0, 50)
        self.tableWidget_2.setColumnWidth(1, 150)
        self.tableWidget_2.setColumnWidth(2, 50)
        self.tableWidget_2.setColumnWidth(3, 75)
        self.tableWidget_2.setColumnWidth(4, 75)
        self.tableWidget_2.setColumnWidth(5, 60)

        self.show()
        self.lineEdit.setFocus(True)


class Recete(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.recete2 = Recete2()

        self.lineEdit.textChanged.connect(self.slottextch)
        self.tableWidget.cellClicked.connect(self.slotrecete2)

    @pyqtSlot(int, int)
    def slotrecete2(self, item):
        myddb = Myddb()

        self.recete2.lineEdit.setText("")
        #   recete2 ekranı hazırlanıyor
        deger0 = self.tableWidget.item(item, 1).text()

        self.recete2.label_2.setText(str(item))
        self.recete2.label_3.setText(deger0)
        file = open("./tempnenra/" + deger0 + ".txt", "w")

        deger0 = self.tableWidget.item(item, 1).text()
        deger1 = deger0 + " " + self.tableWidget.item(item, 2).text() + "  "
        self.recete2.label.setText(deger1)

        # veritabanından bilgi çek

        bul2 = myddb.cek2(deger0, "recete", "menukod")
        bul = myddb.cek("select * from hammadde where kategori=2")
        myddb.conn.commit()
        self.recete2.comboBox.clear()
        i = len(bul)
        for xx1 in range(i):
            self.recete2.comboBox.addItem(str(bul[xx1][1]) + " " + bul[xx1][2])

        i = len(bul2)
        self.recete2.tableWidget_2.setRowCount(i)
        aa = 0
        toplam = 0
        topelma = 0

        for row1 in bul2:
            item = str(row1[2])

            bul3 = myddb.cek2(item, "hammadde", "hamkod")
            myddb.conn.commit()

            item = str(bul3[0][1])
            file.write(item + " ")
            self.recete2.tableWidget_2.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            item = bul3[0][2]
            # file.write(item+" ")
            self.recete2.tableWidget_2.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            item = bul3[0][3]
            file.write(item + " ")
            self.recete2.tableWidget_2.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
            item = str(row1[3])
            self.recete2.tableWidget_2.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
            file.write(item + " ")

            item = str(bul3[0][6])
            file.write(item + "\n")
            self.recete2.tableWidget_2.setItem(aa, 4, QtWidgets.QTableWidgetItem(item))

            elma = (bul3[0][6]) * (row1[3]) * (100 + (bul3[0][4])) / 100
            topelma = topelma + elma
            item = str(elma)
            file.write(item + "\n")
            item = str("{:.2f}".format(elma))
            item = QtWidgets.QTableWidgetItem(item)
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

            self.recete2.tableWidget_2.setItem(aa, 5, QtWidgets.QTableWidgetItem(item))

            aa = aa + 1

        self.recete2.label_4.setText(str("{:.2f}".format(topelma)))

        file.close()

        self.recete2.tableWidget.setColumnWidth(0, 50)
        self.recete2.tableWidget.setColumnWidth(1, 250)
        self.recete2.tableWidget.setColumnWidth(2, 50)
        self.recete2.tableWidget.setColumnWidth(3, 50)
        self.recete2.tableWidget_2.setColumnWidth(0, 50)
        self.recete2.tableWidget_2.setColumnWidth(1, 150)
        self.recete2.tableWidget_2.setColumnWidth(2, 50)
        self.recete2.tableWidget_2.setColumnWidth(3, 75)
        self.recete2.tableWidget_2.setColumnWidth(4, 75)
        self.recete2.tableWidget_2.setColumnWidth(5, 60)

        self.recete2.show()
        self.recete2.lineEdit.setFocus(True)

    @pyqtSlot()
    def slottextch(self):
        myddb = Myddb()

        a = "%" + self.lineEdit.text() + "%"
        sql3 = "select * from hammadde where (kategori=2 or kategori=3) and " \
               " ( hamkod like '" + a \
               + "' or hamad like '" + a + "'  ) order by hamkod"

        myddb.cur.execute(sql3)
        bul = myddb.cur.fetchall()

        i = len(bul)
        self.tableWidget.setRowCount(i)
        aa = 0
        toplam = 0
        for row1 in bul:
            item = str(row1[0])
            self.tableWidget.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            item = str(row1[1])
            self.tableWidget.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            item = row1[2]
            self.tableWidget.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
            item = str(row1[3])
            self.tableWidget.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
            item = str(row1[4])
            self.tableWidget.setItem(aa, 4, QtWidgets.QTableWidgetItem(item))
            aa = aa + 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    recete = Recete()
    recete.show()
    recete.raise_()

    app.exec_()
