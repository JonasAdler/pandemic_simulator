from model.healthconditions import healthconditions

class MyParticle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = None # possible directions: NW(Nord-West), NO(Nord-Ost), SW(Süd-West), SO(Süd-Ost)
        # self.status = healthconditions.HEALTHY  -> Enum eventuell überflüssig
        self.status = "HEALTHY" # possible status: HEALTHY, INFECTED, DECEASED, IMMUNE
