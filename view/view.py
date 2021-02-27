import pyqtgraph as pg
import numpy as np

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from resources import constVariables

from view.mainwindow import Ui_MainWindow

class View(QtWidgets.QMainWindow, Ui_MainWindow):
    startSimulationSignal = QtCore.pyqtSignal(int, int, int, int, int, int, int, int,
                                              bool, bool, bool, int, int, int, int)
    pauseSimulationSignal = QtCore.pyqtSignal()
    resumeSimulationSignal = QtCore.pyqtSignal()
    resetSimulationSignal = QtCore.pyqtSignal()
    exportCsvSignal = QtCore.pyqtSignal()

    infectionRadiusSignal = QtCore.pyqtSignal(int)
    riskOfInfectionSignal = QtCore.pyqtSignal(int)
    rateOfDeathSignal = QtCore.pyqtSignal(int)
    riskOfQuarantineSignal = QtCore.pyqtSignal(int)
    avgInfectionTimeSignal = QtCore.pyqtSignal(int)
    avgImmuneTimeSignal = QtCore.pyqtSignal(int)
    speedOfSimSignal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)

        # create counter
        self.counter = 0

        # hide the buttons that only appear after another is clicked
        self.resetSimButton.hide()
        self.resumeSimButton.hide()
        self.pauseSimButton.hide()
        self.exportCsvButton.hide()

        self.socialDistancingLabel.hide()
        self.socialDistancingSpinBox.hide()

        self.vaccineDaysLabel.hide()
        self.vaccineDaysSpinBox.hide()

        self.capacityLabel.hide()
        self.deathRateMultiplierLabel.hide()
        self.healthCareCapacitySpinBox.hide()
        self.deathRateMultiplierSpinBox.hide()
        self.warningCapacityLabel.hide()

        self.connectSignals()

        # set the scene and initialize necessary tools
        self.scene = QtWidgets.QGraphicsScene(0, 0, constVariables.worldSize, constVariables.worldSize)
        self.redBrush = QBrush(Qt.red)
        self.greenBrush = QBrush(Qt.green)
        self.greyBrush = QBrush(Qt.gray)
        self.yellowBrush = QBrush(Qt.yellow)
        self.whiteBrush = QBrush(Qt.white)
        self.pen = QPen(Qt.black)

        # set the color of the LCDs
        self.palette = self.daysPassedLCD.palette()
        # foreground color
        self.palette.setColor(self.palette.WindowText, QtGui.QColor(0, 0, 0))
        # background color
        self.palette.setColor(self.palette.Background, QtGui.QColor(0, 0, 0))
        # "light" border
        self.palette.setColor(self.palette.Light, QtGui.QColor(0, 0, 0))
        # "dark" border
        self.palette.setColor(self.palette.Dark, QtGui.QColor(0, 0, 0))
        # set the palette
        self.daysPassedLCD.setPalette(self.palette)
        self.multiplyLCD.setPalette(self.palette)
        self.percentageInfectedLCD.setPalette(self.palette)

        # initiate second palette for later
        self.palette2 = self.percentageInfectedLCD.palette()

        # prepare the live plot
        self.quantityList = []
        self.healthyPlot = []
        self.infectedPlot = []
        self.immunePlot = []
        self.deceasedPlot = []

        self.graphicWidget.setBackground("w")
        self.graphicWidget.addLegend()
        self.plotHealthy = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                   self.healthyPlot, pen=pg.mkPen(width=3, color="g"), name="Healthy")
        self.plotInfected = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                    self.infectedPlot, pen=pg.mkPen(width=3, color="r"),
                                                    name="Infected")
        self.plotImmune = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                  self.immunePlot, pen=pg.mkPen(width=3, color=(255, 255, 0)),
                                                  name="Immune")
        self.plotDeceased = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                    self.deceasedPlot, pen=pg.mkPen(width=3, color=(80, 80, 80)),
                                                    name="Deceased")
        self.plotCapacity = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                    np.full((int(self.counter / constVariables.dayLength),),
                                                            self.healthCareCapacitySpinBox.value()),
                                                    pen=pg.mkPen(width=3, color="r", style=QtCore.Qt.DotLine),
                                                    name="Capacity")

    # connect signals -> reaction if a button is clicked
    def connectSignals(self):
        # buttons
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resumeSimButton.pressed.connect(self.resumeSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)
        self.exportCsvButton.pressed.connect(self.exportCsvClicked)
        self.resetParameterButton.pressed.connect(self.resetParamsClicked)

        # check-boxes
        self.deflectEachOtherCheckBox.clicked.connect(self.deflectionCheckBoxClicked)
        self.vaccineCheckBox.clicked.connect(self.vaccineCheckBoxClicked)
        self.healthCareOverloadedCheckBox.clicked.connect(self.healthCareCheckBoxClicked)

        # parameters
        self.riskOfInfSpinBox.valueChanged.connect(self.riskOfInfectionChanged)
        self.rateOfDeathSpinBox.valueChanged.connect(self.rateOfDeathChanged)
        self.percentageQuarantineSpinBox.valueChanged.connect(self.percentageOfQuarantineChanged)
        self.avgImmuneTimeSpinBox.valueChanged.connect(self.avgImmuneTimeChanged)
        self.avgInfectionTimeSpinBox.valueChanged.connect(self.avgInfectedTimeChanged)
        self.infectionRadiusSpinBox.valueChanged.connect(self.infectionRadiusChanged)

        self.speedOfSimSlider.valueChanged.connect(self.speedOfSimChanged)

    # accumulation of events that happen, if buttons are pressed

    def startSimulationClicked(self):
        # if no error, pass all the start values to the presenter
        if self.entitiesSpinBox.value() >= self.initiallyInfectedSpinBox.value():
            self.startSimulationSignal.emit(self.entitiesSpinBox.value(), self.initiallyInfectedSpinBox.value(),
                                            self.riskOfInfSpinBox.value() * 10, self.rateOfDeathSpinBox.value() * 10,
                                            self.percentageQuarantineSpinBox.value() * 10,
                                            self.avgInfectionTimeSpinBox.value(),
                                            self.avgImmuneTimeSpinBox.value(), self.infectionRadiusSpinBox.value(),
                                            self.deflectEachOtherCheckBox.isChecked(),
                                            self.healthCareOverloadedCheckBox.isChecked(),
                                            self.vaccineCheckBox.isChecked(), self.socialDistancingSpinBox.value(),
                                            self.vaccineDaysSpinBox.value(), self.healthCareCapacitySpinBox.value(),
                                            self.deathRateMultiplierSpinBox.value())

            # disable modifiers and spin boxes
            self.socialDistancingLabel.setDisabled(True)
            self.socialDistancingSpinBox.setDisabled(True)
            self.vaccineCheckBox.setDisabled(True)
            self.healthCareOverloadedCheckBox.setDisabled(True)
            self.deflectEachOtherCheckBox.setDisabled(True)
            self.vaccineDaysLabel.setDisabled(True)
            self.vaccineDaysSpinBox.setDisabled(True)
            self.capacityLabel.setDisabled(True)
            self.deathRateMultiplierLabel.setDisabled(True)
            self.healthCareCapacitySpinBox.setDisabled(True)
            self.deathRateMultiplierSpinBox.setDisabled(True)

            self.entitiesSpinBox.setDisabled(True)
            self.initiallyInfectedSpinBox.setDisabled(True)

            # show/hide the buttons
            self.startSimButton.hide()
            self.pauseSimButton.show()
            self.resetSimButton.show()
            self.exportCsvButton.show()
            self.resetParameterButton.hide()

            # fit the scene
            self.simulationGraphicsView.fitInView(0, 0, constVariables.worldSize, constVariables.worldSize)

        # if there are more particles initially infected than total
        else:
            self.errorTooManyInfected()

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
        self.startSimButton.show()
        self.resetParameterButton.show()
        self.warningCapacityLabel.hide()
        self.simulationGraphicsView.fitInView(0, 0, constVariables.worldSize, constVariables.worldSize)

        # reset display items to a state they were in at the beginning
        self.resetValues()

    # resets all the values to the state they were in before the simulation has started
    def resetValues(self):
        # reset parameters
        self.counter = 0
        self.daysPassedLCD.display(0)
        self.percentageInfectedLCD.display(0)

        # reset days-lcd to black
        self.palette.setColor(self.palette.WindowText, QtGui.QColor(0, 0, 0))
        self.palette.setColor(self.palette.Background, QtGui.QColor(0, 0, 0))
        self.palette.setColor(self.palette.Light, QtGui.QColor(0, 0, 0))
        self.palette.setColor(self.palette.Dark, QtGui.QColor(0, 0, 0))
        self.daysPassedLCD.setPalette(self.palette)

        # reset percentage-lcd to black
        self.palette2.setColor(self.palette2.WindowText, QtGui.QColor(0, 0, 0))
        self.palette2.setColor(self.palette2.Background, QtGui.QColor(0, 0, 0))
        self.palette2.setColor(self.palette2.Light, QtGui.QColor(0, 0, 0))
        self.palette2.setColor(self.palette2.Dark, QtGui.QColor(0, 0, 0))
        self.percentageInfectedLCD.setPalette(self.palette2)

        # reset multiply lcd to black
        self.multiplyLCD.setPalette(self.palette)

        # enable the modifiers and spin boxes
        self.socialDistancingLabel.setEnabled(True)
        self.socialDistancingSpinBox.setEnabled(True)
        self.vaccineCheckBox.setEnabled(True)
        self.healthCareOverloadedCheckBox.setEnabled(True)
        self.deflectEachOtherCheckBox.setEnabled(True)
        self.vaccineDaysLabel.setEnabled(True)
        self.vaccineDaysSpinBox.setEnabled(True)
        self.capacityLabel.setEnabled(True)
        self.deathRateMultiplierLabel.setEnabled(True)
        self.healthCareCapacitySpinBox.setEnabled(True)
        self.deathRateMultiplierSpinBox.setEnabled(True)

        self.entitiesSpinBox.setEnabled(True)
        self.initiallyInfectedSpinBox.setEnabled(True)

        # reset plot variables
        self.healthyPlot = []
        self.infectedPlot = []
        self.immunePlot = []
        self.deceasedPlot = []

        # clear the graph widget and recreate the plots
        self.graphicWidget.clear()
        self.plotHealthy = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                   self.healthyPlot, pen=pg.mkPen(width=3, color="g"), name="Healthy")
        self.plotInfected = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                    self.infectedPlot, pen=pg.mkPen(width=3, color="r"),
                                                    name="Infected")
        self.plotImmune = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                  self.immunePlot, pen=pg.mkPen(width=3, color=(255, 255, 0)),
                                                  name="Immune")
        self.plotDeceased = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                    self.deceasedPlot, pen=pg.mkPen(width=3, color=(0, 0, 0)),
                                                    name="Deceased")
        self.plotCapacity = self.graphicWidget.plot(np.arange(int(self.counter / constVariables.dayLength)),
                                                    np.full((int(self.counter / constVariables.dayLength),),
                                                            self.healthCareCapacitySpinBox.value()),
                                                    pen=pg.mkPen(width=3, color="r", style=QtCore.Qt.DotLine),
                                                    name="Capacity")

    # resets all variables and parameters to default values
    def resetParamsClicked(self):
        # reset parameters on left side
        self.entitiesSpinBox.setValue(constVariables.entitiesSpinBoxDefault)
        self.initiallyInfectedSpinBox.setValue(constVariables.initiallyInfectedSpinBoxDefault)
        self.granularitySpinBox.setValue(constVariables.granularitySpinBoxDefault)

        # reset parameters on the right side
        self.riskOfInfSpinBox.setValue(constVariables.riskOfInfSpinBoxDefault)
        self.rateOfDeathSpinBox.setValue(constVariables.rateOfDeathSpinBoxDefault)
        self.percentageQuarantineSpinBox.setValue(constVariables.percentageQuarantineSpinBoxDefault)
        self.avgInfectionTimeSpinBox.setValue(constVariables.avgInfectionTimeSpinBoxDefault)
        self.avgImmuneTimeSpinBox.setValue(constVariables.avgImmuneTimeSpinBoxDefault)
        self.infectionRadiusSpinBox.setValue(constVariables.infectionRadiusSpinBoxDefault)

        # reset remaining parameters
        self.speedOfSimSlider.setValue(constVariables.speedOfSimSliderDefault)
        self.socialDistancingSpinBox.setValue(constVariables.socialDistancingSpinBoxDefault)
        self.vaccineDaysSpinBox.setValue(constVariables.vaccineDaysSpinBoxDefault)
        self.healthCareCapacitySpinBox.setValue(constVariables.healthCareCapacitySpinBoxDefault)
        self.deathRateMultiplierSpinBox.setValue(constVariables.deathRateMultiplierSpinBoxDefault)

    # drop-down managing
    def healthCareCheckBoxClicked(self):
        if self.healthCareOverloadedCheckBox.isChecked():
            self.capacityLabel.show()
            self.deathRateMultiplierLabel.show()
            self.healthCareCapacitySpinBox.show()
            self.deathRateMultiplierSpinBox.show()
        else:
            self.capacityLabel.hide()
            self.deathRateMultiplierLabel.hide()
            self.healthCareCapacitySpinBox.hide()
            self.deathRateMultiplierSpinBox.hide()

    def vaccineCheckBoxClicked(self):
        if self.vaccineCheckBox.isChecked():
            self.vaccineDaysLabel.show()
            self.vaccineDaysSpinBox.show()
        else:
            self.vaccineDaysLabel.hide()
            self.vaccineDaysSpinBox.hide()

    def deflectionCheckBoxClicked(self):
        if self.deflectEachOtherCheckBox.isChecked():
            self.socialDistancingLabel.show()
            self.socialDistancingSpinBox.show()
        else:
            self.socialDistancingLabel.hide()
            self.socialDistancingSpinBox.hide()

# parameter change methods
    def riskOfInfectionChanged(self):
        self.riskOfInfectionSignal.emit(self.riskOfInfSpinBox.value() * 10)  # "*10" to get a whole number

    def rateOfDeathChanged(self):
        self.rateOfDeathSignal.emit(self.rateOfDeathSpinBox.value() * 10)

    def percentageOfQuarantineChanged(self):
        self.riskOfQuarantineSignal.emit(self.percentageQuarantineSpinBox.value() * 10)

    def avgInfectedTimeChanged(self):
        self.avgInfectionTimeSignal.emit(self.avgInfectionTimeSpinBox.value())

    def avgImmuneTimeChanged(self):
        self.avgImmuneTimeSignal.emit(self.avgImmuneTimeSpinBox.value())

    def infectionRadiusChanged(self):
        self.infectionRadiusSignal.emit(self.infectionRadiusSpinBox.value())

    def speedOfSimChanged(self):
        self.speedOfSimSignal.emit(self.speedOfSimSlider.value())
        self.updateMultiplier()

    def exportCsvClicked(self):
        self.pauseSimulationClicked()
        self.exportCsvSignal.emit()

    def startSimulation(self):
        print("SIMULATION STARTED!")

# update visible elements
    # updates the scene on the graphicsView
    def updateScene(self):
        self.simulationGraphicsView.setScene(self.scene)
        self.simulationGraphicsView.fitInView(0, 0, constVariables.worldSize, constVariables.worldSize)

    # draws the particles on the scene with right color, quantity,...
    # -> needs to take an input for the amount of simulated particles later
    def drawItems(self, particleList):

        # clear the scene to remove the old and outdated items, then draw new ones
        self.scene.clear()

        for i in range(len(particleList)):
            if particleList[i].status == constVariables.healthy:
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, constVariables.particleSize,
                                                     constVariables.particleSize, self.pen, self.greenBrush)
            elif particleList[i].status == constVariables.infected:
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, constVariables.particleSize,
                                                     constVariables.particleSize, self.pen, self.redBrush)
            elif particleList[i].status == constVariables.deceased:
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, constVariables.particleSize,
                                                     constVariables.particleSize, self.pen, self.greyBrush)
            elif particleList[i].status == constVariables.immune:
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, constVariables.particleSize,
                                                     constVariables.particleSize, self.pen, self.yellowBrush)
            elif particleList[i].status == constVariables.quarantined:
                ellipse_item = self.scene.addEllipse(particleList[i].x, particleList[i].y, constVariables.particleSize,
                                                     constVariables.particleSize, self.pen, self.whiteBrush)
            # draw infection radius if option is selected
            if self.actionInfection_radius.isChecked():
                self.drawRadiusInfection(particleList, i)
            # draw social distancing radius if option is selected
            if self.actionSocial_distancing_radius.isChecked():
                self.drawRadiusSocialDistance(particleList, i)

    def drawRadiusInfection(self, particleList, i):
        self.scene.addEllipse(particleList[i].x - 4, particleList[i].y - 4,
                                                    self.infectionRadiusSpinBox.value(),
                                                    self.infectionRadiusSpinBox.value(),
                                                    pen=pg.mkPen(width=2, color=(220, 50, 20)))

    def drawRadiusSocialDistance(self, particleList, i):
        self.scene.addEllipse(particleList[i].x + 4, particleList[i].y + 4,
                                                         self.socialDistancingSpinBox.value(),
                                                         self.socialDistancingSpinBox.value(),
                                                         pen=pg.mkPen(width=2, color=(255, 255, 0)))

    # updates elements such as the counter, LCDs, the information for the plots, ...
    def updateElements(self, days, quantityList):

        # update the counter
        self.counter += 1

        # percentage of infected particles corresponding to all "still alive" particles (also check for division by 0)
        if quantityList[days][5] != 0:
            percentageOfLiving = quantityList[days][2] / quantityList[days][5]  # percentage between 0 and 1
        else:
            percentageOfLiving = 0.0
        percentage_string = "{:.1%}".format(percentageOfLiving)
        self.daysPassedLCD.display(days)
        self.percentageInfectedLCD.display(percentage_string)  # percentage as non-fractional number

        # if capacity gets overrun -> show the label
        if self.healthCareOverloadedCheckBox.isChecked() and \
                int(quantityList[days][2] * 100 / self.entitiesSpinBox.value()) > \
                self.healthCareCapacitySpinBox.value():
            self.warningCapacityLabel.show()
        else:
            self.warningCapacityLabel.hide()

        # change the colour scheme corresponding to the spread of the disease and set the new palette again
        self.updateColourScheme(percentageOfLiving)

        # update the quantity list and plot the graph with the new information
        self.quantityList = quantityList
        self.plotGraph()

    # updates the colour scheme of the LCD items
    def updateColourScheme(self, percentageOfLiving):
        if percentageOfLiving < 0.33:
            self.palette2.setColor(self.palette2.WindowText, QtGui.QColor(50, 205, 50))
            self.palette2.setColor(self.palette2.Background, QtGui.QColor(50, 205, 50))
            self.palette2.setColor(self.palette2.Light, QtGui.QColor(50, 205, 50))
            self.palette2.setColor(self.palette2.Dark, QtGui.QColor(50, 205, 50))

        elif percentageOfLiving < 0.66:
            self.palette2.setColor(self.palette2.WindowText, QtGui.QColor(255, 140, 0))
            self.palette2.setColor(self.palette2.Background, QtGui.QColor(255, 140, 0))
            self.palette2.setColor(self.palette2.Light, QtGui.QColor(255, 140, 0))
            self.palette2.setColor(self.palette2.Dark, QtGui.QColor(255, 140, 0))

        else:
            self.palette2.setColor(self.palette2.WindowText, QtGui.QColor(220, 20, 60))
            self.palette2.setColor(self.palette2.Background, QtGui.QColor(220, 20, 60))
            self.palette2.setColor(self.palette2.Light, QtGui.QColor(220, 20, 60))
            self.palette2.setColor(self.palette2.Dark, QtGui.QColor(220, 20, 60))
        # set the palette
        self.percentageInfectedLCD.setPalette(self.palette2)

    # updates the "speed multiplier"-LCD
    def updateMultiplier(self):
        # Format the multiply
        multi_lcd = '{0:0.1f}'.format(self.speedOfSimSlider.value() / constVariables.dayLength)
        self.multiplyLCD.setPalette(self.palette)
        self.multiplyLCD.display(multi_lcd)

    # function for plotting the graph
    def plotGraph(self):
        # plot each second
        if self.counter % constVariables.dayLength == 0:
            # update the plot data
            self.healthyPlot.append(self.quantityList[int(self.counter / constVariables.dayLength)][1])
            self.infectedPlot.append(self.quantityList[int(self.counter / constVariables.dayLength)][2])
            self.immunePlot.append(self.quantityList[int(self.counter / constVariables.dayLength)][3])
            self.deceasedPlot.append(self.quantityList[int(self.counter / constVariables.dayLength)][4])
            # plot the graph
            self.plotHealthy.setData(np.arange(self.counter / constVariables.dayLength), self.healthyPlot)
            self.plotInfected.setData(np.arange(self.counter / constVariables.dayLength), self.infectedPlot)
            self.plotImmune.setData(np.arange(self.counter / constVariables.dayLength), self.immunePlot)
            self.plotDeceased.setData(np.arange(self.counter / constVariables.dayLength), self.deceasedPlot)
            # if modifier is activated the capacity also gets plotted
            if self.healthCareOverloadedCheckBox.isChecked():
                self.plotCapacity.setData(np.arange(int(self.counter / constVariables.dayLength)),
                                          np.full((int(self.counter / constVariables.dayLength),),
                                                  int((self.healthCareCapacitySpinBox.value() *
                                                       self.entitiesSpinBox.value())) / 100))

    # get user input path and return parameters for export
    def getExportParameters(self):

        # WARNING: The path has to be saved as a .csv manually, otherwise the program will crash
        path, filetype = QFileDialog.getSaveFileName(self, "Save File")

        # return the path (and the filetype)
        return path, filetype, self.granularitySpinBox.value()

    # opens up an error message box
    def errorTooManyInfected(self):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText("The amount of initially infected particles exceeds the total amount of particles!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Close)
        x = msg.exec()
