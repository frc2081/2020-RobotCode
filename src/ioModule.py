import wpilib
import rev
import ctre

from networktables import NetworkTables

class io:
    def __init__(self, interfaces):
        self.sd = NetworkTables.getTable("SmartDashboard")

        #Swerve System
        self.swerveLFDMotor = ctre.WPI_TalonSRX(2)
        self.swerveRFDMotor = ctre.WPI_TalonSRX(3)
        self.swerveLBDMotor = ctre.WPI_TalonSRX(4)
        self.swerveRBDMotor = ctre.WPI_TalonSRX(1)
        self.swerveLFTMotor = rev.CANSparkMax(30, rev.MotorType.kBrushless)
        self.swerveRFTMotor = rev.CANSparkMax(33, rev.MotorType.kBrushless)
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
        self.shooterIntakeArmMotor = rev.CANSparkMax(26, rev.MotorType.kBrushed)

        #Encoders
        self.swerveLFTEncoder = self.swerveLFTMotor.getEncoder()
        self.swerveRFTEncoder = self.swerveRFTMotor.getEncoder()
        self.swerveLBTEncoder = self.swerveLBTMotor.getEncoder()
        self.swerveRBTEncoder = self.swerveRBTMotor.getEncoder()

        self.intakeArmEncoder = self.shooterIntakeArmMotor.getEncoder()
        #self.indexerEncoder = self.shooterIndexerMotor.getAlternateEncoder(rev.CANEncoder.AlternateEncoderType.kQuadrature, 8192)
        self.intakePhotoSensor = wpilib.DigitalInput(4)

        #PID Setup
        self.swerveDriveP = 0.0005
        self.swerveDriveI = 0
        self.swerveDriveOutputMin = -1
        self.swerveDriveOutputMax = 1
        self.swerveDriveConversionFactor = 1

        self.swerveTurnP = 0
        self.swerveTurnI = 0
        self.swerveTurnOutputMin = 0
        self.swerveTurnOutputMax = 0
        self.swerveTurnConversionFactor = 1

        self.swerveLFTEncoder.setPositionConversionFactor(self.swerveDriveConversionFactor)
        self.swerveRFTEncoder.setPositionConversionFactor(self.swerveDriveConversionFactor)
        self.swerveLBTEncoder.setPositionConversionFactor(self.swerveDriveConversionFactor)
        self.swerveRBTEncoder.setPositionConversionFactor(self.swerveDriveConversionFactor)     

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

        self.shooterP = 0.005
        self.shooterI = 0
        self.shooterF = 0
        self.shooterOutputMin = 0
        self.shooterOutputMax = 0
        self.shooterConversionFactor = 1

        self.shooterTopWheelPID = self.shooterTopWheelMotor.getPIDController()
        self.shooterTopWheelPID.setP(self.shooterP)
        self.shooterTopWheelPID.setI(self.shooterI)
        self.shooterTopWheelPID.setF(self.shooterF)
        self.shooterTopWheelPID.setOutputRange(self.shooterOutputMin, self.shooterOutputMax)

        self.shooterBottomWheelPID = self.shooterBottomWheelMotor.getPIDController()
        self.shooterBottomWheelPID.setP(self.shooterP)
        self.shooterBottomWheelPID.setI(self.shooterI)
        self.shooterBottomWheelPID.setF(self.shooterF)
        self.shooterBottomWheelPID.setOutputRange(self.shooterOutputMin, self.shooterOutputMax)

        self.shooterIndexerP = 0.0005
        self.shooterIndexerI = 0
        self.shooterIndexerOutputMin = -1
        self.shooterIndexerOutputMax = 1
        self.shooterIndexerConversionFactor = 360

        self.intakeArmPID = self.shooterIntakeArmMotor.getPIDController()
        self.intakeArmP = 0.005
        self.intakeArmI = 0
        self.intakeArmOutputMin = -1
        self.intakeArmOutputMax = 1
        self.intakeArmConversionFactor = 0.086 #42cpr * 100:1 gear ratio / 360 degress/rev = 11.66 counts per degree = .086 degrees per count
    
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
        
        interfaces.intakeBallDetected = self.intakePhotoSensor.get()

        self.sd.putNumber("indexer desired", interfaces.indexerAngle)
        self.sd.putNumber("indexer actual", interfaces.indexerEncoder)
        self.sd.putNumber("Shooter Top desired", interfaces.shooterTopSpeed)
        self.sd.putNumber("Shooter Top actual", interfaces.shooterTopSpeedEncoder)
        self.sd.putNumber("Shooter Bottom desired", interfaces.shooterBottomSpeed)
        self.sd.putNumber("Shooter Bottom actual", interfaces.shooterBottomSpeedEncoder)

        self.sd.putNumber("Intake Arm Angle", interfaces.intakeActualPos)
        self.sd.putNumber("Ball Detected", interfaces.intakeBallDetected)

        #self.sd.putNumber("LFD Encoder", self.swerveLFDEncoder.getVelocity())
        #self.sd.putNumber("RFD Encoder", self.swerveRFDEncoder.getVelocity())
        #self.sd.putNumber("LBD Encoder", self.swerveLBDEncoder.getVelocity())
        #self.sd.putNumber("RBD Encoder", self.swerveRBDEncoder.getVelocity())
        self.sd.putNumber("RFT Encoder", self.swerveRFTEncoder.getPosition())
        self.sd.putNumber("LBT Encoder", self.swerveLBTEncoder.getPosition())
        self.sd.putNumber("RBT Encoder", self.swerveRBTEncoder.getPosition())
        self.sd.putNumber("LFT Encoder", self.swerveLFTEncoder.getPosition())

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
            self.shooterTopWheelPID.setF(self.shooterF)       
            self.shooterBottomWheelPID.setF(self.shooterF)    

    def teleopInit(self, interfaces):
        self.sd.putNumber("Shooter P", self.shooterP)
        self.sd.putNumber("Shooter I", self.shooterI)
        self.sd.putNumber("Shooter F", self.shooterF)

        self.sd.putNumber("indexer P", self.shooterIndexerP)
        self.sd.putNumber("indexer I", self.shooterIndexerI)

    def teleopPeriodic(self, interfaces):
      
        if(interfaces.indexerManMode == True):
            self.shooterIndexerMotor.set(interfaces.indexerManPower)
            self.shooterTopWheelPID.setReference(interfaces.shooterManTopDesSpd , rev.ControlType.kVelocity)
            self.shooterBottomWheelPID.setReference(interfaces.shooterManBotDesSpd, rev.ControlType.kVelocity)
        else:
            #**********NEED INDEXER DESIRED ANGLE SET HERE**********
            self.shooterTopWheelPID.setReference(interfaces.shooterTopSpeed, rev.ControlType.kVelocity)
            self.shooterBottomWheelPID.setReference(interfaces.shooterBottomSpeed, rev.ControlType.kVelocity)            
        
        self.shooterIntakeMotor.set(interfaces.intakeWheelSpeed)
        #need intake angle command set here - need the PID controller for it, too

        self.climberWinchAMotor.set(interfaces.dClimbWinchPower)  
        self.climberWinchBMotor.set(interfaces.dClimbWinchPower) 
        self.climberRaiseMotor.set(interfaces.dClimbRaisePower) 

        #swerve motors
        self.swerveLFDMotor.set(interfaces.swerveLFDDesSpd)
        self.swerveRFDMotor.set(interfaces.swerveRFDDesSpd)
        self.swerveLBDMotor.set(interfaces.swerveLBDDesSpd)
        self.swerveRBDMotor.set(interfaces.swerveRBDDesSpd)

        self.swerveLFTPID.setReference(interfaces.swerveLFTDesAng, rev.ControlType.kVelocity)
        self.swerveLFTPID.setReference(interfaces.swerveRFTDesAng, rev.ControlType.kVelocity)
        self.swerveLFTPID.setReference(interfaces.swerveLBTDesAng, rev.ControlType.kVelocity)
        self.swerveLFTPID.setReference(interfaces.swerveRBTDesAng, rev.ControlType.kVelocity) 

        self.intakeArmPID.setReference(interfaces.intakeDesiredPos, rev.ControlType.kPosition)