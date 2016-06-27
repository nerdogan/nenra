# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recete2.ui'
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

class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName(_fromUtf8("Dialog2"))
        Dialog2.resize(674, 586)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("nenra.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog2.setWindowIcon(icon)
        Dialog2.setStyleSheet(_fromUtf8(""))
        self.lineEdit = QtGui.QLineEdit(Dialog2)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 191, 20))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 251, 202);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tableWidget = QtGui.QTableWidget(Dialog2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 471, 181))
        self.tableWidget.setStyleSheet(_fromUtf8(";"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2 = QtGui.QTableWidget(Dialog2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 250, 471, 301))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.label = QtGui.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(240, 10, 391, 21))
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
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../../muhasebe-2/Pictures/Adsız.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog2)
        self.pushButton.setGeometry(QtCore.QRect(500, 370, 121, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog2)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 440, 121, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(500, 320, 71, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_3 = QtGui.QPushButton(Dialog2)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 250, 121, 41))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setStyleSheet(_fromUtf8("background =rgb(255, 16, 60)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.comboBox = QtGui.QComboBox(Dialog2)
        self.comboBox.setGeometry(QtCore.QRect(500, 160, 161, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(Dialog2)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog2.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        Dialog2.setWindowTitle(_translate("Dialog2", "Reçete", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog2", "KOD", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog2", "AÇIKLAMA", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog2", "BİRİM", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog2", "N", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog2", "KOD", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog2", "AÇIKLAMA", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog2", "BİRİM", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog2", "MİKTAR", None))
        self.label.setText(_translate("Dialog2", "TextLabel", None))
        self.pushButton.setText(_translate("Dialog2", "Kaydet", None))
        self.pushButton_2.setText(_translate("Dialog2", "İptal", None))
        self.label_3.setText(_translate("Dialog2", "TextLabel", None))
        self.pushButton_3.setText(_translate("Dialog2", "Satır Sil", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog2 = QtGui.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())

