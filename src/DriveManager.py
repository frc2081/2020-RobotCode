import swervelib
import wpilib
import rev
from networktables import NetworkTables
import math

class DriveManager:

    driveBaseWidth = 23
    driveBaseLength = 32

    accelerationControlEnabled = False

    #those numbers are the width and lenth of wheel center to wheel center
    _swervelib = swervelib.SwerveLib(driveBaseWidth, driveBaseLength)

    _maxdrivespeed = 1 #Speed is represented as -100% to 100%. Conversion to phsyical units is handled by drive system
    _currangrf = 0
    _curranglf = 0
    _curranglb = 0
    _currangrb = 0
    _lfwhlangoffset = 0
    _rfwhlangoffset = 0
    _lbwhlangoffset = 0
    _rbwhlangoffset = 0

    drvAngLim = 0
    drvMagLim = 0
    drvAngRoC = 18 #allowed rate of change for drive angle command in degrees per loop - calibrated for 20hZ update rate
    drvMagRoC = 0.1 #allowd rate of change for drive magnitude command in % per loop - calibrated for 20hz upate rate

    def ramp(self, target, current, RoC):
        ramped = current

        if((target < current + RoC) and (target > current - RoC)):
            ramped = target
        elif(target < current):
            ramped -= RoC
        elif(target > current):
            ramped += RoC
        else:
            ramped = target
            
        return ramped

    def DriveManagerInit(self, interfaces):
        pass

    def DriveManagerPeriodic(self, interfaces):
        self.CalculateVectors(interfaces)
        #self.ApplyIntellegintSwerve(interfaces)
        self.UpdateDashboard(interfaces)

    def DriveManagerAutoPeriodic(self, interfaces):
        self.CalculateVectors(interfaces)
        self.ApplyIntellegintSwerve()

    def CalculateVectors(self, interfaces):

        self._drvAng = (math.atan2(-interfaces.dMoveX, -interfaces.dMoveY) * 180/3.14159265)
        self._drvMag = math.sqrt(pow(interfaces.dMoveX, 2) + pow(interfaces.dMoveY, 2))
        self._drvRot = interfaces.dTurn

        wpilib.SmartDashboard.putNumber("Swerve Angle", self._drvAng)
        wpilib.SmartDashboard.putNumber("Swerve Mag", self._drvMag)
        wpilib.SmartDashboard.putNumber("Swerve Rot", self._drvRot)

        _currangrf = self._swervelib.whl.angle1
        _curranglf = self._swervelib.whl.angle2
        _curranglb = self._swervelib.whl.angle3
        _currangrb = self._swervelib.whl.angle4

        #limit rate of change of driver commanded direction and speed to prevent tipping the robot over
        if(self.accelerationControlEnabled == True):
            self.drvAngLim = self.ramp(self._drvAng, self.drvAngLim, self.drvAngRoC)
            self.drvMagLim = self.ramp(self._drvMag, self.drvMagLim, self.drvMagRoC)
        else:
            self.drvAngLim = self._drvAng
            self.drvMagLim = self._drvMag

        #If driver is not commanding any movement, keep the wheels in the current position
        if ((self.drvMagLim != 0) or (self._drvRot != 0)):
            self._swervelib.calcWheelVect(self.drvMagLim, self.drvAngLim, self._drvRot)
        else:
            self._swervelib.whl.speed1 = 0
            self._swervelib.whl.speed2 = 0
            self._swervelib.whl.speed3 = 0
            self._swervelib.whl.speed4 = 0

            self._swervelib.whl.angle1 = _currangrf
            self._swervelib.whl.angle2 = _curranglf
            self._swervelib.whl.angle3 = _curranglb
            self._swervelib.whl.angle4 = _currangrb

        interfaces.swerveLFDDesSpd = self._swervelib.whl.speed2
        interfaces.swerveRFDDesSpd = self._swervelib.whl.speed1
        interfaces.swerveLBDDesSpd = self._swervelib.whl.speed3
        interfaces.swerveRBDDesSpd = self._swervelib.whl.speed4

        interfaces.swerveLFTDesAng = self._swervelib.whl.angle2
        interfaces.swerveRFTDesAng = self._swervelib.whl.angle1
        interfaces.swerveLBTDesAng = self._swervelib.whl.angle3
        interfaces.swerveRBTDesAng = self._swervelib.whl.angle4

    #This function modifies the output of the swerve library to control the turn motors more intelligently
    #It works to prevent the wheels from turning completely around when they would only need to move a bit and then reverse to reach a target vector
    #If the desired angle is more than 90 and less than 270 degrees away from the current angle, Add 180 to the target angle and reverse the wheel
    def ApplyIntellegintSwerve(self, interfaces):

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

        interfaces.swerveLFDDesSpd = self._swervelib.whl.speed2
        interfaces.swerveRFDDesSpd = self._swervelib.whl.speed1
        interfaces.swerveLBDDesSpd = self._swervelib.whl.speed3
        interfaces.swerveRBDDesSpd = self._swervelib.whl.speed4

        interfaces.swerveLFTDesAng = self._swervelib.whl.angle2
        interfaces.swerveRFTDesAng = self._swervelib.whl.angle1
        interfaces.swerveLBTDesAng = self._swervelib.whl.angle3
        interfaces.swerveRBTDesAng = self._swervelib.whl.angle4

    def UpdateDashboard(self, interfaces):
        #Swerve Desired Wheel Vectors
        wpilib.SmartDashboard.putNumber("Swerve LF Angle Des", interfaces.swerveLFTDesAng)	
        wpilib.SmartDashboard.putNumber("Swerve RF Angle Des", interfaces.swerveRFTDesAng)	
        wpilib.SmartDashboard.putNumber("Swerve LB Angle Des", interfaces.swerveLBTDesAng)	
        wpilib.SmartDashboard.putNumber("Swerve RB Angle Des", interfaces.swerveRBTDesAng)	

        wpilib.SmartDashboard.putNumber("Swerve LF Speed Des", self._swervelib.whl.speed2)	
        wpilib.SmartDashboard.putNumber("Swerve RF Speed Des", self._swervelib.whl.speed1)	
        wpilib.SmartDashboard.putNumber("Swerve LB Speed Des", self._swervelib.whl.speed3)	
        wpilib.SmartDashboard.putNumber("Swerve RB Speed Des", self._swervelib.whl.speed4)