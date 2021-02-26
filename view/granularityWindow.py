# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow.ui'
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
        self.granulartiyLabelSW = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.granulartiyLabelSW.setFont(font)
        self.granulartiyLabelSW.setObjectName("granulartiyLabelSW")
        self.horizontalLayout_2.addWidget(self.granulartiyLabelSW)
        self.granularitySpinBoxSW = QtWidgets.QSpinBox(Dialog)
        self.granularitySpinBoxSW.setMinimum(1)
        self.granularitySpinBoxSW.setMaximum(100)
        self.granularitySpinBoxSW.setObjectName("granularitySpinBoxSW")
        self.horizontalLayout_2.addWidget(self.granularitySpinBoxSW)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.granulartiyLabelSW.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Only exports days that are multiples of the selected value</span></p></body></html>"))
        self.granulartiyLabelSW.setText(_translate("Dialog", "Select a granularity for the export:"))
        self.pushButton.setText(_translate("Dialog", "Confirm"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
