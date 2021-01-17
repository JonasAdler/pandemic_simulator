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
