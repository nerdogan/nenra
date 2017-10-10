# -*- coding: utf-8 -*-

import sys
import time as ttim
import re
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore,QtTest
from ui_fatura import Ui_Dialog3

from modulemdb import *



class Fatura(QtGui.QDialog , Ui_Dialog3):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        self.fisno=None
        self.comb={}
        self.tableWidget_2.setColumnWidth(0, 50)
        self.tableWidget_2.setColumnWidth(1, 200)
        self.tableWidget_2.setColumnWidth(2, 40)
        self.tableWidget_2.setColumnWidth(3, 40)
        self.tableWidget_2.setColumnWidth(4, 75)
        self.tableWidget_2.setColumnWidth(5, 75)
        self.tableWidget_2.setColumnWidth(6, 75)

        self.lineEdit_4.textChanged.connect(self.vadeartir)
        self.pushButton_5.clicked.connect(lambda : self.fisgetir( self.lineEdit_5.text()))

        self.lineEdit_3.textChanged.connect(self.linechange)
        self.lineEdit_2.textChanged.connect(self.slotfaturakont)
        self.lineEdit.textChanged.connect(self.slotfaturakont)
        self.pushButton.clicked.connect(self.slotfaturakaydet)
        self.tableWidget.cellClicked.connect(self.slotfatura)
        self.pushButton_3.clicked.connect(self.slotfaturasatirsil)
        self.pushButton_4.clicked.connect(self.slotfaturasil)
        self.tableWidget_2.itemChanged.connect(self.toplamdegisti)
        self.comboBox.currentIndexChanged.connect(self.odemeyap)

    def kontrol(self,girdi):
        girdi = str(girdi)
        ara = re.search(",", girdi)
        if ara:
            derle = re.compile(",")
            cikti = derle.sub(".", girdi)
            return cikti
        return girdi

    def addcomb(self, row, col):
        #if self.old_row >= 0:
        #    self.table.setCellWidget(self.old_row, self.old_col, None)
        self.old_row = row
        self.old_col = col

        comb1 = QtGui.QComboBox()
        self.comb[row]=comb1


        self.tableWidget_2.setCellWidget(row, col, self.comb[row])

    def goster(self):
        print "fatura arayüzü açıldı"
        self.myddb = Myddb()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.label_3.setText("")
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        # some_date = QtCore.QDate(2011,4,22)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(some_date)
        self.dateEdit_2.setDate(some_date)
        self.show()
        self.raise_()
        self.lineEdit.setFocus(True)

    @pyqtSlot(int, str)
    def vadeartir(self, item2):
        if len(item2)>0:
            some_date=self.dateEdit.date()
            self.dateEdit_2.setDate(some_date.addDays(int(item2)))

    @pyqtSlot(int, str)
    def odemeyap(self, item2):
        elma = self.toplam
        elma1 = self.cari
        some_date = self.dateEdit.date()

        self.lineEdit_2.setText("")
        self.lineEdit.setText("TED")
        self.dateEdit.setDate(some_date)

        self.linechange(QtCore.QString(elma1))

        self.slotfatura(0, 0)

        if self.comboBox.currentIndex()==1:
            self.linechange(QtCore.QString("NAKIT"))
        elif self.comboBox.currentIndex()==2:
            self.linechange(QtCore.QString("DENIZBANK"))
        elif self.comboBox.currentIndex()==3:
            self.linechange(QtCore.QString("YKB"))
        self.slotfatura(0, 0)
        self.tableWidget_2.setItem(0, 4, QtGui.QTableWidgetItem("-1"))
        self.tableWidget_2.setItem(0, 5, QtGui.QTableWidgetItem(elma))
        self.comboBox.blockSignals(True)
        self.comboBox.setCurrentIndex(0)
        self.comboBox.blockSignals(False)





    @pyqtSlot(int, str)
    def fisgetir(self, item2):
        print item2,"elmaarmut kelmahmut"
        self.comboBox.blockSignals(True)
        self.comboBox.setCurrentIndex(0)
        self.comboBox.blockSignals(False)

        if self.lineEdit_5.text()!="":
            sql = "select serino,sirano from cari_har where  fisno='" + str(self.lineEdit_5.text())  + "'"
            sonuc = self.myddb.cek(sql)
            self.lineEdit.setText(str(sonuc[0][0]))
            self.lineEdit_2.setText(str(sonuc[0][1]))

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
            item = str(row1[4])
            self.tableWidget.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item = str(row1[6])
            self.tableWidget.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            aa = aa + 1

        if (aa==1 and self.label_5.text()=="4"):
            self.slotfatura(0,0)
            self.lineEdit_3.setText("")
            self.tableWidget_2.scrollToBottom()

    @pyqtSlot()
    def slotfaturakont(self):
        self.fisno=None
        self.label_5.setText("")

        deger5 = self.lineEdit.text()
        deger6 = self.lineEdit_2.text()
        sql = "select * from cari_har where  serino='" + str(deger5) + "' and sirano='" + str(deger6) + "'"
        sonuc =self.myddb.cek(sql)
        self.label_3.setText("")
        self.tableWidget_2.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        # some_date = QtCore.QDate(2011,4,22)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(some_date)
        # tediye fişi ted olunca otomatik sıra numarası veriyor
        if ( deger5=="ted" or deger5=="TED" or deger5=="say" or deger5=="SAY") and deger6=="":
            maxbelgeno = self.myddb.cek("select max(sirano) from cari_har where serino='" + str(deger5) + "' ")
            deger6 = str(maxbelgeno[0][0] + 1)
            self.lineEdit_2.setText(deger6)


        if len(sonuc) > 0:
            dt = sonuc[0][6]
            dt1 = sonuc[0][9]

            #QtGui.QMessageBox.information(self.tableWidget,
            #						"QTableWidget Cell Click",
            #						"Text: " + str(dt.year))
            print sonuc
            self.tableWidget_2.blockSignals(True)
            for item3 in sonuc:
                self.dateEdit.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
                self.dateEdit_2.setDate(QtCore.QDate(dt1.year, dt1.month, dt1.day))
                self.lineEdit_4.setText(str((dt1-dt).days))
                sonuc1 = self.myddb.cek2(item3[1], "cari", "cariid")
                for item2 in sonuc1:
                    print item2
                    self.label_5.setText(str(item2[1]))

                    deger0 = str(item2[1]) + " " + item2[2] + " " + item2[3]
                    self.cari=item2[3]
                    self.label_3.setText(deger0)
                    bul1 = str(item3[0])

                bul2 = self.myddb.cek2(item3[3], "cariay", "fisno")
                self.fisno = item3[3]
                print self.fisno , "ahada bu"
                self.setWindowTitle(QtCore.QString.fromUtf8("Fiş Girişi " + str(self.fisno)))

                print bul2
                i = len(bul2)
                j = 6
                self.tableWidget_2.setRowCount(i)

                aa = 0
                toplam = 0
                for row1 in bul2:
                    item = str(row1[4])
                    self.tableWidget_2.setItem(aa, 0, QtGui.QTableWidgetItem(item))
                    elma=item
                    bul3 = self.myddb.cek2(elma, "hammadde", "hamkod")

                    item = bul3[0][2]
                    self.tableWidget_2.setItem(aa, 1, QtGui.QTableWidgetItem(item))
                    item = bul3[0][3]
                    self.tableWidget_2.setItem(aa, 2, QtGui.QTableWidgetItem(item))
                    self.addcomb(aa,2)
                    self.comb[aa].setProperty("row",aa)
                    self.comb[aa].setProperty("old", 1)
                    self.myddb.cur.execute("select birim,katsayi from birim where hamkod=%s order by katsayi",[elma])
                    bul4 = self.myddb.cur.fetchall()
                    for satirr in  bul4:
                        self.comb[aa].addItem(satirr[0])
                        self.comb[aa].setProperty(satirr[0],satirr[1] )

                    self.connect(self.comb[aa], QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.birimdegisti)

                    item = str(row1[7])
                    self.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
                    item = str(row1[5])
                    self.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item))
                    item = str(row1[6])
                    item=QtGui.QTableWidgetItem(item)
                    if self.label_5.text()=="100":
                        item.setFlags( QtCore.Qt.ItemIsEditable)
                    self.tableWidget_2.setItem(aa, 5, item)
                    item = str(round((row1[6]*row1[5]),2))
                    item = QtGui.QTableWidgetItem(item)
                    if self.label_5.text() == "100":
                        item.setFlags(QtCore.Qt.ItemIsEditable)

                    self.tableWidget_2.setItem(aa, 6, QtGui.QTableWidgetItem(item))
                    aa = aa + 1


            self.lineEdit_3.setFocus(True)

            self.tableWidget_2.blockSignals(False)
            self.toplamgoster()

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
            self.lineEdit_3.setFocus(True)
            self.slotfaturakaydet()

            return

        if len(self.label_3.text()) > 12:
            #   hammadde listesinden çiftklikle tablewidget_2 ye hammadde bilgisini ekliyor.
            self.tableWidget_2.blockSignals(True)
            i = self.tableWidget_2.rowCount()
            deger1 = self.tableWidget.item(item, 0).text()
            deger2 = self.tableWidget.item(item, 1).text()
            deger3 = self.tableWidget.item(item, 2).text()
            deger4 = self.tableWidget.item(item, 3).text()
            deger5 = self.tableWidget.item(item, 4).text()

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

            self.addcomb(aa, 2)
            self.comb[aa].setProperty("row", aa)
            self.comb[aa].setProperty("old", 1)
            self.myddb.cur.execute("select birim,katsayi from birim where hamkod=%s order by katsayi", [deger1])
            bul4 = self.myddb.cur.fetchall()
            for satirr in bul4:
                self.comb[aa].addItem(satirr[0])
                self.comb[aa].setProperty(satirr[0], satirr[1])

            self.connect(self.comb[aa], QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.birimdegisti)

            item = deger4
            self.tableWidget_2.setItem(aa, 3, QtGui.QTableWidgetItem(item))
            item = '1'
            self.tableWidget_2.setItem(aa, 4, QtGui.QTableWidgetItem(item))
            item = deger5
            item = QtGui.QTableWidgetItem(item)
            if self.label_5.text() == "100":
                item.setFlags(QtCore.Qt.ItemIsEditable)

            self.tableWidget_2.setItem(aa, 5, QtGui.QTableWidgetItem(item))
            item = deger5
            item = QtGui.QTableWidgetItem(item)
            if self.label_5.text() == "100":
                item.setFlags(QtCore.Qt.ItemIsEditable)

            self.tableWidget_2.setItem(aa, 6, QtGui.QTableWidgetItem(item))
            self.lineEdit_3.setFocus(True)
            self.tableWidget_2.blockSignals(False)

    @pyqtSlot()
    def slotfaturakaydet(self):
        toplam = 0
        kdv = 0
        deger0 = self.label_5.text()
        deger5 = str(self.lineEdit.text()).upper()
        deger6 = self.lineEdit_2.text()
        deger7 = self.dateEdit.date().toPyDate()
        self.deger8 = self.dateEdit_2.date().toPyDate()
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

            if deger0 == "4":
                self.fistipi1 = 90

            elif deger0=="100":
                self.fistipi1=22
            elif deger5 == "TED":
                self.fistipi1 = 11


            else:
                self.fistipi1=10

            sql1 = "insert into cari_har (cariid,serino,sirano,tarih,fistipi,fisno,vade) values (%s,%s,%s,%s,%s,%s,%s)"
            print sql1
            self.setWindowTitle(QtCore.QString.fromUtf8("Fiş Girişi " + str(maxfisno1 + 1)))
            self.myddb.cur.execute(sql1, (deger0, deger5, deger6, deger7, self.fistipi1, maxfisno1 + 1,self.deger8))
            self.myddb.conn.commit()

        else:
            print " fatura kaydı var"
            self.myddb.sil(sonuc[0][3], "cariay", "fisno")
            self.myddb.conn.commit()
            son=self.myddb.cur.execute("select max(caid) from cariay")
            son1="ALTER TABLE cariay AUTO_INCREMENT ="+str(son)
            self.myddb.cur.execute(son1)
            satir = 0

        i = self.tableWidget_2.rowCount()
        if i==0:
            return
        for item in range(i):
            satir += 1
            deger10 = self.tableWidget_2.item(item, 0).text()
            deger11 = self.tableWidget_2.item(item, 3).text()
            deger12 = self.tableWidget_2.item(item, 4).text()
            deger13 = self.tableWidget_2.item(item, 5).text()
            deger12 = self.kontrol(deger12)

            deger13 = self.kontrol(deger13)
            print deger12
            print deger13
            toplam += float(deger12) * float(deger13)
            kdv += float(deger11) * float(deger12) * float(deger13) / 100
            print deger10 , toplam , kdv
            sql2 = "insert into cariay (fisno,fissatir,fistipi,hamkod,kdv,miktar,birimfiy,tarih) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            self.myddb.cur.execute(sql2, (sonuc[0][3], satir, sonuc[0][2], deger10, deger11, deger12, deger13,sonuc[0][6]))
        sql3 = "UPDATE cari_har SET tutar=%s where fisno=%s "
        sql4 = "update cariay targetTable  left join hammadde sourceTable on targetTable.hamkod = sourceTable.hamkod set  targetTable.muhkod = sourceTable.muhkod "
        print sql3

        self.myddb.cur.execute(sql3, ((toplam+kdv),sonuc[0][3]))
        self.myddb.conn.commit()
        SQL5= self.myddb.cur.execute(sql4)
        self.myddb.conn.commit()
        self.emit(QtCore.SIGNAL("acac"), SQL5)
        self.label_6.setText("{0}  {1}  {2}".format(str("{0:.2f}".format(toplam)), str("{0:.2f}".format(kdv)),
                                                    str("{0:.2f}".format(toplam + kdv))))
        self.lineEdit_3.setFocus(True)

    @pyqtSlot()
    def slotfaturasatirsil(self):
        bb = self.tableWidget_2.currentRow()
        self.tableWidget_2.removeRow(bb)

    def toplamgoster(self):
        i = self.tableWidget_2.rowCount()
        toplam=0
        kdv=0
        for item in range(i):

            deger10 = self.tableWidget_2.item(item, 0).text()
            deger11 = self.tableWidget_2.item(item, 3).text()
            deger12 = self.tableWidget_2.item(item, 4).text()
            deger13 = self.tableWidget_2.item(item, 5).text()
            deger12 = self.kontrol(deger12)

            deger13 = self.kontrol(deger13)
            toplam += float(deger12) * float(deger13)
            kdv += float(deger11) * float(deger12) * float(deger13) / 100
            print deger10, toplam, kdv
            self.toplam="{0:.2f}".format(toplam + kdv)
            self.label_6.setText("{0}  {1}  {2}".format(str("{0:.2f}".format(toplam)), str("{0:.2f}".format(kdv)),
                                                        str("{0:.2f}".format(toplam + kdv))))

    @pyqtSlot()
    def slotfaturasil(self):
        print "fiş silme ekran"
        if self.fisno is not None:
            print self.fisno
            _fromUtf8 = QtCore.QString.fromUtf8
            msg = QtGui.QMessageBox()
            msg.setWindowTitle(_fromUtf8("Fiş Silme"))
            msg.setIcon(QtGui.QMessageBox.Critical)

            msg.setText(_fromUtf8("Fiş Siliniyor !!!"))
            msg.setInformativeText(_fromUtf8(str(self.fisno)+" nolu fiş silmek istediğinizden eminmisiniz ?"))

            msg.setDetailedText(str(self.fisno) + "Siliniyor !!!")
            msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
            #msg.buttonClicked.connect(msgbtn)

            retval = msg.exec_()
            if retval==1024:
                print "value of pressed message box button:", retval
                print self.myddb.sil(self.fisno, "cariay", "fisno")
                print self.myddb.sil(self.fisno, "cari_har", "fisno")
                self.myddb.conn.commit()
                self.tableWidget_2.clearContents()
                self.tableWidget.setRowCount(0)
                self.tableWidget_2.setRowCount(0)

    @pyqtSlot(int,int)
    def toplamdegisti(self,item):

        self.tableWidget_2.blockSignals(True)

        if item.column()==6:
            self.tableWidget_2.setItem(item.row(),5,QtGui.QTableWidgetItem(str(float(self.kontrol(item.text()))/float(self.tableWidget_2.item(item.row(),4).text()  ))))
        if item.column()==4:
            self.tableWidget_2.setItem(item.row(), 6, QtGui.QTableWidgetItem(
                str(float(self.kontrol(item.text())) * float(self.tableWidget_2.item(item.row(), 5).text()))))
        if item.column() == 5:
            self.tableWidget_2.setItem(item.row(), 6, QtGui.QTableWidgetItem(
                str(float(self.kontrol(item.text())) * float(self.tableWidget_2.item(item.row(), 4).text()))))
        self.tableWidget_2.blockSignals(False)
        self.toplamgoster()

    @pyqtSlot()
    def birimdegisti(self,item):
        bb = self.sender().property('row').toInt()[0]
        cc = self.sender().property(item).toInt()[0]
        dd = self.sender().property('old').toInt()[0]
        self.sender().setProperty('old',cc)

        print bb,item,cc ,dd


        self.tableWidget_2.setItem(bb,5,QtGui.QTableWidgetItem(str(float(self.tableWidget_2.item(bb,5).text()  )*(float(cc)/float(dd)))))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    fatura1=Fatura()
    fatura1.goster()
    app.exec_()