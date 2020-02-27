import wpilib
import rev
import ctre

from networktables import NetworkTables
from wpilib import controller

class io:

    def __init__(self, interfaces):
        self.sd = NetworkTables.getTable("SmartDashboard")

        #Swerve System
        self.swerveLFDMotor = ctre.WPI_TalonSRX(2)
        self.swerveRFDMotor = ctre.WPI_TalonSRX(3)
        self.swerveLBDMotor = ctre.WPI_TalonSRX(4)
        self.swerveRBDMotor = ctre.WPI_TalonSRX(1)
        self.swerveLFTMotor = rev.CANSparkMax(30, rev.MotorType.kBrushless)
        self.swerveRFTMotor = rev.CANSparkMax(23, rev.MotorType.kBrushless)
        self.swerveLBTMotor = rev.CANSparkMax(31, rev.MotorType.kBrushless)
        self.swerveRBTMotor = rev.CANSparkMax(32, rev.MotorType.kBrushless)

        #Climbing System
        self.climberWinchAMotor = rev.CANSparkMax(21, rev.MotorType.kBrushless)
        self.climberWinchBMotor = rev.CANSparkMax(22, rev.MotorType.kBrushless)
        self.climberRaiseMotor = rev.CANSparkMax(29, rev.MotorType.kBrushed)

        #Shooter System
        self.shooterTopWheelMotor = rev.CANSparkMax(35, rev.MotorType.kBrushless)
        self.shooterBottomWheelMotor = rev.CANSparkMax(34, rev.MotorType.kBrushless)
        self.shooterIndexerMotor = rev.CANSparkMax(24, rev.MotorType.kBrushed)
        self.shooterIntakeMotor = rev.CANSparkMax(20, rev.MotorType.kBrushed)
        self.shooterIntakeArmMotor = rev.CANSparkMax(28, rev.MotorType.kBrushed)

        #Encoders
        self.swerveLFTEncoder = self.swerveLFTMotor.getEncoder()
        self.swerveRFTEncoder = self.swerveRFTMotor.getEncoder()
        self.swerveLBTEncoder = self.swerveLBTMotor.getEncoder()
        self.swerveRBTEncoder = self.swerveRBTMotor.getEncoder()

        self.intakeArmEncoder = wpilib.Encoder(6,7)
        self.intakeWhlEncoder = wpilib.Encoder(0,1)
        self.indexerEncoder = wpilib.Encoder(8,9)
        self.intakePhotoSensor = wpilib.DigitalInput(4)

        self.intakeArmEncoder.setDistancePerPulse(1/1024*360)
        self.intakeWhlEncoder.setDistancePerPulse(1/1024)
        self.indexerEncoder.setDistancePerPulse(1/2048*360)

        self.intakeArmHomeSwitch = wpilib.DigitalInput(2)

        #PID Setup
        self.swerveDriveP = 0
        self.swerveDriveI = 0
        self.swerveDriveOutputMin = -1
        self.swerveDriveOutputMax = 1
        self.swerveDriveConversionFactor = 1

        self.swerveTurnP = 0.005
        self.swerveTurnI = 0
        self.swerveTurnOutputMin = -1
        self.swerveTurnOutputMax = 1
        self.swerveTurnConversionFactor = 9.6

        self.swerveLFTEncoder.setPositionConversionFactor(self.swerveTurnConversionFactor)
        self.swerveRFTEncoder.setPositionConversionFactor(self.swerveTurnConversionFactor)
        self.swerveLBTEncoder.setPositionConversionFactor(self.swerveTurnConversionFactor)
        self.swerveRBTEncoder.setPositionConversionFactor(self.swerveTurnConversionFactor)

        self.swerveLFTPIDNew = wpilib.controller.PIDController(self.swerveTurnP,self.swerveTurnI, 0)
        self.swerveRFTPIDNew = wpilib.controller.PIDController(self.swerveTurnP,self.swerveTurnI, 0)
        self.swerveLBTPIDNew = wpilib.controller.PIDController(self.swerveTurnP,self.swerveTurnI, 0)
        self.swerveRBTPIDNew = wpilib.controller.PIDController(self.swerveTurnP,self.swerveTurnI, 0)

        self.swerveLFTPIDNew.enableContinuousInput(0,360)
        self.swerveRFTPIDNew.enableContinuousInput(0,360)
        self.swerveLBTPIDNew.enableContinuousInput(0,360)
        self.swerveRBTPIDNew.enableContinuousInput(0,360)

        self.shooterTopWheelEncoder = self.shooterTopWheelMotor.getEncoder()
        self.shooterTopWheelEncoder.setPosition(0)

        self.shooterBottomWheelEncoder = self.shooterBottomWheelMotor.getEncoder()
        self.shooterBottomWheelEncoder.setPosition(0)

        self.shooterP = 0.00005
        self.shooterI = 0
        self.shooterF = 0.0005
        self.shooterOutputMin = -1
        self.shooterOutputMax = 1
        self.shooterConversionFactor = 1
        self.shooterRampRate = .25

        self.shooterTopWheelPID = self.shooterTopWheelMotor.getPIDController()
        self.shooterTopWheelPID.setP(self.shooterP)
        self.shooterTopWheelPID.setI(self.shooterI)
        self.shooterTopWheelPID.setFF(self.shooterF)
        self.shooterTopWheelPID.setOutputRange(self.shooterOutputMin, self.shooterOutputMax)
        self.shooterTopWheelMotor.setClosedLoopRampRate(self.shooterRampRate)

        self.shooterBottomWheelPID = self.shooterBottomWheelMotor.getPIDController()
        self.shooterBottomWheelPID.setP(self.shooterP)
        self.shooterBottomWheelPID.setI(self.shooterI)
        self.shooterBottomWheelPID.setFF(self.shooterF)
        self.shooterBottomWheelPID.setOutputRange(self.shooterOutputMin, self.shooterOutputMax)
        self.shooterBottomWheelMotor.setClosedLoopRampRate(self.shooterRampRate)

        self.shooterIndexerP = 0.0005
        self.shooterIndexerI = 0
        self.shooterIndexerOutputMin = -1
        self.shooterIndexerOutputMax = 1
        self.shooterIndexerConversionFactor = 360

        #self.intakeArmPID = self.shooterIntakeArmMotor.getPIDController()
        self.intakeArmP = 0.018 #0.006
        self.intakeArmI = 0.00000 #0.0001
        self.intakeArmOutputMin = -1
        self.intakeArmOutputMax = 1

        #self.intakeArmPID.setP(self.intakeArmP)
        #self.intakeArmPID.setI(self.intakeArmI)
        #self.intakeArmPID.setOutputRange(self.intakeArmOutputMin, self.intakeArmOutputMax)

    def robotPeriodic(self, interfaces):        
        interfaces.shooterTopSpeedEncoder = self.shooterTopWheelEncoder.getVelocity()
        interfaces.shooterBottomSpeedEncoder = self.shooterBottomWheelEncoder.getVelocity()
        interfaces.intakeActualPos = self.intakeArmEncoder.getDistance()
        interfaces.indexerActAng = self.indexerEncoder.getDistance()
        interfaces.intakeWheelSpeedAct = -self.intakeWhlEncoder.getRate() * 60
        interfaces.intakeBallDetected = not(self.intakePhotoSensor.get())
        interfaces.intakeArmHomeDetected = self.intakeArmHomeSwitch.get()      
          
        interfaces.swerveLFDActSpd = 0
        interfaces.swerveRFDActSpd = 0
        interfaces.swerveLBDActSpd = 0
        interfaces.swerveRBDActSpd = 0
        interfaces.swerveLFTActPos = self.swerveLFTEncoder.getPosition()
        interfaces.swerveRFTActPos = self.swerveRFTEncoder.getPosition()
        interfaces.swerveLBTActPos = self.swerveLBTEncoder.getPosition()
        interfaces.swerveRBTActPos = self.swerveRBTEncoder.getPosition()             

        self.sd.putNumber("indexer desired Ang", interfaces.indexerDesAng)
        self.sd.putNumber("indexer actual Ang", interfaces.indexerActAng)
        self.sd.putNumber("Shooter Top desired", interfaces.shooterManTopDesSpd)
        self.sd.putNumber("Shooter Top actual", interfaces.shooterTopSpeedEncoder)
        self.sd.putNumber("Shooter Bottom desired", interfaces.shooterManBotDesSpd)
        self.sd.putNumber("Shooter Bottom actual", interfaces.shooterBottomSpeedEncoder)

        self.sd.putNumber("Intake Arm Angle", interfaces.intakeActualPos)
        self.sd.putNumber("Intake Arm Desired Angle", interfaces.intakeDesiredPos)
        self.sd.putNumber("Intake Wheel Speed Actual", interfaces.intakeWheelSpeedAct)
        self.sd.putBoolean("Ball Detected", interfaces.intakeBallDetected)

        #self.sd.putNumber("LFD Encoder", interfaces.swerveLFDActSpd)
        #self.sd.putNumber("RFD Encoder", interfaces.swerveRFDActSpd)
        #self.sd.putNumber("LBD Encoder", interfaces.swerveLBDActSpd)
        #self.sd.putNumber("RBD Encoder", interfaces.swerveRBDActSpd)
        self.sd.putNumber("RFT Encoder", interfaces.swerveRFTActPos)
        self.sd.putNumber("LBT Encoder", interfaces.swerveLBTActPos)
        self.sd.putNumber("RBT Encoder", interfaces.swerveRBTActPos)
        self.sd.putNumber("LFT Encoder", interfaces.swerveLFTActPos)


    def teleopInit(self, interfaces):
        self.sd.putNumber("Shooter P", self.shooterP)
        self.sd.putNumber("Shooter I", self.shooterI)
        self.sd.putNumber("Shooter F", self.shooterF)

        self.sd.putNumber("indexer P", self.shooterIndexerP)
        self.sd.putNumber("indexer I", self.shooterIndexerI)


    def teleopPeriodic(self, interfaces):
        shooterNewP = self.sd.getNumber("Shooter P", 0.00005)
        shooterNewI = self.sd.getNumber("Shooter I", 0)
        shooterNewF = self.sd.getNumber("Shooter F", 0.0005)

        if (shooterNewP) != self.shooterP:
            self.shooterP = shooterNewP
            self.shooterTopWheelPID.setP(self.shooterP)           
            self.shooterBottomWheelPID.setP(self.shooterP)

        if (shooterNewI) != self.shooterI:
            self.shooterI = shooterNewI
            self.shooterTopWheelPID.setI(self.shooterI)       
            self.shooterBottomWheelPID.setI(self.shooterI)   

        if (shooterNewF) != self.shooterF:
            self.shooterF = shooterNewF
            self.shooterTopWheelPID.setFF(self.shooterF)       
            self.shooterBottomWheelPID.setFF(self.shooterF)         

        if(interfaces.indexerManMode == True):
            self.shooterIndexerMotor.set(interfaces.indexerManPower)
            print(str(interfaces.shooterManTopDesSpd))
            self.shooterTopWheelPID.setReference(interfaces.shooterManTopDesSpd , rev.ControlType.kVelocity)
            self.shooterBottomWheelPID.setReference(interfaces.shooterManBotDesSpd, rev.ControlType.kVelocity)
        else:
            #**********NEED INDEXER DESIRED ANGLE SET HERE**********
            self.shooterIndexerMotor.set(0)
            self.shooterTopWheelPID.setReference(interfaces.shooterTopSpeed, rev.ControlType.kVelocity)
            self.shooterBottomWheelPID.setReference(interfaces.shooterBottomSpeed, rev.ControlType.kVelocity)            
        
        #set indexer angle here
        # positive drive = clockwise motion

        #intake wheel speed PID
        if(interfaces.intakeReverse): 
            self.shooterIntakeMotor.set(pidP(self, 0.0005, .001, 450, interfaces.intakeWheelSpeedAct,-1, 1))
            self.shooterIntakeArmMotor.set(pidP(self, self.intakeArmP, 0, 50, interfaces.intakeActualPos, -.5, .5))
        else:         
            self.shooterIntakeMotor.set(pidP(self, 0.0005, .001, interfaces.intakeWheelSpeed, interfaces.intakeWheelSpeedAct, -1, 1))
            if((interfaces.intakeDesiredPos < 5) and (interfaces.intakeActualPos < 5)):
                self.shooterIntakeArmMotor.set(-0.15)
            else:
                self.shooterIntakeArmMotor.set(pidP(self, self.intakeArmP, 0, interfaces.intakeDesiredPos, interfaces.intakeActualPos, -.5, .5))

        print(self.shooterIntakeArmMotor.get())
        self.climberWinchAMotor.set(interfaces.dClimbWinchPower)  
        self.climberWinchBMotor.set(interfaces.dClimbWinchPower) 
        self.climberRaiseMotor.set(interfaces.dClimbRaisePower) 

        #swerve motors
        #Rear motors are reversed to account for swerve module installation orientation
        self.swerveLFDMotor.set(interfaces.swerveLFDDesSpd)
        self.swerveRFDMotor.set(interfaces.swerveRFDDesSpd)
        self.swerveLBDMotor.set(-interfaces.swerveLBDDesSpd)
        self.swerveRBDMotor.set(-interfaces.swerveRBDDesSpd)

        self.swerveLFTPIDNew.setSetpoint(interfaces.swerveLFTDesAng)
        self.swerveRFTPIDNew.setSetpoint(interfaces.swerveRFTDesAng)
        self.swerveLBTPIDNew.setSetpoint(interfaces.swerveLBTDesAng)
        self.swerveRBTPIDNew.setSetpoint(interfaces.swerveRBTDesAng)

        self.swerveLFTMotor.set(self.swerveLFTPIDNew.calculate(interfaces.swerveLFTActPos))
        self.swerveRFTMotor.set(self.swerveRFTPIDNew.calculate(interfaces.swerveRFTActPos))
        self.swerveLBTMotor.set(self.swerveLBTPIDNew.calculate(interfaces.swerveLBTActPos))
        self.swerveRBTMotor.set(self.swerveRBTPIDNew.calculate(interfaces.swerveRBTActPos))

def pidP(self, p, f, des, act, negcmdlim, poscmdlim):
    error = des-act
    cmdff = f * des
    pcmd = p * error
    cmd = pcmd + cmdff

    if(cmd < -1):
        cmd = -1
    elif(cmd > 1):
        cmd = 1

    return cmd