# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hyperlinkEditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hyperlinkEditor(object):
    def setupUi(self, hyperlinkEditor):
        hyperlinkEditor.setObjectName("hyperlinkEditor")
        hyperlinkEditor.resize(427, 132)
        self.centralwidget = QtWidgets.QWidget(hyperlinkEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(160, 80, 101, 28))
        self.create.setObjectName("create")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(20, 10, 55, 16))
        self.name.setObjectName("name")
        self.text = QtWidgets.QLineEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(70, 10, 341, 22))
        self.text.setObjectName("text")
        self.name_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_2.setGeometry(QtCore.QRect(10, 40, 55, 16))
        self.name_2.setObjectName("name_2")
        self.hyperlink = QtWidgets.QLineEdit(self.centralwidget)
        self.hyperlink.setGeometry(QtCore.QRect(70, 40, 341, 22))
        self.hyperlink.setObjectName("hyperlink")
        hyperlinkEditor.setCentralWidget(self.centralwidget)

        self.retranslateUi(hyperlinkEditor)
        QtCore.QMetaObject.connectSlotsByName(hyperlinkEditor)

    def retranslateUi(self, hyperlinkEditor):
        _translate = QtCore.QCoreApplication.translate
        hyperlinkEditor.setWindowTitle(_translate("hyperlinkEditor", "Hyperlink Editor"))
        self.create.setText(_translate("hyperlinkEditor", "Create"))
        self.name.setText(_translate("hyperlinkEditor", "Text:"))
        self.name_2.setText(_translate("hyperlinkEditor", "Hyperlink"))
