# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stok.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog6(object):
    def setupUi(self, Dialog6):
        Dialog6.setObjectName("Dialog6")
        Dialog6.resize(1000, 600)
        font = QtGui.QFont()
        font.setFamily(".Noto Sans Universal")
        Dialog6.setFont(font)
        self.dateEdit = QtWidgets.QDateEdit(Dialog6)
        self.dateEdit.setGeometry(QtCore.QRect(20, 40, 151, 41))
        font = QtGui.QFont()
        font.setFamily(".Noto Sans Universal")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog6)
        self.dateEdit_2.setGeometry(QtCore.QRect(20, 130, 151, 41))
        font = QtGui.QFont()
        font.setFamily(".Noto Sans Universal")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label = QtWidgets.QLabel(Dialog6)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily(".Noto Sans Universal")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog6)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 141, 16))
        font = QtGui.QFont()
        font.setFamily(".Noto Sans Universal")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog6)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 161, 51))
        font = QtGui.QFont()
        font.setFamily(".Noto Sans Universal")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog6)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 450, 61, 51))
        font = QtGui.QFont()
        font.setFamily(".Noto Sans Universal")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog6)
        self.tableWidget.setGeometry(QtCore.QRect(180, 10, 801, 581))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog6)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 450, 61, 51))
        font = QtGui.QFont()
        font.setFamily(".Noto Sans Universal")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog6)
        QtCore.QMetaObject.connectSlotsByName(Dialog6)

    def retranslateUi(self, Dialog6):
        _translate = QtCore.QCoreApplication.translate
        Dialog6.setWindowTitle(_translate("Dialog6", "STOK"))
        self.label.setText(_translate("Dialog6", "Başlama Tarihi"))
        self.label_2.setText(_translate("Dialog6", "Bitiş Tarihi"))
        self.pushButton.setText(_translate("Dialog6", "Listele"))
        self.pushButton_2.setText(_translate("Dialog6", "PDF"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog6", "."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog6", "."))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog6", "."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog6", "."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog6", "."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog6", "."))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog6", "."))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog6", "."))
        self.pushButton_3.setText(_translate("Dialog6", "XLS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog6 = QtWidgets.QDialog()
    ui = Ui_Dialog6()
    ui.setupUi(Dialog6)
    Dialog6.show()
    sys.exit(app.exec_())
