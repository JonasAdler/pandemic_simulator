# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PandemieSimulator_AdlerJonas_skaliert.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1142, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.entitiesSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.entitiesSpinBox.setMinimum(1)
        self.entitiesSpinBox.setMaximum(100)
        self.entitiesSpinBox.setDisplayIntegerBase(10)
        self.entitiesSpinBox.setObjectName("entitiesSpinBox")
        self.horizontalLayout_5.addWidget(self.entitiesSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_15.addWidget(self.label_10)
        self.initiallyInfectedSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.initiallyInfectedSpinBox.setMinimum(1)
        self.initiallyInfectedSpinBox.setMaximum(100)
        self.initiallyInfectedSpinBox.setObjectName("initiallyInfectedSpinBox")
        self.horizontalLayout_15.addWidget(self.initiallyInfectedSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_5.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_5.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_5.addWidget(self.checkBox_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.granularitySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.granularitySpinBox.setMinimum(1)
        self.granularitySpinBox.setObjectName("granularitySpinBox")
        self.horizontalLayout.addWidget(self.granularitySpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.riskOfInfSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.riskOfInfSpinBox.setDecimals(3)
        self.riskOfInfSpinBox.setMaximum(1.0)
        self.riskOfInfSpinBox.setSingleStep(0.01)
        self.riskOfInfSpinBox.setProperty("value", 0.0)
        self.riskOfInfSpinBox.setObjectName("riskOfInfSpinBox")
        self.horizontalLayout_3.addWidget(self.riskOfInfSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.rateOfDeathSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rateOfDeathSpinBox.setDecimals(3)
        self.rateOfDeathSpinBox.setMaximum(1.0)
        self.rateOfDeathSpinBox.setSingleStep(0.01)
        self.rateOfDeathSpinBox.setObjectName("rateOfDeathSpinBox")
        self.horizontalLayout_4.addWidget(self.rateOfDeathSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.rateOfQuarantineSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rateOfQuarantineSpinBox.setPrefix("")
        self.rateOfQuarantineSpinBox.setDecimals(3)
        self.rateOfQuarantineSpinBox.setMaximum(1.0)
        self.rateOfQuarantineSpinBox.setSingleStep(0.001)
        self.rateOfQuarantineSpinBox.setProperty("value", 0.5)
        self.rateOfQuarantineSpinBox.setObjectName("rateOfQuarantineSpinBox")
        self.horizontalLayout_10.addWidget(self.rateOfQuarantineSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.avgInfectionTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.avgInfectionTimeSpinBox.setObjectName("avgInfectionTimeSpinBox")
        self.horizontalLayout_11.addWidget(self.avgInfectionTimeSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        self.avgImmuneTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.avgImmuneTimeSpinBox.setObjectName("avgImmuneTimeSpinBox")
        self.horizontalLayout_14.addWidget(self.avgImmuneTimeSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_13.addWidget(self.graphicsView_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(10, -1, 0, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_12.addWidget(self.graphicsView_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.startSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.startSimButton.setObjectName("startSimButton")
        self.horizontalLayout_8.addWidget(self.startSimButton)
        self.resetSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetSimButton.setObjectName("resetSimButton")
        self.horizontalLayout_8.addWidget(self.resetSimButton)
        self.pauseSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseSimButton.setObjectName("pauseSimButton")
        self.horizontalLayout_8.addWidget(self.pauseSimButton)
        self.resumeSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.resumeSimButton.setEnabled(True)
        self.resumeSimButton.setObjectName("resumeSimButton")
        self.horizontalLayout_8.addWidget(self.resumeSimButton)
        self.exportCsvButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportCsvButton.setObjectName("exportCsvButton")
        self.horizontalLayout_8.addWidget(self.exportCsvButton)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1142, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select amount of entities (1- 100): "))
        self.label_10.setText(_translate("MainWindow", "Select initially infected entities:"))
        self.label_4.setText(_translate("MainWindow", "Select modifier:"))
        self.checkBox.setText(_translate("MainWindow", "Modifier 1"))
        self.checkBox_2.setText(_translate("MainWindow", "Modifier 2"))
        self.checkBox_3.setText(_translate("MainWindow", "Modifier 3"))
        self.label_11.setText(_translate("MainWindow", "Select granularity:"))
        self.label_2.setText(_translate("MainWindow", "Select risk of infection: "))
        self.label_3.setText(_translate("MainWindow", "Select rate of death"))
        self.label_7.setText(_translate("MainWindow", "Select percentage of being quarantined:"))
        self.label_8.setText(_translate("MainWindow", "Select average infection-time:"))
        self.label_9.setText(_translate("MainWindow", "Select average immune-time:"))
        self.label_5.setText(_translate("MainWindow", "Simulation"))
        self.label_6.setText(_translate("MainWindow", "Live-Statistics"))
        self.startSimButton.setText(_translate("MainWindow", "Start"))
        self.resetSimButton.setText(_translate("MainWindow", "Reset"))
        self.pauseSimButton.setText(_translate("MainWindow", "Pause"))
        self.resumeSimButton.setText(_translate("MainWindow", "Resume"))
        self.exportCsvButton.setText(_translate("MainWindow", "Export"))