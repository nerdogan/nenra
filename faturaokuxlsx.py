__author__ = 'NAMIK'

from PyQt5 import QtCore, QtWidgets
from fatura import Fatura
import pandas as pd
import re, sys
import datetime, time
from mdb.modulemdb import *

app = QtWidgets.QApplication(sys.argv)
mydb = Myddb()
fname = QtWidgets.QFileDialog.getOpenFileName()
print(fname[0])
openfile = fname[0]
# openfile='/Users/namikerdogan/Downloads/HAVVA AYDIN  EYLÜL 2021 SATIŞ FATURALAR.xlsx'
df = pd.ExcelFile(openfile)

print(df)
elma = "elma"
ana = df.parse(skiprows=2, index_col=None, na_values=['NA'])
ana['Tarih'] = pd.to_datetime(ana['Tarih'], dayfirst=True)
satir1 = 1
satir2 = 1
dur = 0.05

fatura = Fatura()
fatura.goster()

print(len(ana.index))
for i in range(len(ana.index)):
    print(ana.iloc[i, 0])
    if elma != (ana.iloc[i, 0]):
        elma = str((ana.iloc[i, 0]))
        armut = int(elma.rsplit("N012022")[1])
        dt = (ana.iloc[i, 1])

        fatura.lineEdit.setText('N03')
        fatura.lineEdit_2.setText(str(armut))
        fatura.dateEdit.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
        time.sleep(dur)
        if fatura.label_5.text() == "":
            fatura.lineEdit_3.setText("tdy")
            time.sleep(dur)
            fatura.slotfatura(0, 0)
            time.sleep(dur)
            satir2 = 1
        else:
            fatura.tableWidget_2.setRowCount(0)
            satir2 = 1

    satir2 = satir2 + 1
    satir = satir2

    sql = "insert into hambarkod (barkodno) values (%s)"
    try:
        mydb.cur.execute(sql, ((ana.iloc[i, 6]),))
        mydb.conn.commit()
    except MySQLdb.IntegrityError as e:

        if not e.args[0] == 1062:
            raise
        else:
            print(u"Veritabanı girişi zaten yapılmış", satir1)
            satir1 = satir1 + 1

    sql = "select hamkod1,miktar from hambarkod where barkodno=%s"
    mydb.cur.execute(sql, ((ana.iloc[i, 6]),))
    bul = mydb.cur.fetchone()
    if bul:
        # print(bul)
        fatura.lineEdit_3.setText(str(bul[0]))
        miktar = float(ana.iloc[i, 8]) * bul[1]

    time.sleep(dur)
    if fatura.tableWidget.rowCount() == 0 or fatura.tableWidget.rowCount() > 1:
        print("kdv bölümü", str(ana.iloc[i, 11]))
        if str(ana.iloc[i, 11]) == "1.0":
            fatura.lineEdit_3.setText("yiyecek")
        if str(ana.iloc[i, 11]) == "8.0":
            fatura.lineEdit_3.setText("yiyecek")
        if str(ana.iloc[i, 11]) == "18.0":
            fatura.lineEdit_3.setText("temizlik")
        if str(ana.iloc[i, 11]) == "1":
            fatura.lineEdit_3.setText("yiyecek")
        if str(ana.iloc[i, 11]) == "8":
            fatura.lineEdit_3.setText("yiyecek")
        if str(ana.iloc[i, 11]) == "18":
            fatura.lineEdit_3.setText("temizlik")

    print(fatura.lineEdit_3.text())
    time.sleep(dur)
    print(ana.iloc[i, 5], (ana.iloc[i, 6]))

    fatura.slotfatura(0, 0)

    time.sleep(dur)
    fatura.tableWidget_2.setItem((satir - 2), 3, QtWidgets.QTableWidgetItem(str(ana.iloc[i, 11])))
    if str(ana.iloc[i, 9]) == "Kilogram":
        miktar = (float(ana.iloc[i, 8]) * 1000)

    fatura.tableWidget_2.setItem((satir - 2), 4, QtWidgets.QTableWidgetItem(str(miktar)))
    fatura.tableWidget_2.setItem((satir - 2), 6,
                                 QtWidgets.QTableWidgetItem(str((float(ana.iloc[i, 8]) * float(ana.iloc[i, 10])))))
    time.sleep(dur)
    fatura.slotfaturakaydet()
