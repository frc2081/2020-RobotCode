import wpilib
from enum import IntEnum
import interfacesModule
import robot
import ioModule
from networktables import NetworkTables

class indexerSystem():

    mIndexerDesAng = 0 #internal value of indexer desired angle
    mIndexerDesAngRamped = 0 #internal value of indexer with rate of change limit applied
    mIndexerIncrement = 120 #distance in degrees to move the indexer when it is commanded to move to the next Angition
    mIndexerAllowedAngError = 5 #distance in degrees before indexer is considered to have been moved manually out of position
 
    mIndexerAdvanceSpd = 60 #rate in degrees per second to move the indexer when it is advancing to the next position
    mIndexerReverseSpd = 60 #rate in degrees per second to move ht indexer when it is reverseing to the previous position

    def __init__(self, interfaces):
        pass

    def teleopInit(self, interfaces):
        pass

    def teleopPeriodic(self, interfaces):
        
        if(interfaces.mIndexerAdvance):
            self.mIndexerDesAng += self.mIndexerIncrement
        elif(interfaces.mIndexerReverse):
            self.mIndexerDesAng -= self.mIndexerIncrement

        #Keep indexer desired position in sync when indexer is being moved via manual control
        #if indexer moves past next or previous increment under manual control, set the desired position to that increment
        if(interfaces.indexerActAng > (self.mIndexerDesAng + self.mIndexerIncrement + self.mIndexerAllowedAngError)):
            self.mIndexerDesAng = self.mIndexerDesAng + self.mIndexerIncrement
        elif(interfaces.indexerActAng < (self.mIndexerDesAng - self.mIndexerIncrement - self.mIndexerAllowedAngError)):
            self.mIndexerDesAng =self.mIndexerDesAng - self.mIndexerIncrement

        if((self.mIndexerDesAngRamped < self.mIndexerDesAng + self.mIndexerAllowedAngError) and (self.mIndexerDesAngRamped > self.mIndexerDesAng - self.mIndexerAllowedAngError)):
            self.mIndexerDesAngRamped = self.mIndexerDesAng
        elif(self.mIndexerDesAng > self.mIndexerDesAngRamped):
            self.mIndexerDesAngRamped += (self.mIndexerAdvanceSpd * interfaces.robotUpdatePeriod)
        elif(self.mIndexerDesAng < self.mIndexerDesAngRamped):
            self.mIndexerDesAngRamped -= (self.mIndexerReverseSpd * interfaces.robotUpdatePeriod)

        interfaces.indexerDesAng = self.mIndexerDesAngRamped