import wpilib

import interfacesModule
import ioModule
import controllerManager
import indexerSubsystem
import intakeSubSystem

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.ioInst = ioModule.io()
        self.interfaces = interfacesModule.interfaces()
        self.driveManagerInst = DriveManager.DriveManager()

        self.interfaces.interfacesInit()

        self.controllerManagerInst = controllerManager.controllerManager()
        self.controllerManagerInst.controllerInit(self.interfaces)
        self.ioModuleInst = ioModule.io(self.interfaces)

        self.indexerSubsystemInst = indexerSubsystem.indexer() 
        self.indexerSubsystemInst.indexerInit(self.interfaces)

        self.intake = intakeSubSystem.intakeSystem(self.interfaces)
        self.intake.intakeInit(self.interfaces)

    def robotPeriodic(self):

        self.ioModuleInst.periodic(self.interfaces)
        self.indexerSubsystemInst.indexerPeriodic(self.interfaces)
        self.ioInst.robotPeriodic()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        self.controllerManagerInst.controllerManagerPeriodic(self.interfaces)
        self.controllerManagerInst.controllerManagerSmartDashboard(self.interfaces)
        self.ioModuleInst.teleopperiodic(self.interfaces)
        self.intake.intakePeriodic(self.interfaces)

if __name__ == "__main__":
    wpilib.run(MyRobot)