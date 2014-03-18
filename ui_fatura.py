# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fatura.ui'
#
# Created: Tue Mar 18 20:37:38 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName(_fromUtf8("Dialog3"))
        Dialog3.resize(796, 625)
        self.lineEdit = QtGui.QLineEdit(Dialog3)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 61, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog3)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 10, 151, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog3)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 70, 561, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label = QtGui.QLabel(Dialog3)
        self.label.setGeometry(QtCore.QRect(20, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog3)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dateEdit = QtGui.QDateEdit(Dialog3)
        self.dateEdit.setGeometry(QtCore.QRect(470, 10, 110, 22))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.tableWidget = QtGui.QTableWidget(Dialog3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 601, 131))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget_2 = QtGui.QTableWidget(Dialog3)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 240, 601, 391))
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.pushButton = QtGui.QPushButton(Dialog3)
        self.pushButton.setGeometry(QtCore.QRect(620, 570, 75, 23))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog3)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 570, 75, 23))
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Dialog3)
        self.label_3.setGeometry(QtCore.QRect(70, 40, 491, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog3)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog3)
        self.label_5.setGeometry(QtCore.QRect(690, 300, 71, 51))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog3)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog3.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog3)
        Dialog3.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog3.setTabOrder(self.lineEdit_2, self.dateEdit)
        Dialog3.setTabOrder(self.dateEdit, self.lineEdit_3)
        Dialog3.setTabOrder(self.lineEdit_3, self.pushButton)
        Dialog3.setTabOrder(self.pushButton, self.pushButton_2)
        Dialog3.setTabOrder(self.pushButton_2, self.tableWidget)
        Dialog3.setTabOrder(self.tableWidget, self.tableWidget_2)

    def retranslateUi(self, Dialog3):
        Dialog3.setWindowTitle(_translate("Dialog3", "Fatura", None))
        self.label.setText(_translate("Dialog3", "Seri/Sıra", None))
        self.label_2.setText(_translate("Dialog3", "Cari ", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog3", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog3", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog3", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog3", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog3", "New Column", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog3", "Ürün Kodu", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog3", "Ürün Açıklama", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog3", "Birim", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog3", "KDV", None))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog3", "Miktar", None))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog3", "Birim Fiyat", None))
        self.pushButton.setText(_translate("Dialog3", "Kaydet", None))
        self.pushButton_2.setText(_translate("Dialog3", "İptal", None))
        self.label_4.setText(_translate("Dialog3", "Ara", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog3 = QtGui.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec_())

