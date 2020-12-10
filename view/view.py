from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QBrush, QPen, QPainter
from PyQt5.QtCore import Qt
import random
from resources.healthconditions import healthconditions
from view.mainwindow import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)

        self.connectSignals()

        self.scene = QtWidgets.QGraphicsScene(0, 0, 500, 500)
        self.redBrush = QBrush(Qt.red)
        self.greenBrush = QBrush(Qt.green)
        self.pen = QPen(Qt.black)
        self.scene.addRect(0, 0, 500, 500)

    def connectSignals(self):
        self.startSimButton.pressed.connect(self.startSimulationClicked)

    def startSimulationClicked(self):
        self.startSimulationSignal.emit()

    def startSimulation(self):
        print("SIMULATION STARTED!")

    # updates the scene on the graphicsView
    def updateScene(self):
        self.graphicsView_2.setScene(self.scene)
        #self.graphicsView.fitInView(0, 0, 500, 500)

    # returns the scene parameters to bound the movement area of the particles
    def getSceneParamters(self):
        return self.scene.width(), self.scene.height()

    # draws the particles on the scene with right color, quantity,...
    # -> needs to take an input for the amount of simulated particles later
    def drawItems(self, particlelist):
        self.scene.clear() #clear the scene to remove the old and outdated items, then draw new ones
        for i in range(0, 50):
            if particlelist[i].status == healthconditions.HEALTHY:
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, particlelist[i].width,
                                                 particlelist[i].height, self.pen, self.greenBrush)
            elif particlelist[i].status == healthconditions.INFECTED:
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, particlelist[i].width,
                                                     particlelist[i].height, self.pen, self.redBrush)
        self.scene.addRect(0, 0, 500, 500)

