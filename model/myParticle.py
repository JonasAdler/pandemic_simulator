import random
import numpy as np
from resources import constVariables

class MyParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = None  # possible directions: NW(North-West), NO(North-East), SW(South-West), SO(South-East)
        self.status = constVariables.healthy  # possible status: HEALTHY, INFECTED, DECEASED, IMMUNE, QUARANTINED
        self.daysInfected = 0  # duration of infection
        self.daysImmune = 0  # duration of immunity
        self.daysQuarantined = 0  # duration of quarantine

        # stores the position of the particles (in the particle list) that...
        self.infectionCollisions = []  # ... are within the infection radius of this particle
        # ... are in the personal space of this particle
        self.deflectionCollisions = []
        self.isVaccinated = False  # is the particle vaccinated

    def collidesWith(self, particleList, i, infectionRadius, socialDistancingRadius, deflectEnabled):
        # reset the colliding particles for each function call
        self.infectionCollisions = []
        self.deflectionCollisions = []
        # iterate over the list starting with the "next" particle
        # -> every particle with a position smaller than "i" has already been compared to "i"
        for j in range(i + 1, len(particleList)):

            if np.sqrt(abs(self.x - particleList[j].x)**2 + abs(self.y - particleList[j].y)**2) <= infectionRadius + constVariables.particleSize:
                self.infectionCollisions.append(j)
            # differentiate in collision method between social distancing enabled/disabled
            if deflectEnabled:
                if np.sqrt(abs(self.x - particleList[j].x)**2 + abs(self.y - particleList[j].y)**2) <= socialDistancingRadius + constVariables.particleSize:
                    self.deflectionCollisions.append(j)
            else:
                if np.sqrt(abs(self.x - particleList[j].x)**2 + abs(self.y - particleList[j].y)**2) <= constVariables.particleSize:
                    self.deflectionCollisions.append(j)

    # moves the particle in a random direction, but will not let it go out of bounds
    def moveParticle(self):
        if self.direction == constVariables.NE:
            dx = 1
            dy = -1
        elif self.direction == constVariables.NW:
            dx = -1
            dy = -1
        elif self.direction == constVariables.SE:
            dx = 1
            dy = 1
        elif self.direction == constVariables.SW:
            dx = -1
            dy = 1
        else:
            dx = 0
            dy = 0

        # if possible, move the particle
        if constVariables.particleSize/2 < self.x + dx < constVariables.boundary \
                and constVariables.particleSize/2 < self.y + dy < constVariables.boundary:
            self.x = self.x + dx
            self.y = self.y + dy
        else:
            newDirection = random.randint(1, 2)

            if self.x + dx >= constVariables.boundary:  # only possible direction is West
                if newDirection == 1:
                    self.direction = constVariables.NW
                if newDirection == 2:
                    self.direction = constVariables.SW

            elif self.x + dx <= constVariables.particleSize/2:  # only possible direction is East
                if newDirection == 1:
                    self.direction = constVariables.NE
                if newDirection == 2:
                    self.direction = constVariables.SE

            elif self.y + dy >= constVariables.boundary:  # only possible direction is North
                if newDirection == 1:
                    self.direction = constVariables.NW
                if newDirection == 2:
                    self.direction = constVariables.NE

            elif self.y + dy <= constVariables.particleSize/2:  # only possible direction is South
                if newDirection == 1:
                    self.direction = constVariables.SW
                if newDirection == 2:
                    self.direction = constVariables.SE

            # process through the same particle again
            self.moveParticle()

    # gives random direction to particle at position "i"
    def setDirection(self):
        direction = random.randint(1, 4)
        if direction == 1:
            self.direction = constVariables.NE
        if direction == 2:
            self.direction = constVariables.NW
        if direction == 3:
            self.direction = constVariables.SE
        if direction == 4:
            self.direction = constVariables.SW
