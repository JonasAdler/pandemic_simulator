import pyqtgraph as pg
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox

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
        self.scene = QtWidgets.QGraphicsScene(0, 0, 500, 500)
        self.redBrush = QBrush(Qt.red)
        self.greenBrush = QBrush(Qt.green)
        self.greyBrush = QBrush(Qt.gray)
        self.yellowBrush = QBrush(Qt.yellow)
        self.whiteBrush = QBrush(Qt.white)
        self.pen = QPen(Qt.black)

        self.granularity = self.granularitySpinBox.value()

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

        self.palette2 = self.percentageInfectedLCD.palette()
        # foreground color
        self.palette2.setColor(self.palette2.WindowText, QtGui.QColor(0, 0, 0))
        # background color
        self.palette2.setColor(self.palette2.Background, QtGui.QColor(0, 0, 0))
        # "light" border
        self.palette2.setColor(self.palette2.Light, QtGui.QColor(0, 0, 0))
        # "dark" border
        self.palette2.setColor(self.palette2.Dark, QtGui.QColor(0, 0, 0))
        # set the palette
        self.percentageInfectedLCD.setPalette(self.palette2)

        # prepare the live plot
        self.quantityList = []
        self.healthyPlot = []
        self.infectedPlot = []
        self.immunePlot = []
        self.deceasedPlot = []

        self.graphicWidget.setBackground("w")
        self.graphicWidget.addLegend()
        self.plotHealthy = self.graphicWidget.plot(np.arange(int(self.counter/60)), self.healthyPlot,
                                                   pen=pg.mkPen(width=3, color="g"), name="Healthy")
        self.plotInfected = self.graphicWidget.plot(np.arange(int(self.counter/60)), self.infectedPlot,
                                                    pen=pg.mkPen(width=3, color="r"), name="Infected")
        self.plotImmune = self.graphicWidget.plot(np.arange(int(self.counter/60)), self.immunePlot,
                                                  pen=pg.mkPen(width=3, color=(255, 255, 0)), name="Immune")
        self.plotDeceased = self.graphicWidget.plot(np.arange(int(self.counter/60)), self.deceasedPlot,
                                                    pen=pg.mkPen(width=3, color=(80, 80, 80)), name="Deceased")
        self.plotCapacity = self.graphicWidget.plot(np.arange(int(self.counter/60)),
                                                    np.full((int(self.counter/60),),
                                                            self.healthCareCapacitySpinBox.value()),
                                                    pen=pg.mkPen(width=3, color="r", style=QtCore.Qt.DotLine),
                                                    name="Capacity")

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
        self.granularitySpinBox.valueChanged.connect(self.granularityChanged)
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
                                            self.riskOfInfSpinBox.value()*10, self.rateOfDeathSpinBox.value()*10,
                                            self.percentageQuarantineSpinBox.value()*10,
                                            self.avgInfectionTimeSpinBox.value(),
                                            self.avgImmuneTimeSpinBox.value(), self.infectionRadiusSpinBox.value(),
                                            self.deflectEachOtherCheckBox.isChecked(),
                                            self.healthCareOverloadedCheckBox.isChecked(),
                                            self.vaccineCheckBox.isChecked(), self.socialDistancingSpinBox.value(),
                                            self.vaccineDaysSpinBox.value(), self.healthCareCapacitySpinBox.value(),
                                            self.deathRateMultiplierSpinBox.value())
            # disable the modifiers
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

            # show/hide the buttons
            self.startSimButton.hide()
            self.pauseSimButton.show()
            self.resetSimButton.show()
            self.exportCsvButton.show()
            self.resetParameterButton.hide()

            self.simulationGraphicsView.fitInView(0, 0, 500, 500)
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
        self.simulationGraphicsView.fitInView(0, 0, 500, 500)
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

        # enable the modifiers
        self.socialDistancingLabel.setEnabled(True)
        self.socialDistancingSpinBox.setEnabled(True)
        self.vaccineCheckBox.setDisabled(False)
        self.healthCareOverloadedCheckBox.setDisabled(False)
        self.deflectEachOtherCheckBox.setDisabled(False)
        self.vaccineDaysLabel.setDisabled(False)
        self.vaccineDaysSpinBox.setDisabled(False)
        self.capacityLabel.setDisabled(False)
        self.deathRateMultiplierLabel.setDisabled(False)
        self.healthCareCapacitySpinBox.setDisabled(False)
        self.deathRateMultiplierSpinBox.setDisabled(False)

        # reset plot variables
        self.healthyPlot = []
        self.infectedPlot = []
        self.immunePlot = []
        self.deceasedPlot = []

        # clear the graph widget and recreate the plots
        self.graphicWidget.clear()
        self.plotHealthy = self.graphicWidget.plot(np.arange(int(self.counter / 60)), self.healthyPlot,
                                                   pen=pg.mkPen(width=3, color="g"), name="Healthy")
        self.plotInfected = self.graphicWidget.plot(np.arange(int(self.counter / 60)), self.infectedPlot,
                                                    pen=pg.mkPen(width=3, color="r"), name="Infected")
        self.plotImmune = self.graphicWidget.plot(np.arange(int(self.counter / 60)), self.immunePlot,
                                                  pen=pg.mkPen(width=3, color=(255, 255, 0)), name="Immune")
        self.plotDeceased = self.graphicWidget.plot(np.arange(int(self.counter / 60)), self.deceasedPlot,
                                                    pen=pg.mkPen(width=3, color=(0, 0, 0)), name="Deceased")
        self.plotCapacity = self.graphicWidget.plot(np.arange(int(self.counter / 60)),
                                                    np.full((int(self.counter / 60),),
                                                            self.healthCareCapacitySpinBox.value()),
                                                    pen=pg.mkPen(width=3, color="r", style=QtCore.Qt.DotLine),
                                                    name="Capacity")

    # resets all variables and parameters to default values
    def resetParamsClicked(self):
        # reset parameters on left side
        self.entitiesSpinBox.setValue(50)
        self.initiallyInfectedSpinBox.setValue(5)
        self.granularitySpinBox.setValue(1)

        # reset parameters on the right side
        self.riskOfInfSpinBox.setValue(5.0)
        self.rateOfDeathSpinBox.setValue(1.0)
        self.percentageQuarantineSpinBox.setValue(20.0)
        self.avgInfectionTimeSpinBox.setValue(7)
        self.avgImmuneTimeSpinBox.setValue(10)
        self.infectionRadiusSpinBox.setValue(10)

        # reset remaining parameters
        self.speedOfSimSlider.setValue(60)
        self.socialDistancingSpinBox.setValue(8)
        self.vaccineDaysSpinBox.setValue(15)
        self.healthCareCapacitySpinBox.setValue(65)
        self.deathRateMultiplierSpinBox.setValue(1.0)

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
    def granularityChanged(self):
        self.granularity = self.granularitySpinBox.value()

    def riskOfInfectionChanged(self):
        self.riskOfInfectionSignal.emit(self.riskOfInfSpinBox.value()*10)  # "*10" to get a whole number

    def rateOfDeathChanged(self):
        self.rateOfDeathSignal.emit(self.rateOfDeathSpinBox.value()*10)

    def percentageOfQuarantineChanged(self):
        self.riskOfQuarantineSignal.emit(self.percentageQuarantineSpinBox.value()*10)

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
        self.simulationGraphicsView.fitInView(0, 0, 500, 500)

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

    # opens up an error message box
    def errorTooManyInfected(self):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText("The amount of initially infected particles exceeds the total amount of particles!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Close)
        x = msg.exec()

# update elements
    # updates elements such as the counter, LCDs, the information for the plots, ...
    def updateElements(self, days, quantityList):

        # update the counter
        self.counter += 1

        # percentage of infected particles corresponding to all "still alive" particles
        percentageOfLiving = quantityList[days][2] / quantityList[days][5]  # percentage between 0 and 1
        percentage_string = "{:.1%}".format(percentageOfLiving)
        self.daysPassedLCD.display(days + 1)
        self.percentageInfectedLCD.display(percentage_string)  # percentage as non-fractional number

        # if capacity gets overrun -> show the label
        if self.healthCareOverloadedCheckBox.isChecked() and \
                int(quantityList[days][2]*100 / self.entitiesSpinBox.value()) > self.healthCareCapacitySpinBox.value():
            self.warningCapacityLabel.show()
        else:
            self.warningCapacityLabel.hide()

        # change the colour scheme corresponding to the spread of the disease and set the new palette again
        self.updateColourScheme(percentageOfLiving)
        self.percentageInfectedLCD.setPalette(self.palette2)

        # update the quantity list and plot the graph with the new information
        self.quantityList = quantityList
        self.plotGraph()

    # updates the colour scheme of the LCD items
    def updateColourScheme(self, percentageOfLiving):
        if percentageOfLiving < 0.33:

            self.palette2.setColor(self.palette2.WindowText, QtGui.QColor(50, 205, 50))
            # background color
            self.palette2.setColor(self.palette2.Background, QtGui.QColor(50, 205, 50))
            # "light" border
            self.palette2.setColor(self.palette2.Light, QtGui.QColor(50, 205, 50))
            # "dark" border
            self.palette2.setColor(self.palette2.Dark, QtGui.QColor(50, 205, 50))

        elif percentageOfLiving < 0.66:

            self.palette2.setColor(self.palette2.WindowText, QtGui.QColor(255, 140, 0))
            # background color
            self.palette2.setColor(self.palette2.Background, QtGui.QColor(255, 140, 0))
            # "light" border
            self.palette2.setColor(self.palette2.Light, QtGui.QColor(255, 140, 0))
            # "dark" border
            self.palette2.setColor(self.palette2.Dark, QtGui.QColor(255, 140, 0))

        else:

            self.palette2.setColor(self.palette2.WindowText, QtGui.QColor(220, 20, 60))
            # background color
            self.palette2.setColor(self.palette2.Background, QtGui.QColor(220, 20, 60))
            # "light" border
            self.palette2.setColor(self.palette2.Light, QtGui.QColor(220, 20, 60))
            # "dark" border
            self.palette2.setColor(self.palette2.Dark, QtGui.QColor(220, 20, 60))

    # updates the "speed multiplier"-LCD
    def updateMultiplier(self):
        # Format the multiply
        multi_lcd = '{0:0.1f}'.format(self.speedOfSimSlider.value()/60)
        self.multiplyLCD.setPalette(self.palette)
        self.multiplyLCD.display(multi_lcd)

    # function for plotting the graph
    def plotGraph(self):
        # plot each second
        if self.counter % 60 == 0:
            # update the plot data
            self.healthyPlot.append(self.quantityList[int(self.counter/60)][1])
            self.infectedPlot.append(self.quantityList[int(self.counter/60)][2])
            self.immunePlot.append(self.quantityList[int(self.counter/60)][3])
            self.deceasedPlot.append(self.quantityList[int(self.counter/60)][4])
            # plot the graph
            self.plotHealthy.setData(np.arange(self.counter / 60), self.healthyPlot)
            self.plotInfected.setData(np.arange(self.counter / 60), self.infectedPlot)
            self.plotImmune.setData(np.arange(self.counter / 60), self.immunePlot)
            self.plotDeceased.setData(np.arange(self.counter / 60), self.deceasedPlot)
            if self.healthCareOverloadedCheckBox.isChecked():
                self.plotCapacity.setData(np.arange(int(self.counter / 60)),
                                          np.full((int(self.counter / 60),),
                                          int((self.healthCareCapacitySpinBox.value() *
                                               self.entitiesSpinBox.value()))/100))