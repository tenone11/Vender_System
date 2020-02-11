from PyQt5 import QtCore, QtWidgets
from Admin.Sources import user_json


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(165, 65)
        self.setWindowTitle("地区确认")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 165, 30))
        self.comboBox.addItems(user_json.area())
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(0, 35, 100, 30))
        self.pushButton.setText('OK')
