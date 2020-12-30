from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from model.healthconditions import healthconditions
from view.mainwindow import Ui_MainWindow


class View(QtWidgets.QMainWindow, Ui_MainWindow):

    startSimulationSignal = QtCore.pyqtSignal()
    pauseSimulationSignal = QtCore.pyqtSignal()
    resumeSimulationSignal = QtCore.pyqtSignal()
    resetSimulationSignal = QtCore.pyqtSignal()

    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)

        # hide the buttons that only appear after another is clicked
        self.resetSimButton.hide()
        self.resumeSimButton.hide()
        self.pauseSimButton.hide()

        self.connectSignals()

        # set the scene and initialize necessary tools
        self.scene = QtWidgets.QGraphicsScene(0, 0, 500, 500)
        self.redBrush = QBrush(Qt.red)
        self.greenBrush = QBrush(Qt.green)
        self.greyBrush = QBrush(Qt.gray)
        self.yellowBrush = QBrush(Qt.yellow)
        self.whiteBrush = QBrush(Qt.white)
        self.pen = QPen(Qt.black)

    def connectSignals(self):
        self.startSimButton.pressed.connect(self.startSimulationClicked)
        self.pauseSimButton.pressed.connect(self.pauseSimulationClicked)
        self.resumeSimButton.pressed.connect(self.resumeSimulationClicked)
        self.resetSimButton.pressed.connect(self.resetSimulationClicked)

    def startSimulationClicked(self):
        self.startSimulationSignal.emit()
        self.startSimButton.hide()
        self.pauseSimButton.show()
        self.resetSimButton.show()

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
        self.startSimButton.show()


    def startSimulation(self):
        print("SIMULATION STARTED!")

    # updates the scene on the graphicsView
    def updateScene(self):
        self.graphicsView_2.setScene(self.scene)
        self.graphicsView_2.fitInView(0, 0, 500, 500)

    # returns the scene parameters to bound the movement area of the particles
    def getSceneParamters(self):
        return self.scene.width(), self.scene.height()

    # draws the particles on the scene with right color, quantity,...
    # -> needs to take an input for the amount of simulated particles later
    def drawItems(self, particlelist):

        # clear the scene to remove the old and outdated items, then draw new ones
        self.scene.clear()

        for i in range(0, 50):
            if particlelist[i].status == "HEALTHY":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, particlelist[i].width,
                                                     particlelist[i].height, self.pen, self.greenBrush)
            elif particlelist[i].status == "INFECTED":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, particlelist[i].width,
                                                     particlelist[i].height, self.pen, self.redBrush)
            elif particlelist[i].status == "DECEASED":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, particlelist[i].width,
                                                     particlelist[i].height, self.pen, self.greyBrush)
            elif particlelist[i].status == "IMMUNE":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, particlelist[i].width,
                                                     particlelist[i].height, self.pen, self.yellowBrush)
            elif particlelist[i].status == "QUARANTINED":
                ellipse_item = self.scene.addEllipse(particlelist[i].x, particlelist[i].y, particlelist[i].width,
                                                     particlelist[i].height, self.pen, self.whiteBrush)
