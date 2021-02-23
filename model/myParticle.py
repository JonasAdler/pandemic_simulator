
class MyParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 8
        self.direction = None  # possible directions: NW(North-West), NO(North-East), SW(South-West), SO(South-East)
        self.status = "HEALTHY"  # possible status: HEALTHY, INFECTED, DECEASED, IMMUNE, QUARANTINED
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
            if abs(particleList[i].x - particleList[j].x) < infectionRadius and \
                    abs(particleList[i].y - particleList[j].y) < infectionRadius:
                self.infectionCollisions.append(j)

            # detect particles that collide directly with another particle
            if abs(particleList[i].x - particleList[j].x) < socialDistancingRadius and \
                    abs(particleList[i].y - particleList[j].y) < socialDistancingRadius:
                self.deflectionCollisions.append(j)
