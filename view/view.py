import csv

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from model.healthconditions import healthconditions
from view.mainwindow import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal()
    pauseSimulationSignal = QtCore.pyqtSignal()
    resumeSimulationSignal = QtCore.pyqtSignal()
    resetSimulationSignal = QtCore.pyqtSignal()
    exportCsvSignal = QtCore.pyqtSignal()

    infectionRadiusSignal = QtCore.pyqtSignal(int)
    riskOfInfectionSignal = QtCore.pyqtSignal(int)  #ToDo: Fragen -> Float?
    rateOfDeathSignal = QtCore.pyqtSignal(int)
    riskOfQuarantine = QtCore.pyqtSignal(int)
    avgInfectionTimeSignal = QtCore.pyqtSignal(int)
    avgImmuneTimeSignal = QtCore.pyqtSignal(int)


    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)

        # hide the buttons that only appear after another is clicked
        self.resetSimButton.hide()
        self.resumeSimButton.hide()
        self.pauseSimButton.hide()
        self.exportCsvButton.hide()

        self.connectSignals()

        # set the scene and initialize necessary tools
        self.scene = QtWidgets.QGraphicsScene(0, 0, 500, 500)
        self.redBrush = QBrush(Qt.red)
        self.greenBrush = QBrush(Qt.green)
        self.greyBrush = QBrush(Qt.gray)
        self.yellowBrush = QBrush(Qt.yellow)
        self.whiteBrush = QBrush(Qt.white)
        self.pen = QPen(Qt.black)

        # initialize default values -> only change-methods needed -> ToDo: "Wollen sie die Parameter zurücksetzen?" bei Reset -> Nach Milestone
        self.granularity = 1
        self.riskOfInfection = 5
        self.rateOfDeath = 1
        self.riskOfQuarantine = 20
        self.avgInfectedTime = 14
        self.avgImmuneTime = 15
        self.infectionRadius = 8

    def connectSignals(self):
        # buttons
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resumeSimButton.pressed.connect(self.resumeSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)
        self.exportCsvButton.pressed.connect(self.exportCsvClicked)

        # parameters
        self.granularitySpinBox.valueChanged.connect(self.granularityChanged)
        self.riskOfInfSpinBox.valueChanged.connect(self.riskOfInfectionChanged)
        self.rateOfDeathSpinBox.valueChanged.connect(self.rateOfDeathChanged)
        self.percentageQuarantineSpinBox.valueChanged.connect(self.percentageOfQuarantineChanged)
        self.avgImmuneTimeSpinBox.valueChanged.connect(self.avgImmuneTimeChanged)
        self.avgInfectionTimeSpinBox.valueChanged.connect(self.avgInfectedTimeChanged)
        self.spinBox.valueChanged.connect(self.infectionRadiusChanged)
    # accumulation of events that happen, if buttons are pressed

    def startSimulationClicked(self):
        self.startSimulationSignal.emit()
        self.startSimButton.hide()
        self.pauseSimButton.show()
        self.resetSimButton.show()
        self.exportCsvButton.show()

    def pauseSimulationClicked(self):
        self.pauseSimulationSignal.emit()
        self.pauseSimButton.hide()
        self.resumeSimButton.show()

    def resumeSimulationClicked(self):
        self.resumeSimulationSignal.emit()
        self.resumeSimButton.hide()
        self.pauseSimButton.show()

    def resetSimulationClicked(self):
        self.resetSimulationSignal.emit()
        self.resetSimButton.hide()
        self.pauseSimButton.hide()
        self.resumeSimButton.hide()
        self.exportCsvButton.hide()
        self.granularitySpinBox.setValue(1)
        # ToDo: Inputs wieder auf Default-Werte zurücksetzten
        self.startSimButton.show()

    def granularityChanged(self):
        self.granularity = self.granularitySpinBox.value()

    def riskOfInfectionChanged(self):
        print("riskOfInf")
        #self.radiusSignal.emit(self.riskOfInfSpinBox.value())

    def rateOfDeathChanged(self):
        print("rate")

    def percentageOfQuarantineChanged(self):
        print("pOQ")

    def avgInfectedTimeChanged(self):
        print("avgInf")

    def avgImmuneTimeChanged(self):
        print("avgImm")

    def infectionRadiusChanged(self):
        print("inf")

    def exportCsvClicked(self):
        self.pauseSimulationClicked()
        self.exportCsvSignal.emit()

    def startSimulation(self):
        print("SIMULATION STARTED!")

    # updates the scene on the graphicsView
    def updateScene(self):
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(0, 0, 500, 500)

    # draws the particles on the scene with right color, quantity,...
    # -> needs to take an input for the amount of simulated particles later
    def drawItems(self, particleList):

        # clear the scene to remove the old and outdated items, then draw new ones
        self.scene.clear()

        for i in range(len(particleList)):
            if particleList[i].status == "HEALTHY":
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, 8,
                                                     8, self.pen, self.greenBrush)
            elif particleList[i].status == "INFECTED":
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, 8,
                                                     8, self.pen, self.redBrush)
            elif particleList[i].status == "DECEASED":
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, 8,
                                                     8, self.pen, self.greyBrush)
            elif particleList[i].status == "IMMUNE":
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, 8,
                                                     8, self.pen, self.yellowBrush)
            elif particleList[i].status == "QUARANTINED":
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, 8,
                                                     8, self.pen, self.whiteBrush)

    # get user input path and return parameters for export
    def getExportParameters(self):

        # WARNING: The path has to be saved as a .csv manually, otherwise the program will crash
        path, filetype = QFileDialog.getSaveFileName(self, "Save File")

        # return the path (and the filetype)
        return path, filetype, self.granularity



