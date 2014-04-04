# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maliyet.ui'
#
# Created: Fri Apr 04 19:35:45 2014
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

class Ui_Dialog4(object):
    def setupUi(self, Dialog4):
        Dialog4.setObjectName(_fromUtf8("Dialog4"))
        Dialog4.resize(800, 600)
        self.dateEdit = QtGui.QDateEdit(Dialog4)
        self.dateEdit.setGeometry(QtCore.QRect(10, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit_2 = QtGui.QDateEdit(Dialog4)
        self.dateEdit_2.setGeometry(QtCore.QRect(10, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.label = QtGui.QLabel(Dialog4)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog4)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog4)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog4)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 270, 161, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tableWidget = QtGui.QTableWidget(Dialog4)
        self.tableWidget.setGeometry(QtCore.QRect(180, 10, 611, 581))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
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

        self.retranslateUi(Dialog4)
        QtCore.QMetaObject.connectSlotsByName(Dialog4)

    def retranslateUi(self, Dialog4):
        Dialog4.setWindowTitle(_translate("Dialog4", "Maliyet", None))
        self.label.setText(_translate("Dialog4", "Başlama Tarihi", None))
        self.label_2.setText(_translate("Dialog4", "Bitiş Tarihi", None))
        self.pushButton.setText(_translate("Dialog4", "Ürün Maliyet Raporu", None))
        self.pushButton_2.setText(_translate("Dialog4", "PushButton", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog4", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog4", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog4", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog4", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog4", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog4", "New Column", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog4 = QtGui.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi(Dialog4)
    Dialog4.show()
    sys.exit(app.exec_())

