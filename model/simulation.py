
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QBrush, QPen, QPainter
from PyQt5.QtCore import Qt
import random



class Simulation:
    def __init__(self):
        print("Simulation Created")
        self.stepCounter = 0
        self.scene = QtWidgets.QGraphicsScene(0, 0, 500, 500)
        self.redBrush = QBrush(Qt.red)
        self.greenBrush = QBrush(Qt.green)
        self.pen = QPen(Qt.black)
        self.particleList = {}
        self.erstelleItems()

    def performStep(self):
        self.stepCounter += 1
        print("Simulation step {} processed.".format(self.stepCounter))
        # We want each particle to move with a constant amount of time in between, so that the simulation looks smooth ->Solution: Moveing a particle with each step we make.
        self.moveParticle()

    def getData(self):
        return self.stepCounter

    # returns the updated scene to the presenter, so that the view can print it out
    def getScene(self):
        return self.scene

    # creates the amount of items on the scene, needs to take an input for the amount of simulated particles later
    def erstelleItems(self):
        for i in range(0, 50):
            ellipse_item = self.scene.addEllipse(random.randint(0, 500), random.randint(0, 500), 8, 8, self.pen, self.greenBrush)
            self.particleList[i] = ellipse_item

    # gives the particles directions for their movement (dir could be saved as a variable of my "particle class"(later, should have: Direction, position and status)
    def moveParticle(self):
        if(self.stepCounter % 30 == 0):
            for i in range(0, 50):
                self.particleList[i].setX(self.particleList[i].x() + 10) #https://doc.qt.io/qt-5/qpointf.html ->Nur so werden die Positionen aktualisiert, ohne das ...x() wird nur ein Referenzwert genommen
                self.particleList[i].setY(self.particleList[i].y() + 10) #https://doc.qt.io/qt-5/qpointf.html ->Nur so werden die Positionen aktualisiert, ohne das ...y() wird nur ein Referenzwert genommen

    #def changeState(self): ->Will change the state of a particle after colliding with another (color and status will change)
    #->cases: healthy and infected, healthy and healthy, infected and infected