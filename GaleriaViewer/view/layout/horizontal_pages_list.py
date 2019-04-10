# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/layout_ui/horizontal_pages_list.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pagesListScrollArea = QtWidgets.QScrollArea(Form)
        self.pagesListScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pagesListScrollArea.setWidgetResizable(True)
        self.pagesListScrollArea.setObjectName("pagesListScrollArea")
        self.pagesList = QtWidgets.QWidget()
        self.pagesList.setGeometry(QtCore.QRect(0, 0, 398, 298))
        self.pagesList.setObjectName("pagesList")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pagesList)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pagesListScrollArea.setWidget(self.pagesList)
        self.horizontalLayout.addWidget(self.pagesListScrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
