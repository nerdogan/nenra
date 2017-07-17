# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cari.ui'
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

class Ui_Dialog5(object):
    def setupUi(self, Dialog5):
        Dialog5.setObjectName(_fromUtf8("Dialog5"))
        Dialog5.resize(889, 600)
        self.dateEdit = QtGui.QDateEdit(Dialog5)
        self.dateEdit.setGeometry(QtCore.QRect(10, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit_2 = QtGui.QDateEdit(Dialog5)
        self.dateEdit_2.setGeometry(QtCore.QRect(10, 220, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.label = QtGui.QLabel(Dialog5)
        self.label.setGeometry(QtCore.QRect(10, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog5)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog5)
        self.pushButton.setGeometry(QtCore.QRect(0, 290, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog5)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 450, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tableWidget = QtGui.QTableWidget(Dialog5)
        self.tableWidget.setGeometry(QtCore.QRect(180, 10, 681, 581))
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
        self.pushButton_3 = QtGui.QPushButton(Dialog5)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 450, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.lineEdit = QtGui.QLineEdit(Dialog5)
        self.lineEdit.setGeometry(QtCore.QRect(12, 49, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_3 = QtGui.QLabel(Dialog5)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox = QtGui.QCheckBox(Dialog5)
        self.checkBox.setGeometry(QtCore.QRect(10, 380, 161, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.retranslateUi(Dialog5)
        QtCore.QMetaObject.connectSlotsByName(Dialog5)

    def retranslateUi(self, Dialog5):
        Dialog5.setWindowTitle(_translate("Dialog5", "CARİ", None))
        self.label.setText(_translate("Dialog5", "Başlama Tarihi", None))
        self.label_2.setText(_translate("Dialog5", "Bitiş Tarihi", None))
        self.pushButton.setText(_translate("Dialog5", "Ekstre", None))
        self.pushButton_2.setText(_translate("Dialog5", "PDF", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog5", ".", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog5", ".", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog5", ".", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog5", ".", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog5", ".", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog5", ".", None))
        self.pushButton_3.setText(_translate("Dialog5", "XLS", None))
        self.label_3.setText(_translate("Dialog5", "Firma Adı", None))
        self.checkBox.setText(_translate("Dialog5", "Bakiyesi olmayanları gösterme", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog5 = QtGui.QDialog()
    ui = Ui_Dialog5()
    ui.setupUi(Dialog5)
    Dialog5.show()
    sys.exit(app.exec_())

