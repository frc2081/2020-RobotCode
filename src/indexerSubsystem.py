import wpilib
from enum import IntEnum
import interfacesModule
import robot
import ioModule
from networktables import NetworkTables

class indexer():

    class indexerDuck(IntEnum):
        ballInFrontOfSensor = 1
        indexingBall = 2
        noBallInFrontOfSensor = 3

    def indexerInit(self, interfaces):
        self.sd = NetworkTables.getTable("SmartDashboard")
        self.state = self.indexerDuck.noBallInFrontOfSensor #saying the state is there is no ball in front of the sensor
        self.indexerAngle = 0
        self.counterBoi = 0


    def indexerPeriodic(self, interfaces):

        if (interfaces.mShootAgainstWall == True):
            interfaces.shooterTopSpeed = 100
            interfaces.shooterBottomSpeed = 100
            #Do the thing with the >< so it can index and do the thing idk what saying lets just do it!!!!
            if ((interfaces.shooterTopSpeedEncoder <= self.shooterTopSpeed + 5) and (interfaces.shooterTopSpeedEncoder >= self.shooterTopSpeed - 5) and (interfaces.shooterBottomSpeedEncoder <= self.shooterBottomSpeed + 5) and (interfaces.shooterBottomSpeedEncoder >= self.shooterBottomSpeed - 5)):
                self.state = self.indexerDuck.indexingBall

        if self.state == self.indexerDuck.noBallInFrontOfSensor: 
            #print("There is no ball in front of the sensor")
            if interfaces.photoSensorBack:
                self.state = self.indexerDuck.ballInFrontOfSensor
                #print("there is a ball in front of the sensor")
            self.counterBoi = 0
        
        elif self.state == self.indexerDuck.ballInFrontOfSensor:
            print("Photo sensor Back: " + str(interfaces.photoSensorBack))
            print("Photo sensor Front: " + str(interfaces.photoSensorFront))
            if(interfaces.photoSensorBack == True and interfaces.photoSensorFront == False):
                self.state = self.indexerDuck.indexingBall
                #print("go to index the ball")

        elif self.state == self.indexerDuck.indexingBall:
            #if the encder value is greater than the desired + 10 and less than 10 away from desired
            if self.counterBoi == 0:
                self.indexerAngle += 120
                self.counterBoi += 1
            if (interfaces.indexerEncoder <= self.indexerAngle + 5) and (interfaces.indexerEncoder >= self.indexerAngle - 5):
                self.state = self.indexerDuck.noBallInFrontOfSensor


        self.sd.putNumber("Indexer State", int(self.state))
        #print(self.indexerAngle)

        interfaces.indexerAngle = self.indexerAngle
        #print(interfaces.indexerEncoder)