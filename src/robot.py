import wpilib

import interfacesModule
import ioModule
import controllerManager
import DriveManager

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.ioInst = ioModule.io()
        self.interfaces = interfacesModule.interfaces()
        self.driveManagerInst = DriveManager.DriveManager()

        #self.io = ioModule.io()
        #self.subSysOne = subSystemOneModule.subSystemOne()
        #self.subSysTwo = subSystemTwoModule.subSystemTwo()
        self.interfaces.interfacesInit()
        self.controllerManagerInst = controllerManager.controllerManager()
        self.controllerManagerInst.controllerInit(self.interfaces)

    def robotPeriodic(self):
        #self.io.periodic(self.interfaces)
        #self.subSysOne.periodic(self.interfaces)
        #self.subSysTwo.periodic(self.interfaces)
        self.ioInst.robotPeriodic()
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        self.controllerManagerInst.controllerManagerPeriodic(self.interfaces)
        self.controllerManagerInst.controllerManagerSmartDashboard(self.interfaces)
        self.driveManagerInst.DriveManagerPeriodic(self.interfaces)

if __name__ == "__main__":
    wpilib.run(MyRobot)