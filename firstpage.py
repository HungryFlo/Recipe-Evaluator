# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_firstpage(object):
    def setupUi(self, firstpage):
        firstpage.setObjectName("firstpage")
        firstpage.resize(400, 240)
        firstpage.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        firstpage.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(firstpage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QtWidgets.QLabel(firstpage)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(28)
        self.name_label.setFont(font)
        self.name_label.setTextFormat(QtCore.Qt.PlainText)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.slogan_label = QtWidgets.QLabel(firstpage)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.slogan_label.setFont(font)
        self.slogan_label.setObjectName("slogan_label")
        self.verticalLayout.addWidget(self.slogan_label)
        self.newRecipe_Button = QtWidgets.QPushButton(firstpage)
        self.newRecipe_Button.setObjectName("newRecipe_Button")
        self.verticalLayout.addWidget(self.newRecipe_Button)
        self.Browse_Button = QtWidgets.QPushButton(firstpage)
        self.Browse_Button.setObjectName("Browse_Button")
        self.verticalLayout.addWidget(self.Browse_Button)

        self.retranslateUi(firstpage)
        QtCore.QMetaObject.connectSlotsByName(firstpage)

    def retranslateUi(self, firstpage):
        _translate = QtCore.QCoreApplication.translate
        firstpage.setWindowTitle(_translate("firstpage", "膳食助手"))
        self.name_label.setText(_translate("firstpage", "膳食助手"))
        self.slogan_label.setText(_translate("firstpage", "均衡营养，健康生活。"))
        self.newRecipe_Button.setText(_translate("firstpage", "新建食谱"))
        self.Browse_Button.setText(_translate("firstpage", "膳食指南"))
