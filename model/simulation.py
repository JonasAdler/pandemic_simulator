import random
import model.myParticle
from model.healthconditions import healthconditions

class Simulation:
    def __init__(self):
        print("Simulation Created")
        self.stepCounter = 0
        self.particleList = {}
        self.createParticle()

    def performStep(self):
        self.stepCounter += 1
        print("Simulation step {} processed.".format(self.stepCounter))
        # We want each particle to move with a constant amount of time in between, so that the simulation looks smooth
        # ->Solution: Moving a particle with each step the program makes.
        # We also want to update the state of the particle after moving it.

        self.moveParticle()
        self.changeState()

    def getData(self):
        return self.stepCounter

    # returns the list of myParticles to the presenter
    def getParticleList(self):
        return self.particleList

    # creates myParticle that holds the needed parameters for each particle
    def createParticle(self):
        for i in range(0, 50):
            self.particleList[i] = model.myParticle.MyParticle(random.randint(0, 492), random.randint(0, 492), 8, 8) # Erstellen eines Partikel-Objekts
        for i in range(45, 50):
            self.particleList[i].status = "INFECTED"

    # moves the particle in a random direction, but will not let it go out of bounds
    def moveParticle(self):
        for i in range(0, 50):
            dx = random.randint(-2, 2) # random directions are selected for the particle to move to, negative is left, positive is right
            dy = random.randint(-2, 2) # random directions are selected for the particle to move to, negative is upwards, positive is downwards
            if 0 < self.particleList[i].x + dx < 492 and 0 < self.particleList[i].y + dy < 492:
                self.particleList[i].x = self.particleList[i].x + dx
                self.particleList[i].y = self.particleList[i].y + dy
            else:  # if the particle-position exceeds one of those boundaries we will recalculate another value for it by going through it one more time in the loop
                i = i - 1

    # Will change the state of a particle after colliding with another
    # (ToDo/Question: Could this be made more efficient?)
    def changeState(self):
        for i in range(0, 50):
            for j in range(0, 50):
                riskOfInf = random.randint(0, 100)  # new number has to be generated inside a loop,
                # otherwise there may be multiple infections at once
                if i != j:
                    if abs(self.particleList[i].x - self.particleList[j].x) < 10 and \
                            abs(self.particleList[i].y - self.particleList[j].y) < 10 and \
                            (self.particleList[i].status == "INFECTED" or self.particleList[j].status == "INFECTED"):  # an assembly of necessary conditions
                        # Accuracy has to be adjustable by the user ("< 10" -> infection radius)
                        if riskOfInf < 90: # variable name # -> just a reminder, not the actual risk as it is the random number # (0,5% would be the risk here)
                            self.particleList[i].status = "INFECTED"
