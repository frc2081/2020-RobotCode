import wpilib

import interfacesModule
import ioModule
import subSystemOneModule
import subSystemTwoModule

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        interfaces = interfacesModule.interfaces()
        io = ioModule.io()
        subSysOne = subSystemOneModule.subSystemOne()
        subSysTwo = subSystemTwoModule.subSystemTwo()

    def robotPeriodic(self):
        io.periodic(interfaces)
        subSysOne.periodic(interfaces)
        subSysTwo.periodic(interfaces)

    def autonomousInit(self):

    def autonomousPeriodic(self):

    def teleopPeriodic(self):

if __name__ == "__main__":
    wpilib.run(MyRobot)