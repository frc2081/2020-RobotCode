import wpilib

import interfacesModule
import ioModule
import controllerManager
import indexerSubsystem

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.interfaces = interfacesModule.interfaces()
        #self.io = ioModule.io()
        #self.subSysOne = subSystemOneModule.subSystemOne()
        #self.subSysTwo = subSystemTwoModule.subSystemTwo()
        self.interfaces.interfacesInit()
        self.controllerManagerInst = controllerManager.controllerManager()
        self.controllerManagerInst.controllerInit(self.interfaces)
        self.ioModuleInst = ioModule.io(self.interfaces)
        self.indexerSubsystemInst = indexerSubsystem.indexer() 
        self.indexerSubsystemInst.indexerInit(self.interfaces)
        #self.ioModuleInst.__init__(self.interfaces)

    def robotPeriodic(self):
        #self.io.periodic(self.interfaces)
        #self.subSysOne.periodic(self.interfaces)
        #self.subSysTwo.periodic(self.interfaces)
        self.ioModuleInst.periodic(self.interfaces)
        self.indexerSubsystemInst.indexerPeriodic(self.interfaces)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        self.controllerManagerInst.controllerManagerPeriodic(self.interfaces)
        self.controllerManagerInst.controllerManagerSmartDashboard(self.interfaces)
        self.ioModuleInst.teleopperiodic(self.interfaces)

if __name__ == "__main__":
    wpilib.run(MyRobot)