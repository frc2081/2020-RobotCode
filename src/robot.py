import wpilib

import interfacesModule
import ioModule
import subSystemOneModule
import subSystemTwoModule

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.interfaces = interfacesModule.interface()
        self.io = ioModule.io()
        self.subSysOne = subSystemOneModule.subSystemOne()
        self.subSysTwo = subSystemTwoModule.subSystemTwo()

    def robotPeriodic(self):
        self.io.periodic(self.interfaces)
        self.subSysOne.periodic(self.interfaces)
        self.subSysTwo.periodic(self.interfaces)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)