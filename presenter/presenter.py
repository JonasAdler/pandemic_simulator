from PyQt5 import QtCore

from resources import constVariables
from view.view import View
from model.simulation import Simulation

import csv


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
        self.timer.start(int(1000 / constVariables.FPS))
        self.framecounter = 0

        self._connectUIElements()

    # perform the steps and draw the items on the scene for each step while the simulation is running
    def mainLoop(self):
        if self.isSimulationRunning:
            self.simulation.performStep()
            self.ui.drawItems(self.simulation.getParticleList())
            self.ui.updateScene()
            self.ui.updateElements(self.simulation.getDays(), self.simulation.getQuantityList())

    # create the simulation and hand it all the predetermined values
    def startSimulation(self, amountOfParticles, initiallyInfected, riskOfInfection, rateOfDeath, riskOfQuarantine,
                        avgInfectedTime, avgImmuneTime, infectionRadius, modifierDeflect, modifierHealth,
                        modifierVaccine, socialDistanceRadius, vaccineDays, healthCareCapacity, deathRateMultiplier):
        self.isSimulationRunning = True
        print("Hello World from Presenter")
        self.simulation = Simulation(amountOfParticles, initiallyInfected, riskOfInfection, rateOfDeath,
                                     riskOfQuarantine, avgInfectedTime, avgImmuneTime, infectionRadius,
                                     modifierDeflect, modifierHealth, modifierVaccine, socialDistanceRadius,
                                     vaccineDays, healthCareCapacity, deathRateMultiplier)
        self.ui.startSimulation()

    # pause the simulation
    def pauseSimulation(self):
        self.isSimulationRunning = False
        print("Simulation is paused at {} days.".format(self.simulation.stepCounter/constVariables.dayLength))

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
            fieldnames = ["Step", "Healthy", "Infected", "Immune", "Deceased", "Alive"]
            self.writer.writerow(fieldnames)
            self.writer.writerow(quantityList[0])
            for i in range(granularity, len(quantityList), granularity):
                self.writer.writerow(quantityList[i])
        self.f.close()

# set of methods that connect with the parameters in the simulation class if a value is changed
# if simulation has been created,...

    # ...change the risk of infection in the simulation
    def changeRiskOfI(self, risk):
        if self.simulation:
            self.simulation.changeRiskOfInfectionS(risk)

    # ...change rate of death
    def changeRate(self, rate):
        if self.simulation:
            self.simulation.changeRateOfDeathS(rate)

    # ...change risk of being quarantined
    def changeRiskOfQ(self, risk):
        if self.simulation:
            self.simulation.changeRiskOfQuarantineS(risk)

    # ...change average infected time
    def changeAvgInfectedTime(self, time):
        if self.simulation:
            self.simulation.changeAvgInfectedTimeS(time)

    # ...change average immune time
    def changeAvgImmuneTime(self, time):
        if self.simulation:
            self.simulation.changeAvgImmuneTimeS(time)

    # ...change infection radius
    def changeInfectionRadius(self, radius):
        if self.simulation:
            self.simulation.changeInfectionRadiusS(radius)

    def changeSpeedOfSim(self, newSpeed):
        self.timer.start(int(1000/newSpeed))

    # connect elements of the view
    def _connectUIElements(self) -> None:
        # elements of the main window
        self.ui.startSimulationSignal.connect(self.startSimulation)
        self.ui.pauseSimulationSignal.connect(self.pauseSimulation)
        self.ui.resumeSimulationSignal.connect(self.resumeSiumlation)
        self.ui.resetSimulationSignal.connect(self.resetSimulation)
        self.ui.exportCsvSignal.connect(self.exportCsv)
        self.ui.riskOfInfectionSignal.connect(self.changeRiskOfI)
        self.ui.rateOfDeathSignal.connect(self.changeRate)
        self.ui.riskOfQuarantineSignal.connect(self.changeRiskOfQ)
        self.ui.avgInfectionTimeSignal.connect(self.changeAvgInfectedTime)
        self.ui.avgImmuneTimeSignal.connect(self.changeAvgImmuneTime)
        self.ui.infectionRadiusSignal.connect(self.changeInfectionRadius)
        self.ui.speedOfSimSignal.connect(self.changeSpeedOfSim)
