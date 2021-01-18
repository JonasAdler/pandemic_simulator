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
    #riskOfInfectionSignal = QtCore.pyqtSignal(int)  #ToDo: Fragen -> Float?

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
        self.granularity = 1

    def connectSignals(self):
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resumeSimButton.pressed.connect(self.resumeSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)
        self.exportCsvButton.pressed.connect(self.exportCsvClicked)
        self.granularitySpinBox.valueChanged.connect(self.granularityChanged)
        #self.riskOfInfSpinBox.valueChanged.connect(self.riskOfInfectionChanged)

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
        self.radiusSignal.emit(self.riskOfInfSpinBox.value()*1000)

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
    def drawItems(self, particlelist):

        # clear the scene to remove the old and outdated items, then draw new ones
        self.scene.clear()

        for i in range(0, 50):
            if particlelist[i].status == "HEALTHY":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, 8,
                                                     8, self.pen, self.greenBrush)
            elif particlelist[i].status == "INFECTED":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, 8,
                                                     8, self.pen, self.redBrush)
            elif particlelist[i].status == "DECEASED":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, 8,
                                                     8, self.pen, self.greyBrush)
            elif particlelist[i].status == "IMMUNE":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, 8,
                                                     8, self.pen, self.yellowBrush)
            elif particlelist[i].status == "QUARANTINED":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, 8,
                                                     8, self.pen, self.whiteBrush)

    # select granularity and save the csv to a selected path
    def exportCsv(self, quantityList):

        # WARNING: The path has to be saved as a .csv manually, otherwise the program will crash
        path, filetype = QFileDialog.getSaveFileName(self, "Save File")

        # write to csv if path is given
        if path and self.granularity:
            with open(path, mode='w', newline='') as self.f:
                self.writer = csv.writer(self.f)
                fieldnames = ["Step", "Healthy", "Infected", "Immune", "Deceased"]
                self.writer.writerow(fieldnames)
                self.writer.writerow(quantityList[0])
                for i in range(self.granularity, len(quantityList), self.granularity):
                    self.writer.writerow(quantityList[i])
        else:
            print("Something went wrong.")



