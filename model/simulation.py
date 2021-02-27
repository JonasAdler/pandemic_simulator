import random
import model.myParticle
from resources import constVariables


class Simulation:
    def __init__(self, amountOfParticles, initiallyInfected, riskOfInfection, rateOfDeath, riskOfQuarantine,
                 avgInfectedTime, avgImmuneTime, infectionRadius, modifierDeflect, modifierHealthcare, modifierVaccine,
                 socialDistancingRadius, vaccineDays, healthCareCapacity, deathRateMultiplier):
        print("Simulation Created")

        self.stepCounter = 0
        self.isSimulationFinished = False

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

        # create a reference value that saves the selected "rate of death" input
        self.rateOfDeathReference = rateOfDeath

        self.healthCareCapacity = healthCareCapacity
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
        for i in range(self.amountOfParticles):
            self.particleList[i].moveParticle()

        # we also want to change the state of the particles after contact with infected ones

        self.infectParticle()

        # particles deflect each other
        self.changeDirectionAfterCollision()

        # if the modifier is enabled -> ...
        if self.modifierHealthCareEnabled:
            # if more then "self.healthCareCapacity" of the population is infected -> Increase death rate
            if 100 * self.countInf / self.amountOfParticles > self.healthCareCapacity:
                self.increaseDeathRate()
            # otherwise reset the rate of death to the selected value
            else:
                self.rateOfDeath = self.rateOfDeathReference

        # one day equals 60 steps or 1 second
        # operations that have to occur just once a day
        if self.stepCounter % constVariables.dayLength == 0:
            day = int(self.stepCounter / constVariables.dayLength)

            # vaccinate particles each day if modifier enabled
            if self.modifierVaccineEnabled:
                if day >= self.vaccineDays:
                    self.vaccinateParticles()

            # change the amount of infected days, immune days, ... for each particle
            # or, by chance kill or quarantine an infected particle
            self.changeStatus()

            # log the quantity of each group inside a list of lists
            self.quantityList.append([int(self.stepCounter/constVariables.dayLength), self.countHealthy, self.countInf,
                                      self.countImmune, self.countDeceased, self.countStillAlive])

            # check if the simulation is finished
            self.isFinished(day)
            print("Days passed since the outbreak: {}".format(day))

    def getDays(self):
        return int(self.stepCounter / constVariables.dayLength)

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
            randomX = random.randint(0, constVariables.boundary)
            randomY = random.randint(0, constVariables.boundary)
            # create a particle
            self.particleList[i] = model.myParticle.MyParticle(randomX, randomY)
            # give the particle a random start-direction
            self.particleList[i].setDirection()

        # infect
        for i in range(self.initiallyInfected):
            self.particleList[i].status = constVariables.infected
            self.particleList[i].daysInfected = random.randint(self.avgInfectedTime - int(self.avgInfectedTime*0.25),
                                                               self.avgInfectedTime + int(self.avgInfectedTime*0.25))

    # will change the state of a particle after colliding with another
    def infectParticle(self):
        # iterate over the particles (only to the second last, see for loop in "MyParticle.collidesWith()")
        for i in range(self.amountOfParticles - 1):
            randomRisk = random.randint(0, 1000)
            deviationInfDays = int(self.avgInfectedTime*0.25)
            # check for collisions
            self.particleList[i].collidesWith(self.particleList, i, self.infectionRadius, self.socialDistancingRadius)

            # if a collision has been detected for the particle
            if len(self.particleList[i].infectionCollisions) > 0:
                for j in self.particleList[i].infectionCollisions:
                    if randomRisk < self.riskOfInfection:
                        # either "i" is infected infects "j"...
                        if (self.particleList[i].status == constVariables.infected) \
                                and (self.particleList[j].status == constVariables.healthy):
                            self.particleList[j].status = constVariables.infected
                            # deviation of 25% of the selected average -> Infection time different for each particle
                            self.particleList[j].daysInfected = random.randint(self.avgInfectedTime - deviationInfDays,
                                                                               self.avgInfectedTime + deviationInfDays)
                        # ...or "i" is healthy and gets infected by "j"
                        if (self.particleList[i].status == constVariables.healthy) \
                                and (self.particleList[j].status == constVariables.infected):
                            self.particleList[i].status = constVariables.infected
                            self.particleList[i].daysInfected = random.randint(self.avgInfectedTime - deviationInfDays,
                                                                               self.avgInfectedTime + deviationInfDays)

    # change directions if particles collide
    def changeDirectionAfterCollision(self):
        for i in range(self.amountOfParticles - 1):
            if len(self.particleList[i].deflectionCollisions) > 0:
                # dead and quarantined particles are excluded from collisions
                if (self.particleList[i].status != constVariables.deceased and
                        self.particleList[i].status != constVariables.quarantined):
                    for j in self.particleList[i].deflectionCollisions:
                        if (self.particleList[j].status != constVariables.deceased and
                                self.particleList[j].status != constVariables.quarantined):
                            # give the particles new directions
                            self.setOppositeDirection(i, j)

    # vaccinates particles
    def vaccinateParticles(self):
        # per day at least 1 and a maximum of 5% of the population get a vaccine
        vaccinationsPerDay = random.randint(1, int(self.amountOfParticles*0.05))
        for i in range(self.amountOfParticles):
            # vaccinate particles with the necessary conditions
            if not self.particleList[i].isVaccinated and self.particleList[i].status == constVariables.healthy:
                self.particleList[i].isVaccinated = True
                self.particleList[i].status = constVariables.immune
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
            self.particleList[i].status = constVariables.deceased
            self.particleList[i].daysInfected = 0
            self.particleList[i].direction = None

        # if a particle is still infected and the probability occurs -> quarantine the particle
        if randomQuarantine < self.riskOfQuarantine and self.particleList[i].daysInfected > 0:
            self.particleList[i].status = constVariables.quarantined
            self.particleList[i].direction = None
            self.particleList[i].daysQuarantined = self.particleList[i].daysInfected + 1
            self.particleList[i].daysInfected = 0

        # if the particle survived the infection -> set the status to constVariables.immune
        if self.particleList[i].daysInfected == 0 and self.particleList[i].status == constVariables.infected:
            self.particleList[i].status = constVariables.immune
            # + 1 because it will immediately be decremented in the same method once
            self.particleList[i].daysImmune = random.randint(self.avgImmuneDays - int(self.avgImmuneDays*0.25),
                                                             self.avgImmuneDays + int(self.avgImmuneDays*0.25)) + 1

    # necessary interactions with quarantined particles
    def updateQuarantined(self, i, randomDeath):
        self.particleList[i].daysQuarantined = self.particleList[i].daysQuarantined - 1
        deviationImmuneDays = int(self.avgImmuneDays*0.25)
        # particles can still die in quarantine
        if randomDeath < self.rateOfDeath and self.particleList[i].daysQuarantined > 0:
            self.particleList[i].status = constVariables.deceased
            self.particleList[i].direction = None

        # release one from quarantine after time is over
        if self.particleList[i].daysQuarantined == 0 and self.particleList[i].status == constVariables.quarantined:
            self.particleList[i].status = constVariables.immune
            self.particleList[i].daysImmune = random.randint(self.avgImmuneDays - deviationImmuneDays,
                                                             self.avgImmuneDays + deviationImmuneDays) + 1
            self.particleList[i].setDirection()  # if the particle was quarantined it needs a new direction

    # necessary interactions with immune particles
    def updateImmune(self, i):
        self.particleList[i].daysImmune = self.particleList[i].daysImmune - 1
        if self.particleList[i].daysImmune == 0 and self.particleList[i].status == constVariables.immune:
            self.particleList[i].status = constVariables.healthy

    # count each group
    def countGroups(self, i):
        if self.particleList[i].status == constVariables.healthy:
            self.countHealthy = self.countHealthy + 1
        # assumption: as long as a particle is quarantined it counts as infected
        elif self.particleList[i].status == constVariables.infected \
                or self.particleList[i].status == constVariables.quarantined:
            self.countInf = self.countInf + 1

        elif self.particleList[i].status == constVariables.immune:
            self.countImmune = self.countImmune + 1

        elif self.particleList[i].status == constVariables.deceased:
            self.countDeceased = self.countDeceased + 1

    def setOppositeDirection(self, i, j):
        movements = int(self.socialDistancingRadius * 0.2)
        # change direction for particle i
        if self.particleList[i].direction == constVariables.NW:
            self.particleList[i].direction = constVariables.SE
            for k in range(movements):
                self.particleList[i].moveParticle()

        elif self.particleList[i].direction == constVariables.SW:
            self.particleList[i].direction = constVariables.NE
            for k in range(movements):
                self.particleList[i].moveParticle()

        elif self.particleList[i].direction == constVariables.NE:
            self.particleList[i].direction = constVariables.SW
            for k in range(movements):
                self.particleList[i].moveParticle()

        elif self.particleList[i].direction == constVariables.SE:
            self.particleList[i].direction = constVariables.NW
            for k in range(movements):
                self.particleList[i].moveParticle()

        # change direction for particle j
        if self.particleList[j].direction == constVariables.NW:
            self.particleList[j].direction = constVariables.SE
            for k in range(movements):
                self.particleList[j].moveParticle()

        elif self.particleList[j].direction == constVariables.SW:
            self.particleList[j].direction = constVariables.NE
            for k in range(movements):
                self.particleList[j].moveParticle()

        elif self.particleList[j].direction == constVariables.NE:
            self.particleList[j].direction = constVariables.SW
            for k in range(movements):
                self.particleList[j].moveParticle()

        elif self.particleList[j].direction == constVariables.SE:
            self.particleList[j].direction = constVariables.NW
            for k in range(movements):
                self.particleList[j].moveParticle()

    def isFinished(self, day):
        # if no one is infected or all are dead
        if self.quantityList[day][2] == 0 or self.quantityList[day][4] == self.amountOfParticles:
            self.isSimulationFinished = True

    def getIsFinished(self):
        return self.isSimulationFinished
