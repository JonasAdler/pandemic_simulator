# -*- coding: utf-8 -*-
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
# Form implementation generated from reading ui file 'PandemieSimulator_AdlerJonas_skaliert.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 774)
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
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.entitiesSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.entitiesSpinBox.setMinimum(1)
        self.entitiesSpinBox.setMaximum(200)
        self.entitiesSpinBox.setProperty("value", 50)
        self.entitiesSpinBox.setDisplayIntegerBase(10)
        self.entitiesSpinBox.setObjectName("entitiesSpinBox")
        self.horizontalLayout_5.addWidget(self.entitiesSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_15.addWidget(self.label_10)
        self.initiallyInfectedSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.initiallyInfectedSpinBox.setMinimum(1)
        self.initiallyInfectedSpinBox.setMaximum(200)
        self.initiallyInfectedSpinBox.setProperty("value", 5)
        self.initiallyInfectedSpinBox.setObjectName("initiallyInfectedSpinBox")
        self.horizontalLayout_15.addWidget(self.initiallyInfectedSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.deflectEachOtherCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.deflectEachOtherCheckBox.setObjectName("deflectEachOtherCheckBox")
        self.verticalLayout_5.addWidget(self.deflectEachOtherCheckBox)
        self.closureOfSchoolsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.closureOfSchoolsCheckBox.setObjectName("closureOfSchoolsCheckBox")
        self.verticalLayout_5.addWidget(self.closureOfSchoolsCheckBox)
        self.vaccineCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.vaccineCheckBox.setObjectName("vaccineCheckBox")
        self.verticalLayout_5.addWidget(self.vaccineCheckBox)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_9.addWidget(self.label_16)
        self.vaccineDaysSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.vaccineDaysSpinBox.setObjectName("vaccineDaysSpinBox")
        self.horizontalLayout_9.addWidget(self.vaccineDaysSpinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.healthCareOverloadedCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.healthCareOverloadedCheckBox.setObjectName("healthCareOverloadedCheckBox")
        self.verticalLayout_5.addWidget(self.healthCareOverloadedCheckBox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setMouseTracking(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.granularitySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.granularitySpinBox.setMinimum(1)
        self.granularitySpinBox.setMaximum(100)
        self.granularitySpinBox.setObjectName("granularitySpinBox")
        self.horizontalLayout.addWidget(self.granularitySpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.riskOfInfSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.riskOfInfSpinBox.setMaximum(100.0)
        self.riskOfInfSpinBox.setSingleStep(0.1)
        self.riskOfInfSpinBox.setProperty("value", 5.0)
        self.riskOfInfSpinBox.setObjectName("riskOfInfSpinBox")
        self.horizontalLayout_3.addWidget(self.riskOfInfSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.rateOfDeathSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rateOfDeathSpinBox.setMaximum(100.0)
        self.rateOfDeathSpinBox.setSingleStep(0.1)
        self.rateOfDeathSpinBox.setProperty("value", 1.0)
        self.rateOfDeathSpinBox.setObjectName("rateOfDeathSpinBox")
        self.horizontalLayout_4.addWidget(self.rateOfDeathSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.percentageQuarantineSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.percentageQuarantineSpinBox.setDecimals(1)
        self.percentageQuarantineSpinBox.setSingleStep(0.1)
        self.percentageQuarantineSpinBox.setProperty("value", 20.0)
        self.percentageQuarantineSpinBox.setObjectName("percentageQuarantineSpinBox")
        self.horizontalLayout_10.addWidget(self.percentageQuarantineSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.avgInfectionTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.avgInfectionTimeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.avgInfectionTimeSpinBox.setMinimum(1)
        self.avgInfectionTimeSpinBox.setMaximum(60)
        self.avgInfectionTimeSpinBox.setProperty("value", 7)
        self.avgInfectionTimeSpinBox.setObjectName("avgInfectionTimeSpinBox")
        self.horizontalLayout_11.addWidget(self.avgInfectionTimeSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        self.avgImmuneTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.avgImmuneTimeSpinBox.setMinimum(1)
        self.avgImmuneTimeSpinBox.setMaximum(999)
        self.avgImmuneTimeSpinBox.setProperty("value", 10)
        self.avgImmuneTimeSpinBox.setObjectName("avgImmuneTimeSpinBox")
        self.horizontalLayout_14.addWidget(self.avgImmuneTimeSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.infectionRadiusSpinBox = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.infectionRadiusSpinBox.setFont(font)
        self.infectionRadiusSpinBox.setObjectName("infectionRadiusSpinBox")
        self.horizontalLayout_18.addWidget(self.infectionRadiusSpinBox)
        self.infectionRadiusSpinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.infectionRadiusSpinBox_2.setMinimum(1)
        self.infectionRadiusSpinBox_2.setMaximum(100)
        self.infectionRadiusSpinBox_2.setProperty("value", 10)
        self.infectionRadiusSpinBox_2.setObjectName("infectionRadiusSpinBox_2")
        self.horizontalLayout_18.addWidget(self.infectionRadiusSpinBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
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
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.daysPassedLCD = QtWidgets.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.daysPassedLCD.setFont(font)
        self.daysPassedLCD.setLineWidth(1)
        self.daysPassedLCD.setMidLineWidth(0)
        self.daysPassedLCD.setSmallDecimalPoint(False)
        self.daysPassedLCD.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.daysPassedLCD.setObjectName("daysPassedLCD")
        self.horizontalLayout_12.addWidget(self.daysPassedLCD)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_12.addWidget(self.label_14)
        self.percentageInfectedLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.percentageInfectedLCD.setObjectName("percentageInfectedLCD")
        self.horizontalLayout_12.addWidget(self.percentageInfectedLCD)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.speedOfSimSlider = QtWidgets.QSlider(self.centralwidget)
        self.speedOfSimSlider.setMinimum(30)
        self.speedOfSimSlider.setMaximum(240)
        self.speedOfSimSlider.setProperty("value", 60)
        self.speedOfSimSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedOfSimSlider.setInvertedControls(False)
        self.speedOfSimSlider.setObjectName("speedOfSimSlider")
        self.horizontalLayout_16.addWidget(self.speedOfSimSlider)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_16.addWidget(self.label_15)
        self.multiplyLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.multiplyLCD.setInputMethodHints(QtCore.Qt.ImhNone)
        self.multiplyLCD.setSmallDecimalPoint(True)
        self.multiplyLCD.setDigitCount(2)
        self.multiplyLCD.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.multiplyLCD.setProperty("value", 1.0)
        self.multiplyLCD.setProperty("intValue", 1)
        self.multiplyLCD.setObjectName("multiplyLCD")
        self.horizontalLayout_16.addWidget(self.multiplyLCD)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pandemic"))
        self.label.setText(_translate("MainWindow", "Select amount of entities (1- 200): "))
        self.label_10.setText(_translate("MainWindow", "Select initially infected entities:"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic; text-decoration: underline;\">Either &quot;closure of schools &quot;or &quot;particles deflect each other&quot;!</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Select modifier:"))
        self.deflectEachOtherCheckBox.setText(_translate("MainWindow", "Particles deflect each other"))
        self.closureOfSchoolsCheckBox.setText(_translate("MainWindow", "Closure of schools"))
        self.vaccineCheckBox.setText(_translate("MainWindow", "Develop a vaccine"))
        self.label_16.setText(_translate("MainWindow", "Development in days:"))
        self.healthCareOverloadedCheckBox.setText(_translate("MainWindow", "Health care system can fail"))
        self.label_11.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Only exports days that are multiples of the selected value</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Select granularity:"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Risk of infection for a healthy particle for each frame it is in the infection area of an infected particle</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Select risk of infection in percent: "))
        self.label_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">% of dying for an infected particle each day</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Select rate of death in percent:"))
        self.label_7.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">% of being quarantined for an infected particle each day</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Select percentage of being quarantined:"))
        self.label_8.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Randomly selects a time within a deviation of 25% of the selected value</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Select average infectied-time in days:"))
        self.label_9.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Randomly selects a time within a deviation of 25% of the selected value</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Select average immune-time in days:"))
        self.infectionRadiusSpinBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Comparison: Size of a particle is &quot;8&quot;</span></p></body></html>"))
        self.infectionRadiusSpinBox.setText(_translate("MainWindow", "Select infection radius:"))
        self.label_5.setText(_translate("MainWindow", "Simulation"))
        self.label_6.setText(_translate("MainWindow", "Live-Statistics"))
        self.label_13.setText(_translate("MainWindow", "Current Day:"))
        self.label_14.setText(_translate("MainWindow", "Infected:"))
        self.label_12.setText(_translate("MainWindow", "Simulation speed:"))
        self.label_15.setText(_translate("MainWindow", "Multiplier:"))
        self.startSimButton.setText(_translate("MainWindow", "Start"))
        self.resetSimButton.setText(_translate("MainWindow", "Reset"))
        self.pauseSimButton.setText(_translate("MainWindow", "Pause"))
        self.resumeSimButton.setText(_translate("MainWindow", "Resume"))
        self.exportCsvButton.setText(_translate("MainWindow", "Export"))