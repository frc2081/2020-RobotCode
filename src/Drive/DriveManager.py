import swervelib
import wpilib
from RobotCommands import RobotCMDS

#error due to unmerged code
from ..ioModule import io

class DriveManager:
    _io = io

    driveBaseWidth = 0
    driveBaseLength = 0

    _swervelib = swervelib.swervelib(driveBaseWidth, driveBaseLength)
    #_cntls = cntls #for controller library

    _pidpollrate = 0.01

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
    
    #Set up swerve turning motor PID controllers
    _lfturnpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, io, io, _pidpollrate)
    _rfturnpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, io, io, _pidpollrate)
    _rbturnpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, io, io, _pidpollrate)
    _lbturnpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, io, io, _pidpollrate)
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

    _lfdrvpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, io, io, _pidpollrate)
    #_lfdrvpid.Enable()

    _rfdrvpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, io, io, _pidpollrate)
    #_rfdrvpid.Enable()

    _lbdrvpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, io, io, _pidpollrate)
    #_lbdrvpid.Enable()

    _rbdrvpid = wpilib.PIDController(_turnpidp, _turnpidi, _turnpidp, io, io, _pidpollrate)
    #_rbdrvpid.Enable()

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
        wpilib.SmartDashboard.putNumber("Swerve Turn P", self.turnP)
        wpilib.SmartDashboard.putNumber("Swerve Turn I", self.turnI)
        wpilib.SmartDashboard.putNumber("Swerve Turn D", self.turnD)

        wpilib.SmartDashboard.putNumber("Swerve Drive P", self.drvP)
        wpilib.SmartDashboard.putNumber("Swerve Drive I", self.drvI)
        wpilib.SmartDashboard.putNumber("Swerve Drive D", self.drvD)
        wpilib.SmartDashboard.putNumber("Swerve Drive F", self.drvF)

    def DriveManagerPeriodic(self):
        self.UpdatePIDTunes()
        self.CalculateVectors()
        self.ApplyIntellegintSwerve()
        self.ApplyPIDControl()

    def DriveManagerAutoPeriodic(self):
        self.CalculateVectors()
        self.ApplyIntellegintSwerve()

    """
    #need code to change digital encoder signal to angle
    """

    def CalculateVectors(self):

        #Determine if the driver or the guidance system is in control of the drivetrain
        #and use the appropriate drive commands
        _drvang = RobotCMDS.drvang
        _drvmag = RobotCMDS.drvmag
        _drvrot = RobotCMDS.drvrot
        
        _currangrf = self._swervelib.whl.angleRF
        _curranglf = self._swervelib.whl.angleLF
        _currangrb = self._swervelib.whl.angleRB
        _curranglb = self._swervelib.whl.angleLB
        if (_drvmag != 0 or _drvrot != 0):
            self._swervelib.calcWheelVect(_drvmag, _drvang, _drvrot)
        else:
            self._swervelib.whl.speedLF = 0
            self._swervelib.whl.speedRF = 0
            self._swervelib.whl.speedLB = 0
            self._swervelib.whl.speedRB = 0

            self._swervelib.whl.angleRF = _currangrf
            self._swervelib.whl.angleLF = _curranglf
            self._swervelib.whl.angleRB = _currangrb
            self._swervelib.whl.angleLB = _curranglb

    #This function modifies the output of the swerve library to control the turn motors more intelligently
    #It works to prevent the wheels from turning completely around when they would only need to move a bit and then reverse to reach a target vector
    def ApplyIntellegintSwerve(self):
        if (abs(self._swervelib.whl.angleRF - self._currangrf) > 90 and
           (self._swervelib.whl.angleRF - self._currangrf < 270)):
            self._swervelib.whl.angleRF = (self._swervelib.whl.angleRF + 180) % 360
            self._swervelib.whl.speedRF *= -1
        if (abs(self._swervelib.whl.angleLF - self._curranglf) > 90 and
           (self._swervelib.whl.angleLF - self._curranglf < 270)):
            self._swervelib.whl.angleLF = (self._swervelib.whl.angleLF + 180) % 360
            self._swervelib.whl.speedLF *= -1
        if (abs(self._swervelib.whl.angleRB - self._currangrb) > 90 and
           (self._swervelib.whl.angleRB - self._currangrb < 270)):
            self._swervelib.whl.angleRB = (self._swervelib.whl.angleRB + 180) % 360
            self._swervelib.whl.speedRB *= -1
        if (abs(self._swervelib.whl.angleLB - self._curranglb) > 90 and
           (self._swervelib.whl.angleLB - self._curranglb < 270)):
            self._swervelib.whl.angleLB = (self._swervelib.whl.angleLB + 180) % 360
            self._swervelib.whl.speedLB *= -1
    
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
        self._lfturnpid.SetSetpoint(self.WhlAngCalcOffset(self._swervelib.whl.angleLF, self._lfwhlangoffset))
        self._rfturnpid.SetSetpoint(self.WhlAngCalcOffset(self._swervelib.whl.angleRF, self._rfwhlangoffset))
        self._lbturnpid.SetSetpoint(self.WhlAngCalcOffset(self._swervelib.whl.angleLB, self._lbwhlangoffset))
        self._rbturnpid.SetSetpoint(self.WhlAngCalcOffset(self._swervelib.whl.angleRB, self._rbwhlangoffset))
        """

        self._swervelib.whl.speedLF *= self._maxdrivespeed
        self._swervelib.whl.speedRF *= self._maxdrivespeed
        self._swervelib.whl.speedLB *= self._maxdrivespeed
        self._swervelib.whl.speedRB *= self._maxdrivespeed

        io.Set(self._swervelib.whl.speedLF)
        io.Set(self._swervelib.whl.speedRF)
        io.Set(self._swervelib.whl.speedLB)
        io.Set(self._swervelib.whl.speedRB)

    def UpdateDashboard(self):
        #Swerve Desired Wheel Vectors
        wpilib.SmartDashboard.putNumber("Swerve Left Front Angle Desired", self._swervelib.whl.angleLF)	
        wpilib.SmartDashboard.putNumber("Swerve Right Front Angle Desired", self._swervelib.whl.angleRF)	
        wpilib.SmartDashboard.putNumber("Swerve Left Back Angle Desired", self._swervelib.whl.angleLB)	
        wpilib.SmartDashboard.putNumber("Swerve Right Back Angle Desired", self._swervelib.whl.angleRB)	

        wpilib.SmartDashboard.putNumber("Swerve Left Front Speed Desired", self._swervelib.whl.speedLF)	
        wpilib.SmartDashboard.putNumber("Swerve Right Front Speed Desired", self._swervelib.whl.speedRF)	
        wpilib.SmartDashboard.putNumber("Swerve Left Back Speed Desired", self._swervelib.whl.speedLB)	
        wpilib.SmartDashboard.putNumber("Swerve Right Back Speed Desired", self._swervelib.whl.speedRB)

        #Swerve Actual Wheel Vectors     **encoders**
        #encoder location
        wpilib.SmartDashboard.putNumber("Swerve Left Front Angle Actual", io)
        wpilib.SmartDashboard.putNumber("Swerve Right Front Angle Actual", io)	
        wpilib.SmartDashboard.putNumber("Swerve Left Back Angle Actual", io)
        wpilib.SmartDashboard.putNumber("Swerve Right Back Angle Actual", io)
        #encoder speed
        wpilib.SmartDashboard.putNumber("Swerve Left Front Speed Actual", io)
        wpilib.SmartDashboard.putNumber("Swerve Right Front Speed Actual", io)
        wpilib.SmartDashboard.putNumber("Swerve Left Back Speed Actual", io)
        wpilib.SmartDashboard.putNumber("Swerve Right Back Speed Actual", io)

        #Swerve Encoder offset calibrations
        wpilib.SmartDashboard.putNumber("Swerve Left Front Encoder Offset", self._lfwhlangoffset)
        wpilib.SmartDashboard.putNumber("Swerve Right Front Encoder Offset", self._rfwhlangoffset)
        wpilib.SmartDashboard.putNumber("Swerve Left Back Encoder Offset", self._lbwhlangoffset)
        wpilib.SmartDashboard.putNumber("Swerve Right Back Encoder Offset", self._rbwhlangoffset)

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