# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'granularityWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 226)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.granulartiyLabelGW = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.granulartiyLabelGW.setFont(font)
        self.granulartiyLabelGW.setObjectName("granulartiyLabelGW")
        self.horizontalLayout_2.addWidget(self.granulartiyLabelGW)
        self.granularitySpinBoxGW = QtWidgets.QSpinBox(Dialog)
        self.granularitySpinBoxGW.setMinimum(1)
        self.granularitySpinBoxGW.setMaximum(100)
        self.granularitySpinBoxGW.setObjectName("granularitySpinBoxGW")
        self.horizontalLayout_2.addWidget(self.granularitySpinBoxGW)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.confirmButtonGW = QtWidgets.QPushButton(Dialog)
        self.confirmButtonGW.setDefault(True)
        self.confirmButtonGW.setObjectName("confirmButtonGW")
        self.horizontalLayout_3.addWidget(self.confirmButtonGW)
        self.cancelButtonGW = QtWidgets.QPushButton(Dialog)
        self.cancelButtonGW.setObjectName("cancelButtonGW")
        self.horizontalLayout_3.addWidget(self.cancelButtonGW)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.granulartiyLabelGW.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Only exports days that are multiples of the selected value</span></p></body></html>"))
        self.granulartiyLabelGW.setText(_translate("Dialog", "Select a granularity for the export:"))
        self.confirmButtonGW.setText(_translate("Dialog", "Confirm"))
        self.cancelButtonGW.setText(_translate("Dialog", "Cancel"))


