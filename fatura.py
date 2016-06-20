# -*- coding: utf-8 -*-
import sys

from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_fatura import Ui_Dialog3

from modulemdb import *



class Fatura(QtGui.QDialog , Ui_Dialog3):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.myddb = Myddb()
        self.lineEdit_3.textChanged.connect(self.linechange)
        self.lineEdit_2.textChanged.connect(self.slotfaturakont)
        self.lineEdit.textChanged.connect(self.slotfaturakont)

    def goster(self):
        print "fatura arayüzü açıldı"
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.label_3.setText("")
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        # some_date = QtCore.QDate(2011,4,22)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(some_date)
        self.show()
        self.lineEdit.setFocus(True)
        self.emit(QtCore.SIGNAL("acac(int)"), 33)

    @pyqtSlot(int,str)
    def linechange(self,item2):
	    print "fatura"
	    a = item2.toUtf8()
	    a = str(a)
	    print a
	    bul = self.myddb.cek1(a, "cari", "cariad")

	    if len(self.label_3.text()) > 12:
		    bul = self.myddb.cek1(a, "hammadde", "hamad")

	    i = len(bul)
	    j = 5
	    self.tableWidget.setRowCount(i)
	    aa = 0
	    toplam = 0
	    for row1 in bul:
		    item = str(row1[1])
		    self.tableWidget.setItem(aa, 0, QtGui.QTableWidgetItem(item))
		    item = row1[2]
		    self.tableWidget.setItem(aa, 1, QtGui.QTableWidgetItem(item))
		    item = row1[3]
		    self.tableWidget.setItem(aa, 2, QtGui.QTableWidgetItem(item))
		    item = row1[4]
		    self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
		    item = str(row1[4])
		    self.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
		    aa = aa + 1

    @pyqtSlot()
    def slotfaturakont(self):

	    deger5 = self.lineEdit.text()
	    deger6 = self.lineEdit_2.text()
	    sql = "select * from cari_har where  serino='" + str(deger5) + "' and sirano='" + str(deger6) + "'"
	    sonuc =self.myddb.cek(sql)
	    self.label_3.setText("")
	    self.tableWidget.setRowCount(0)
	    self.tableWidget_2.setRowCount(0)
	    # some_date = QtCore.QDate(2011,4,22)
	    some_date = QtCore.QDate.currentDate()
	    self.dateEdit.setDate(some_date)

	    if len(sonuc) > 0:
		    dt = sonuc[0][6]

		    QtGui.QMessageBox.information(self.tableWidget,
		                            "QTableWidget Cell Click",
		                            "Text: " + str(dt.year))
		    print sonuc
		    for item in sonuc:
			    self.dateEdit.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
			    sonuc1 = self.myddb.cek2(item[1], "cari", "cariid")
			    for item2 in sonuc1:
				    print item2

				    deger0 = str(item2[1]) + " " + item2[2] + " " + item2[3]
				    self.label_3.setText(deger0)
				    bul1 = str(item[0])

			    bul2 = self.myddb.cek2(item[0], "cariay", "fisno")
			    print bul2
			    i = len(bul2)
			    j = 6
			    self.tableWidget_2.setRowCount(i)
			    aa = 0
			    toplam = 0
			    for row1 in bul2:
				    item = str(row1[4])
				    self.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
				    bul3 = self.myddb.cek2(item, "hammadde", "hamkod")
				    print (bul3)
				    item = str(bul3[0][2])
				    self.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
				    item = bul3[0][3]
				    self.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
				    item = str(row1[7])
				    self.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
				    item = str(row1[5])
				    self.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item))
				    item = str(row1[6])
				    self.tableWidget_2.setItem(aa, 5, QtGui.QTableWidgetItem(item))
				    aa = aa + 1
		    self.lineEdit_3.setFocus(True)
		    return



if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	fatura1=Fatura()
	fatura1.show()
	app.exec_()