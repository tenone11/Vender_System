#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QBrush, QColor
from datetime import date
import openpyxl
from Main import Insert_Contact


class Ui_MainWindow(object):
    def __init__(self):
        self.button_width = 100
        self.button_height = 45
        self.table_width = 2600

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, self.button_width, self.button_height))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 0, self.button_width, self.button_height))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, self.table_width, 1500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionzengjia_waibaoshang = QtWidgets.QAction(MainWindow)
        self.actionzengjia_waibaoshang.setObjectName("actionzengjia_waibaoshang")
        self.action_insert_contact = QtWidgets.QAction(MainWindow)
        self.action_insert_contact.setObjectName("action_insert_contact")
        self.actionshanchu_hetong = QtWidgets.QAction(MainWindow)
        self.actionshanchu_hetong.setObjectName("actionshanchu_hetong")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionzengjia_waibaoshang)
        self.menuEdit.addAction(self.action_insert_contact)
        self.menuEdit.addAction(self.actionshanchu_hetong)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.actionOpen.triggered.connect(self.openfile)
        self.action_insert_contact.triggered.connect(self.insert_contact)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "增加合同"))
        self.pushButton_2.setText(_translate("MainWindow", "删除合同"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionzengjia_waibaoshang.setText(_translate("MainWindow", "zengjia waibaoshang"))
        self.action_insert_contact.setText(_translate("MainWindow", "增加合同"))
        self.actionshanchu_hetong.setText(_translate("MainWindow", "shanchu hetong"))

    def openfile(self):  # import vendor excel, Please don't
        excel_file, _ = QFileDialog.getOpenFileName(None,
                                                    'Choose Files',
                                                    'E:\\Test\\',
                                                    'Excel Files (*.xlsx)')
        wb = openpyxl.load_workbook(filename=excel_file)
        ws = wb.active
        self.tableWidget.setRowCount(ws.max_row)
        self.tableWidget.setColumnCount(ws.max_column)
        head_item = []
        for row in ws.iter_rows(max_row=1):
            for cell in row:
                head_item.append(cell.value)
        self.tableWidget.setHorizontalHeaderLabels(head_item)  # get excel head item
        for i in range(2, ws.max_row + 1):
            for x in range(1, ws.max_column + 1):
                if ws.cell(i, x).value is None:
                    self.tableWidget.setItem(i - 2, x - 1, QTableWidgetItem(' '))
                elif isinstance(ws.cell(i, x).value, date):
                    ymd = date.isoformat(ws.cell(i, x).value)
                    self.tableWidget.setItem(i - 2, x - 1, QTableWidgetItem(ymd))
                else:
                    self.tableWidget.setItem(i - 2, x - 1, QTableWidgetItem(str(ws.cell(i, x).value)))
        fillbg_row = []
        for merged_cell in ws.merged_cells:
            r1, r2, c1, c2 = merged_cell.min_row, merged_cell.max_row, merged_cell.min_col, merged_cell.max_col
            print(r1, c1, r2, c2)
            self.tableWidget.setSpan(r1 - 2, c1 - 1, r2 - (r1 - 1), c2)
            fillbg_row.append(r2)
        for row in fillbg_row:  # fill background for null space
            for i in range(0, ws.max_column):
                item = QTableWidgetItem()
                item.setBackground(QBrush(QColor(128, 128, 128)))
                self.tableWidget.setItem(row - 1, i, item)
        self.tableWidget.resizeColumnsToContents()  # cell width follow the content length

    def import_file(self):
        pass

    def save_file(self):
        pass

    def exit_file(self):
        pass

    def insert_contact(self):
        frame = QtWidgets.QDialog()
        insert_contact = Insert_Contact.Ui_Dialog()
        print("bbbb")
        insert_contact.setupUi(frame)
        frame.exec()

    def add_vendor(self):
        pass













