from PyQt5 import QtCore

from view.view import View
from model.simulation import Simulation

import csv
FPS = 60

class Presenter(QtCore.QObject):
    def __init__(self):
        super(Presenter, self).__init__()
        # create main window

        self.ui = View()
        self.simulation = None
        self.isSimulationRunning = False

        # create timer that will call the mainLoop every 1000/FPS milliseconds
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mainLoop)
        self.timer.start(int(1000 / FPS))
        self.framecounter = 0

        self._connectUIElements()

    # perform the steps and draw the items on the scene for each step while the simulation is running
    def mainLoop(self):
        if self.isSimulationRunning:
            self.simulation.performStep()
            self.ui.drawItems(self.simulation.getParticleList())
            self.ui.updateScene()
            #self.ui.updateData(self.simulation.getData())

    # create the simulation and hand it all the predetermined values
    def startSimulation(self, amountOfParticles, initiallyInfected, riskOfInfection, rateOfDeath, riskOfQuarantine, avgInfectedTime, avgImmuneTime, infectionRadius):
        self.isSimulationRunning = True
        print("Hello World from Presenter")
        self.simulation = Simulation(amountOfParticles, initiallyInfected, riskOfInfection, rateOfDeath, riskOfQuarantine, avgInfectedTime, avgImmuneTime, infectionRadius)
        self.ui.startSimulation()

    # pause the simulation
    def pauseSimulation(self):
        self.isSimulationRunning = False
        print("Simulation is paused at {} days.".format(self.simulation.stepCounter/120))

    # resume the simulation
    def resumeSiumlation(self):
        self.isSimulationRunning = True
        print("Resuming the simulation!")

    # reset the simulation
    def resetSimulation(self):
        self.isSimulationRunning = False
        self.ui.scene.clear()
        self.simulation = None

    # hand the given parameters with the quantityList to the write-Operation
    def exportCsv(self):
        path, filetype, granularity = self.ui.getExportParameters()
        if path and granularity:
            self.writeInCsv(path, filetype, granularity, self.simulation.getQuantityList())
        else:
            print("Something went wrong.")

    # writes to the csv
    def writeInCsv(self, path, filetype, granularity, quantityList):
        with open(path, mode='w', newline='') as self.f:
            self.writer = csv.writer(self.f)
            fieldnames = ["Step", "Healthy", "Infected", "Immune", "Deceased"]
            self.writer.writerow(fieldnames)
            self.writer.writerow(quantityList[0])
            for i in range(granularity, len(quantityList), granularity):
                self.writer.writerow(quantityList[i])
        self.f.close()

    # if a simulation has been created, change the risk of infection in the simulation
    def changeRisk(self, risk):
        if self.simulation:
            self.simulation.changeRiskOfInfection(risk)

    def _connectUIElements(self) -> None:
        # elements of the main window
        self.ui.startSimulationSignal.connect(self.startSimulation)
        self.ui.pauseSimulationSignal.connect(self.pauseSimulation)
        self.ui.resumeSimulationSignal.connect(self.resumeSiumlation)
        self.ui.resetSimulationSignal.connect(self.resetSimulation)
        self.ui.exportCsvSignal.connect(self.exportCsv)
        self.ui.riskOfInfectionSignal.connect(self.changeRisk)



