import csv
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from model.healthconditions import healthconditions
from view.mainwindow import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal(int, int, int, int, int, int, int, int, bool, bool, bool, bool, int)
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

        # hide the buttons that only appear after another is clicked
        self.resetSimButton.hide()
        self.resumeSimButton.hide()
        self.pauseSimButton.hide()
        self.exportCsvButton.hide()
        self.label_16.hide()  # label for "Development in days"
        self.vaccineDaysSpinBox.hide()

        self.connectSignals()

        # set the scene and initialize necessary tools
        self.scene = QtWidgets.QGraphicsScene(0, 0, 500, 500)
        self.redBrush = QBrush(Qt.red)
        self.greenBrush = QBrush(Qt.green)
        self.greyBrush = QBrush(Qt.gray)
        self.yellowBrush = QBrush(Qt.yellow)
        self.whiteBrush = QBrush(Qt.white)
        self.pen = QPen(Qt.black)

        # ToDo: "Wollen sie die Parameter zurücksetzen?" bei Reset -> Nach Milestone
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

        self.multiplyLCD.setPalette(self.palette)

        #self.graphicsView_3 = pg.PlotWidget(self.centralwidget)
        #self.graphicsView_3.setBackground("w")
        #self.graphicsView_3 = pg.PlotWidget(self.centralwidget)
        #self.graphicsView_3.setBackground("w")
        #self.verticalLayout_12.addWidget(self.graphicsView_3)

    def connectSignals(self):
        # buttons
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resumeSimButton.pressed.connect(self.resumeSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)
        self.exportCsvButton.pressed.connect(self.exportCsvClicked)

        # check-boxes
        self.deflectEachOtherCheckBox.clicked.connect(self.deflectCheckBoxClicked)
        self.closureOfSchoolsCheckBox.clicked.connect(self.closureCheckBoxClicked)
        self.vaccineCheckBox.clicked.connect(self.vaccineCheckBoxClicked)

        # parameters
        self.granularitySpinBox.valueChanged.connect(self.granularityChanged)
        self.riskOfInfSpinBox.valueChanged.connect(self.riskOfInfectionChanged)
        self.rateOfDeathSpinBox.valueChanged.connect(self.rateOfDeathChanged)
        self.percentageQuarantineSpinBox.valueChanged.connect(self.percentageOfQuarantineChanged)
        self.avgImmuneTimeSpinBox.valueChanged.connect(self.avgImmuneTimeChanged)
        self.avgInfectionTimeSpinBox.valueChanged.connect(self.avgInfectedTimeChanged)
        self.infectionRadiusSpinBox_2.valueChanged.connect(self.infectionRadiusChanged)

        self.speedOfSimSlider.valueChanged.connect(self.speedOfSimChanged)

    # accumulation of events that happen, if buttons are pressed

    def startSimulationClicked(self):
        # if no error, pass all the start values to the presenter
        if self.entitiesSpinBox.value() >= self.initiallyInfectedSpinBox.value():
            self.startSimulationSignal.emit(self.entitiesSpinBox.value(), self.initiallyInfectedSpinBox.value(),
                                            self.riskOfInfSpinBox.value()*10, self.rateOfDeathSpinBox.value()*10,
                                            self.percentageQuarantineSpinBox.value()*10,
                                            self.avgInfectionTimeSpinBox.value(),
                                            self.avgImmuneTimeSpinBox.value(), self.infectionRadiusSpinBox_2.value(),
                                            self.deflectEachOtherCheckBox.isChecked(), self.closureOfSchoolsCheckBox.isChecked(),
                                            self.healthCareOverloadedCheckBox.isChecked(), self.vaccineCheckBox.isChecked(),
                                            self.vaccineDaysSpinBox.value())
            # disable the modifiers
            self.vaccineCheckBox.setDisabled(True)
            self.closureOfSchoolsCheckBox.setDisabled(True)
            self.healthCareOverloadedCheckBox.setDisabled(True)
            self.deflectEachOtherCheckBox.setDisabled(True)
            self.label_16.setDisabled(True)
            self.vaccineDaysSpinBox.setDisabled(True)

            # show/hide the buttons
            self.startSimButton.hide()
            self.pauseSimButton.show()
            self.resetSimButton.show()
            self.exportCsvButton.show()
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
        # ToDo: Inputs wieder auf Default-Werte zurücksetzten
        self.resetValues()

    def resetValues(self):
        # reset parameters
        self.granularitySpinBox.setValue(1)
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
        self.vaccineCheckBox.setDisabled(False)
        self.closureOfSchoolsCheckBox.setDisabled(False)
        self.healthCareOverloadedCheckBox.setDisabled(False)
        self.deflectEachOtherCheckBox.setDisabled(False)
        self.label_16.setDisabled(False)
        self.vaccineDaysSpinBox.setDisabled(False)

# checkbox checked methods
    def deflectCheckBoxClicked(self):
        # implicit change as only one of the two can be selected
        if self.closureOfSchoolsCheckBox.isChecked():
            self.closureOfSchoolsCheckBox.setChecked(False)

    def closureCheckBoxClicked(self):
        # implicit change as only one of the two can be selected
        if self.deflectEachOtherCheckBox.isChecked():
            self.deflectEachOtherCheckBox.setChecked(False)

    def vaccineCheckBoxClicked(self):
        if self.vaccineCheckBox.isChecked():
            self.label_16.show()
            self.vaccineDaysSpinBox.show()
        else:
            self.label_16.hide()
            self.vaccineDaysSpinBox.hide()

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
        self.infectionRadiusSignal.emit(self.infectionRadiusSpinBox_2.value())

    def speedOfSimChanged(self):
        self.speedOfSimSignal.emit(self.speedOfSimSlider.value())
        self.updateMultiplier()

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

    def errorTooManyInfected(self):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText("The amount of initially infected particles exceeds the total amount of particles!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Close)
        x = msg.exec()

    def updateLCD(self, days, quantityList):
        percentageOfTotal = quantityList[days][2] / self.entitiesSpinBox.value()  # percentage between 0 and 1
        percentage_string = "{:.1%}".format(percentageOfTotal)
        self.daysPassedLCD.display(days + 1)
        self.percentageInfectedLCD.display(percentage_string)  # percentage as non-fractional number

        # with increasing percentage, the "green"-value decreases while the "red"-value increases
        self.palette2.setColor(self.palette2.WindowText, QtGui.QColor(150*percentageOfTotal, 150 - 150*percentageOfTotal, 0))
        # background color
        self.palette2.setColor(self.palette2.Background, QtGui.QColor(150*percentageOfTotal, 150 - 150*percentageOfTotal, 0))
        # "light" border
        self.palette2.setColor(self.palette2.Light, QtGui.QColor(150*percentageOfTotal, 150 - 150*percentageOfTotal, 0))
        # "dark" border
        self.palette2.setColor(self.palette2.Dark, QtGui.QColor(150*percentageOfTotal, 150 - 150*percentageOfTotal, 0))
        # set the new palette again
        self.percentageInfectedLCD.setPalette(self.palette2)

    def updateMultiplier(self):
        # Format the multiply
        multi_lcd = '{0:0.1f}'.format(self.speedOfSimSlider.value()/60)
        self.multiplyLCD.setPalette(self.palette)
        self.multiplyLCD.display(multi_lcd)

    def plotGraph(self, quantityList):
        pass