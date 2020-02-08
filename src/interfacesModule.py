import wpilib
import ioModule
import robot

class interfaces:

    #CONTROLLER INPUTS
    #\/---------\/

    #driver controller
    dTurn = 0
    dMoveX = 0
    dMoveY = 0
    dBallIntake = False
    #self.dBallOther = False
    dClimbRelease = False
    dClimbWinch = 0

    #mechanism controller
    mSpinnyRaise = False
    mSpinnyPhase1 = False
    mSpinnyPhase2 = False
    mShootAgainstWall = False
    mShootStartLine = False
    mShootStartLineAuto = False
    mShootTrench = False
    mShootTrenchAuto = False
    mReverseIndexer = False
    mStartShooter = 0

    #MOTORS
    #\/---------\/

    #swerve
    driveMotor1 = 0
    driveMotor2 = 0
    driveMotor3 = 0
    driveMotor4 = 0
    turnMotor1 = 0
    turnMotor2 = 0
    turnMotor3 = 0
    turnMotor4 = 0

    #shooter
    #shooter speed is in rpm
    shooterTopSpeed = 0
    shooterBottomSpeed = 0
    shooterTopSpeedEncoder = 0
    shooterBottomSpeedEncoder = 0
    indexerAngle = 0
    photoSensorFront = False
    photoSensorBack = False
    indexerEncoder = 0

    #control panel
    spinnerUpDown = 0
    spinnerSpeed = 0

    #intake
    #Release solenoid?
    intakeWheelSpeed = 0

    #climber
    #climber release is an angle (maybe)
    climberRelease = 0
    climberWinchSpeed = 0


    def __init__(self):
        pass

    def interfacesInit(self):
        pass
