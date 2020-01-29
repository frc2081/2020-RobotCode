import wpilib
from enum import Enum

class indexer():

    class indexerDuck(Enum):
        ballInFrontOfSensor = 1
        indexingBall = 2
        noBallInFrontOfSensor = 3
        stopped = 4

    def indexerInit(self):
        self.photosensor = wpilib.DigitalInput(0) #!photosensor in pin 0
        self.indexerMotor = wpilib.Talon(3) #!Change number for where it actualy is
        self.state = self.indexerDuck.noBallInFrontOfSensor #saying the state is there is no ball in front of the sensor
        self.indexerAngle = 120 #!placeholding for other input

    def indexerPeriodic(self):
        ballSeen = self.photosensor.get() #Gets photosensor data

        if self.state == self.indexerDuck.stopped:
        #"""If ball shot switch to doing other 3"""
            pass #placeholding
        
        #"""stays here till there is a ball in front of the photosensor"""
        elif self.state == self.indexerDuck.noBallInFrontOfSensor:
            print("There is no ball in front of the sensor")
            if ballSeen: 
                self.state = self.indexerDuck.ballInFrontOfSensor
                print("there is a ball in front of the sensor") #can be taken out later is to test code to test transfering between states

        #"""When there is a ball in front of the sensor go to index ball"""
        elif self.state == self.indexerDuck.ballInFrontOfSensor:
            if ballSeen: #If there is a ball in front of the sensor set state to index ball
                self.state = self.indexerDuck.indexingBall
                print("go to index the ball")

        #"""After ball is indexed there is no ball in front of the photo sensor wait till there is"""
        elif self.state == self.indexerDuck.indexingBall:
            #"""Need to put motor controls here"""
            print("ball indexed")
            if self.indexerAngle == 120:
                self.state = self.indexerDuck.noBallInFrontOfSensor