# -*- coding: utf-8 -*-

import sys
import re
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_fatura import Ui_Dialog3

from modulemdb import *



class Fatura(QtGui.QDialog , Ui_Dialog3):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.setupUi(self)
		self.myddb = Myddb()
		self.myddb.cur.execute('SET AUTOCOMMIT=0;')
		self.tableWidget_2.setColumnWidth(0, 50)
		self.tableWidget_2.setColumnWidth(1, 200)
		self.tableWidget_2.setColumnWidth(2, 40)
		self.tableWidget_2.setColumnWidth(3, 40)
		self.tableWidget_2.setColumnWidth(4, 75)
		self.tableWidget_2.setColumnWidth(5, 75)
		self.tableWidget_2.setColumnWidth(6, 75)

		self.lineEdit_3.textChanged.connect(self.linechange)
		self.lineEdit_2.textChanged.connect(self.slotfaturakont)
		self.lineEdit.textChanged.connect(self.slotfaturakont)
		self.pushButton.clicked.connect(self.slotfaturakaydet)
		self.tableWidget.cellClicked.connect(self.slotfatura)
		self.pushButton_3.clicked.connect(self.slotfaturasatirsil)
		self.tableWidget_2.itemChanged.connect(self.toplamdegisti)

	def kontrol(self,girdi):
		girdi = str(girdi)
		ara = re.search(",", girdi)
		if ara:
			derle = re.compile(",")
			cikti = derle.sub(".", girdi)
			return cikti
		return girdi

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

		if len(self.label_3.text()) > 12:
			bul = self.myddb.cek1(a, "hammadde", "hamad")
			self.tableWidget.setColumnWidth(0, 75)
			self.tableWidget.setColumnWidth(1, 220)
			self.tableWidget.setColumnWidth(2, 50)
			self.tableWidget.setColumnWidth(3, 50)
		else:
			bul = self.myddb.cek1(a, "cari", "cariad")
			self.tableWidget.setColumnWidth(0, 75)
			self.tableWidget.setColumnWidth(1, 50)
			self.tableWidget.setColumnWidth(2, 220)
			self.tableWidget.setColumnWidth(3, 50)

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

	@pyqtSlot(int, int)
	def slotfatura(self,item, item2):
		#   cari listesinden çiftklikle line edite cari firma bilgisini yazıyor
		print item, item2

		if len(self.label_3.text()) < 12:
			deger1 = self.tableWidget.item(item, 0).text()
			deger2 = self.tableWidget.item(item, 1).text()
			deger3 = self.tableWidget.item(item, 2).text()
			deger4 = self.tableWidget.item(item, 3).text()
			self.label_5.setText(deger1)
			self.label_3.setText(deger1 + " " + deger2 + " " + deger3)
			bul1 = str(deger1)
			self.lineEdit_3.setText("")
			self.slotfaturakaydet()

			return

		if len(self.label_3.text()) > 12:
			#   hammadde listesinden çiftklikle tablewidget_2 ye hammadde bilgisini ekliyor.
			i = self.tableWidget_2.rowCount()
			deger1 = self.tableWidget.item(item, 0).text()
			deger2 = self.tableWidget.item(item, 1).text()
			deger3 = self.tableWidget.item(item, 2).text()
			deger4 = self.tableWidget.item(item, 4).text()

			i = i + 1
			j = 5
			self.tableWidget_2.setRowCount(i)
			aa = i - 1

			item = deger1
			self.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
			item = deger2
			self.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
			item = deger3
			self.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
			item = deger4
			self.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
			item = '0'
			self.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item))
			item = '0'
			self.tableWidget_2.setItem(aa, 5, QtGui.QTableWidgetItem(item))
			self.lineEdit_3.setFocus(True)

	@pyqtSlot()
	def slotfaturakaydet(self):
		toplam = 0
		kdv = 0
		deger0 = self.label_5.text()
		deger5 = self.lineEdit.text()
		deger6 = self.lineEdit_2.text()
		deger7 = self.dateEdit.date().toPyDate()
		sql = "select * from cari_har where  serino='" + str(deger5) + "' and sirano='" + str(deger6) + "'"
		sonuc = self.myddb.cek(sql)
		print sonuc
		if len(sonuc) == 0:
			print "fatura kaydı yok"
			maxfisno = self.myddb.cek("select max(fisno) from cari_har ")

			if maxfisno[0][0] is None:
				maxfisno1=0
			else:
				maxfisno1=maxfisno[0][0]

			if deger0=="100":
				self.fistipi1=22
			else:
				self.fistipi1=10

			sql1 = "insert into cari_har (cariid,serino,sirano,tarih,fistipi,fisno) values (%s,%s,%s,%s,%s,%s)"
			print sql1
			self.myddb.cur.execute(sql1, (deger0, deger5, deger6, deger7, self.fistipi1, maxfisno1 + 1))
			self.myddb.conn.commit()

		else:
			print " fatura kaydı var"
			self.myddb.sil(sonuc[0][0], "cariay", "fisno")
			self.myddb.conn.commit()
			satir = 0

		i = self.tableWidget_2.rowCount()
		for item in range(i):
			satir += 1
			deger10 = self.tableWidget_2.item(item, 0).text()
			deger11 = self.tableWidget_2.item(item, 3).text()
			deger12 = self.tableWidget_2.item(item, 4).text()
			deger13 = self.tableWidget_2.item(item, 5).text()
			deger12 = self.kontrol(deger12)
			deger13 = self.kontrol(deger13)
			toplam += float(deger12) * float(deger13)
			kdv += float(deger11) * float(deger12) * float(deger13) / 100
			print deger10
			sql2 = "insert into cariay (fisno,fissatir,fistipi,hamkod,kdv,miktar,birimfiy,tarih) values (%s,%s,%s,%s,%s,%s,%s,%s)"
			self.myddb.cur.execute(sql2, (sonuc[0][0], satir, sonuc[0][2], deger10, deger11, deger12, deger13,sonuc[0][6]))

		self.myddb.conn.commit()
		self.label_6.setText("{0}  {1}".format(str(toplam), str("{0:.3f}".format(kdv))))
		self.lineEdit_3.setFocus(True)

	@pyqtSlot()
	def slotfaturasatirsil(self):
		bb = self.tableWidget_2.currentRow()
		self.tableWidget_2.removeRow(bb)

	@pyqtSlot(int,int)
	def toplamdegisti(self,item):
		if item.column()==6:
			self.tableWidget_2.setItem(item.row(),5,QtGui.QTableWidgetItem(str(float(self.kontrol(item.text()))/float(self.tableWidget_2.item(item.row(),4).text()  ))))


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	fatura1=Fatura()
	fatura1.goster()
	app.exec_()