# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stok.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog6(object):
    def setupUi(self, Dialog6):
        Dialog6.setObjectName(_fromUtf8("Dialog6"))
        Dialog6.resize(1000, 600)
        self.dateEdit = QtGui.QDateEdit(Dialog6)
        self.dateEdit.setGeometry(QtCore.QRect(20, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit_2 = QtGui.QDateEdit(Dialog6)
        self.dateEdit_2.setGeometry(QtCore.QRect(20, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.label = QtGui.QLabel(Dialog6)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog6)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog6)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog6)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 450, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tableWidget = QtGui.QTableWidget(Dialog6)
        self.tableWidget.setGeometry(QtCore.QRect(180, 10, 801, 581))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
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
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton_3 = QtGui.QPushButton(Dialog6)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 450, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Dialog6)
        QtCore.QMetaObject.connectSlotsByName(Dialog6)

    def retranslateUi(self, Dialog6):
        Dialog6.setWindowTitle(_translate("Dialog6", "STOK", None))
        self.label.setText(_translate("Dialog6", "Başlama Tarihi", None))
        self.label_2.setText(_translate("Dialog6", "Bitiş Tarihi", None))
        self.pushButton.setText(_translate("Dialog6", "Listele", None))
        self.pushButton_2.setText(_translate("Dialog6", "PDF", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog6", ".", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog6", ".", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog6", ".", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog6", ".", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog6", ".", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog6", ".", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog6", ".", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog6", ".", None))
        self.pushButton_3.setText(_translate("Dialog6", "XLS", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog6 = QtGui.QDialog()
    ui = Ui_Dialog6()
    ui.setupUi(Dialog6)
    Dialog6.show()
    sys.exit(app.exec_())

