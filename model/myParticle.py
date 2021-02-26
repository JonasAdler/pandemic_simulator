import random

from resources import constVariables


class MyParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = None  # possible directions: NW(North-West), NO(North-East), SW(South-West), SO(South-East)
        self.status = constVariables.healthy  # possible status: HEALTHY, INFECTED, DECEASED, IMMUNE, QUARANTINED
        self.daysInfected = 0
        self.daysImmune = 0
        self.daysQuarantined = 0
        # stores the position of the particles (in the particle list) that...
        # ... are within the infection radius of this particle
        self.infectionCollisions = []
        # ... are in the personal space of this particle
        self.deflectionCollisions = []
        self.isVaccinated = False

    def collidesWith(self, particleList, i, infectionRadius, socialDistancingRadius):
        # reset the colliding particles for each function call
        self.infectionCollisions = []
        self.deflectionCollisions = []
        # iterate over the list starting with the "next" particle
        # -> every particle with a position smaller than "i" has already been compared to "i"
        for j in range(i + 1, len(particleList)):

            # detect particles that step into the infection radius of an infected particle
            if abs(self.x - particleList[j].x) < infectionRadius and \
                    abs(self.y - particleList[j].y) < infectionRadius:
                self.infectionCollisions.append(j)

            # detect particles that collide directly with another particle
            if abs(self.x - particleList[j].x) < socialDistancingRadius and \
                    abs(self.y - particleList[j].y) < socialDistancingRadius:
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
        if 0 < self.x + dx < constVariables.boundary \
                and 0 < self.y + dy < constVariables.boundary:
            self.x = self.x + dx
            self.y = self.y + dy
        else:
            newDirection = random.randint(1, 2)

            if self.x + dx >= constVariables.boundary:  # only possible direction is West
                if newDirection == 1:
                    self.direction = constVariables.NW
                if newDirection == 2:
                    self.direction = constVariables.SW

            elif self.x + dx <= 0:  # only possible direction is East
                if newDirection == 1:
                    self.direction = constVariables.NE
                if newDirection == 2:
                    self.direction = constVariables.SE

            elif self.y + dy >= constVariables.boundary:  # only possible direction is North
                if newDirection == 1:
                    self.direction = constVariables.NW
                if newDirection == 2:
                    self.direction = constVariables.NE

            elif self.y + dy <= 0:  # only possible direction is South
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
