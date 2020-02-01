#!/usr/bin/env
import math
from networktables import NetworkTables
import wpilib
#pi is math.pi

def degrees_to_radians(degrees):
    radians = 0
    radians = (degrees * math.pi) / 180
    return radians

def radians_to_degrees(radians):
    degrees = 0
    degrees = radians * 180 / math.pi
    return degrees



class wheel():
    #front right, front left, rear left, rear right
    speed1 = 0
    speed2 = 0
    speed3 = 0
    speed4 = 0
    #front right, front left, rear left, rear right
    angle1 = 0
    angle2 = 0
    angle3 = 0
    angle4 = 0

#width and length are between the wheels, not the robot's dimensions
class SwerveLib():
    _targetWhlSpeed_RF = 0
    _targetWhlSpeed_LF = 0
    _targetWhlSpeed_LB = 0
    _targetWhlSpeed_RB = 0
    _targetWhlAng_RF = 0
    _targetWhlAng_LF = 0
    _targetWhlAng_LB = 0
    _targetWhlAng_RB = 0
    _currAngRF = 0
    _currAngLF = 0
    _currAngLB = 0
    _currAngRB = 0
    _MaxWhlSpeed = 0

    _A = 0
    _B = 0
    _C = 0
    _D = 0

    whl = wheel()

    #Radius of robot - corner to center
    def __init__(self, width, length):
        self._radius = math.sqrt(pow(width, 2) + pow(length, 2))
        self._width = width
        self._length = length



    def calcWheelVect(self, mag, ang, rudder):

        #Constructs a X and Y vector from the given magnitude and angle
        _centerVecX = mag * math.cos(degrees_to_radians(ang+90))
        _centerVecY = mag * math.sin(degrees_to_radians(ang+90))

        wpilib.SmartDashboard.putNumber("Swerve Center Vec X", _centerVecX)
        wpilib.SmartDashboard.putNumber("Swerve Center Vec Y", _centerVecY)

        #Last commanded wheel angles
        _currAngRF = self.whl.speed1
        _currAngLF = self.whl.speed2
        _currAngLB = self.whl.speed3
        _currAngRB = self.whl.speed4

        #Calculate the wheel motion vectors.
        #Wheel 1
        #X = B
        #Y = C
        #Wheel 2
        #X = B
        #Y = D
        #Wheel 3
        #X = A
        #Y = D
        #Wheel 4
        #X = A
        #Y = C

        _A = _centerVecX - rudder * (self._length / self._radius)
        _B = _centerVecX + rudder * (self._length / self._radius)
        _C = _centerVecY - rudder * (self._width / self._radius)
        _D = _centerVecY + rudder * (self._width / self._radius)

        #Calculate the wheel speeds. Only Pythagroean Therom
        _targetWhlSpeed_RF = math.sqrt(pow(_B, 2) + pow(_C, 2))
        _targetWhlSpeed_LF = math.sqrt(pow(_B, 2) + pow(_D, 2))
        _targetWhlSpeed_LB = math.sqrt(pow(_A, 2) + pow(_D, 2))
        _targetWhlSpeed_RB = math.sqrt(pow(_A, 2) + pow(_C, 2))
        _MaxWhlSpeed = max(_targetWhlSpeed_RF, _targetWhlSpeed_LF, _targetWhlSpeed_LB, _targetWhlSpeed_RB)

        #Reducing any speed that is over 1, the max a motor can be commanded, to 1
        if (_MaxWhlSpeed > 1):
            _targetWhlSpeed_RF /= _MaxWhlSpeed
            _targetWhlSpeed_LF /= _MaxWhlSpeed
            _targetWhlSpeed_LB /= _MaxWhlSpeed
            _targetWhlSpeed_RB /= _MaxWhlSpeed
            
        #Calculating wanted angle of each wheel by taking an arc tangent of the wheel's vectors
        _targetWhlAng_RF = radians_to_degrees(math.atan2(_B, _C))
        _targetWhlAng_LF = radians_to_degrees(math.atan2(_B, _D))
        _targetWhlAng_LB = radians_to_degrees(math.atan2(_A, _D))
        _targetWhlAng_RB = radians_to_degrees(math.atan2(_A, _C))


        #Set the wheel speeds and angles to be accessed outside of the class
        self.whl.speed1 = _targetWhlSpeed_RF
        self.whl.speed2 = _targetWhlSpeed_LF
        self.whl.speed3 = _targetWhlSpeed_LB
        self.whl.speed4 = _targetWhlSpeed_RB

        self.whl.angle1 = 360 - (_targetWhlAng_RF + 180)
        self.whl.angle2 = 360 - (_targetWhlAng_LF + 180)
        self.whl.angle3 = 360 - (_targetWhlAng_LB + 180)
        self.whl.angle4 = 360 - (_targetWhlAng_RB + 180)
