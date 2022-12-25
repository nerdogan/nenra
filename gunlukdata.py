# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      muhasebe-2
#
# Created:     28.01.2014
# Copyright:   (c) muhasebe-2 2014
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import sys
from PyQt5 import QtGui, QtCore, QtSql, QtWidgets
from PyQt5.QtCore import pyqtSlot

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

appcore = QtCore.QCoreApplication(sys.argv)
db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
db.setHostName('nen.duckdns.org')
db.setPort(30000)
db.setDatabaseName('test')
db.setUserName('nen')
db.setPassword('654152')

if db.open() == False:
    print('fail')


def initializeModel(model):
    model.setQuery("select * from cari_har where  fistipi=10 and tarih between '2022-09-01' and '2022-09-30'")


    model.setHeaderData(0, QtCore.Qt.Horizontal, " ")
    model.setHeaderData(1, QtCore.Qt.Horizontal, " ")
    model.setHeaderData(2, QtCore.Qt.Horizontal, " ")


def createView(title, model):
    view = QtWidgets.QTableView()
    view.setModel(model)

    view.setWindowTitle(title)
    return view


def addrow(i):
    i=model.index(i,0)
    ret = (str(model.data(i).toString()))
    print(ret)
    model.setQuery('select * from cariay where  fisno="' + ret + '" ')
    view1.setModel(model)


def geridon(i):
    model.setQuery('select tarih, sum(tutar) from kasa where tutar<0 and posid=2000 group by tarih')


    view1.setModel(model)


def findrow(i):
    delrow = i.row()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    model = QtSql.QSqlQueryModel()
    delrow = -1
    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)

    dlg = QtWidgets.QDialog()
    dlg.resize(850,500)
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(view1)

    button = QtWidgets.QPushButton(_fromUtf8("Ayrıntı Göster"))
    button.clicked.connect(lambda: addrow(view1.currentIndex().row()))
    layout.addWidget(button)

    btn1 = QtWidgets.QPushButton(_fromUtf8("Geri Dön "))
    btn1.clicked.connect(geridon)
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Masraflar")
    dlg.show()
    sys.exit(app.exec_())





