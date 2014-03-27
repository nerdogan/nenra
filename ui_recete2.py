# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recete2.ui'
#
# Created: Thu Mar 27 16:58:48 2014
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

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName(_fromUtf8("Dialog2"))
        Dialog2.resize(813, 638)
        self.lineEdit = QtGui.QLineEdit(Dialog2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tableWidget = QtGui.QTableWidget(Dialog2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 521, 151))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
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
        self.tableWidget_2 = QtGui.QTableWidget(Dialog2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 210, 521, 371))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(5)
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
        self.label = QtGui.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(330, 10, 451, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(530, 50, 251, 191))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/muhasebe-2/Pictures/Adsız.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(630, 360, 71, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog2)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 360, 71, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(550, 360, 71, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog2)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog2.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(_translate("Dialog2", "Reçete", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog2", "1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog2", "ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog2", "KOD", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog2", "AÇIKLAMA", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog2", "BİRİM", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog2", "N", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog2", "ID", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog2", "KOD", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog2", "AÇIKLAMA", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog2", "BİRİM", None))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog2", "MİKTAR", None))
        self.label.setText(_translate("Dialog2", "TextLabel", None))
        self.pushButton.setText(_translate("Dialog2", "Kaydet", None))
        self.pushButton_2.setText(_translate("Dialog2", "İptal", None))
        self.label_3.setText(_translate("Dialog2", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog2 = QtGui.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())

