import wpilib
import ioModule
import robot

class interfaces:

    robotUpdatePeriod = 0.05 #Main robot loop time in seconds

    #CONTROLLER INPUTS
    #\/---------\/

    #driver controller
    dTurn = 0
    dMoveX = 0
    dMoveY = 0
    dBallIntake = False
    #self.dBallOther = False
    dClimbWinchPower = 0
    dClimbRaisePower = 0

    #mechanism controller
    mSpinnyRaise = False
    mSpinnyPhase1 = False
    mSpinnyPhase2 = False
    mShootAgainstWall = False
    mShootStartLine = False
    mShootStartLineAuto = False
    mShootTrench = False
    mShootTrenchAuto = False
    mStartShooter = 0
    mIndexerAdvance = False
    mIndexerReverse = False

    #MOTORS
    #\/---------\/

    #swerve
    swerveLFDDesSpd = 0
    swerveRFDDesSpd = 0
    swerveLBDDesSpd = 0
    swerveRBDDesSpd = 0
    swerveLFTDesAng = 0
    swerveRFTDesAng = 0
    swerveLBTDesAng = 0
    swerveRBTDesAng = 0

    swerveLFDActSpd = 0
    swerveRFDActSpd = 0
    swerveLBDActSpd = 0
    swerveRBDActSpd = 0
    swerveLFTActPos = 0
    swerveRFTActPos = 0
    swerveLBTActPos = 0
    swerveRBTActPos = 0

    #shooter
    #shooter speed is in rpm
    shooterTopSpeed = 0
    shooterBottomSpeed = 0
    shooterTopSpeedEncoder = 0
    shooterBottomSpeedEncoder = 0
    indexerDesAng = 0
    indexerActAng = 0
    photoSensorFront = False
    photoSensorBack = False
    indexerEncoder = 0

    shooterSpdTopLongShot = 700     #700
    shooterSpdBotLongShot = -3500   #-1800
    shooterSpdTopWallShot = 1050     #200    #600
    shooterSpdBotWallShot = -4600   #-1600

    indexerManMode = False
    indexerManPower = 0
    shooterManTopDesSpd = 0
    shooterManBotDesSpd = 0

    #control panel
    spinnerUpDown = 0
    spinnerSpeed = 0

    #intake
    #Release solenoid?
    intakeWheelSpeed = 0
    intakeWheelSpeedAct = 0
    intakeActualPos = 0
    intakeDesiredPos = 0
    intakeBallDetected = False

    intakeReverse = False
    intakeArmHomeDetected = False


    def __init__(self):
        pass

    def interfacesInit(self):
        pass
