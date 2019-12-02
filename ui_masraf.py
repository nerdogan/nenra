# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'masraf.ui'
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

class Ui_Masraf(object):
    def setupUi(self, Masraf):
        Masraf.setObjectName(_fromUtf8("Masraf"))
        Masraf.resize(802, 792)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Masraf)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(30, 10, 30, 10)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Masraf)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.dateEdit = QtGui.QDateEdit(Masraf)
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.dateEdit.setFont(font)
        self.dateEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout.addWidget(self.dateEdit)
        self.pushButton_2 = QtGui.QPushButton(Masraf)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtGui.QTableWidget(Masraf)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 182))
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.tableWidget_2 = QtGui.QTableWidget(Masraf)
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setAlternatingRowColors(True)
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
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_3 = QtGui.QPushButton(Masraf)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(120, 80))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.retranslateUi(Masraf)
        QtCore.QMetaObject.connectSlotsByName(Masraf)

    def retranslateUi(self, Masraf):
        Masraf.setWindowTitle(_translate("Masraf", "Masraf", None))
        self.pushButton.setText(_translate("Masraf", "<--", None))
        self.pushButton_2.setText(_translate("Masraf", "-->", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Masraf", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Masraf", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Masraf", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Masraf", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Masraf", "New Column", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Masraf", "New Column", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Masraf", "New Column", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Masraf", "New Column", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Masraf", "New Column", None))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Masraf", "New Column", None))
        self.pushButton_3.setText(_translate("Masraf", "Kaydet", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Masraf = QtGui.QDialog()
    ui = Ui_Masraf()
    ui.setupUi(Masraf)
    Masraf.show()
    sys.exit(app.exec_())

