# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cari.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog5(object):
    def setupUi(self, Dialog5):
        Dialog5.setObjectName("Dialog5")
        Dialog5.resize(889, 600)
        self.gridLayout = QtWidgets.QGridLayout(Dialog5)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Dialog5)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 10, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(Dialog5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 7, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 9, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
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
        self.gridLayout.addWidget(self.tableWidget, 0, 2, 16, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 15, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 14, 0, 1, 1)

        self.retranslateUi(Dialog5)
        QtCore.QMetaObject.connectSlotsByName(Dialog5)

    def retranslateUi(self, Dialog5):
        _translate = QtCore.QCoreApplication.translate
        Dialog5.setWindowTitle(_translate("Dialog5", "CARİ"))
        self.label.setText(_translate("Dialog5", "Başlama Tarihi"))
        self.checkBox.setText(_translate("Dialog5", "Bakiyesi olmayanları gösterme"))
        self.label_3.setText(_translate("Dialog5", "Firma Adı"))
        self.label_2.setText(_translate("Dialog5", "Bitiş Tarihi"))
        self.pushButton.setText(_translate("Dialog5", "Ekstre"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog5", "."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog5", "."))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog5", "."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog5", "."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog5", "."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog5", "."))
        self.pushButton_3.setText(_translate("Dialog5", "XLS"))
        self.pushButton_2.setText(_translate("Dialog5", "PDF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog5 = QtWidgets.QDialog()
    ui = Ui_Dialog5()
    ui.setupUi(Dialog5)
    Dialog5.show()
    sys.exit(app.exec_())
