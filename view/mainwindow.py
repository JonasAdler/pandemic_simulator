# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1242, 901)
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
        self.entitiesLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.entitiesLabel.setFont(font)
        self.entitiesLabel.setObjectName("entitiesLabel")
        self.horizontalLayout_5.addWidget(self.entitiesLabel)
        self.entitiesSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.entitiesSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.entitiesSpinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.entitiesSpinBox.setMinimum(1)
        self.entitiesSpinBox.setMaximum(200)
        self.entitiesSpinBox.setProperty("value", 50)
        self.entitiesSpinBox.setDisplayIntegerBase(10)
        self.entitiesSpinBox.setObjectName("entitiesSpinBox")
        self.horizontalLayout_5.addWidget(self.entitiesSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.initiallyInfectedLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.initiallyInfectedLabel.setFont(font)
        self.initiallyInfectedLabel.setObjectName("initiallyInfectedLabel")
        self.horizontalLayout_15.addWidget(self.initiallyInfectedLabel)
        self.initiallyInfectedSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.initiallyInfectedSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.initiallyInfectedSpinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.initiallyInfectedSpinBox.setMinimum(1)
        self.initiallyInfectedSpinBox.setMaximum(200)
        self.initiallyInfectedSpinBox.setProperty("value", 5)
        self.initiallyInfectedSpinBox.setObjectName("initiallyInfectedSpinBox")
        self.horizontalLayout_15.addWidget(self.initiallyInfectedSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.modifierLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.modifierLabel.setFont(font)
        self.modifierLabel.setObjectName("modifierLabel")
        self.horizontalLayout_6.addWidget(self.modifierLabel)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.deflectEachOtherCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.deflectEachOtherCheckBox.setObjectName("deflectEachOtherCheckBox")
        self.verticalLayout_5.addWidget(self.deflectEachOtherCheckBox)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.socialDistancingLabel = QtWidgets.QLabel(self.centralwidget)
        self.socialDistancingLabel.setObjectName("socialDistancingLabel")
        self.horizontalLayout_19.addWidget(self.socialDistancingLabel)
        self.socialDistancingSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.socialDistancingSpinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.socialDistancingSpinBox.setMaximumSize(QtCore.QSize(60, 20))
        self.socialDistancingSpinBox.setMinimum(0)
        self.socialDistancingSpinBox.setMaximum(8)
        self.socialDistancingSpinBox.setProperty("value", 0)
        self.socialDistancingSpinBox.setObjectName("socialDistancingSpinBox")
        self.horizontalLayout_19.addWidget(self.socialDistancingSpinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_19)
        self.vaccineCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.vaccineCheckBox.setObjectName("vaccineCheckBox")
        self.verticalLayout_5.addWidget(self.vaccineCheckBox)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.vaccineDaysLabel = QtWidgets.QLabel(self.centralwidget)
        self.vaccineDaysLabel.setObjectName("vaccineDaysLabel")
        self.horizontalLayout_9.addWidget(self.vaccineDaysLabel)
        self.vaccineDaysSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.vaccineDaysSpinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.vaccineDaysSpinBox.setMaximumSize(QtCore.QSize(60, 20))
        self.vaccineDaysSpinBox.setMinimum(1)
        self.vaccineDaysSpinBox.setMaximum(365)
        self.vaccineDaysSpinBox.setProperty("value", 15)
        self.vaccineDaysSpinBox.setObjectName("vaccineDaysSpinBox")
        self.horizontalLayout_9.addWidget(self.vaccineDaysSpinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.healthCareOverloadedCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.healthCareOverloadedCheckBox.setObjectName("healthCareOverloadedCheckBox")
        self.verticalLayout_5.addWidget(self.healthCareOverloadedCheckBox)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.capacityLabel = QtWidgets.QLabel(self.centralwidget)
        self.capacityLabel.setObjectName("capacityLabel")
        self.horizontalLayout_20.addWidget(self.capacityLabel)
        self.healthCareCapacitySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.healthCareCapacitySpinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.healthCareCapacitySpinBox.setMaximumSize(QtCore.QSize(60, 20))
        self.healthCareCapacitySpinBox.setMaximum(100)
        self.healthCareCapacitySpinBox.setProperty("value", 35)
        self.healthCareCapacitySpinBox.setObjectName("healthCareCapacitySpinBox")
        self.horizontalLayout_20.addWidget(self.healthCareCapacitySpinBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.deathRateMultiplierLabel = QtWidgets.QLabel(self.centralwidget)
        self.deathRateMultiplierLabel.setObjectName("deathRateMultiplierLabel")
        self.horizontalLayout_21.addWidget(self.deathRateMultiplierLabel)
        self.deathRateMultiplierSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.deathRateMultiplierSpinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.deathRateMultiplierSpinBox.setMaximumSize(QtCore.QSize(60, 20))
        self.deathRateMultiplierSpinBox.setMinimum(1.0)
        self.deathRateMultiplierSpinBox.setMaximum(3.0)
        self.deathRateMultiplierSpinBox.setSingleStep(0.1)
        self.deathRateMultiplierSpinBox.setProperty("value", 1.5)
        self.deathRateMultiplierSpinBox.setObjectName("deathRateMultiplierSpinBox")
        self.horizontalLayout_21.addWidget(self.deathRateMultiplierSpinBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_21)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.riskOfInfectionLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.riskOfInfectionLabel.setFont(font)
        self.riskOfInfectionLabel.setObjectName("riskOfInfectionLabel")
        self.horizontalLayout_3.addWidget(self.riskOfInfectionLabel)
        self.riskOfInfSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.riskOfInfSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.riskOfInfSpinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.riskOfInfSpinBox.setMaximum(100.0)
        self.riskOfInfSpinBox.setSingleStep(0.1)
        self.riskOfInfSpinBox.setProperty("value", 10.0)
        self.riskOfInfSpinBox.setObjectName("riskOfInfSpinBox")
        self.horizontalLayout_3.addWidget(self.riskOfInfSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rateOfDeathLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rateOfDeathLabel.setFont(font)
        self.rateOfDeathLabel.setObjectName("rateOfDeathLabel")
        self.horizontalLayout_4.addWidget(self.rateOfDeathLabel)
        self.rateOfDeathSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.rateOfDeathSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.rateOfDeathSpinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.rateOfDeathSpinBox.setMaximum(100.0)
        self.rateOfDeathSpinBox.setSingleStep(0.1)
        self.rateOfDeathSpinBox.setProperty("value", 1.0)
        self.rateOfDeathSpinBox.setObjectName("rateOfDeathSpinBox")
        self.horizontalLayout_4.addWidget(self.rateOfDeathSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.percentageOfQuarantineLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.percentageOfQuarantineLabel.setFont(font)
        self.percentageOfQuarantineLabel.setObjectName("percentageOfQuarantineLabel")
        self.horizontalLayout_10.addWidget(self.percentageOfQuarantineLabel)
        self.percentageQuarantineSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.percentageQuarantineSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.percentageQuarantineSpinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.percentageQuarantineSpinBox.setDecimals(1)
        self.percentageQuarantineSpinBox.setSingleStep(0.1)
        self.percentageQuarantineSpinBox.setProperty("value", 10.0)
        self.percentageQuarantineSpinBox.setObjectName("percentageQuarantineSpinBox")
        self.horizontalLayout_10.addWidget(self.percentageQuarantineSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.avgInfectionTimeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.avgInfectionTimeLabel.setFont(font)
        self.avgInfectionTimeLabel.setObjectName("avgInfectionTimeLabel")
        self.horizontalLayout_11.addWidget(self.avgInfectionTimeLabel)
        self.avgInfectionTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.avgInfectionTimeSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.avgInfectionTimeSpinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.avgInfectionTimeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.avgInfectionTimeSpinBox.setMinimum(1)
        self.avgInfectionTimeSpinBox.setMaximum(100)
        self.avgInfectionTimeSpinBox.setProperty("value", 7)
        self.avgInfectionTimeSpinBox.setObjectName("avgInfectionTimeSpinBox")
        self.horizontalLayout_11.addWidget(self.avgInfectionTimeSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.avgImmuneTimeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.avgImmuneTimeLabel.setFont(font)
        self.avgImmuneTimeLabel.setObjectName("avgImmuneTimeLabel")
        self.horizontalLayout_14.addWidget(self.avgImmuneTimeLabel)
        self.avgImmuneTimeSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.avgImmuneTimeSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.avgImmuneTimeSpinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.avgImmuneTimeSpinBox.setMinimum(1)
        self.avgImmuneTimeSpinBox.setMaximum(999)
        self.avgImmuneTimeSpinBox.setProperty("value", 10)
        self.avgImmuneTimeSpinBox.setObjectName("avgImmuneTimeSpinBox")
        self.horizontalLayout_14.addWidget(self.avgImmuneTimeSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.infectionRadiusLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.infectionRadiusLabel.setFont(font)
        self.infectionRadiusLabel.setObjectName("infectionRadiusLabel")
        self.horizontalLayout_18.addWidget(self.infectionRadiusLabel)
        self.infectionRadiusSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.infectionRadiusSpinBox.setMinimumSize(QtCore.QSize(150, 0))
        self.infectionRadiusSpinBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.infectionRadiusSpinBox.setMinimum(1)
        self.infectionRadiusSpinBox.setMaximum(100)
        self.infectionRadiusSpinBox.setProperty("value", 16)
        self.infectionRadiusSpinBox.setObjectName("infectionRadiusSpinBox")
        self.horizontalLayout_18.addWidget(self.infectionRadiusSpinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.resetParameterButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetParameterButton.setObjectName("resetParameterButton")
        self.verticalLayout_3.addWidget(self.resetParameterButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.simulationLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.simulationLabel.setFont(font)
        self.simulationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.simulationLabel.setObjectName("simulationLabel")
        self.verticalLayout_13.addWidget(self.simulationLabel)
        self.simulationGraphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.simulationGraphicsView.setObjectName("simulationGraphicsView")
        self.verticalLayout_13.addWidget(self.simulationGraphicsView)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(10, -1, 0, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.liveStatisticsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.liveStatisticsLabel.setFont(font)
        self.liveStatisticsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.liveStatisticsLabel.setObjectName("liveStatisticsLabel")
        self.verticalLayout_12.addWidget(self.liveStatisticsLabel)
        self.graphicWidget = PlotWidget(self.centralwidget)
        self.graphicWidget.setObjectName("graphicWidget")
        self.verticalLayout_12.addWidget(self.graphicWidget)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.currentDayLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.currentDayLabel.setFont(font)
        self.currentDayLabel.setObjectName("currentDayLabel")
        self.horizontalLayout_12.addWidget(self.currentDayLabel)
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
        self.precentageInfectedLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.precentageInfectedLabel.setFont(font)
        self.precentageInfectedLabel.setObjectName("precentageInfectedLabel")
        self.horizontalLayout_12.addWidget(self.precentageInfectedLabel)
        self.percentageInfectedLCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.percentageInfectedLCD.setDigitCount(6)
        self.percentageInfectedLCD.setObjectName("percentageInfectedLCD")
        self.horizontalLayout_12.addWidget(self.percentageInfectedLCD)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.simSpeedLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.simSpeedLabel.setFont(font)
        self.simSpeedLabel.setObjectName("simSpeedLabel")
        self.horizontalLayout_16.addWidget(self.simSpeedLabel)
        self.speedOfSimSlider = QtWidgets.QSlider(self.centralwidget)
        self.speedOfSimSlider.setMinimum(30)
        self.speedOfSimSlider.setMaximum(240)
        self.speedOfSimSlider.setProperty("value", 60)
        self.speedOfSimSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedOfSimSlider.setInvertedControls(False)
        self.speedOfSimSlider.setObjectName("speedOfSimSlider")
        self.horizontalLayout_16.addWidget(self.speedOfSimSlider)
        self.speedMultiplierLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.speedMultiplierLabel.setFont(font)
        self.speedMultiplierLabel.setObjectName("speedMultiplierLabel")
        self.horizontalLayout_16.addWidget(self.speedMultiplierLabel)
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
        self.warningCapacityLabel = QtWidgets.QLabel(self.centralwidget)
        self.warningCapacityLabel.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.warningCapacityLabel.setFont(font)
        self.warningCapacityLabel.setObjectName("warningCapacityLabel")
        self.horizontalLayout_16.addWidget(self.warningCapacityLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.startSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.startSimButton.setFlat(False)
        self.startSimButton.setObjectName("startSimButton")
        self.horizontalLayout_8.addWidget(self.startSimButton)
        self.resetSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetSimButton.setAutoDefault(False)
        self.resetSimButton.setDefault(False)
        self.resetSimButton.setFlat(False)
        self.resetSimButton.setObjectName("resetSimButton")
        self.horizontalLayout_8.addWidget(self.resetSimButton)
        self.pauseSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseSimButton.setObjectName("pauseSimButton")
        self.horizontalLayout_8.addWidget(self.pauseSimButton)
        self.resumeSimButton = QtWidgets.QPushButton(self.centralwidget)
        self.resumeSimButton.setEnabled(True)
        self.resumeSimButton.setObjectName("resumeSimButton")
        self.horizontalLayout_8.addWidget(self.resumeSimButton)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.exportCsvButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportCsvButton.setObjectName("exportCsvButton")
        self.verticalLayout_7.addWidget(self.exportCsvButton)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1242, 21))
        self.menubar.setObjectName("menubar")
        self.menuAdvanced_Options = QtWidgets.QMenu(self.menubar)
        self.menuAdvanced_Options.setObjectName("menuAdvanced_Options")
        self.menuShow_Hide = QtWidgets.QMenu(self.menuAdvanced_Options)
        self.menuShow_Hide.setObjectName("menuShow_Hide")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionShow_social_distancing_radius = QtWidgets.QAction(MainWindow)
        self.actionShow_social_distancing_radius.setObjectName("actionShow_social_distancing_radius")
        self.actionChange_default_values = QtWidgets.QAction(MainWindow)
        self.actionChange_default_values.setObjectName("actionChange_default_values")
        self.actionInfection_radius = QtWidgets.QAction(MainWindow)
        self.actionInfection_radius.setCheckable(True)
        self.actionInfection_radius.setObjectName("actionInfection_radius")
        self.actionSocial_distancing_radius = QtWidgets.QAction(MainWindow)
        self.actionSocial_distancing_radius.setCheckable(True)
        self.actionSocial_distancing_radius.setObjectName("actionSocial_distancing_radius")
        self.actionShow_Legend = QtWidgets.QAction(MainWindow)
        self.actionShow_Legend.setObjectName("actionShow_Legend")
        self.actionMin_Max_values = QtWidgets.QAction(MainWindow)
        self.actionMin_Max_values.setObjectName("actionMin_Max_values")
        self.menuShow_Hide.addAction(self.actionInfection_radius)
        self.menuShow_Hide.addAction(self.actionSocial_distancing_radius)
        self.menuAdvanced_Options.addAction(self.menuShow_Hide.menuAction())
        self.menuHelp.addAction(self.actionShow_Legend)
        self.menuHelp.addAction(self.actionMin_Max_values)
        self.menubar.addAction(self.menuAdvanced_Options.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pandemic"))
        self.entitiesLabel.setText(_translate("MainWindow", "Select amount of entities (1- 200): "))
        self.initiallyInfectedLabel.setText(_translate("MainWindow", "Select initially infected entities:"))
        self.modifierLabel.setText(_translate("MainWindow", "Select modifier:"))
        self.deflectEachOtherCheckBox.setText(_translate("MainWindow", "Social distancing"))
        self.socialDistancingLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Select the social distancing distance for the particles! (For reference: The size of a particle is 8 -&gt; MinValue = 0, MaxValue = 8; </span><span style=\" font-style:italic;\">You can activate the visibility of the social distancing radius in the top left corner under &quot;Advanced Options&quot;!</span><span style=\" font-style:italic;\">)</span></p></body></html>"))
        self.socialDistancingLabel.setText(_translate("MainWindow", "Social distancing radius:"))
        self.vaccineCheckBox.setText(_translate("MainWindow", "Develop a vaccine"))
        self.vaccineDaysLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">How many days it takes until the vaccine is ready to use!</span></p></body></html>"))
        self.vaccineDaysLabel.setText(_translate("MainWindow", "Development in days:"))
        self.healthCareOverloadedCheckBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">If the amount of infected particles exceeds the health care system capaity, the death rate increases as treatment is no longer available for everybody!</span></p></body></html>"))
        self.healthCareOverloadedCheckBox.setText(_translate("MainWindow", "Health care system can fail"))
        self.capacityLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Percentage of total particles -&gt; Maximum amount of infected particles that the health care system can carry! This leads to an increased death rate!</span></p></body></html>"))
        self.capacityLabel.setText(_translate("MainWindow", "Capacity:"))
        self.deathRateMultiplierLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">How much the death rate increases for particles where treatment is no longer possible. (MinValue = 1, MaxValue = 3.0)</span></p></body></html>"))
        self.deathRateMultiplierLabel.setText(_translate("MainWindow", "Multiplier:"))
        self.riskOfInfectionLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Risk of infection for a healthy particle for each frame it is in the infection area of an infected particle</span></p></body></html>"))
        self.riskOfInfectionLabel.setText(_translate("MainWindow", "Select risk of infection in percent: "))
        self.rateOfDeathLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">% of dying for an infected particle each day</span></p></body></html>"))
        self.rateOfDeathLabel.setText(_translate("MainWindow", "Select rate of death in percent:"))
        self.percentageOfQuarantineLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">% of being quarantined for an infected particle each day</span></p></body></html>"))
        self.percentageOfQuarantineLabel.setText(_translate("MainWindow", "Select percentage of being quarantined:"))
        self.avgInfectionTimeLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Randomly selects a time within a deviation of 25% of the selected value</span></p></body></html>"))
        self.avgInfectionTimeLabel.setText(_translate("MainWindow", "Select average infection-time in days:"))
        self.avgImmuneTimeLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Randomly selects a time within a deviation of 25% of the selected value</span></p></body></html>"))
        self.avgImmuneTimeLabel.setText(_translate("MainWindow", "Select average immune-time in days:"))
        self.infectionRadiusLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Comparison: Size of a particle is &quot;8&quot; (You can activate the visibility of the infection radius in the top left corner under &quot;Advanced Options&quot;!)</span></p></body></html>"))
        self.infectionRadiusLabel.setText(_translate("MainWindow", "Select infection radius:"))
        self.resetParameterButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Resets all changable values to their respective default value!</span></p></body></html>"))
        self.resetParameterButton.setText(_translate("MainWindow", "Reset parameters"))
        self.simulationLabel.setText(_translate("MainWindow", "Simulation"))
        self.liveStatisticsLabel.setText(_translate("MainWindow", "Live-Statistics"))
        self.currentDayLabel.setText(_translate("MainWindow", "Current Day:"))
        self.precentageInfectedLabel.setText(_translate("MainWindow", "Infected:"))
        self.percentageInfectedLCD.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Percentage of infected particles among </span><span style=\" font-style:italic; text-decoration: underline;\">all living</span><span style=\" font-style:italic;\"> particles!</span></p></body></html>"))
        self.simSpeedLabel.setText(_translate("MainWindow", "Simulation speed:"))
        self.speedMultiplierLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Percentage of infected particles compared to all living particles!</span></p></body></html>"))
        self.speedMultiplierLabel.setText(_translate("MainWindow", "Multiplier:"))
        self.warningCapacityLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#cc0d0d;\">WARNING: Health care capacity exceeded!</span></p></body></html>"))
        self.startSimButton.setText(_translate("MainWindow", "Start"))
        self.resetSimButton.setText(_translate("MainWindow", "Reset"))
        self.pauseSimButton.setText(_translate("MainWindow", "Pause"))
        self.resumeSimButton.setText(_translate("MainWindow", "Resume"))
        self.exportCsvButton.setText(_translate("MainWindow", "Export"))
        self.menuAdvanced_Options.setTitle(_translate("MainWindow", "Advanced Options"))
        self.menuShow_Hide.setTitle(_translate("MainWindow", "Show/Hide..."))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionShow_social_distancing_radius.setText(_translate("MainWindow", "Show/Hide social distancing radius"))
        self.actionChange_default_values.setText(_translate("MainWindow", "Change default values"))
        self.actionInfection_radius.setText(_translate("MainWindow", "Infection radius"))
        self.actionSocial_distancing_radius.setText(_translate("MainWindow", "Social distancing radius"))
        self.actionShow_Legend.setText(_translate("MainWindow", "Show Legend..."))
        self.actionMin_Max_values.setText(_translate("MainWindow", "Min-/Max-values"))

from pyqtgraph import PlotWidget


