# Form implementation generated from reading ui file 'fatura.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog3(object):
    def setupUi(self, Dialog3):
        Dialog3.setObjectName("Dialog3")
        Dialog3.resize(820, 800)
        Dialog3.setMinimumSize(QtCore.QSize(800, 600))
        Dialog3.setMaximumSize(QtCore.QSize(820, 16777215))
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog3)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(Dialog3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog3)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(Dialog3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog3)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(Dialog3)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setLineWidth(1)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(90)
        self.gridLayout.addWidget(self.tableWidget_2, 4, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog3)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Dialog3)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog3)
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog3)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.dateEdit = QtWidgets.QDateEdit(Dialog3)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.label_7 = QtWidgets.QLabel(Dialog3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog3)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_3.addWidget(self.dateEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog3)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(Dialog3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/nenra.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog3)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 4, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(120, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.comboBox = QtWidgets.QComboBox(Dialog3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(120, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog3)
        self.tableWidget.setMaximumSize(QtCore.QSize(21700, 150))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.horizontalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog3)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 660)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog3)
        self.pushButton_2.clicked.connect(Dialog3.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog3)
        Dialog3.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog3.setTabOrder(self.lineEdit_2, self.dateEdit)
        Dialog3.setTabOrder(self.dateEdit, self.lineEdit_4)
        Dialog3.setTabOrder(self.lineEdit_4, self.lineEdit_3)
        Dialog3.setTabOrder(self.lineEdit_3, self.dateEdit_2)
        Dialog3.setTabOrder(self.dateEdit_2, self.tableWidget_2)
        Dialog3.setTabOrder(self.tableWidget_2, self.pushButton_2)
        Dialog3.setTabOrder(self.pushButton_2, self.pushButton)
        Dialog3.setTabOrder(self.pushButton, self.pushButton_4)
        Dialog3.setTabOrder(self.pushButton_4, self.pushButton_3)
        Dialog3.setTabOrder(self.pushButton_3, self.lineEdit_5)
        Dialog3.setTabOrder(self.lineEdit_5, self.pushButton_5)
        Dialog3.setTabOrder(self.pushButton_5, self.comboBox)
        Dialog3.setTabOrder(self.comboBox, self.tableWidget)

    def retranslateUi(self, Dialog3):
        _translate = QtCore.QCoreApplication.translate
        Dialog3.setWindowTitle(_translate("Dialog3", "Fiş Girişi"))
        self.label_2.setText(_translate("Dialog3", "Cari "))
        self.label_8.setText(_translate("Dialog3", "Gün"))
        self.label_4.setText(_translate("Dialog3", "Ara"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog3", "Ürün Kodu"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog3", "Ürün Açıklama"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog3", "Birim"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog3", "KDV"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog3", "Miktar"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog3", "Birim Fiyat"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Dialog3", "Toplam"))
        self.pushButton_4.setText(_translate("Dialog3", "Fiş Sil"))
        self.label.setText(_translate("Dialog3", "Seri/Sıra"))
        self.label_7.setText(_translate("Dialog3", "Vade"))
        self.pushButton_3.setText(_translate("Dialog3", "Satır Sil"))
        self.pushButton.setText(_translate("Dialog3", "Kaydet"))
        self.pushButton_2.setText(_translate("Dialog3", "İptal"))
        self.pushButton_5.setText(_translate("Dialog3", "Fiş Getir"))
        self.comboBox.setItemText(0, _translate("Dialog3", "ÖDEME YAP"))
        self.comboBox.setItemText(1, _translate("Dialog3", "Nakit Ödeme"))
        self.comboBox.setItemText(2, _translate("Dialog3", "Denizbank "))
        self.comboBox.setItemText(3, _translate("Dialog3", "Yapı Kredi"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog3", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog3", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog3", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog3", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog3", "New Column"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog3 = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()
    sys.exit(app.exec())
