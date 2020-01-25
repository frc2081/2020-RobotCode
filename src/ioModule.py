import wpilib
import rev

class io:
    def __init__(self):
        self.swerveLFDMotor = rev.CANSparkMax(1, rev.MotorType.kBrushless)
        self.swerveRFDMotor = rev.CANSparkMax(2, rev.MotorType.kBrushless)

        
    def periodic(self, interfaces):
        self.swerveLFDMotor.set(.5)
        print("io Periodic function called")