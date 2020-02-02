#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Admin.Sources import user_json
from PyQt5 import QtCore, QtWidgets


class LogIn(object):
    def __init__(self):
        self.accounts = user_json.accounts()
        self.passwords = user_json.passwords()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 80, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close | QtWidgets.QDialogButtonBox.Help | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 281, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")

        for i in self.accounts:
            self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        self.retranslateUi(Dialog)

        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "外包管理系统 - 管理员登录"))
        self.label.setText(_translate("Dialog", "Admin"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.comboBox.setCurrentText(_translate("Dialog", self.accounts[0]))
        for i in range(len(self.accounts)):
            self.comboBox.setItemText(i, _translate("Dialog", self.accounts[i]))