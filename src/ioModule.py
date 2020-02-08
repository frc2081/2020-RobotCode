import wpilib
import rev
import interfacesModule
import robot

from networktables import NetworkTables



class io:
    def __init__(self, interfaces):
        self.sd = NetworkTables.getTable("SmartDashboard")

        #Swerve System
        """
        self.swerveLFDMotor = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.swerveRFDMotor = rev.CANSparkMax(2, rev.MotorType.kBrushless)
        self.swerveLBDMotor = rev.CANSparkMax(3, rev.MotorType.kBrushless)
        self.swerveRBDMotor = rev.CANSparkMax(4, rev.MotorType.kBrushless)
        self.swerveLFTMotor = rev.CANSparkMax(5, rev.MotorType.kBrushless)
        self.swerveRFTMotor = rev.CANSparkMax(6, rev.MotorType.kBrushless)
        self.swerveLBTMotor = rev.CANSparkMax(7, rev.MotorType.kBrushless)
        self.swerveRBTMotor = rev.CANSparkMax(8, rev.MotorType.kBrushless)

        self.swerveLFDEncoder = self.swerveLFDMotor.getEncoder()
        self.swerveRFDEncoder = self.swerveRFDMotor.getEncoder()
        self.swerveLBDEncoder = self.swerveLBDMotor.getEncoder()
        self.swerveRBDEncoder = self.swerveRBDMotor.getEncoder()
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

        self.swerveLFDEncoder.setVelocityConversionFactor(self.swerveDriveConversionFactor)
        self.swerveRFDEncoder.setVelocityConversionFactor(self.swerveDriveConversionFactor)
        self.swerveLBDEncoder.setVelocityConversionFactor(self.swerveDriveConversionFactor)
        self.swerveRBDEncoder.setVelocityConversionFactor(self.swerveDriveConversionFactor)
        self.swerveLFTEncoder.setPositionConversionFactor(self.swerveDriveConversionFactor)
        self.swerveRFTEncoder.setPositionConversionFactor(self.swerveDriveConversionFactor)
        self.swerveLBTEncoder.setPositionConversionFactor(self.swerveDriveConversionFactor)
        self.swerveRBTEncoder.setPositionConversionFactor(self.swerveDriveConversionFactor)
        

        self.swerveLFDPID = self.swerveLFDMotor.getPIDController()
        self.swerveLFDPID.setP(self.swerveDriveP)
        self.swerveLFDPID.setI(self.swerveDriveI)
        self.swerveLFDPID.setOutputRange(self.swerveDriveOutputMin, self.swerveDriveOutputMax)

        self.swerveRFDPID = self.swerveRFDMotor.getPIDController()
        self.swerveRFDPID.setP(self.swerveDriveP)
        self.swerveRFDPID.setI(self.swerveDriveI)
        self.swerveRFDPID.setOutputRange(self.swerveDriveOutputMin, self.swerveDriveOutputMax)

        self.swerveLBDPID = self.swerveLBDMotor.getPIDController()
        self.swerveLBDPID.setP(self.swerveDriveP)
        self.swerveLBDPID.setI(self.swerveDriveI)
        self.swerveLBDPID.setOutputRange(self.swerveDriveOutputMin, self.swerveDriveOutputMax)

        self.swerveRBDPID = self.swerveRBDMotor.getPIDController()
        self.swerveRBDPID.setP(self.swerveDriveP)
        self.swerveRBDPID.setI(self.swerveDriveI)
        self.swerveRBDPID.setOutputRange(self.swerveDriveOutputMin, self.swerveDriveOutputMax)

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
        """
        self.shooterTopWheelMotor = rev.CANSparkMax(9, rev.MotorType.kBrushless)
        self.shooterBottomWheelMotor = rev.CANSparkMax(10, rev.MotorType.kBrushless)
        
        self.shooterIndexerMotor = rev.CANSparkMax(11, rev.MotorType.kBrushless)
        """
        self.shooterIntakeMotor = rev.CANSparkMax(12, rev.MotorType.kBrushless)
        self.shooterIntakeElevationMotor = rev.CANSparkMax(13, rev.MotorType.kBrushless)
        """
        self.shooterTopWheelEncoder = self.shooterTopWheelMotor.getEncoder()
        self.shooterTopWheelEncoder.setPosition(0)

        self.shooterBottomWheelEncoder = self.shooterBottomWheelMotor.getEncoder()
        self.shooterBottomWheelEncoder.setPosition(0)
        
        self.shooterIndexerEncoder = self.shooterIndexerMotor.getEncoder()
        self.shooterIndexerEncoder.setPosition(0)
        """
        self.shooterIntakeEncoder = self.shooterIntakeMotor.getEncoder()
        self.shooterIntakeElevationEncoder = self.shooterIntakeElevationMotor.getEncoder()

        """

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

        self.shooterIndexerPID = self.shooterIndexerMotor.getPIDController()
        self.shooterIndexerPID.setP(self.shooterIndexerP)
        self.shooterIndexerPID.setI(self.shooterIndexerI)
        self.shooterIndexerPID.setOutputRange(self.shooterIndexerOutputMin, self.shooterIndexerOutputMax)
        """
        self.shooterIntakeP = 0
        self.shooterIntakeI = 0
        self.shooterIntakeOutputMin = 0
        self.shooterIntakeOutputMax = 0
        self.shooterIntakeConversionFactor = 1

        self.shooterIntakePID = self.shooterIntakeMotor.getPIDController()
        self.shooterIntakePID.setP(self.shooterIntakeP)
        self.shooterIntakePID.setI(self.shooterIntakeI)
        self.shooterIntakePID.setOutputRange(self.shooterIntakeOutputMin, self.shooterIntakeOutputMax)

        self.shooterIntakeElevationP = 0
        self.shooterIntakeElevationI = 0
        self.shooterIntakeElevationOutputMin = 0
        self.shooterIntakeElevationOutputMax = 0
        self.shooterIntakeElevationConversionFactor = 1

        self.shooterIntakeElevationPID = self.shooterIntakeElevationMotor.getPIDController()
        self.shooterIntakeElevationPID.setP(self.shooterIntakeElevationP)
        self.shooterIntakeElevationPID.setI(self.shooterIntakeElevationI)
        self.shooterIntakeElevationPID.setOutputRange(self.shooterIntakeElevationOutputMin, self.shooterIntakeElevationOutputMax)

        self.shooterTopWheelEncoder.setVelocityConversionFactor(self.shooterWheelConversionFactor)
        self.shooterBottomWheelEncoder.setVelocityConversionFactor(self.shooterWheelConversionFactor)
        """
        self.shooterIndexerEncoder.setPositionConversionFactor(self.shooterIndexerConversionFactor)
        """
        self.shooterIntakeEncoder.setVelocityConversionFactor(self.shooterIntakeConversionFactor)
        self.shooterIntakeElevationEncoder.setPositionConversionFactor(self.shooterIntakeElevationConversionFactor)

        #Control Panel System
        self.cpanelSpinMotor = rev.CANSparkMax(14, rev.MotorType.kBrushless)
        self.cpanelElevationMotor = rev.CANSparkMax(15, rev.MotorType.kBrushless)

        self.cpanelSpinEncoder = self.cpanelSpinMotor.getEncoder()
        self.cpanelElevationEncoder = self.cpanelElevationMotor.getEncoder()

        self.cpanelSpinConversionFactor = 1
        self.cpanelSpinEncoder.setPositionConversionFactor(self.cpanelSpinConversionFactor)
        self.cpanelElevationConversionFactor = 1
        self.cpanelElevationEncoder.setPositionConversionFactor(self.cpanelElevationConversionFactor)


        #Climbing System
        self.climberWinchAMotor = rev.CANSparkMax(16, rev.MotorType.kBrushless)
        self.climberWinchBMotor = rev.CANSparkMax(17, rev.MotorType.kBrushless)

        self.climberWinchAEncoder = self.climberWinchAMotor.getEncoder()
        self.climberWinchBEncoder = self.climberWinchBMotor.getEncoder()

        self.climberWinchAConversionFactor = 1
        self.climberWinchAEncoder.setVelocityConversionFactor(self.climberWinchAConversionFactor)
        self.climberWinchBConversionFactor = 1
        self.climberWinchBEncoder.setVelocityConversionFactor(self.climberWinchBConversionFactor)
        """
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

        #sensors
        self.photoSensorFront = wpilib.DigitalInput(0)
        self.photoSensorBack = wpilib.DigitalInput(1)

    def periodic(self, interfaces):
        #self.sd.putNumber("LFD Encoder", self.swerveLFDEncoder.getVelocity())
        #self.sd.putNumber("RFD Encoder", self.swerveRFDEncoder.getVelocity())
        #self.sd.putNumber("LBD Encoder", self.swerveLBDEncoder.getVelocity())
        #self.sd.putNumber("RBD Encoder", self.swerveRBDEncoder.getVelocity())
        #self.sd.putNumber("LFT Encoder", self.swerveLFTEncoder.getPosition())
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
        

        #sensors
        interfaces.photoSensorFront = self.photoSensorFront.get() #under the shooter
        interfaces.photoSensorBack = self.photoSensorBack.get() #away from the shooter
        
        interfaces.indexerEncoder = self.shooterIndexerEncoder.getPosition()
        interfaces.shooterTopSpeedEncoder = self.shooterTopWheelEncoder.getPosition()
        interfaces.shooterBottomSpeedEncoder = self.shooterBottomWheelEncoder.getPosition()

        if (self.sd.getNumber("indexer P", 0)) != self.shooterIndexerP:
            self.shooterIndexerP = self.sd.getNumber("indexer P", 0)

        if (self.sd.getNumber("indexer I", 0)) != self.shooterIndexerI:
            self.shooterIndexerI = self.sd.getNumber("indexer I", 0)

        self.shooterIndexerPID.setP(self.shooterIndexerP)
        self.shooterIndexerPID.setI(self.shooterIndexerI)
        self.sd.putNumber("indexer desired", interfaces.indexerAngle)
        self.sd.putNumber("indexer actual", interfaces.indexerEncoder)        


        #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        if (self.sd.getNumber("Shooter Top P", 0)) != self.shooterTopWheelP:
            self.shooterTopWheelP = self.sd.getNumber("Shooter Top P", 0)

        if (self.sd.getNumber("Shooter Top I", 0)) != self.shooterTopWheelI:
            self.shooterTopWheelI = self.sd.getNumber("Shooter Top I", 0)

        self.shooterTopWheelPID.setP(self.shooterTopWheelP)
        self.shooterTopWheelPID.setI(self.shooterTopWheelI)
        
        self.sd.putNumber("Shooter Top desired", interfaces.shooterTopSpeed)
        self.sd.putNumber("Shooter Top actual", interfaces.shooterTopSpeedEncoder)

        #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        if (self.sd.getNumber("Shooter Bottom P", 0)) != self.shooterBottomWheelP:
            self.shooterTopBottomP = self.sd.getNumber("Shooter Bottom P", 0)

        if (self.sd.getNumber("Shooter Bottom I", 0)) != self.shooterBottomWheelI:
            self.shooterBottomWheelI = self.sd.getNumber("Shooter Bottom I", 0)

        self.shooterBottomWheelPID.setP(self.shooterBottomWheelP)
        self.shooterBottomWheelPID.setI(self.shooterBottomWheelI)
        
        self.sd.putNumber("Shooter Bottom desired", interfaces.shooterBottomSpeed)
        self.sd.putNumber("Shooter Bottom actual", interfaces.shooterBottomSpeedEncoder)

    def teleopperiodic(self, interfaces):
        self.shooterIndexerPID.setReference(interfaces.indexerAngle, rev.ControlType.kPosition)
      
        #self.shooterIntakeMotor
        #self.shooterIntakeElevationMotor