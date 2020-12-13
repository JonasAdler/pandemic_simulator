from model.healthconditions import healthconditions

class MyParticle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.status = healthconditions.HEALTHY  -> Enum eventuell überflüssig
        self.status = "HEALTHY"
