
from PyQt5 import QtWidgets
import random
from PyQt5.QtGui import QBrush, QColor


class Simulation:
    def __init__(self):
        print("Simulation Created")
        self.stepCounter = 0
        self.scene = QtWidgets.QGraphicsScene(0, 0, 500, 500)
        self.erstelleItems(self.scene)

    def performStep(self):
        self.stepCounter += 1
        print("Simulation step {} processed.".format(self.stepCounter))
        if(self.stepCounter % 30 == 0):
            self.scene.addRect(random.randint(0, 500), random.randint(0, 500), 20, 20)

    def getData(self):
        return self.stepCounter

    def getScene(self):
        return self.scene

    def erstelleItems(self, scene):
        for i in range(0, 100):
            self.scene.addRect(random.randint(0, 500), random.randint(0, 500), 8, 8)

    #def changeScene(self, scene):
