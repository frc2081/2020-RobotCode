import wpilib
from enum import IntEnum
import interfacesModule
import robot
import ioModule
from networktables import NetworkTables

class intakeSystem():

    class intakeStates(IntEnum):
        Idle = 1 #Intake raised
        Running = 2 #In position to grab a ball, waiting for one to be detected
        Loading = 3 #Moving a ball upwards into the robot

    intakeState = intakeStates.Idle #Current state of the intake state machine

    intakeWheelSpdHold = 0 #intake speed to run when the intake is "idle" set to non-zero to hold balls in position at top of intake
    intakeWheelSpdLoading = -.5 # intake speed to run when moving a ball from the ground into the robot
    intakeWheelSpdRunning = -1 # intake speed to run when intake is lowered and pulling balls in

    intakePosLowered = 80 #intake position in degrees of "lowered" position for intaking baslls
    intakePosRaised = -8#-15 intake position in degrees when it is "raised." Same as intake starting position
    intakeRaisedThreshold = intakePosRaised + 5 #Threshold to consider the intake to be in the "raised" position
    intakeLoweredThreshold = intakePosLowered - 10 #Threshold to consider the intake to be in the "raised" position
    intakeAllowedPosError = 1 #Allowed intake positon error in degrees

    intakeLoweringSpd = 60 #45degrees per second to move the intake when lowering it
    intakeRaisingSpd = 20 #degrees per secont to move the intake when raising it
    
    mIntakeActPos = 0 #internal actual position of the intake arm
    mIntakeDesPos = 0 #internal desired position of the intake arm
    mIntakeDesPosRamped = 0 #desired intake position with a ramp applied
    mIntakeSpeed = 0 #internal desired speed of the intake wheels


    def __init__(self, interfaces):
        self.mIntakeActPos = 0 #internal actual position of the intake arm
        self.mIntakeDesPos = 0 #internal desired position of the intake arm
        self.mIntakeSpeed = 0 #internal desired speed of the intake wheels

    def init(self, interfaces):
        interfaces.intakeDesiredPos = 0

    def teleopPeriodic(self, interfaces):
        
        self.mIntakeActPos = interfaces.intakeActualPos

        if(self.intakeState == self.intakeStates.Idle):
            self.mIntakeSpeed = self.intakeWheelSpdHold
            self.mIntakeDesPos = self.intakePosRaised

            #transition conditions
            if(interfaces.dBallIntake == True):
                self.intakeState = self.intakeStates.Running

        elif(self.intakeState == self.intakeStates.Running):
            self.mIntakeSpeed = self.intakeWheelSpdRunning
            self.mIntakeDesPos = self.intakePosLowered          

            #transition conditions
            if((interfaces.intakeBallDetected == True) and interfaces.intakeActualPos > self.intakeLoweredThreshold):
                self.intakeState = self.intakeStates.Loading
            elif(interfaces.dBallIntake == False):
                self.intakeState = self.intakeStates.Idle

        elif(self.intakeState == self.intakeStates.Loading):
            self.mIntakeSpeed = self.intakeWheelSpdLoading
            self.mIntakeDesPos = self.intakePosRaised

            #transition conditions
            if(interfaces.intakeActualPos < self.intakeRaisedThreshold):
                self.intakeState = self.intakeStates.Idle
        
        #Code to ramp the intake desired position up and down slowly to prevent the PID controller from slamming it against the hard stops
        #Step 1: Check if the ramped position is near the desired position. If it is, just set them equal.
        #Step 2: Otherwise, increment the ramped desired position toward the final desired position        
        if((self.mIntakeDesPosRamped < self.mIntakeDesPos + self.intakeAllowedPosError) and (self.mIntakeDesPosRamped > self.mIntakeDesPos - self.intakeAllowedPosError)):
            self.mIntakeDesPosRamped = self.mIntakeDesPos
        elif(self.mIntakeDesPos > self.mIntakeDesPosRamped):
            self.mIntakeDesPosRamped += (self.intakeLoweringSpd * interfaces.robotUpdatePeriod)
        elif(self.mIntakeDesPos < self.mIntakeDesPosRamped):
            self.mIntakeDesPosRamped -= (self.intakeRaisingSpd * interfaces.robotUpdatePeriod)

        #Set final desired values to send to hardware
        interfaces.intakeDesiredPos = self.mIntakeDesPosRamped
        interfaces.intakeWheelSpeed = self.mIntakeSpeed

        print(self.intakeState)