from model import simulation
from model.healthconditions import healthconditions

class MyParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = None  # possible directions: NW(Nord-West), NO(Nord-Ost), SW(Süd-West), SO(Süd-Ost)
        # self.status = healthconditions.HEALTHY  -> Enum eventuell überflüssig
        self.status = "HEALTHY"  # possible status: HEALTHY, INFECTED, DECEASED, IMMUNE, QUARANTINED
        self.daysInfected = 0
        self.daysImmune = 0
        self.daysQuarantined = 0
        # stores the position of the particles in the list that collide with this particle object
        self.collisions = []

    def collidesWith(self, particleList, i, infectionRadius):
        # reset the colliding particles for each function call
        self.collisions = []
        # iterate over the list starting with the "next" particle
        # -> every particle with a position smaller than "i" has already been compared to "i"
        for j in range(i + 1, len(particleList)):
            if abs(particleList[i].x - particleList[j].x) < infectionRadius and \
                    abs(particleList[i].y - particleList[j].y) < infectionRadius:
                # append the list for the particle
                self.collisions.append(j)