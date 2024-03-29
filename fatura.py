import sys
import re
from hesapmak import Hesap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from ui_fatura import Ui_Dialog3

from mdb.modulemdb import *


class Fatura(QtWidgets.QDialog, Ui_Dialog3):
    acac = pyqtSignal(int)

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.hesapla = Hesap()
        self.hesapla.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.fisno = None
        self.comb = {}
        self.tableWidget_2.setColumnWidth(0, 50)
        self.tableWidget_2.setColumnWidth(1, 200)
        self.tableWidget_2.setColumnWidth(2, 55)
        self.tableWidget_2.setColumnWidth(3, 40)
        self.tableWidget_2.setColumnWidth(4, 75)
        self.tableWidget_2.setColumnWidth(5, 75)
        self.tableWidget_2.setColumnWidth(6, 75)

        self.lineEdit_4.textChanged.connect(self.vadeartir)
        self.pushButton_5.clicked.connect(lambda: self.fisgetir(self.lineEdit_5.text()))

        self.lineEdit_3.textChanged.connect(self.linechange)
        self.lineEdit_2.textChanged.connect(self.slotfaturakont)
        self.lineEdit.textChanged.connect(self.slotfaturakont)
        self.pushButton.clicked.connect(self.slotfaturakaydet)
        self.tableWidget.cellClicked.connect(self.slotfatura)
        self.pushButton_3.clicked.connect(self.slotfaturasatirsil)
        self.pushButton_4.clicked.connect(self.slotfaturasil)
        self.tableWidget_2.itemChanged.connect(self.toplamdegisti)
        self.comboBox.currentIndexChanged.connect(self.odemeyap)
        self.keyPressEvent = (self.keyPressEvent1)

        self.quitSc = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Equal), self)
        self.quitSc.activated.connect(self.slothesapmakgoster)

        self.hamfiyat = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.ALT + QtCore.Qt.Key_H), self)
        self.hamfiyat.activated.connect(self.slothamfiyat)

        # self.connect(self, QtCore.SIGNAL('triggered()'), self.closeEvent)
        #  self.connect(QtWidgets.QShortcut(QtWidgets.QKeySequence(QtCore.Qt.Key_Equal), self.tableWidget_2),
        #                     QtCore.SIGNAL('activated()'), self.slothesapmakgoster)

        #        self.connect(self.hesapla, QtCore.SIGNAL("acac"), self.slotitemyaz)
        self.hesapla.acac.connect(self.slotitemyaz)

    def keyPressEvent1(self, e):
        print(e.key())
        if e.key() == 16777220:
            self.tabyap()
            return
        elif e.key() == 16777221:
            self.tabyap()
            return
        else:
            print("hiçbiri")

    def tabyap(self):
        elma = self.tableWidget_2.currentRow()
        elma1 = self.tableWidget_2.currentColumn()
        elma2 = self.tableWidget_2.rowCount()
        print(elma, elma1, elma2)
        if ((elma2 - elma) == 1) and (elma1 == 6):
            print("sjkfjskfjskf")
            self.lineEdit_4.setFocus()
            # abc = QKeyEvent(QEvent.KeyPress, Qt.Key_Tab, Qt.NoModifier)
            # QCoreApplication.postEvent(self, abc)

        else:
            print("atla")
            self.tableWidget_2.focusNextChild()

    def closeEvent(self, event):
        print("Closing")
        self.myddb.kapat()

    def kontrol(self, girdi):
        girdi = str(girdi)
        ara = re.search(",", girdi)
        if ara:
            derle = re.compile(",")
            cikti = derle.sub(".", girdi)
            return cikti
        return girdi

    def addcomb(self, row, col):
        # if self.old_row >= 0:
        #    self.table.setCellWidget(self.old_row, self.old_col, None)
        self.old_row = row
        self.old_col = col

        comb1 = QtWidgets.QComboBox()
        self.comb[row] = comb1

        self.tableWidget_2.setCellWidget(row, col, self.comb[row])

    def goster(self):
        print("fatura arayüzü açıldı")
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
        self.lineEdit.setFocus()

    @pyqtSlot( 'QString')
    def vadeartir(self, item2):
        if len(item2) > 0:
            some_date = self.dateEdit.date()
            try:
                self.dateEdit_2.setDate(some_date.addDays(int(item2)))
            except:
                self.dateEdit_2.setDate(some_date.addDays(0))

    @pyqtSlot(int)
    def odemeyap(self, item2):
        elma = self.toplam
        elma1 = self.cari
        some_date = self.dateEdit.date()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit.setText("TED")
        self.dateEdit.setDate(some_date)

        self.linechange((elma1))

        self.slotfatura(0, 0)

        if self.comboBox.currentIndex() == 1:
            self.linechange(("NAKIT"))
        elif self.comboBox.currentIndex() == 2:
            self.linechange(("DENIZBANK"))
        elif self.comboBox.currentIndex() == 3:
            self.linechange(("YKB"))
        self.slotfatura(0, 0)
        self.tableWidget_2.setItem(0, 4, QtWidgets.QTableWidgetItem("-1"))
        self.tableWidget_2.setItem(0, 5, QtWidgets.QTableWidgetItem(elma))
        self.comboBox.blockSignals(True)
        self.comboBox.setCurrentIndex(0)
        self.comboBox.blockSignals(False)

    @pyqtSlot(int, str)
    def fisgetir(self, item2):
        print(item2, "elmaarmut kelmahmut")
        self.comboBox.blockSignals(True)
        self.comboBox.setCurrentIndex(0)
        self.comboBox.blockSignals(False)
        self.lineEdit.setText("")

        sql = "select serino,sirano from cari_har where  fisno='" + str(item2) + "'"
        try:
            print(self.myddb.conn.sqlstate())
            sonuc = self.myddb.cek(sql)
        except self.myddb.cur.OperationalError:
            self.myddb = Myddb()
            sonuc = self.myddb.cek(sql)

        if len(sonuc) == 0:
            print("fis yok")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.label_6.setText("")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle(("Fiş Bulunamadı"))
            msg.setIcon(QtWidgets.QMessageBox.Critical)

            msg.setText(("Bu numarada bir fiş bulunamadı !!!"))
            msg.setInformativeText((" Bu fiş yok"))
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()


        else:
            self.lineEdit.setText(str(sonuc[0][0]))
            self.lineEdit_2.setText(str(sonuc[0][1]))

    @pyqtSlot('QString')
    def linechange(self, item2):

        a = item2
        a = str(a)

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
            self.tableWidget.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            item = row1[2]
            self.tableWidget.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            item = row1[3]
            self.tableWidget.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
            item = str(row1[4])
            self.tableWidget.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
            item = str(row1[6])
            self.tableWidget.setItem(aa, 4, QtWidgets.QTableWidgetItem(item))
            aa = aa + 1

        if (aa == 1 and self.label_5.text() == "4"):
            self.slotfatura(0, 0)
            self.lineEdit_3.setText("")
            self.tableWidget_2.scrollToBottom()

    @pyqtSlot()
    def slotfaturakont(self):
        self.fisno = None
        self.label_5.setText("")

        deger5 = self.lineEdit.text()
        deger6 = self.lineEdit_2.text()
        sql = "select * from cari_har where  serino='" + str(deger5) + "' and sirano='" + str(deger6) + "'"
        sonuc = self.myddb.cek(sql)
        self.myddb.conn.commit()
        self.label_3.setText("")
        self.tableWidget_2.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        # some_date = QtCore.QDate(2011,4,22)
        some_date = QtCore.QDate.currentDate()
        self.dateEdit.setDate(some_date)
        # tediye fişi ted olunca otomatik sıra numarası veriyor
        if (
                deger5 == "ted" or deger5 == "TED" or deger5 == "ZZ" or deger5 == "say" or deger5 == "SAY" or deger5 == "MAS") and deger6 == "":
            maxbelgeno = self.myddb.cek("select  max(sirano) from cari_har where serino='" + str(deger5) + "' ")
            self.myddb.conn.commit()
            deger6 = str(maxbelgeno[0][0] + 1)
            self.lineEdit_2.setText(deger6)

        if len(sonuc) > 0:
            dt = sonuc[0][6]
            dt1 = sonuc[0][9]

            # QtWidgets.QMessageBox.information(self.tableWidget,
            #						"QTableWidget Cell Click",
            #						"Text: " + str(dt.year))
            print(sonuc)
            self.tableWidget_2.blockSignals(True)
            for item3 in sonuc:
                self.dateEdit.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
                self.dateEdit_2.setDate(QtCore.QDate(dt1.year, dt1.month, dt1.day))
                self.lineEdit_4.setText(str((dt1 - dt).days))
                sonuc1 = self.myddb.cek2(item3[1], "cari", "cariid")
                for item2 in sonuc1:
                    self.label_5.setText(str(item2[1]))

                    deger0 = str(item2[1]) + " " + item2[2] + " " + item2[3]
                    self.cari = item2[3]
                    self.label_3.setText(deger0)
                    bul1 = str(item3[0])

                bul2 = self.myddb.cek2(item3[3], "cariay", "fisno")
                self.myddb.conn.commit()
                self.fisno = item3[3]
                print(self.fisno, "ahada bu")
                self.setWindowTitle(("Fiş Girişi " + str(self.fisno)))

                i = len(bul2)
                j = 6
                self.tableWidget_2.setRowCount(i)

                aa = 0
                toplam = 0
                for row1 in bul2:
                    item = str(row1[4])
                    self.tableWidget_2.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
                    elma = item
                    bul3 = self.myddb.cek2(elma, "hammadde", "hamkod")
                    item = bul3[0][2]
                    if row1[10] is not None:
                        item = (row1[10])
                    self.tableWidget_2.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
                    item = bul3[0][3]
                    self.tableWidget_2.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))
                    self.addcomb(aa, 2)
                    self.comb[aa].setProperty("row", aa)
                    self.comb[aa].setProperty("old", 1)
                    self.myddb.cur.execute("select birim,katsayi from birim where hamkod=%s order by katsayi", [elma])
                    bul4 = self.myddb.cur.fetchall()
                    for satirr in bul4:
                        self.comb[aa].addItem(satirr[0])
                        self.comb[aa].setProperty(satirr[0], satirr[1])

                    self.comb[aa].currentTextChanged.connect(self.birimdegisti)

         # self.connect(self.comb[aa], QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.birimdegisti)

                    item = str(row1[7])
                    self.tableWidget_2.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
                    item = str(row1[5])
                    self.tableWidget_2.setItem(aa, 4, QtWidgets.QTableWidgetItem(item))
                    item = str(row1[6])
                    item = QtWidgets.QTableWidgetItem(item)
                    if self.label_5.text() == "100":
                        item.setFlags(QtCore.Qt.ItemIsEditable)
                    self.tableWidget_2.setItem(aa, 5, item)
                    item = str("{:.2f}".format((row1[6] * row1[5])))
                    item = QtWidgets.QTableWidgetItem(item)
                    item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
                    if self.label_5.text() == "100":
                        item.setFlags(Qt.ItemFlag.ItemIsEditable)

                    self.tableWidget_2.setItem(aa, 6, QtWidgets.QTableWidgetItem(item))
                    aa = aa + 1

            self.lineEdit_3.setFocus()

            self.tableWidget_2.blockSignals(False)
            self.toplamgoster()

            return

    @pyqtSlot(int, int)
    def slotfatura(self, item, item2):
        #   cari listesinden çiftklikle line edite cari firma bilgisini yazıyor

        if len(self.label_3.text()) < 12:
            deger1 = self.tableWidget.item(item, 0).text()
            deger2 = self.tableWidget.item(item, 1).text()
            deger3 = self.tableWidget.item(item, 2).text()
            deger4 = self.tableWidget.item(item, 3).text()
            self.label_5.setText(deger1)
            self.label_3.setText(deger1 + " " + deger2 + " " + deger3)
            bul1 = str(deger1)
            self.lineEdit_3.setText("")
            self.lineEdit_3.setFocus()
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
            self.tableWidget_2.setItem(aa, 0, QtWidgets.QTableWidgetItem(item))
            item = deger2
            self.tableWidget_2.setItem(aa, 1, QtWidgets.QTableWidgetItem(item))
            item = deger3
            self.tableWidget_2.setItem(aa, 2, QtWidgets.QTableWidgetItem(item))

            self.addcomb(aa, 2)
            self.comb[aa].setProperty("row", aa)
            self.comb[aa].setProperty("old", 1)
            self.myddb.cur.execute("select birim,katsayi from birim where hamkod=%s order by katsayi", [deger1])
            bul4 = self.myddb.cur.fetchall()
            for satirr in bul4:
                self.comb[aa].addItem(satirr[0])
                self.comb[aa].setProperty(satirr[0], satirr[1])

            self.comb[aa].currentTextChanged.connect(self.birimdegisti)

          #  self.connect(self.comb[aa], QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.birimdegisti)

            item = deger4
            self.tableWidget_2.setItem(aa, 3, QtWidgets.QTableWidgetItem(item))
            item = '1'
            self.tableWidget_2.setItem(aa, 4, QtWidgets.QTableWidgetItem(item))
            item = deger5
            item = QtWidgets.QTableWidgetItem(item)
            if self.label_5.text() == "100":
                item.setFlags(QtCore.Qt.ItemIsEditable)

            self.tableWidget_2.setItem(aa, 5, QtWidgets.QTableWidgetItem(item))
            item = deger5
            item = QtWidgets.QTableWidgetItem(item)
            if self.label_5.text() == "100":
                item.setFlags(QtCore.Qt.ItemIsEditable)

            self.tableWidget_2.setItem(aa, 6, QtWidgets.QTableWidgetItem(item))
            self.lineEdit_3.setFocus()
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
        self.myddb.conn.commit()

        if len(sonuc) == 0:
            # print "fatura kaydı yok"
            maxfisno = self.myddb.cek("select max(fisno) from cari_har ")
            self.myddb.conn.commit()

            if maxfisno[0][0] is None:
                maxfisno1 = 0
            else:
                maxfisno1 = maxfisno[0][0]

            if deger0 == "4":
                self.fistipi1 = 90

            elif deger0 == "100":
                self.fistipi1 = 22
            elif deger5 == "TED":
                self.fistipi1 = 11


            else:
                self.fistipi1 = 10

            sql1 = "insert into cari_har (cariid,serino,sirano,tarih,fistipi,fisno,vade) values (%s,%s,%s,%s,%s,%s,%s)"
            #        print sql1
            self.setWindowTitle(("Fiş Girişi " + str(maxfisno1 + 1)))
            self.myddb.cur.execute(sql1, (deger0, deger5, deger6, deger7, self.fistipi1, maxfisno1 + 1, self.deger8))
            self.myddb.conn.commit()

        else:
            #            print " fatura kaydı var"
            self.myddb.sil(sonuc[0][3], "cariay", "fisno")
            #self.myddb.conn.commit()
            # son=self.myddb.cur.execute("select max(caid) from cariay")
            # son1="ALTER TABLE cariay AUTO_INCREMENT ="+str(son)
            # self.myddb.cur.execute(son1)
            # self.myddb.conn.commit()
            satir = 0

        i = self.tableWidget_2.rowCount()
        if i == 0:
            return
        for item in range(i):
            satir += 1

            try:
                cc = (self.comb[item].property(self.comb[item].currentText()))
                if cc is not None:
                    self.tableWidget_2.setItem(item, 4, QtWidgets.QTableWidgetItem(
                        str(float(self.tableWidget_2.item(item, 4).text()) * (float(cc)))))
                    self.tableWidget_2.setItem(item, 5, QtWidgets.QTableWidgetItem(
                        str(float(self.kontrol(self.tableWidget_2.item(item, 5).text())) / (float(cc)))))
            except:
                pass
            deger10 = self.tableWidget_2.item(item, 0).text()
            deger11 = self.tableWidget_2.item(item, 3).text()  # kdv
            deger12 = self.tableWidget_2.item(item, 4).text()  # miktar
            deger13 = self.tableWidget_2.item(item, 5).text()  # birimfiyat
            deger14 = self.tableWidget_2.item(item, 1).text().upper()

            deger12 = self.kontrol(deger12)
            deger13 = self.kontrol(deger13)
            #            print deger12
            #            print deger13
            toplam += float(deger12) * float(deger13)
            kdv += float(deger11) * float(deger12) * float(deger13) / 100
            #            print deger10 , toplam , kdv
            sql2 = "insert into cariay (fisno,fissatir,fistipi,hamkod,kdv,miktar,birimfiy,tarih,aciklama) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.myddb.cur.execute(sql2, (
                sonuc[0][3], satir, sonuc[0][2], deger10, deger11, deger12, deger13, sonuc[0][6], deger14))

        sql3 = "UPDATE cari_har SET tutar=%s where fisno=%s "
        sql4 = "update cariay targetTable  left join hammadde sourceTable on targetTable.hamkod = sourceTable.hamkod set  targetTable.muhkod = sourceTable.muhkod "
        #        print sql3

        self.myddb.cur.execute(sql3, ((toplam + kdv), sonuc[0][3]))
        self.myddb.conn.commit()
        SQL5 = self.myddb.cur.execute(sql4)
        self.myddb.conn.commit()

        self.acac.emit(SQL5)
        self.label_6.setText("{0}  {1}  {2}".format(str("{0:.2f}".format(toplam)), str("{0:.2f}".format(kdv)),
                                                    str("{0:.2f}".format(toplam + kdv))))
        self.lineEdit_3.setFocus()
        self.slotfaturakont()


    @pyqtSlot()
    def slotfaturasatirsil(self):
        bb = self.tableWidget_2.currentRow()
        self.tableWidget_2.removeRow(bb)
        self.slotfaturakaydet()

    def toplamgoster(self):
        i = self.tableWidget_2.rowCount()
        toplam = 0
        kdv = 0
        for item in range(i):
            deger10 = self.tableWidget_2.item(item, 0).text()
            deger11 = self.tableWidget_2.item(item, 3).text()
            deger12 = self.tableWidget_2.item(item, 4).text()
            deger13 = self.tableWidget_2.item(item, 5).text()
            deger12 = self.kontrol(deger12)

            deger13 = self.kontrol(deger13)
            toplam += float(deger12) * float(deger13)
            kdv += float(deger11) * float(deger12) * float(deger13) / 100
            #            print deger10, toplam, kdv
            self.toplam = "{0:.2f}".format(toplam + kdv)
            self.label_6.setText("{0}  {1}  {2}".format(str("{0:.2f}".format(toplam)), str("{0:.2f}".format(kdv)),
                                                        str("{0:.2f}".format(toplam + kdv))))

    @pyqtSlot()
    def slotfaturasil(self):
        #        print "fiş silme ekran"
        if self.fisno is not None:
            #            print self.fisno
            #           _fromUtf8 = QtCore.QString.fromUtf8
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle(("Fiş Silme"))
            msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)

            msg.setText(("Fiş Siliniyor !!!"))
            msg.setInformativeText((str(self.fisno) + " nolu fiş silmek istediğinizden eminmisiniz ?"))

            msg.setDetailedText(str(self.fisno) + "Siliniyor !!!")
            msg.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            # msg.buttonClicked.connect(msgbtn)

            retval = msg.exec()
            if retval == 1024:
                print("value of pressed message box button:", retval)
                print(self.myddb.sil(self.fisno, "cariay", "fisno"))
                print(self.myddb.sil(self.fisno, "cari_har", "fisno"))
                self.myddb.conn.commit()
                self.tableWidget_2.clearContents()
                self.tableWidget.setRowCount(0)
                self.tableWidget_2.setRowCount(0)

    @pyqtSlot('QTableWidgetItem*')
    def toplamdegisti(self, item):

        self.tableWidget_2.blockSignals(True)

        if item.column() == 6:
            self.tableWidget_2.setItem(item.row(), 5, QtWidgets.QTableWidgetItem(
                str(float(self.kontrol(item.text())) / float(self.tableWidget_2.item(item.row(), 4).text()))))
        if item.column() == 4:
            item1 = QtWidgets.QTableWidgetItem(
                str("{:06.2f}".format(
                    (float(self.kontrol(item.text())) * float(
                        self.kontrol(self.tableWidget_2.item(item.row(), 5).text()))))))
            item1.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)

            self.tableWidget_2.setItem(item.row(), 6, item1)

        if item.column() == 5:
            elma = ("{:06.2f}".format(
                (float(self.kontrol(item.text())) * float(self.tableWidget_2.item(item.row(), 4).text()))))
            #    print elma
            self.tableWidget_2.setItem(item.row(), 6, QtWidgets.QTableWidgetItem(elma))
        self.tableWidget_2.blockSignals(False)
        self.toplamgoster()

    @pyqtSlot('QString')
    def birimdegisti(self, item):
        bb = self.sender().property('row')
        cc = self.sender().property(item)
        dd = self.sender().property('old')
        self.sender().setProperty('old', cc)

        print("satır", bb, "birim", item, cc, dd)

        self.tableWidget_2.setItem(bb, 4, QtWidgets.QTableWidgetItem(
            str(float(self.tableWidget_2.item(bb, 4).text()) / (float(cc) / float(dd)))))
        self.tableWidget_2.setItem(bb, 5, QtWidgets.QTableWidgetItem(
            str(float(self.tableWidget_2.item(bb, 5).text()) * (float(cc) / float(dd)))))

    @pyqtSlot()
    def slothamfiyat(self):
        ahammadde = self.tableWidget_2.currentRow()
        sql3 = "UPDATE hammadde SET fiyat1=%s where hamkod=%s "
        print(ahammadde)
        # if ahammadde<0:

        self.myddb.cur.execute(sql3, (
        self.tableWidget_2.item(ahammadde, 5).text(), self.tableWidget_2.item(ahammadde, 0).text()))
        self.myddb.conn.commit()
        sql3 = "select tarih,fisno,birimfiy from cariay where hamkod=%s order by tarih"
        self.myddb.cur.execute(sql3, (self.tableWidget_2.item(ahammadde, 0).text(),))
        elma = self.myddb.cur.fetchall()
        for bul in elma:
            print(bul[0], bul[1], bul[2])

    @pyqtSlot()
    def slothesapmakgoster(self):
        self.hide()
        self.hesapla.goster()
        self.a = self.tableWidget_2.currentRow()
        self.b = self.tableWidget_2.currentColumn()

    @pyqtSlot(str)
    def slotitemyaz(self, sonuc):
        print(sonuc)
        self.show()

        #        print sonuc
        self.tableWidget_2.setItem(self.a, self.b, QtWidgets.QTableWidgetItem(sonuc))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fatura1 = Fatura()
    fatura1.goster()
    app.exec_()
    print("fatura kapandı")
