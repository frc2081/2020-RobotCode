import swervelib
import wpilib
import rev
from networktables import NetworkTables
import math

#error due to unmerged code
#from ..ioModule import io

#yAxis = self.driveController.getY(wpilib.XboxController.Hand.kRightHand)
"""
def io(self):
    drvrfmot = rev.SparkMax(0)		
    drvlfmot = rev.SparkMax(1)
    drvrbmot = rev.SparkMax(2)
    drvlbmot = rev.SparkMax(3)
    turnrfmot = rev.SparkMax(4)
    turnlfmot = rev.SparkMax(5)
    turnrbmot = rev.SparkMax(6)
    turnlbmot = rev.SparkMax(7)
"""
class DriveManager:

    driveBaseWidth = 23
    driveBaseLength = 32

    #those numbers are the width and lenth of wheel center to wheel center
    _swervelib = swervelib.SwerveLib(driveBaseWidth, driveBaseLength)

    #_cntls = cntls #for controller library

    #_pidpollrate = 0.01

    _drvang = 0
    _drvmag = 0
    _drvrot = 0
    _drvpidi = 0
    drvI = 0
    _drvpidd = 0
    drvD = 0
    _drvpidp = 0
    drvP = 0
    _drvpidf = 0
    drvF = 0
    _turnpidp = 0
    turnP = 0
    _turnpidi = 0
    turnI = 0
    _turnpidd = 0
    turnD = 0

    driveMotor = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushless)
    turnMotor = rev.CANSparkMax(1, rev.CANSparkMax.MotorType.kBrushless)

    #*
    #* max speed - 11.5 ft/s . 3.5052 m/s or 660 RPM of wheel
    #* 138 pulses/rotation of wheel
    #* 20 pulses/rotation of cim
    #* 6.9 cim rotations/1 wheel rotation
    #* 4554 RPM on cim - max
    #*
    _maxdrivespeed = 1 #Speed is in encoder pulses

    _currangrf = 0
    _curranglf = 0
    _curranglb = 0
    _currangrb = 0
    _lfwhlangoffset = 0
    _rfwhlangoffset = 0
    _lbwhlangoffset = 0
    _rbwhlangoffset = 0
    """
    #Set up swerve turning motor PID controllers
    _lfturnpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, _pidpollrate) #io, io,
    _rfturnpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, _pidpollrate) #io, io,
    _rbturnpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, _pidpollrate) #io, io,
    _lbturnpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, _pidpollrate) #io, io,
    _lfturnpid.SetInputRange(0, 360)
    _lfturnpid.SetOutputRange(-1, 1)
    _lfturnpid.SetContinuous()
    _lfturnpid.Enable()
    _rfturnpid.SetInputRange(0, 360)
    _rfturnpid.SetOutputRange(-1, 1)
    _rfturnpid.Enable()
    _lbturnpid.SetInputRange(0, 360)
    _lbturnpid.SetOutputRange(-1, 1)
    _lbturnpid.SetContinuous()
    _rbturnpid.SetOutputRange(-1, 1)
    _rbturnpid.SetContinuous()
    _rbturnpid.Enable()
    """
    """
    _lfdrvpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, _pidpollrate) #io, io,
    #_lfdrvpid.Enable()

    _rfdrvpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, _pidpollrate) #io, io,
    #_rfdrvpid.Enable()

    _lbdrvpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, _pidpollrate) #io, io,
    #_lbdrvpid.Enable()

    _rbdrvpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, _pidpollrate) #io, io,
    #_rbdrvpid.Enable()
    """
    """
    #for absolute encoders
    #Preferences file to save swerve drive encoder offset calibrations
    _prefs = frc.Preferences::GetInstance()
    _lfwhlangoffset = _prefs.GetDouble("LFOffset", 0)
    _rfwhlangoffset = _prefs.GetDouble("RFOffset", 0)
    _lbwhlangoffset = _prefs.GetDouble("LBOffset", 0)
    _rbwhlangoffset = _prefs.GetDouble("RBOffset", 0)
    """

    def DriveManagerInit(self):
        #self.sd = NetworkTables.getTable('SmartDashboard')
        pass

    def DriveManagerPeriodic(self, interfaces):
        #self.UpdatePIDTunes()
        self.CalculateVectors(interfaces)
        self.ApplyIntellegintSwerve()
        self.UpdateDashboard()
        #self.cntlManager()
        #self.ApplyPIDControl()
        #self.motorTest()

    def motorTest(self):
        self.driveMotor.set(self._swervelib.whl.speed1)
        self.turnMotor.set(0)

    def DriveManagerAutoPeriodic(self, interfaces):
        self.CalculateVectors(interfaces)
        self.ApplyIntellegintSwerve()

    """
    #need code to change digital encoder signal to angle
    """

    def CalculateVectors(self, interfaces):

        #Determine if the driver or the guidance system is in control of the drivetrain
        #and use the appropriate drive commands

        self._drvang = (math.atan2(-interfaces.dMoveX, -interfaces.dMoveY) * 180/3.14159265)
        self._drvmag = math.sqrt(pow(interfaces.dMoveX, 2) + pow(interfaces.dMoveY, 2))
        self._drvrot = interfaces.dTurn

        wpilib.SmartDashboard.putNumber("Swerve Angle", self._drvang)
        wpilib.SmartDashboard.putNumber("Swerve Mag", self._drvmag)
        wpilib.SmartDashboard.putNumber("Swerve Rot", self._drvrot)

        _currangrf = self._swervelib.whl.speed1
        _curranglf = self._swervelib.whl.speed2
        _curranglb = self._swervelib.whl.speed3
        _currangrb = self._swervelib.whl.speed4

        if (self._drvmag != 0 or self._drvrot != 0):
            self._swervelib.calcWheelVect(self._drvmag, self._drvang, self._drvrot)
        else:
            self._swervelib.whl.speed1 = 0
            self._swervelib.whl.speed2 = 0
            self._swervelib.whl.speed3 = 0
            self._swervelib.whl.speed4 = 0

            self._swervelib.whl.angle1 = _currangrf
            self._swervelib.whl.angle2 = _curranglf
            self._swervelib.whl.angle3 = _curranglb
            self._swervelib.whl.angle4 = _currangrb

    #This function modifies the output of the swerve library to control the turn motors more intelligently
    #It works to prevent the wheels from turning completely around when they would only need to move a bit and then reverse to reach a target vector
    def ApplyIntellegintSwerve(self):
        if (abs(self._swervelib.whl.angle1 - self._currangrf) > 90 and
           (self._swervelib.whl.angle1 - self._currangrf < 270)):
            self._swervelib.whl.angle1 = (self._swervelib.whl.angle1 + 180) % 360
            self._swervelib.whl.speed1 *= -1
        if (abs(self._swervelib.whl.angle2 - self._curranglf) > 90 and
           (self._swervelib.whl.angle2 - self._curranglf < 270)):
            self._swervelib.whl.angle2 = (self._swervelib.whl.angle2 + 180) % 360
            self._swervelib.whl.speed2 *= -1
        if (abs(self._swervelib.whl.angle4 - self._currangrb) > 90 and
           (self._swervelib.whl.angle4 - self._currangrb < 270)):
            self._swervelib.whl.angle4 = (self._swervelib.whl.angle4 + 180) % 360
            self._swervelib.whl.speed4 *= -1
        if (abs(self._swervelib.whl.angle3 - self._curranglb) > 90 and
           (self._swervelib.whl.angle3 - self._curranglb < 270)):
            self._swervelib.whl.angle3 = (self._swervelib.whl.angle3 + 180) % 360
            self._swervelib.whl.speed3 *= -1
    
    #Function to prevent swerve drive from moving if the wheels have not yet moved to the target angle
    #Mainly used for autonomous navigation and following paths that have sharp corners
    def CheckSetpoint(self, pid : wpilib.PIDController, setpoint, encoder, speed):
        """
        * if encoder value within 10 degrees of setpoint &&
        * if setpoint near 0 . detect values near 360
        * set speed setpoint to speed
        * else speed setpoint to 0
        """
        if(encoder < setpoint + 10 and encoder > setpoint - 10):
            pid.SetSetpoint(speed)
        elif ((360 - encoder) < setpoint + 10 and (360 - encoder) > setpoint + 10):
            pid.SetSetpoint(speed)
        else: 
            pid.SetSetpoint(0)

    def ApplyPIDControl(self):
        """
        #offset for absolute encoders
        self._lfturnpid.SetSetpoint(self.WhlAngCalcOffset(self._swervelib.whl.angle2, self._lfwhlangoffset))
        self._rfturnpid.SetSetpoint(self.WhlAngCalcOffset(self._swervelib.whl.angle1, self._rfwhlangoffset))
        self._lbturnpid.SetSetpoint(self.WhlAngCalcOffset(self._swervelib.whl.angle3, self._lbwhlangoffset))
        self._rbturnpid.SetSetpoint(self.WhlAngCalcOffset(self._swervelib.whl.angle4, self._rbwhlangoffset))
        """

        self._swervelib.whl.speed1 *= self._maxdrivespeed
        self._swervelib.whl.speed2 *= self._maxdrivespeed
        self._swervelib.whl.speed3 *= self._maxdrivespeed
        self._swervelib.whl.speed4 *= self._maxdrivespeed
        """
        io.drvlfmot.Set(self._swervelib.whl.speed2)
        io.drvrfmot.Set(self._swervelib.whl.speed1)
        io.Set(self._swervelib.whl.speed3)
        io.Set(self._swervelib.whl.speed4)
        """
    def UpdateDashboard(self):
        #Swerve Desired Wheel Vectors
        wpilib.SmartDashboard.putNumber("Swerve Left Front Angle Desired", self._swervelib.whl.angle2)	
        wpilib.SmartDashboard.putNumber("Swerve Right Front Angle Desired", self._swervelib.whl.angle1)	
        wpilib.SmartDashboard.putNumber("Swerve Left Back Angle Desired", self._swervelib.whl.angle3)	
        wpilib.SmartDashboard.putNumber("Swerve Right Back Angle Desired", self._swervelib.whl.angle4)	

        wpilib.SmartDashboard.putNumber("Swerve Left Front Speed Desired", self._swervelib.whl.speed2)	
        wpilib.SmartDashboard.putNumber("Swerve Right Front Speed Desired", self._swervelib.whl.speed1)	
        wpilib.SmartDashboard.putNumber("Swerve Left Back Speed Desired", self._swervelib.whl.speed3)	
        wpilib.SmartDashboard.putNumber("Swerve Right Back Speed Desired", self._swervelib.whl.speed4)

        #Swerve Actual Wheel Vectors     **encoders**
        #encoder location
        wpilib.SmartDashboard.putNumber("Swerve Left Front Angle Actual", self._curranglf) #, io
        wpilib.SmartDashboard.putNumber("Swerve Right Front Angle Actual", self._currangrf) #, io
        wpilib.SmartDashboard.putNumber("Swerve Left Back Angle Actual", self._curranglb) #, io
        wpilib.SmartDashboard.putNumber("Swerve Right Back Angle Actual", self._currangrb) #, io
        #encoder speed
        #wpilib.SmartDashboard.putNumber("Swerve Left Front Speed Actual") #, io
        #wpilib.SmartDashboard.putNumber("Swerve Right Front Speed Actual") #, io
        #wpilib.SmartDashboard.putNumber("Swerve Left Back Speed Actual") #, io
        #wpilib.SmartDashboard.putNumber("Swerve Right Back Speed Actual") #, io

        #Swerve Encoder offset calibrations
        #wpilib.SmartDashboard.putNumber("Swerve Left Front Encoder Offset", self._lfwhlangoffset)
        #wpilib.SmartDashboard.putNumber("Swerve Right Front Encoder Offset", self._rfwhlangoffset)
        #wpilib.SmartDashboard.putNumber("Swerve Left Back Encoder Offset", self._lbwhlangoffset)
        #wpilib.SmartDashboard.putNumber("Swerve Right Back Encoder Offset", self._rbwhlangoffset)
    """
    def UpdatePIDTunes(self):

        self._turnpidp = wpilib.SmartDashboard.GetNumber("Swerve Turn P", self.turnP)
        self._turnpidi = wpilib.SmartDashboard.GetNumber("Swerve Turn I", self.turnI)
        self._turnpidd = wpilib.SmartDashboard.GetNumber("Swerve Turn D", self.turnD)

        self._drvpidp = wpilib.SmartDashboard.GetNumber("Swerve Drive P", self.drvP)
        self._drvpidi = wpilib.SmartDashboard.GetNumber("Swerve Drive I", self.drvI)
        self._drvpidd = wpilib.SmartDashboard.GetNumber("Swerve Drive D", self.drvD)
        self._drvpidf = wpilib.SmartDashboard.GetNumber("Swerve Drive F", self.drvF)

        self._lfturnpid.SetP(self._turnpidp)
        self._lfturnpid.SetI(self._turnpidi)
        self._lfturnpid.SetD(self._turnpidd)
        
        self._rfturnpid.SetP(self._turnpidp)
        self._rfturnpid.SetI(self._turnpidi)
        self._rfturnpid.SetD(self._turnpidd)

        self._lbturnpid.SetP(self._turnpidp)
        self._lbturnpid.SetI(self._turnpidi)
        self._lbturnpid.SetD(self._turnpidd)

        self._rbturnpid.SetP(self._turnpidp)
        self._rbturnpid.SetI(self._turnpidi)
        self._rbturnpid.SetD(self._turnpidd)

        self._lfdrvpid.SetP(self._drvpidp)
        self._lfdrvpid.SetI(self._drvpidi)
        self._lfdrvpid.SetD(self._drvpidd)
        self._lfdrvpid.SetF(self._drvpidf)

        self._rfdrvpid.SetP(self._drvpidp)
        self._rfdrvpid.SetI(self._drvpidi)
        self._rfdrvpid.SetD(self._drvpidd)
        self._rfdrvpid.SetF(self._drvpidf)

        self._lbdrvpid.SetP(self._drvpidp)
        self._lbdrvpid.SetI(self._drvpidi)
        self._lbdrvpid.SetD(self._drvpidd)
        self._lbdrvpid.SetF(self._drvpidf)

        self._rbdrvpid.SetP(self._drvpidp)
        self._rbdrvpid.SetI(self._drvpidi)
        self._rbdrvpid.SetD(self._drvpidd)
        self._rbdrvpid.SetF(self._drvpidf)
    """