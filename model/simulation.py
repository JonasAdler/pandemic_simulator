import random
import model.myParticle
import csv
from model.healthconditions import healthconditions

class Simulation:
    def __init__(self, amountOfParticles, initiallyInfected, riskOfInfection, rateOfDeath, riskOfQuarantine,
                 avgInfectedTime, avgImmuneTime, infectionRadius, modifierDeflect, modifierHealthcare, modifierVaccine,
                 socialDistancingRadius, vaccineDays, healthCareCapacity, deathRateMultiplier):
        print("Simulation Created")

        self.stepCounter = 0

        self.boundary = 492

        # default-parameters for all the necessary values
        self.amountOfParticles = amountOfParticles
        self.initiallyInfected = initiallyInfected
        self.riskOfInfection = riskOfInfection
        self.rateOfDeath = rateOfDeath
        self.riskOfQuarantine = riskOfQuarantine
        self.avgInfectedTime = avgInfectedTime
        self.avgImmuneDays = avgImmuneTime
        self.infectionRadius = infectionRadius
        self.socialDistancingRadius = socialDistancingRadius
        self.vaccineDays = vaccineDays

        # create a reference value that saves the given
        self.rateOfDeathReference = rateOfDeath

        self.dayLength = 60
        self.healthCareCapacity = healthCareCapacity  # capacity of 65 percent of all particles
        self.deathRateMultiplier = deathRateMultiplier

        self.countHealthy = amountOfParticles - initiallyInfected
        self.countInf = initiallyInfected
        self.countImmune = 0
        self.countDeceased = 0
        self.countStillAlive = amountOfParticles - self.countDeceased
        self.quantityList = [[0, self.countHealthy, self.countInf, self.countImmune,
                              self.countDeceased, self.countStillAlive]]

        self.particleList = {}

        self.modifierDeflectEnabled = modifierDeflect
        self.modifierHealthCareEnabled = modifierHealthcare
        self.modifierVaccineEnabled = modifierVaccine

        # create the selected amount of particles
        self.createParticle()

    # changes the risk of infection
    def changeRiskOfInfectionS(self, rOI):
        self.riskOfInfection = rOI

    # changes the rate of death
    def changeRateOfDeathS(self, rOD):
        self.rateOfDeath = rOD

    # changes the risk of quarantine
    def changeRiskOfQuarantineS(self, rOQ):
        self.riskOfQuarantine = rOQ

    # changes the average infected time
    def changeAvgInfectedTimeS(self, avgInfTime):
        self.avgInfectedTime = avgInfTime

    # changes the average immune time
    def changeAvgImmuneTimeS(self, avgImmuneTime):
        self.avgImmuneDays = avgImmuneTime

    # changes the infection radius
    def changeInfectionRadiusS(self, radius):
        self.infectionRadius = radius

    def increaseDeathRate(self):
        # increase rate of death
        self.rateOfDeath = self.rateOfDeathReference * self.deathRateMultiplier

    # perform a step
    def performStep(self):

        self.stepCounter += 1

        # we want each particle to move with a constant amount of time in between, so that the simulation looks smooth
        # ->Solution: Moving a particle with each step the program makes.

        self.moveParticle()

        # we also want to change the state of the particles after contact with infected ones

        self.infectParticle()

        # deflect the particles if it is enabled
        if self.modifierDeflectEnabled:
            self.changeDirectionAfterCollision()

        if self.modifierHealthCareEnabled:
            # if more then "self.healthCareCapacity" of the population is infected -> Increase death rate
            if 100 * self.countInf / self.amountOfParticles > self.healthCareCapacity:
                self.increaseDeathRate()
            # otherwise reset the rate of death to the selected value
            else:
                self.rateOfDeath = self.rateOfDeathReference

        # one day equals 60 steps or 1 second
        # operations that have to occur just once a day
        if self.stepCounter % self.dayLength == 0:
            day = int(self.stepCounter / self.dayLength)

            # vaccinate particles each day
            if self.modifierVaccineEnabled:
                if day >= self.vaccineDays:
                    self.vaccinateParticles()

            # change the amount of infected days, immune days, ... for each particle
            # or, by chance kill or quarantine an infected particle
            self.changeStatus()

            # log the quantity of each group inside a list of lists
            self.quantityList.append([int(self.stepCounter/self.dayLength), self.countHealthy, self.countInf,
                                      self.countImmune, self.countDeceased, self.countStillAlive])
            print("Days passed since the outbreak: {}".format(day))



    def getDays(self):
        return int(self.stepCounter / self.dayLength)

    def getStepCounter(self):
        return self.stepCounter

    # returns the list of myParticles to the presenter
    def getParticleList(self):
        return self.particleList

    # returns the quantityList -> contains the quantity of each group for each day
    def getQuantityList(self):
        return self.quantityList

    # creates myParticle that holds the necessary parameters for each particle
    def createParticle(self):
        for i in range(self.amountOfParticles):
            # creating a particle object and saving it in a list
            randomX = random.randint(0, self.boundary)
            randomY = random.randint(0, self.boundary)

            # create a particle
            self.particleList[i] = model.myParticle.MyParticle(randomX, randomY)

            # give the particle a random start-direction
            self.setDirection(i)

        # infect
        for i in range(self.initiallyInfected):
            self.particleList[i].status = "INFECTED"
            self.particleList[i].daysInfected = random.randint(self.avgInfectedTime - 2, self.avgInfectedTime + 2)

    # moves the particle in a random direction, but will not let it go out of bounds
    def moveParticle(self):
        for i in range(self.amountOfParticles):
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
            if 0 < self.particleList[i].x + dx < self.boundary and 0 < self.particleList[i].y + dy < self.boundary:
                self.particleList[i].x = self.particleList[i].x + dx
                self.particleList[i].y = self.particleList[i].y + dy
            else:
                newDirection = random.randint(1, 2)

                if self.particleList[i].x + dx >= self.boundary:  # only possible direction is West
                    if newDirection == 1:
                        self.particleList[i].direction = "NW"
                    if newDirection == 2:
                        self.particleList[i].direction = "SW"

                elif self.particleList[i].x + dx <= 0:  # only possible direction is East
                    if newDirection == 1:
                        self.particleList[i].direction = "NO"
                    if newDirection == 2:
                        self.particleList[i].direction = "SO"

                elif self.particleList[i].y + dy >= self.boundary:  # only possible direction is North
                    if newDirection == 1:
                        self.particleList[i].direction = "NW"
                    if newDirection == 2:
                        self.particleList[i].direction = "NO"

                elif self.particleList[i].y + dy <= 0:  # only possible direction is South
                    if newDirection == 1:
                        self.particleList[i].direction = "SW"
                    if newDirection == 2:
                        self.particleList[i].direction = "SO"

                # process through the same particle again
                i = i - 1

    # will change the state of a particle after colliding with another
    def infectParticle(self):
        # iterate over the particles (only to the second last, see for loop in "MyParticle.collidesWith()")
        for i in range(self.amountOfParticles - 1):
            randomRisk = random.randint(0, 1000)

            # check for collisions
            self.particleList[i].collidesWith(self.particleList, i, self.infectionRadius, self.socialDistancingRadius)

            # if a collision has been detected for the particle
            if len(self.particleList[i].infectionCollisions) > 0:
                for j in self.particleList[i].infectionCollisions:
                    if randomRisk < self.riskOfInfection:
                        # either "i" is infected infects "j"...
                        if (self.particleList[i].status == "INFECTED") and (self.particleList[j].status == "HEALTHY"):
                            self.particleList[j].status = "INFECTED"
                            # deviation of 25% of the selected average -> Infection time different for each particle
                            self.particleList[j].daysInfected = random.randint(self.avgInfectedTime -
                                                                               int(self.avgInfectedTime*0.25),
                                                                               self.avgInfectedTime +
                                                                               int(self.avgInfectedTime*0.25))
                        # ...or "i" is healthy and gets infected by "j"
                        if (self.particleList[i].status == "HEALTHY") and (self.particleList[j].status == "INFECTED"):
                            self.particleList[i].status = "INFECTED"
                            self.particleList[i].daysInfected = random.randint(self.avgInfectedTime -
                                                                               int(self.avgInfectedTime*0.25),
                                                                               self.avgInfectedTime +
                                                                               int(self.avgInfectedTime*0.25))

    # change directions if particles collide
    def changeDirectionAfterCollision(self):
        for i in range(self.amountOfParticles - 1):
            if len(self.particleList[i].deflectionCollisions) > 0:
                # dead and quarantined particles are excluded from collisions
                if (self.particleList[i].status != "DECEASED" and
                        self.particleList[i].status != "QUARANTINED"):
                    for j in self.particleList[i].deflectionCollisions:
                        if (self.particleList[j].status != "DECEASED" and
                                self.particleList[j].status != "QUARANTINED"):
                            # give the particles new directions
                            self.setOppositeDirection(i, j)

    # vaccinates particles
    def vaccinateParticles(self):
        # per day at least 1 and a maximum of 5% of the population get a vaccine
        vaccinationsPerDay = random.randint(1, int(self.amountOfParticles*0.05))
        for i in range(self.amountOfParticles):
            # vaccinate particles with the necessary conditions
            if not self.particleList[i].isVaccinated and self.particleList[i].status == "HEALTHY":
                self.particleList[i].isVaccinated = True
                self.particleList[i].status = "IMMUNE"
                # assumption that the vaccine will not subside in the small time frame of the simulator
                self.particleList[i].immuneDays = 99999
                vaccinationsPerDay = vaccinationsPerDay - 1
            # stop if there are no vaccines left for the day
            if vaccinationsPerDay == 0:
                break

    # changes the behaviour of each particle for the different conditions
    def changeStatus(self):
        # reset the counters -> recounting in the loop after changes are made
        self.countInf = 0
        self.countHealthy = 0
        self.countImmune = 0
        self.countDeceased = 0

        for i in range(self.amountOfParticles):
            randomDeath = random.randint(0, 1000)
            randomQuarantine = random.randint(0, 1000)
            # disease process for an infected particle, if it survives it will be immune for a certain time
            # has also a certain chance to be quarantined, where it cannot infect anyone

            if self.particleList[i].daysInfected > 0:
                self.updateInfected(i, randomDeath, randomQuarantine)

            # reducing the quarantine time for quarantined particle
            if self.particleList[i].daysQuarantined > 0:
                self.updateQuarantined(i, randomDeath)

            # reducing the immune time for an immune particle
            if self.particleList[i].daysImmune > 0:
                self.updateImmune(i)

            # changeStatus is the last method of the main loop, that changes a particles state
            # therefore it makes sense to log the amount of particles for each status here
            # -> No need for another for-loop
            self.countGroups(i)
            self.countStillAlive = self.amountOfParticles - self.countDeceased

    # necessary interactions with infected particles
    def updateInfected(self, i, randomDeath, randomQuarantine):

        self.particleList[i].daysInfected = self.particleList[i].daysInfected - 1

        # if a particle is still infected and the probability occurs -> kill the particle
        if randomDeath < self.rateOfDeath and self.particleList[i].daysInfected > 0:
            self.particleList[i].status = "DECEASED"
            self.particleList[i].daysInfected = 0
            self.particleList[i].direction = None

        # if a particle is still infected and the probability occurs -> quarantine the particle
        if randomQuarantine < self.riskOfQuarantine and self.particleList[i].daysInfected > 0:
            self.particleList[i].status = "QUARANTINED"
            self.particleList[i].direction = None
            self.particleList[i].daysQuarantined = self.particleList[i].daysInfected + 1
            self.particleList[i].daysInfected = 0

        # if the particle survived the infection -> set the status to "IMMUNE"
        if self.particleList[i].daysInfected == 0 and self.particleList[i].status == "INFECTED":
            self.particleList[i].status = "IMMUNE"
            # + 1 because it will immediately be decremented in the same method once
            self.particleList[i].daysImmune = random.randint(self.avgImmuneDays - int(self.avgImmuneDays*0.25),
                                                             self.avgImmuneDays + int(self.avgImmuneDays*0.25)) + 1

    # necessary interactions with quarantined particles
    def updateQuarantined(self, i, randomDeath):
        self.particleList[i].daysQuarantined = self.particleList[i].daysQuarantined - 1

        # particles can still die in quarantine
        if randomDeath < self.rateOfDeath and self.particleList[i].daysQuarantined > 0:
            self.particleList[i].status = "DECEASED"
            self.particleList[i].direction = None

        # release one from quarantine after time is over
        if self.particleList[i].daysQuarantined == 0 and self.particleList[i].status == "QUARANTINED":
            self.particleList[i].status = "IMMUNE"
            self.particleList[i].daysImmune = random.randint(self.avgImmuneDays - int(self.avgImmuneDays*0.25),
                                                             self.avgImmuneDays + int(self.avgImmuneDays*0.25)) + 1
            self.setDirection(i)  # if the particle was quarantined it needs a new direction

    # necessary interactions with immune particles
    def updateImmune(self, i):
        self.particleList[i].daysImmune = self.particleList[i].daysImmune - 1
        if self.particleList[i].daysImmune == 0 and self.particleList[i].status == "IMMUNE":
            self.particleList[i].status = "HEALTHY"

    # count each group
    def countGroups(self, i):
        if self.particleList[i].status == "HEALTHY":
            self.countHealthy = self.countHealthy + 1
        # assumption: as long as a particle is quarantined it counts as infected
        elif self.particleList[i].status == "INFECTED" \
                or self.particleList[i].status == "QUARANTINED":
            self.countInf = self.countInf + 1

        elif self.particleList[i].status == "IMMUNE":
            self.countImmune = self.countImmune + 1

        elif self.particleList[i].status == "DECEASED":
            self.countDeceased = self.countDeceased + 1

    # gives random direction to particle at position "i"
    def setDirection(self, i):
        direction = random.randint(1, 4)
        if direction == 1:
            self.particleList[i].direction = "NO"
        if direction == 2:
            self.particleList[i].direction = "NW"
        if direction == 3:
            self.particleList[i].direction = "SO"
        if direction == 4:
            self.particleList[i].direction = "SW"

    def setOppositeDirection(self, i, j):
        randomLeavingNumber = random.randint(1, 100)
        if self.particleList[i].direction == "NW":
            self.particleList[i].direction = "SO"

        elif self.particleList[i].direction == "SW":
            self.particleList[i].direction = "NO"

        elif self.particleList[i].direction == "NO":
            self.particleList[i].direction = "SW"

        elif self.particleList[i].direction == "SO":
            self.particleList[i].direction = "NW"
        # with a 5% chance, two "stuck" particles will try to part ways (otherwise they may be "talking" forever)
        if randomLeavingNumber < 5:
            return
        else:
            if self.particleList[j].direction == "NW":
                self.particleList[j].direction = "SO"

            elif self.particleList[j].direction == "SW":
                self.particleList[j].direction = "NO"

            elif self.particleList[j].direction == "NO":
                self.particleList[j].direction = "SW"

            elif self.particleList[j].direction == "SO":
                self.particleList[j].direction = "NW"
