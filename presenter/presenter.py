from PyQt5 import QtCore

from resources import constVariables
from view.view import View
from model.simulation import Simulation
from view.viewEndWindow import ViewEndWindow
from view.viewGranularity import ViewGranularityWindow
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

        # create a second window
        self.endWindow = ViewEndWindow()
        self.endWindow.hide()
        self.endWindowGotClosed = False

        # create granularity window
        self.granularityWindow = ViewGranularityWindow()
        self.granularityWindow.hide()

        self._connectUIElements()

    # perform the steps and draw the items on the scene for each step while the simulation is running
    def mainLoop(self):
        if self.isSimulationRunning:
            self.simulation.performStep()
            self.ui.drawItems(self.simulation.getParticleList())
            self.ui.updateScene()
            self.ui.updateElements(self.simulation.getDays(), self.simulation.getQuantityList())

            # track if the simulation is finished
            if self.simulation.getIsFinished() and not self.endWindowGotClosed:
                # pause the "main window"
                self.ui.pauseSimulationClicked()
                # update and show the "end window"
                self.endWindow.updateElements(self.simulation.getQuantityList(),
                                              self.simulation.getHealthCareModifier(), self.simulation.getCapacity())
                self.endWindow.show()
                # ensures that the end window will not pop up again, even if user resumes the simulation
                self.endWindowGotClosed = True

    # create the simulation and hand it all the predetermined values
    def startSimulation(self, amountOfParticles, initiallyInfected, riskOfInfection, rateOfDeath, riskOfQuarantine,
                        avgInfectedTime, avgImmuneTime, infectionRadius, modifierDeflect, modifierHealth,
                        modifierVaccine, socialDistanceRadius, vaccineDays, healthCareCapacity, deathRateMultiplier):
        self.isSimulationRunning = True
        self.simulation = Simulation(amountOfParticles, initiallyInfected, riskOfInfection, rateOfDeath,
                                     riskOfQuarantine, avgInfectedTime, avgImmuneTime, infectionRadius,
                                     modifierDeflect, modifierHealth, modifierVaccine, socialDistanceRadius,
                                     vaccineDays, healthCareCapacity, deathRateMultiplier)
        self.ui.startSimulation()

    # pause the simulation
    def pauseSimulation(self):
        self.isSimulationRunning = False

    # resume the simulation
    def resumeSiumlation(self):
        self.isSimulationRunning = True

    # reset the simulation
    def resetSimulation(self):
        self.isSimulationRunning = False
        # clean up the scene, enable showing "end window" and close the current "end window"
        self.ui.scene.clear()
        self.endWindowGotClosed = False
        self.endWindow.close()
        self.simulation = None

    # show the granularity window
    def showGranularityWindow(self):
        self.granularityWindow.exec_()

    # hand the given parameters with the quantityList to the write-Operation
    def exportCsv(self, granularity):
        path, filetype = self.ui.getExportParameters()
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

    # change the speed of the simulation
    def changeSpeedOfSim(self, newSpeed):
        self.timer.start(int(1000/newSpeed))

    # connect elements of the view
    def _connectUIElements(self) -> None:
        # elements of the main window
        self.ui.startSimulationSignal.connect(self.startSimulation)
        self.ui.pauseSimulationSignal.connect(self.pauseSimulation)
        self.ui.resumeSimulationSignal.connect(self.resumeSiumlation)
        self.ui.resetSimulationSignal.connect(self.resetSimulation)
        self.ui.exportCsvSignal.connect(self.showGranularityWindow)
        self.ui.riskOfInfectionSignal.connect(self.changeRiskOfI)
        self.ui.rateOfDeathSignal.connect(self.changeRate)
        self.ui.riskOfQuarantineSignal.connect(self.changeRiskOfQ)
        self.ui.avgInfectionTimeSignal.connect(self.changeAvgInfectedTime)
        self.ui.avgImmuneTimeSignal.connect(self.changeAvgImmuneTime)
        self.ui.infectionRadiusSignal.connect(self.changeInfectionRadius)
        self.ui.speedOfSimSignal.connect(self.changeSpeedOfSim)
        self.granularityWindow.granularitySelectedSignal.connect(self.exportCsv)
