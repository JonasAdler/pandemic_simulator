# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.menuWidget = QtWidgets.QWidget()
        self.menuWidget.setEnabled(True)
        self.menuWidget.setObjectName("menuWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menuWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.menuWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.startSimButton = QtWidgets.QPushButton(self.menuWidget)
        self.startSimButton.setObjectName("startSimButton")
        self.verticalLayout_3.addWidget(self.startSimButton)
        self.stackedWidget.addWidget(self.menuWidget)
        self.simulatorWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulatorWidget.sizePolicy().hasHeightForWidth())
        self.simulatorWidget.setSizePolicy(sizePolicy)
        self.simulatorWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.simulatorWidget.setObjectName("simulatorWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.simulatorWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dataLabel = QtWidgets.QLabel(self.simulatorWidget)
        self.dataLabel.setObjectName("dataLabel")
        self.gridLayout_2.addWidget(self.dataLabel, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.simulatorWidget)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAdjustParamters = QtWidgets.QAction(MainWindow)
        self.actionAdjustParamters.setObjectName("actionAdjustParamters")
        self.actionAdjustParameters = QtWidgets.QAction(MainWindow)
        self.actionAdjustParameters.setObjectName("actionAdjustParameters")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Infection Simulator"))
        self.startSimButton.setText(_translate("MainWindow", "Start Simulation"))
        self.dataLabel.setText(_translate("MainWindow", "TextLabel"))
        self.actionAdjustParamters.setText(_translate("MainWindow", "AdjustParamters"))
        self.actionAdjustParameters.setText(_translate("MainWindow", "AdjustParameters"))
