import wpilib
import rev

from networktables import NetworkTables



class io:
    def __init__(self):
        self.sd = NetworkTables.getTable("SmartDashboard")

        #Swerve System
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
        self.shooterTopWheelMotor = rev.CANSparkMax(9, rev.MotorType.kBrushless)
        self.shooterBottomWheelMotor = rev.CANSparkMax(10, rev.MotorType.kBrushless)
        self.shooterIndexerMotor = rev.CANSparkMax(11, rev.MotorType.kBrushless)
        self.shooterIntakeMotor = rev.CANSparkMax(12, rev.MotorType.kBrushless)
        self.shooterIntakeElevationMotor = rev.CANSparkMax(13, rev.MotorType.kBrushless)

        self.shooterTopWheelEncoder = self.shooterTopWheelMotor.getEncoder()
        self.shooterBottomWheelEncoder = self.shooterBottomWheelMotor.getEncoder()
        self.shooterIndexerEncoder = self.shooterIndexerMotor.getEncoder()
        self.shooterIntakeEncoder = self.shooterIntakeMotor.getEncoder()
        self.shooterIntakeElevationEncoder = self.shooterIntakeElevationMotor.getEncoder()

        

        self.shooterWheelP = 0
        self.shooterWheelI = 0
        self.shooterWheelOutputMin = 0
        self.shooterWheelOutputMax = 0
        self.shooterWheelConversionFactor = 1

        self.shooterTopWheelPID = self.shooterTopWheelMotor.getPIDController()
        self.shooterTopWheelPID.setP(self.shooterWheelP)
        self.shooterTopWheelPID.setI(self.shooterWheelI)
        self.shooterTopWheelPID.setOutputRange(self.shooterWheelOutputMin, self.shooterWheelOutputMax)

        self.shooterBottomWheelPID = self.shooterBottomWheelMotor.getPIDController()
        self.shooterBottomWheelPID.setP(self.shooterWheelP)
        self.shooterBottomWheelPID.setI(self.shooterWheelI)
        self.shooterBottomWheelPID.setOutputRange(self.shooterWheelOutputMin, self.shooterWheelOutputMax)

        self.shooterIndexerP = 0
        self.shooterIndexerI = 0
        self.shooterIndexerOutputMin = 0
        self.shooterIndexerOutputMax = 0
        self.shooterIndexerConversionFactor = 1

        self.shooterIndexerPID = self.shooterIndexerMotor.getPIDController()
        self.shooterIndexerPID.setP(self.shooterIndexerP)
        self.shooterIndexerPID.setI(self.shooterIndexerI)
        self.shooterIndexerPID.setOutputRange(self.shooterIndexerOutputMin, self.shooterIndexerOutputMax)

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
        self.shooterIndexerEncoder.setPositionConversionFactor(self.shooterIndexerConversionFactor)
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


    def periodic(self, interfaces):
        self.sd.putNumber("LFD Encoder", self.swerveLFDEncoder.getVelocity())
        self.sd.putNumber("RFD Encoder", self.swerveRFDEncoder.getVelocity())
        self.sd.putNumber("LBD Encoder", self.swerveLBDEncoder.getVelocity())
        self.sd.putNumber("RBD Encoder", self.swerveRBDEncoder.getVelocity())
        self.sd.putNumber("LFT Encoder", self.swerveLFTEncoder.getPosition())
        self.sd.putNumber("RFT Encoder", self.swerveRFTEncoder.getPosition())
        self.sd.putNumber("LBT Encoder", self.swerveLBTEncoder.getPosition())
        self.sd.putNumber("RBT Encoder", self.swerveRBTEncoder.getPosition())
        self.sd.putNumber("Top Shooter Wheel Encoder", self.shooterTopWheelEncoder.getVelocity())
        self.sd.putNumber("Bottom Shooter Wheel Encoder", self.shooterBottomWheelEncoder.getVelocity())
        self.sd.putNumber("Shooter Indexer Encoder", self.shooterIndexerEncoder.getPosition())
        self.sd.putNumber("Intake Encoder", self.shooterIntakeEncoder.getVelocity())
        #self.sd.putNumber("Intake Elevation Encoder", self.shooterIntakeElevationEncoder.getPosition())
        #self.sd.putNumber("Control Panel Spin Encoder", self.cpanelSpinEncoder.getPosition())
        #self.sd.putNumber("Control Panel Elevation Encoder", self.cpanelElevationEncoder.getPosition())
        #self.sd.putNumber("Climber Winch A Encoder", self.climberWinchAEncoder.getVelocity())
        #self.sd.putNumber("Climber Winch B Encoder", self.climberWinchBEncoder.getVelocity())

        print("io Periodic function called")