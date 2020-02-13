import wpilib
import rev
import ctre

from networktables import NetworkTables

class io:
    def __init__(self, interfaces):
        self.sd = NetworkTables.getTable("SmartDashboard")

        #Swerve System
        self.swerveLFDMotor = ctre.WPI_TalonSRX(1)
        self.swerveRFDMotor = ctre.WPI_TalonSRX(2)
        self.swerveLBDMotor = ctre.WPI_TalonSRX(3)
        self.swerveRBDMotor = ctre.WPI_TalonSRX(4)
        self.swerveLFTMotor = rev.CANSparkMax(5, rev.MotorType.kBrushless)
        self.swerveRFTMotor = rev.CANSparkMax(6, rev.MotorType.kBrushless)
        self.swerveLBTMotor = rev.CANSparkMax(7, rev.MotorType.kBrushless)
        self.swerveRBTMotor = rev.CANSparkMax(8, rev.MotorType.kBrushless)

        self.swerveLFTEncoder = self.swerveLFTMotor.getEncoder()
        self.swerveRFTEncoder = self.swerveRFTMotor.getEncoder()
        self.swerveLBTEncoder = self.swerveLBTMotor.getEncoder()
        self.swerveRBTEncoder = self.swerveRBTMotor.getEncoder()

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


        #Shooter System
        self.shooterTopWheelMotor = rev.CANSparkMax(9, rev.MotorType.kBrushless)
        self.shooterBottomWheelMotor = rev.CANSparkMax(10, rev.MotorType.kBrushless)
        self.shooterIndexerMotor = rev.CANSparkMax(11, rev.MotorType.kBrushed)
        self.shooterIntakeMotor = rev.CANSparkMax(12, rev.MotorType.kBrushed)
        self.shooterIntakeElevationMotor = rev.CANSparkMax(13, rev.MotorType.kBrushed)
        
        self.shooterTopWheelEncoder = self.shooterTopWheelMotor.getEncoder()
        self.shooterTopWheelEncoder.setPosition(0)

        self.shooterBottomWheelEncoder = self.shooterBottomWheelMotor.getEncoder()
        self.shooterBottomWheelEncoder.setPosition(0)

        self.shooterTopWheelP = 0
        self.shooterTopWheelI = 0
        self.shooterTopWheelOutputMin = 0
        self.shooterTopWheelOutputMax = 0
        self.shooterTopWheelConversionFactor = 1

        self.shooterBottomWheelP = 0
        self.shooterBottomWheelI = 0
        self.shooterBottomWheelOutputMin = 0
        self.shooterBottomWheelOutputMax = 0
        self.shooterBottomWheelConversionFactor = 1

        self.shooterTopWheelPID = self.shooterTopWheelMotor.getPIDController()
        self.shooterTopWheelPID.setP(self.shooterTopWheelP)
        self.shooterTopWheelPID.setI(self.shooterTopWheelI)
        self.shooterTopWheelPID.setOutputRange(self.shooterTopWheelOutputMin, self.shooterTopWheelOutputMax)

        self.shooterBottomWheelPID = self.shooterBottomWheelMotor.getPIDController()
        self.shooterBottomWheelPID.setP(self.shooterBottomWheelP)
        self.shooterBottomWheelPID.setI(self.shooterBottomWheelI)
        self.shooterBottomWheelPID.setOutputRange(self.shooterBottomWheelOutputMin, self.shooterBottomWheelOutputMax)

        self.shooterIndexerP = 0.0005
        self.shooterIndexerI = 0
        self.shooterIndexerOutputMin = -1
        self.shooterIndexerOutputMax = 1
        self.shooterIndexerConversionFactor = 360

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

        self.shooterTopWheelEncoder.setVelocityConversionFactor(self.shooterWheelConversionFactor)
        self.shooterBottomWheelEncoder.setVelocityConversionFactor(self.shooterWheelConversionFactor)
        """
        

        #Control Panel System
        """
        self.cpanelSpinMotor = rev.CANSparkMax(14, rev.MotorType.kBrushless)
        self.cpanelElevationMotor = rev.CANSparkMax(15, rev.MotorType.kBrushless)

        self.cpanelSpinEncoder = self.cpanelSpinMotor.getEncoder()
        self.cpanelElevationEncoder = self.cpanelElevationMotor.getEncoder()

        self.cpanelSpinConversionFactor = 1
        self.cpanelSpinEncoder.setPositionConversionFactor(self.cpanelSpinConversionFactor)
        self.cpanelElevationConversionFactor = 1
        self.cpanelElevationEncoder.setPositionConversionFactor(self.cpanelElevationConversionFactor)
        """

        self.photoSensorFront = wpilib.DigitalInput(0)
        self.photoSensorBack = wpilib.DigitalInput(1)

        #Climbing System
        self.climberWinchAMotor = rev.CANSparkMax(16, rev.MotorType.kBrushless)
        self.climberWinchBMotor = rev.CANSparkMax(17, rev.MotorType.kBrushless)


    def robotPeriodic(self, interfaces):
        self.sd.putNumber("indexer P", self.shooterIndexerP)
        self.sd.putNumber("indexer I", self.shooterIndexerI)

        self.sd.putNumber("indexer desired", interfaces.indexerAngle)
        self.sd.putNumber("indexer actual", interfaces.indexerEncoder)

        #AAAAAAAAAAAAAAAAAAAAAAAAAAAA

        self.sd.putNumber("Shooter Top P", self.shooterTopWheelP)
        self.sd.putNumber("Shooter Top I", self.shooterTopWheelI)

        self.sd.putNumber("Shooter Top desired", interfaces.shooterTopSpeed)
        self.sd.putNumber("Shooter Top actual", interfaces.shooterTopSpeedEncoder)
        #AAAAAAAAAAAAAAAAAAAAAAAAAAAAa

        self.sd.putNumber("Shooter Bottom P", self.shooterIndexerP)
        self.sd.putNumber("Shooter Bottom I", self.shooterIndexerI)

        self.sd.putNumber("Shooter Bottom desired", interfaces.shooterBottomSpeed)
        self.sd.putNumber("Shooter Bottom actual", interfaces.shooterBottomSpeedEncoder)

        #self.sd.putNumber("LFD Encoder", self.swerveLFDEncoder.getVelocity())
        #self.sd.putNumber("RFD Encoder", self.swerveRFDEncoder.getVelocity())
        #self.sd.putNumber("LBD Encoder", self.swerveLBDEncoder.getVelocity())
        #self.sd.putNumber("RBD Encoder", self.swerveRBDEncoder.getVelocity())
        #self.sd.putNumber("RFT Encoder", self.swerveRFTEncoder.getPosition())
        #self.sd.putNumber("LBT Encoder", self.swerveLBTEncoder.getPosition())
        #self.sd.putNumber("RBT Encoder", self.swerveRBTEncoder.getPosition())
        #self.sd.putNumber("Top Shooter Wheel Encoder", self.shooterTopWheelEncoder.getVelocity())
        #self.sd.putNumber("Bottom Shooter Wheel Encoder", self.shooterBottomWheelEncoder.getVelocity())
        #self.sd.putNumber("Shooter Indexer Encoder", self.shooterIndexerEncoder.getPosition())
        #self.sd.putNumber("Intake Encoder", self.shooterIntakeEncoder.getVelocity())
        #self.sd.putNumber("Intake Elevation Encoder", self.shooterIntakeElevationEncoder.getPosition())
        #self.sd.putNumber("Control Panel Spin Encoder", self.cpanelSpinEncoder.getPosition())
        #self.sd.putNumber("Control Panel Elevation Encoder", self.cpanelElevationEncoder.getPosition())
        #self.sd.putNumber("Climber Winch A Encoder", self.climberWinchAEncoder.getVelocity())
        #self.sd.putNumber("Climber Winch B Encoder", self.climberWinchBEncoder.getVelocity())
        
    def teleopPeriodic(self, interfaces):
        interfaces.photoSensorFront = self.photoSensorFront.get() #under the shooter
        interfaces.photoSensorBack = self.photoSensorBack.get() #away from the shooter
        
        interfaces.shooterTopSpeedEncoder = self.shooterTopWheelEncoder.getVelocity()
        interfaces.shooterBottomSpeedEncoder = self.shooterBottomWheelEncoder.getVelocity()

        #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        if (self.sd.getNumber("Shooter Top P", 0)) != self.shooterTopWheelP:
            self.shooterTopWheelP = self.sd.getNumber("Shooter Top P", 0)
            self.shooterTopWheelPID.setP(self.shooterTopWheelP)

        if (self.sd.getNumber("Shooter Top I", 0)) != self.shooterTopWheelI:
            self.shooterTopWheelI = self.sd.getNumber("Shooter Top I", 0)
            self.shooterTopWheelPID.setI(self.shooterTopWheelI)
        
        self.sd.putNumber("Shooter Top desired", interfaces.shooterTopSpeed)
        self.sd.putNumber("Shooter Top actual", interfaces.shooterTopSpeedEncoder)

        #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        if (self.sd.getNumber("Shooter Bottom P", 0)) != self.shooterBottomWheelP:
            self.shooterTopBottomP = self.sd.getNumber("Shooter Bottom P", 0)
            self.shooterBottomWheelPID.setP(self.shooterBottomWheelP)

        if (self.sd.getNumber("Shooter Bottom I", 0)) != self.shooterBottomWheelI:
            self.shooterBottomWheelI = self.sd.getNumber("Shooter Bottom I", 0)
            self.shooterBottomWheelPID.setI(self.shooterBottomWheelI)
        
        self.sd.putNumber("Shooter Bottom desired", interfaces.shooterBottomSpeed)
        self.sd.putNumber("Shooter Bottom actual", interfaces.shooterBottomSpeedEncoder)

    def teleopPeriodic(self, interfaces):
      
        if(interfaces.indexerManMode == True):
            self.indexerMotor.set(interfaces.indexerManPower)
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

        #swerve motors
        self.swerveLFDMotor.set(interfaces.swerveLFDDesSpd)
        self.swerveRFDMotor.set(interfaces.swerveRFDDesSpd)
        self.swerveLBDMotor.set(interfaces.swerveLBDDesSpd)
        self.swerveRBDMotor.set(interfaces.swerveRBDDesSpd)

        self.swerveLFTPID.setReference(interfaces.swerveLFTDesAng, rev.ControlType.kVelocity)
        self.swerveLFTPID.setReference(interfaces.swerveRFTDesAng, rev.ControlType.kVelocity)
        self.swerveLFTPID.setReference(interfaces.swerveLBTDesAng, rev.ControlType.kVelocity)
        self.swerveLFTPID.setReference(interfaces.swerveRBTDesAng, rev.ControlType.kVelocity) 
   
        #self.shooterIntakeElevationMotor