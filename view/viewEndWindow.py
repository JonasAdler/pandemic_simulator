import pyqtgraph as pg
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui

from resources import constVariables
from view.endWindow import Ui_Dialog


class ViewEndWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(ViewEndWindow, self).__init__()
        self.setupUi(self)

        self.allHaveDiedLabel.hide()
        self.pandemicIsOverLabel.hide()

        self.healthyPlot = []
        self.infectedPlot = []
        self.immunePlot = []
        self.deceasedPlot = []

        # increase visibility of LCDs
        self.highlightLCDs()

        # prepare the plot
        self.graphicEndWidget.setBackground("w")
        self.plotHealthy = self.graphicEndWidget.plot(np.arange(int(0 / constVariables.dayLength)),
                                                      self.healthyPlot, pen=pg.mkPen(width=3, color="g"),
                                                      name="Healthy")
        self.plotInfected = self.graphicEndWidget.plot(np.arange(int(0 / constVariables.dayLength)),
                                                       self.infectedPlot, pen=pg.mkPen(width=3, color="r"),
                                                       name="Infected")
        self.plotImmune = self.graphicEndWidget.plot(np.arange(int(0 / constVariables.dayLength)),
                                                     self.immunePlot, pen=pg.mkPen(width=3, color=(255, 255, 0)),
                                                     name="Immune")
        self.plotDeceased = self.graphicEndWidget.plot(np.arange(int(0 / constVariables.dayLength)),
                                                       self.deceasedPlot, pen=pg.mkPen(width=3, color=(80, 80, 80)),
                                                       name="Deceased")
        self.plotCapacity = self.graphicEndWidget.plot(np.arange(int(0 / constVariables.dayLength)),
                                                       np.full((int(0 / constVariables.dayLength),), 1),
                                                       pen=pg.mkPen(width=3, color="r", style=QtCore.Qt.DotLine))

        self.connectSignals()

    def connectSignals(self):
        self.closeEndButton.clicked.connect(self.closeEndButtonClicked)

    def highlightLCDs(self):
        # set the color of the LCDs
        self.palette = self.daysEndLCD.palette()
        # foreground color
        self.palette.setColor(self.palette.WindowText, QtGui.QColor(0, 0, 0))
        # background color
        self.palette.setColor(self.palette.Background, QtGui.QColor(0, 0, 0))
        # "light" border
        self.palette.setColor(self.palette.Light, QtGui.QColor(0, 0, 0))
        # "dark" border
        self.palette.setColor(self.palette.Dark, QtGui.QColor(0, 0, 0))
        # set the palette
        self.deathsEndLCD.setPalette(self.palette)
        self.daysEndLCD.setPalette(self.palette)
        self.maxInfectedEndLCD.setPalette(self.palette)

    def updateElements(self, quantityList, healthCareEnabled, capacity):
        # if everyone is dead -> show "all have died"
        if quantityList[len(quantityList) - 1][5] == 0:
            self.allHaveDiedLabel.show()
        # if no one is infected and there is at least one particle alive -> "pandemic is over"
        elif quantityList[len(quantityList) - 1][2] == 0:
            self.pandemicIsOverLabel.show()

        # update LCDs
        self.updateLCDs(quantityList)

        # show complete graph
        self.showGraph(quantityList, healthCareEnabled, capacity)

        # reset all elements (safety mechanism if the window is not closed via the button but with the "X"-symbol
        self.resetData()

    def updateLCDs(self, quantityList):
        maxInfected = -99999
        for i in range(len(quantityList)):
            if quantityList[i][2] > maxInfected:
                maxInfected = quantityList[i][2]
        self.deathsEndLCD.display(quantityList[len(quantityList) - 1][4])
        self.maxInfectedEndLCD.display(maxInfected)
        self.daysEndLCD.display(len(quantityList) - 1)

    def showGraph(self, quantityList, healthCareEnabled, capacity):
        for i in range(len(quantityList)):
            self.healthyPlot.append(quantityList[i][1])
            self.infectedPlot.append(quantityList[i][2])
            self.immunePlot.append(quantityList[i][3])
            self.deceasedPlot.append(quantityList[i][4])
        self.plotHealthy.setData(np.arange(len(quantityList)), self.healthyPlot)
        self.plotInfected.setData(np.arange(len(quantityList)), self.infectedPlot)
        self.plotImmune.setData(np.arange(len(quantityList)), self.immunePlot)
        self.plotDeceased.setData(np.arange(len(quantityList)), self.deceasedPlot)
        if healthCareEnabled:
            # plot graph with (capacity * all particles)/100 as data
            self.plotCapacity.setData(np.arange(len(quantityList)),
                                      np.full((len(quantityList),),
                                              int((capacity * (quantityList[len(quantityList) - 1][5] +
                                                   quantityList[len(quantityList) - 1][4]) / 100))))

    def resetData(self):
        # reset plot values
        self.healthyPlot = []
        self.infectedPlot = []
        self.immunePlot = []
        self.deceasedPlot = []

    def closeEndButtonClicked(self):
        # hide the labels
        self.allHaveDiedLabel.hide()
        self.pandemicIsOverLabel.hide()

        # clear the capacity plot (as it is constant)
        self.plotCapacity.clear()

        # close the window
        self.close()