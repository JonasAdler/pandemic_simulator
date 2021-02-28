# constants for construction
dayLength = 60
FPS = 60
particleSize = 8
worldSize = 500
boundary = worldSize - particleSize/2

# health conditions
healthy = "HEALTHY"
infected = "INFECTED"
immune = "IMMUNE"
deceased = "DECEASED"
quarantined = "QUARANTINED"

# directions
NW = "NW"  # north west
SW = "SW"  # south west
NE = "NE"  # north east
SE = "SE"  # south east

# default values (for the GUI)
entitiesSpinBoxDefault = 50
initiallyInfectedSpinBoxDefault = 5
granularitySpinBoxDefault = 1

riskOfInfSpinBoxDefault = 10.0
rateOfDeathSpinBoxDefault = 1.0
percentageQuarantineSpinBoxDefault = 10.0
avgInfectionTimeSpinBoxDefault = 7
avgImmuneTimeSpinBoxDefault = 10
infectionRadiusSpinBoxDefault = 16

speedOfSimSliderDefault = 60
socialDistancingSpinBoxDefault = 8
vaccineDaysSpinBoxDefault = 15
healthCareCapacitySpinBoxDefault = 35
deathRateMultiplierSpinBoxDefault = 1.5

# programmer selected constants
deviation = 0.25
vaccinationsPerDayMax = 0.05
