# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rapor.ui'
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

class Ui_Dialog7(object):
    def setupUi(self, Dialog7):
        Dialog7.setObjectName(_fromUtf8("Dialog7"))
        Dialog7.resize(889, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("nenra.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog7.setWindowIcon(icon)
        self.dateEdit = QtGui.QDateEdit(Dialog7)
        self.dateEdit.setGeometry(QtCore.QRect(20, 40, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit_2 = QtGui.QDateEdit(Dialog7)
        self.dateEdit_2.setGeometry(QtCore.QRect(20, 130, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.label = QtGui.QLabel(Dialog7)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog7)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog7)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog7)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 450, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tableWidget = QtGui.QTableWidget(Dialog7)
        self.tableWidget.setGeometry(QtCore.QRect(180, 10, 681, 581))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
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
        self.pushButton_3 = QtGui.QPushButton(Dialog7)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 450, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog7)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 260, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog7)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 370, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.retranslateUi(Dialog7)
        QtCore.QMetaObject.connectSlotsByName(Dialog7)

    def retranslateUi(self, Dialog7):
        Dialog7.setWindowTitle(_translate("Dialog7", "KASA RAPOR", None))
        self.label.setText(_translate("Dialog7", "Başlama Tarihi", None))
        self.label_2.setText(_translate("Dialog7", "Bitiş Tarihi", None))
        self.pushButton.setText(_translate("Dialog7", "Ürün Rapor", None))
        self.pushButton_2.setText(_translate("Dialog7", "PDF", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog7", ".", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog7", ".", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog7", ".", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog7", ".", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog7", ".", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog7", ".", None))
        self.pushButton_3.setText(_translate("Dialog7", "XLS", None))
        self.pushButton_4.setText(_translate("Dialog7", "Kasa Rapor", None))
        self.pushButton_5.setText(_translate("Dialog7", "YAZDIR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog7 = QtGui.QDialog()
    ui = Ui_Dialog7()
    ui.setupUi(Dialog7)
    Dialog7.show()
    sys.exit(app.exec_())

