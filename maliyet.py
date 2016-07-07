# -*- coding: utf-8 -*-
import sys
import re
import datetime
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from ui_maliyet import Ui_Dialog4

from modulemdb import *


class Maliyet(QtGui.QDialog , Ui_Dialog4):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.myddb = Myddb()
        self.tableWidget.setRowCount(0)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(some_date)
        self.dateEdit_2.setDate(some_date)

        StartDate = "07/07/16"

        EndDate = datetime.datetime.strptime(StartDate, "%d/%m/%y")
        now = datetime.datetime.now() - datetime.timedelta(days=1)
        dt = now - EndDate
        print dt.days
        # mainWindow.plainTextEdit.appendPlainText(str(dt.days))
        for i in range(dt.days):
	        EndDate = EndDate + datetime.timedelta(days=1)
	        sql = " select * from harcanan where tarih like %s"
	        sonuc = self.myddb.cur.execute(sql, [(EndDate.strftime('%Y-%m-%d') + "%")])
	        if sonuc == 0:
		        print " kaydediliyor"
		        tar = EndDate.strftime('%d%m%Y')

		        sql2 = "SELECT menu.menukod,hamkod,miktar,adet FROM SATDATA inner join menu on urunkod=menukod and DATE(tarih)=%s  inner join recete on  menu.menuid=recete.menukod "
		        bilgi = self.myddb.cur.execute(sql2, [(EndDate.strftime('%Y-%m-%d'))])
		        print bilgi
		        if bilgi <> 0:
			        bilgi2 = self.myddb.cur.fetchall()
			        for row1 in bilgi2:
				        hmikt = row1[2] * row1[3]
				        print hmikt
				        sql1 = "insert into harcanan (hurunkod,hhammaddeid,hmiktar,fiyat,tarih) values (%s,%s,%s,%s,%s)"
				        self.myddb.cur.execute(sql1, (row1[0], row1[1], hmikt, "0", EndDate))
				        self.myddb.conn.commit()

	        print EndDate.strftime('%d%m%Y')

