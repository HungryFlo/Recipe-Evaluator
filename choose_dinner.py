# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_dinner.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_choose_dinner(object):
    def setupUi(self, choose_dinner):
        choose_dinner.setObjectName("choose_dinner")
        choose_dinner.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        choose_dinner.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        choose_dinner.setWindowIcon(icon)
        self.dinner_menu_list = QtWidgets.QListWidget(choose_dinner)
        self.dinner_menu_list.setGeometry(QtCore.QRect(10, 10, 381, 581))
        self.dinner_menu_list.setObjectName("dinner_menu_list")
        self.dinner_recipe_list = QtWidgets.QListWidget(choose_dinner)
        self.dinner_recipe_list.setGeometry(QtCore.QRect(410, 10, 381, 391))
        self.dinner_recipe_list.setObjectName("dinner_recipe_list")
        self.label = QtWidgets.QLabel(choose_dinner)
        self.label.setGeometry(QtCore.QRect(390, 420, 401, 121))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.cancel_button = QtWidgets.QPushButton(choose_dinner)
        self.cancel_button.setGeometry(QtCore.QRect(580, 560, 91, 31))
        self.cancel_button.setObjectName("cancel_button")
        self.yes_button = QtWidgets.QPushButton(choose_dinner)
        self.yes_button.setGeometry(QtCore.QRect(690, 560, 91, 31))
        self.yes_button.setObjectName("yes_button")

        self.retranslateUi(choose_dinner)
        QtCore.QMetaObject.connectSlotsByName(choose_dinner)

    def retranslateUi(self, choose_dinner):
        _translate = QtCore.QCoreApplication.translate
        choose_dinner.setWindowTitle(_translate("choose_dinner", "选择晚餐"))
        self.label.setText(_translate("choose_dinner", "双击左侧列表项添加食物\n"
"双击右侧列表项移除食物\n"
"多份食物请多次双击添加"))
        self.cancel_button.setText(_translate("choose_dinner", "取消"))
        self.yes_button.setText(_translate("choose_dinner", "确定"))
