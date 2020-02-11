#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
import Main, openpyxl
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QDialog, QMessageBox
from Main import Insert_Contact, Analyze, Add_Vendor, Function, Features, Area_Combo
import pandas as pd


class Ui_MainWindow(object):
    def __init__(self):
        self.max_col = 0
        self.head_item = []
        self.vendor_list = []
        self.first_end = []
        self.vendorcontact_counts = []
        self.splitter = []
        self.msg = QMessageBox()
        self.features = Features

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.resize(645, 498)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, Main.button_width, Main.button_height))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 0, Main.button_width, Main.button_height))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 0, Main.button_width, Main.button_height))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, Main.table_width, 850))
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
        self.actionSave.setShortcut("Ctrl+S")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_add_vendor = QtWidgets.QAction(MainWindow)
        self.action_add_vendor.setObjectName("action_add_vendor")
        self.action_add_contact = QtWidgets.QAction(MainWindow)
        self.action_add_contact.setObjectName("action_insert_contact")
        self.action_del_contact = QtWidgets.QAction(MainWindow)
        self.action_del_contact.setObjectName("action_del_contact")
        self.action_function = QtWidgets.QAction(MainWindow)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_add_vendor)
        self.menuEdit.addAction(self.action_add_contact)
        self.menuEdit.addAction(self.action_del_contact)
        self.menuEdit.addAction(self.action_function)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.actionOpen.triggered.connect(self.openfile)
        self.action_add_contact.triggered.connect(self.check_area)  # connect
        self.action_del_contact.triggered.connect(self.del_contact)
        self.action_add_vendor.triggered.connect(self.add_vendor)
        self.action_function.triggered.connect(self.edit_function)
        self.actionSave.triggered.connect(self.save_file)
        self.pushButton.clicked.connect(self.check_area)
        self.pushButton_2.clicked.connect(self.del_contact)
        self.pushButton_3.clicked.connect(self.open_analyze)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "供应商管理系统"))
        self.pushButton.setText(_translate("MainWindow", "增加合同"))
        self.pushButton_2.setText(_translate("MainWindow", "删除合同"))
        self.pushButton_3.setText(_translate("MainWindow", "数据中心"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.action_add_vendor.setText(_translate("MainWindow", "增加供应商"))
        self.action_add_contact.setText(_translate("MainWindow", "增加合同"))
        self.action_del_contact.setText(_translate("MainWindow", "删除合同"))
        self.action_function.setText(_translate("MainWindow", "函数"))

    def openfile(self):  # import vendor excel, Please don't
        excel_file, _ = QFileDialog.getOpenFileName(None,
                                                    'Choose Files',
                                                    'E:\\Test\\',
                                                    'Excel Files (*.xlsx)')
        if excel_file != '':  # Bug: openfile dialog cancel and quit all window
            wb = openpyxl.load_workbook(filename=excel_file)
            ws = wb.active
            self.max_col = ws.max_column
            self.tableWidget.setRowCount(ws.max_row)
            self.tableWidget.setColumnCount(self.max_col)
            for row in ws.iter_rows(max_row=1):
                for cell in row:
                    self.head_item.append(cell.value)
            self.tableWidget.setHorizontalHeaderLabels(self.head_item)  # get excel head item
            for i in range(2, ws.max_row + 1):
                for x in range(1, self.max_col + 1):
                    if ws.cell(i, x).value is None:
                        self.tableWidget.setItem(i - 2, x - 1, QTableWidgetItem(''))
                    elif isinstance(ws.cell(i, x).value, date):
                        ymd = date.isoformat(ws.cell(i, x).value)
                        self.tableWidget.setItem(i - 2, x - 1, QTableWidgetItem(ymd))
                    else:
                        self.tableWidget.setItem(i - 2, x - 1, QTableWidgetItem(str(ws.cell(i, x).value)))

            for merged_cell in ws.merged_cells:
                r1, r2, c1, c2 = merged_cell.min_row, merged_cell.max_row, merged_cell.min_col, merged_cell.max_col
                # print(r1, r2, c1, c2)
                self.vendorcontact_counts.append(r2 - r1 + 1)
                self.tableWidget.setSpan(r1 - 2, c1 - 1, r2 - (r1 - 1), c2)
                self.vendor_list.append(self.tableWidget.item(r1 - 2, c1 - 1).text())
                self.splitter.append(r2)  # every vendor last row
            for row in self.splitter:  # fill background for null space
                for i in range(0, self.max_col):
                    item = QTableWidgetItem('')
                    item.setBackground(QBrush(QColor(128, 128, 128)))
                    self.tableWidget.setItem(row - 1, i, item)
            self.tableWidget.resizeColumnsToContents()  # cell width follow the content length

    def import_file(self):
        pass

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(None,
                                              'SaveFile',
                                              'E:\\Test\\',
                                              'Excel Files (*.xlsx)')
        try:
            if path != '':
                wb = openpyxl.Workbook()
                ws = wb.create_sheet(index=0, title="VendorSystem")
                for head_val in range(self.tableWidget.columnCount()):
                    head = self.tableWidget.horizontalHeaderItem(head_val).text()
                    ws.cell(1, head_val+1, head)
                for row in range(self.tableWidget.rowCount()):
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            ws.cell(row + 2, column + 1, item.text())
                        else:
                            ws.cell(row + 2, column + 1, ' ')
                for i in range(len(self.splitter)):  # merge cell column 1
                    first = self.splitter[i] - self.vendorcontact_counts[i] + 1
                    ws.merge_cells('A%d:A%d' % (first, self.splitter[i]))
                wb.save(path)
        except Exception as e:
            print(e)

    def exit_file(self):
        pass

    def open_analyze(self):
        self.vendor_list = self.reload_vendor_list()
        vendor_dict = self.get_vendor_info()
        a = Analyze.BrowserWindow(vendor_dict, self.vendor_list)
        a.exec()

    def check_area(self):
        self.confirm_area = Area_Combo.Ui_Dialog()
        self.confirm_area.pushButton.clicked.connect(self.add_contact)
        self.confirm_area.exec()

    def add_contact(self):
        frame = QDialog()
        self.area = self.confirm_area.comboBox.currentText()

        self.vendor_list = self.reload_vendor_list()
        filter_vendor = []
        # print(self.area)
        for i in self.vendor_list:
            if self.area in i:
                filter_vendor.append(i)
        # print(filter_vendor)
        if not filter_vendor:
            self.msg.warning(self.msg, '提示', '没有对应地区的供应商', self.msg.Ok)
        else:
            self.insert_dialog = Insert_Contact.Ui_Dialog(self.head_item, self.max_col, filter_vendor)
            self.insert_dialog.setupUi(frame)
            self.insert_dialog.buttonBox.accepted.connect(self.add_contact_ok)
            frame.exec()

    def add_contact_ok(self):
        signal = False
        vendor_val = self.insert_dialog.comboBox.currentIndex()  # Insert_Contact combo box item
        insert_row = self.splitter[vendor_val] - 1
        firstpostion = insert_row - self.vendorcontact_counts[vendor_val]
        self.tableWidget.insertRow(insert_row)
        self.vendorcontact_counts[vendor_val] += 1
        for i in range(vendor_val, len(self.splitter)):  # every splitter need add 1
            self.splitter[i] += 1
        # print(firstpostion, 0, self.vendorcontact_counts[vendor_val] + 1, 1)
        self.tableWidget.setSpan(firstpostion, 0, self.vendorcontact_counts[vendor_val], 1)
        for val in range(1, self.insert_dialog.tableWidget.columnCount()):
            if val == 5:                                                        # 5 is "类型"
                new_content = self.insert_dialog.tableWidget.cellWidget(0, val).currentText()
            else:
                new_content = self.insert_dialog.tableWidget.item(0, val).text()  # what you type in dialog
            if new_content == '':
                signal = True
            self.tableWidget.setItem(insert_row, val, QTableWidgetItem(new_content))
            # print(new_content)
        if signal:
            self.msg.warning(self.msg, '提示', '你有空白未填写', self.msg.Ok)

    def add_vendor(self):
        frame = QDialog()
        self.add_vendor_dialog = Add_Vendor.Ui_Dialog()
        self.add_vendor_dialog.setupUi(frame)
        self.add_vendor_dialog.buttonBox.accepted.connect(self.add_vendor_ok)
        frame.exec()

    def add_vendor_ok(self):
        last_row = self.splitter[-1]
        if self.add_vendor_dialog.lineEdit.text() == '':
            self.msg.warning(self.msg, '提示', '不允许空', self.msg.Ok)
        else:
            self.tableWidget.insertRow(last_row)
            for i in range(self.max_col):
                item = QTableWidgetItem()
                item.setBackground(QBrush(QColor(128, 128, 128)))
                self.tableWidget.setItem(last_row, i, item)
            self.tableWidget.insertRow(last_row)

            _add = self.tableWidget.rowCount() - 2
            new_content = self.add_vendor_dialog.lineEdit.text()  # what you type in dialog
            self.tableWidget.setItem(_add, 0, QTableWidgetItem(new_content))
            self.vendor_list.append(self.add_vendor_dialog.lineEdit.text())
            self.splitter.append(self.tableWidget.rowCount())
            self.vendorcontact_counts.append(1)

    def del_contact(self):
        only_val = []
        for col in range(self.tableWidget.columnCount()):
            if self.tableWidget.horizontalHeaderItem(col).text() == '凭证字号':
                only_val.append(col)
        if self.tableWidget.currentColumn() != only_val[0]:
            self.msg.warning(self.msg, '提示', "'请选择一个'凭证字号'的单元格再删除此行", QMessageBox.Ok)
        else:
            fianl_warning = self.msg.warning(self.msg, '提示', "确定删除此行？", self.msg.Yes | self.msg.No)
            if fianl_warning == self.msg.Yes:
                splitter_item = 0
                selected_row = self.tableWidget.currentRow()
                for x in range(len(self.splitter)):
                    if selected_row < self.splitter[x]:
                        splitter_item = x
                        break
                self.tableWidget.removeRow(selected_row)
                for i in range(splitter_item, len(self.splitter)):  # every splitter need reduce 1
                    self.splitter[i] -= 1
                self.vendorcontact_counts[splitter_item] -= 1
            elif fianl_warning == self.msg.No:
                self.msg.close()

    def edit_function(self):
        frame = QDialog()
        self.function_dialog = Function.Ui_Dialog()
        self.function_dialog.setupUi(frame)
        self.function_dialog.buttonBox.accepted.connect(self.edit_function_ok)
        frame.exec()

    def edit_function_ok(self):
        if self.function_dialog.lineEdit.text() == '':
            self.msg.warning(self.msg, '提示', '没有函数', self.msg.Ok)
        else:
            val = self.function_dialog.lineEdit.text()
            vendor_dict = self.get_vendor_info()
            result_name = self.features.Features(vendor_dict).run_function(val)  # ['平均人天']
            # print(vendor_dict)
            for col in range(self.tableWidget.columnCount()):
                for i in result_name:
                    if self.tableWidget.horizontalHeaderItem(col).text() == i:
                        for row in range(self.tableWidget.rowCount()):
                            item = vendor_dict.at[row, i]
                            if pd.isnull(item):
                                item = ''
                            else:
                                item = round(item, 2)
                                item = str(item)
                            self.tableWidget.setItem(row, col, QTableWidgetItem(item))
            for col in range(self.tableWidget.columnCount()):
                for i in self.splitter:
                    item = QTableWidgetItem('')
                    item.setBackground(QBrush(QColor(128, 128, 128)))
                    self.tableWidget.setItem(i - 1, col, item)

    def get_vendor_info(self):  # 返回pd数据
        self.vendor_list = self.reload_vendor_list()
        # print(self.vendor_list)
        for i in range(len(self.splitter)):
            first = self.splitter[i] - self.vendorcontact_counts[i] - 1
            end = self.splitter[i] - 1
            self.first_end.append([first, end])
        # print(first_end)  # '上海大宁文化传播有限公司'     first_end[0]= [0, 88]
        head_list = {}
        for col in range(self.tableWidget.columnCount()):
            head_name = self.tableWidget.horizontalHeaderItem(col).text()
            _list = []
            for x in range(len(self.vendor_list)):
                for row in range(self.first_end[x][0], self.first_end[x][1]):
                    if col == 0:
                        item = self.vendor_list[x]
                        _list.append(item)
                    else:
                        item = self.tableWidget.item(row, col).text()
                        _list.append(item)
                _list.append('-')  # add line,  same as tablewidget
                head_list.setdefault(head_name, _list)
        pd_data = pd.DataFrame(head_list)
        for i in ['日期', '业务日期', '付款日期']:
            pd_data[i] = pd.to_datetime(pd_data[i], format='%Y-%m-%d', errors='coerce')
        for i in ['不含税金额', '税率', '付款金额', '单价', '单笔支付', '总人天', '平均人天', '个数']:
            pd_data[i] = pd.to_numeric(pd_data[i], errors='coerce')
        # pd_data["单价"] = pd_data["单价"].astype("int", errors='coerce')
        # print(pd_data)
        return pd_data

    def reload_vendor_list(self):
        self.vendor_list = []
        for row in range(self.tableWidget.rowCount()):
            try:
                item = self.tableWidget.item(row, 0).text()
            except Exception as e:
                print(e)
            finally:
                if item != '' and item != ' ':
                    # print(item)
                    self.vendor_list.append(item)
        return self.vendor_list
