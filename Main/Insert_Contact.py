# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
import Main



class Ui_Dialog(object):
    def __init__(self, sub_item, col_val, comboBoxList):
        self.head_item = sub_item
        self.col_val = col_val
        self.comboBoxList = comboBoxList


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(615, 174)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 110, Main.button_width * 2, Main.button_height))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, Main.table_width, 100))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(self.col_val)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(self.head_item)

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(self.comboBoxList)
        self.tableWidget.setCellWidget(0, 0, self.comboBox)
        self.tableWidget.resizeColumnsToContents()
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加合同"))

