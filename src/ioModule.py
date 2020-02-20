import wpilib
import rev
import ctre

from networktables import NetworkTables

class io:

    swerveRBOldTarget = 0

    def __init__(self, interfaces):
        self.sd = NetworkTables.getTable("SmartDashboard")

        #Swerve System
        self.swerveLFDMotor = ctre.WPI_TalonSRX(2)
        self.swerveRFDMotor = ctre.WPI_TalonSRX(3)
        self.swerveLBDMotor = ctre.WPI_TalonSRX(4)
        self.swerveRBDMotor = ctre.WPI_TalonSRX(1)
        self.swerveLFTMotor = rev.CANSparkMax(33, rev.MotorType.kBrushless)
        self.swerveRFTMotor = rev.CANSparkMax(30, rev.MotorType.kBrushless)
        self.swerveLBTMotor = rev.CANSparkMax(31, rev.MotorType.kBrushless)
        self.swerveRBTMotor = rev.CANSparkMax(32, rev.MotorType.kBrushless)

        #Climbing System
        self.climberWinchAMotor = rev.CANSparkMax(21, rev.MotorType.kBrushless)
        self.climberWinchBMotor = rev.CANSparkMax(22, rev.MotorType.kBrushless)
        self.climberRaiseMotor = rev.CANSparkMax(29, rev.MotorType.kBrushed)

        #Shooter System
        self.shooterTopWheelMotor = rev.CANSparkMax(34, rev.MotorType.kBrushless)
        self.shooterBottomWheelMotor = rev.CANSparkMax(35, rev.MotorType.kBrushless)
        self.shooterIndexerMotor = rev.CANSparkMax(24, rev.MotorType.kBrushed)
        self.shooterIntakeMotor = rev.CANSparkMax(20, rev.MotorType.kBrushed)
        self.shooterIntakeArmMotor = rev.CANSparkMax(26, rev.MotorType.kBrushless)

        #Encoders
        self.swerveLFTEncoder = self.swerveLFTMotor.getEncoder()
        self.swerveRFTEncoder = self.swerveRFTMotor.getEncoder()
        self.swerveLBTEncoder = self.swerveLBTMotor.getEncoder()
        self.swerveRBTEncoder = self.swerveRBTMotor.getEncoder()

        self.intakeArmEncoder = self.shooterIntakeArmMotor.getEncoder()
        #self.indexerEncoder = self.shooterIndexerMotor.getAlternateEncoder(rev.CANEncoder.AlternateEncoderType.kQuadrature, 8192)
        self.intakePhotoSensor = wpilib.DigitalInput(4)

        self.intakeArmConversionFactor = 3.599
        self.intakeArmEncoder.setPositionConversionFactor(self.intakeArmConversionFactor)

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

        self.swerveLFTPID = self.swerveLFTMotor.getPIDController()
        self.swerveLFTPID.setP(self.swerveTurnP)
        self.swerveLFTPID.setI(self.swerveTurnI)
        self.swerveLFTPID.setOutputRange(self.swerveTurnOutputMin, self.swerveTurnOutputMax)

        self.swerveRFTPID = self.swerveRFTMotor.getPIDController()
        self.swerveRFTPID.setP(self.swerveTurnP)
        self.swerveRFTPID.setI(self.swerveTurnI)
        self.swerveRFTPID.setOutputRange(self.swerveTurnOutputMin, self.swerveTurnOutputMax)

        self.swerveLBTPID = self.swerveLBTMotor.getPIDController()
        self.swerveLBTPID.setP(self.swerveTurnP)
        self.swerveLBTPID.setI(self.swerveTurnI)
        self.swerveLBTPID.setOutputRange(self.swerveTurnOutputMin, self.swerveTurnOutputMax)

        self.swerveRBTPID = self.swerveRBTMotor.getPIDController()
        self.swerveRBTPID.setP(self.swerveTurnP)
        self.swerveRBTPID.setI(self.swerveTurnI)
        self.swerveRBTPID.setOutputRange(self.swerveTurnOutputMin, self.swerveTurnOutputMax)
        
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

        self.intakeArmPID = self.shooterIntakeArmMotor.getPIDController()
        self.intakeArmP = 0.005 #0.006
        self.intakeArmI = 0.0000 #0.0001
        self.intakeArmOutputMin = -1
        self.intakeArmOutputMax = 1

    
        self.intakeArmPID.setP(self.intakeArmP)
        self.intakeArmPID.setI(self.intakeArmI)
        self.intakeArmPID.setOutputRange(self.intakeArmOutputMin, self.intakeArmOutputMax)

        """
        self.shooterIntakeP = 0
        self.shooterIntakeI = 0
        self.shooterIntakeOutputMin = 0
        self.shooterIntakeOutputMax = 0
        self.shooterIntakeConversionFactor = 1

        self.shooterIntakeElevationP = 0
        self.shooterIntakeElevationI = 0
        self.shooterIntakeElevationOutputMin = 0
        self.shooterIntakeElevationOutputMax = 0
        self.shooterIntakeElevationConversionFactor = 1
        """


    def robotPeriodic(self, interfaces):        
        interfaces.shooterTopSpeedEncoder = self.shooterTopWheelEncoder.getVelocity()
        interfaces.shooterBottomSpeedEncoder = self.shooterBottomWheelEncoder.getVelocity()
        interfaces.intakeActualPos = self.intakeArmEncoder.getPosition()
       # interfaces.indexerEncoder = self.indexerEncoder.getPosition()
        
        interfaces.swerveLFDActSpd = 0
        interfaces.swerveRFDActSpd = 0
        interfaces.swerveLBDActSpd = 0
        interfaces.swerveRBDActSpd = 0
        interfaces.swerveLFTActPos = self.swerveLFTEncoder.getPosition()
        interfaces.swerveRFTActPos = self.swerveRFTEncoder.getPosition()
        interfaces.swerveLBTActPos = self.swerveLBTEncoder.getPosition()
        interfaces.swerveRBTActPos = self.swerveRBTEncoder.getPosition()             
        
        interfaces.intakeBallDetected = self.intakePhotoSensor.get()

        self.sd.putNumber("indexer desired", interfaces.indexerAngle)
        self.sd.putNumber("indexer actual", interfaces.indexerEncoder)
        self.sd.putNumber("Shooter Top desired", interfaces.shooterManTopDesSpd)
        self.sd.putNumber("Shooter Top actual", interfaces.shooterTopSpeedEncoder)
        self.sd.putNumber("Shooter Bottom desired", interfaces.shooterManBotDesSpd)
        self.sd.putNumber("Shooter Bottom actual", interfaces.shooterBottomSpeedEncoder)

        self.sd.putNumber("Intake Arm Angle", interfaces.intakeActualPos)
        self.sd.putNumber("Intake Arm Desired Angle", interfaces.intakeDesiredPos)
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
        shooterNewP = self.sd.getNumber("Shooter P", 0)
        shooterNewI = self.sd.getNumber("Shooter I", 0)
        shooterNewF = self.sd.getNumber("Shooter F", 0)

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
            self.shooterTopWheelPID.setReference(interfaces.shooterManTopDesSpd , rev.ControlType.kVelocity)
            self.shooterBottomWheelPID.setReference(interfaces.shooterManBotDesSpd, rev.ControlType.kVelocity)
        else:
            #**********NEED INDEXER DESIRED ANGLE SET HERE**********
            self.shooterIndexerMotor.set(0)
            self.shooterTopWheelPID.setReference(interfaces.shooterTopSpeed, rev.ControlType.kVelocity)
            self.shooterBottomWheelPID.setReference(interfaces.shooterBottomSpeed, rev.ControlType.kVelocity)            
        
        self.shooterIntakeMotor.set(interfaces.intakeWheelSpeed)
        self.intakeArmPID.setReference(interfaces.intakeDesiredPos, rev.ControlType.kPosition)

        self.climberWinchAMotor.set(interfaces.dClimbWinchPower)  
        self.climberWinchBMotor.set(interfaces.dClimbWinchPower) 
        self.climberRaiseMotor.set(interfaces.dClimbRaisePower) 

        #swerve motors
        #Rear motors are reversed to account for swerve module installation orientation
        self.swerveLFDMotor.set(interfaces.swerveLFDDesSpd)
        self.swerveRFDMotor.set(interfaces.swerveRFDDesSpd)
        self.swerveLBDMotor.set(-interfaces.swerveLBDDesSpd)
        self.swerveRBDMotor.set(-interfaces.swerveRBDDesSpd)

        LFTDesPosCmd = swerveConvertToEncPosition(self, interfaces.swerveLFTActPos, interfaces.swerveLFTDesAng)
        RFTDesPosCmd = swerveConvertToEncPosition(self, interfaces.swerveRFTActPos, interfaces.swerveRFTDesAng)
        LBTDesPosCmd = swerveConvertToEncPosition(self, interfaces.swerveLBTActPos, interfaces.swerveLBTDesAng)
        RBTDesPosCmd = swerveConvertToEncPosition(self, interfaces.swerveRBTActPos, interfaces.swerveRBTDesAng)

        self.swerveLFTPID.setReference(LFTDesPosCmd, rev.ControlType.kPosition)
        self.swerveRFTPID.setReference(RFTDesPosCmd, rev.ControlType.kPosition)
        self.swerveLBTPID.setReference(LBTDesPosCmd, rev.ControlType.kPosition)
        self.swerveRBTPID.setReference(RBTDesPosCmd, rev.ControlType.kPosition) 

#Translate desired swerve position from the swerve library into a desired positon
#for a swerve module with a relative encoder
def swerveConvertToEncPosition(self, encoderActPos, swerveDesPos):

    self.sd.putNumber("EncoderActPos", encoderActPos)
    self.sd.putNumber("SwerveDesPos", swerveDesPos)

    #Convert from encoder position space (-infinite to + infinite) to swerve library position space (0 to 360)
    swerveActPos = encoderActPos % 360
    degreesToTurn = 0
    direction = 0

    #Determine if the best path to the new position is across a zero-crossing
    #Zero crossing from large angle to small angle (ex. 355 to 5)
    if((swerveActPos > 180) and (swerveDesPos < swerveActPos - 180)):
        degreesToTurn = 360 + swerveActPos - swerveDesPos
        direction = 1
    #Zero crossing from small angle to large angle (ex. 5 to 355)
    elif((swerveActPos < 180) and (swerveDesPos > swerveActPos + 180)):
        degreesToTurn = -360 - swerveActPos + swerveDesPos
        direction = 2
    #no zero crossing
    else:
        degreesToTurn = swerveDesPos - swerveActPos
        direction = 3

    compensatedCmd = encoderActPos + degreesToTurn

    self.sd.putNumber("Direction", direction)
    self.sd.putNumber("RBT Degrees to Turn", degreesToTurn)
    self.sd.putNumber("RBT Compensated Command", compensatedCmd)

    return compensatedCmd