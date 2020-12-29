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

        # We want each particle to move with a constant amount of time in between, so that the simulation looks smooth
        # ->Solution: Moving a particle with each step the program makes.

        self.moveParticle()

        # We also want to change the state of the particles after contact with infected ones

        self.infectParticle()

        # one day equals 120 steps or 2 seconds,
        # we will also change the daysInfected and daysImmune for each particle each day
        if self.stepCounter % 120 == 0:
            self.changeStatus()
            print("Days passed since the outbreak: {}".format(self.stepCounter/120))

    def getData(self):
        return self.stepCounter

    # returns the list of myParticles to the presenter
    def getParticleList(self):
        return self.particleList

    # creates myParticle that holds the needed parameters for each particle
    def createParticle(self):
        for i in range(0, 50):
            # creating a particle object and saving it in a list
            self.particleList[i] = model.myParticle.MyParticle(random.randint(0, 492), random.randint(0, 492))

            # give the particle a random start-direction
            direction = random.randint(1, 4)
            if direction == 1:
                self.particleList[i].direction = "NO"
            if direction == 2:
                self.particleList[i].direction = "NW"
            if direction == 3:
                self.particleList[i].direction = "SO"
            if direction == 4:
                self.particleList[i].direction = "NW"

        for i in range(45, 50): # ToDo: user input, give amount of infected particles for start of simulation, zudem ist das hier provisorisch und sollte besser implementiert werden
            self.particleList[i].status = "INFECTED"
            self.particleList[i].daysInfected = random.randint(12, 14)  # ToDo: hardcoded, has to be interchangeable -> Idee: Frage nach average time, dann als min avg-2 und als max avg+2

    # moves the particle in a random direction, but will not let it go out of bounds
    def moveParticle(self):
        for i in range(0, 50):
            # tells the particle which way to move with its corresponding direction attribute
            if self.particleList[i].direction == "NO":
                dx = 1
                dy = -1
            elif self.particleList[i].direction == "NW":
                dx = -1
                dy = -1
            elif self.particleList[i].direction == "SO":
                dx = 1
                dy = 1
            elif self.particleList[i].direction == "SW":
                dx = -1
                dy = 1
            else:
                dx = 0
                dy = 0

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

                # process through the same particle again
                i = i - 1

    # will change the state of a particle after colliding with another
    # (ToDo/Question: Could this be made more efficient?)
    def infectParticle(self):
        for i in range(0, 50):
            for j in range(0, 50):
                riskOfInf = random.randint(0, 1000)
                if i != j:
                    # ToDo: change "10" to a user-changeable variable as it can be configured
                    if abs(self.particleList[i].x - self.particleList[j].x) < 10 and \
                            abs(self.particleList[i].y - self.particleList[j].y) < 10 and \
                            (self.particleList[i].status == "HEALTHY" and self.particleList[j].status == "INFECTED"):  # an assembly of necessary conditions
                        # accuracy has to be adjustable by the user ("< 10" -> infection radius)
                        if riskOfInf < 1000: # ToDo: change hardcoded % to user input -> 1000*"eingestellter Wert" liefert das richtige Ergebnis
                            self.particleList[i].status = "INFECTED"
                            self.particleList[i].daysInfected = random.randint(12, 14)  # ToDo: hardcoded infection time has to be interchangeable

    def changeStatus(self):
        for i in range(0, 50):
            riskOfDeath = random.randint(0, 1000)
            # disease process for an infected particle, if it survives it will be immune for a certain time
            if self.particleList[i].daysInfected > 0:
                self.particleList[i].daysInfected = self.particleList[i].daysInfected - 1
                if riskOfDeath < 100:  # ToDo: Hardcoded 50 has to be interchangeable
                    self.particleList[i].status = "DECEASED"
                    self.particleList[i].direction = None
                if self.particleList[i].daysInfected == 0 and self.particleList[i].status == "INFECTED":
                    self.particleList[i].status = "IMMUNE"
                    # + 1 because it will immediately be decremented in the same method once
                    self.particleList[i].daysImmune = random.randint(4, 6) + 1  # ToDo: hardcoded immune time has to be interchangeable

            # updating the immune time for an immune particle
            if self.particleList[i].daysImmune > 0:
                self.particleList[i].daysImmune = self.particleList[i].daysImmune - 1
                if self.particleList[i].daysImmune == 0 and self.particleList[i].status == "IMMUNE":
                    self.particleList[i].status = "HEALTHY"
