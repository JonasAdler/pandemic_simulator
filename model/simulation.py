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

        self.moveParticle()

        # We also want to update the state of the particle after moving it.

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
            direction = random.randint(1, 4) # give the particle a random start-direction
            if direction == 1:
                self.particleList[i].direction = "NO"
            if direction == 2:
                self.particleList[i].direction = "NW"
            if direction == 3:
                self.particleList[i].direction = "SO"
            if direction == 4:
                self.particleList[i].direction = "NW"

        for i in range(49, 50): # ToDo: Userinout, give amount of infected particles for start of simulation
            self.particleList[i].status = "INFECTED"

    # moves the particle in a random direction, but will not let it go out of bounds
    def moveParticle(self):
        for i in range(0, 50):
            # tells the particle which way to move with its corresponding direction attribute
            if self.particleList[i].direction == "NO":
                dx = 1
                dy = -1
            if self.particleList[i].direction == "NW":
                dx = -1
                dy = -1
            if self.particleList[i].direction == "SO":
                dx = 1
                dy = 1
            if self.particleList[i].direction == "SW":
                dx = -1
                dy = 1
            # if possible, move the particle
            if 0 < self.particleList[i].x + dx < 492 and 0 < self.particleList[i].y + dy < 492:
                self.particleList[i].x = self.particleList[i].x + dx
                self.particleList[i].y = self.particleList[i].y + dy
            else:
                if self.particleList[i].x + dx >= 492:  # only possible direction is West
                    newdirection = random.randint(1, 2)
                    if newdirection == 1:
                        self.particleList[i].direction = "NW"
                    if newdirection == 2:
                        self.particleList[i].direction = "SW"
                elif self.particleList[i].x + dx <= 0:  # only possible direction is East
                    newdirection = random.randint(1, 2)
                    if newdirection == 1:
                        self.particleList[i].direction = "NO"
                    if newdirection == 2:
                        self.particleList[i].direction = "SO"
                elif self.particleList[i].y + dy >= 492:  # only possible direction is North
                    newdirection = random.randint(1, 2)
                    if newdirection == 1:
                        self.particleList[i].direction = "NW"
                    if newdirection == 2:
                        self.particleList[i].direction = "NO"
                elif self.particleList[i].y + dy <= 0:  # only possible direction is South
                    newdirection = random.randint(1, 2)
                    if newdirection == 1:
                        self.particleList[i].direction = "SW"
                    if newdirection == 2:
                        self.particleList[i].direction = "SO"
                # with elif this becomes more efficient, if we had just generated a random direction whenever the
                # particle hits a wall, there would be a 50% chance that the particle would go out of bounds again
                # as it can only go in the two opposite directions after hitting a wall -> 2/4 = 50%
                # still, this would only mean 50% more iterations through the for-loop,
                # which in our case would not make a difference -> maybe i will change that
                # for the sake of good code overview

                # process the same particle again
                i = i - 1

    # will change the state of a particle after colliding with another
    # (ToDo/Question: Could this be made more efficient?)
    def changeState(self):
        for i in range(0, 50):
            for j in range(0, 50):
                riskOfInf = random.randint(0, 100)
                if i != j:
                    # ToDo: change "10" to a user-changeable variable as it can be configured
                    if abs(self.particleList[i].x - self.particleList[j].x) < 10 and \
                            abs(self.particleList[i].y - self.particleList[j].y) < 10 and \
                            (self.particleList[i].status == "INFECTED" or self.particleList[j].status == "INFECTED"):  # an assembly of necessary conditions
                        # accuracy has to be adjustable by the user ("< 10" -> infection radius)
                        if riskOfInf < 5: # ToDo: variable name # -> just a reminder, not the actual risk as it is the random number # (0,5% would be the risk here)
                            self.particleList[i].status = "INFECTED"
