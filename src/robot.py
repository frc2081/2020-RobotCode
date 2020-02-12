import wpilib

import interfacesModule
import ioModule
import controllerManager
import DriveManager
import indexerSubsystem
import intakeSubSystem

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.interfaces = interfacesModule.interfaces()
        self.interfaces.interfacesInit()       
         
        self.ioInst = ioModule.io(self.interfaces)

        self.driveManagerInst = DriveManager.DriveManager()

        self.controllerManagerInst = controllerManager.controllerManager()
        self.controllerManagerInst.controllerInit(self.interfaces)

        self.indexerSubsystemInst = indexerSubsystem.indexer() 
        self.indexerSubsystemInst.indexerInit(self.interfaces)

        self.intake = intakeSubSystem.intakeSystem(self.interfaces)
        self.intake.init(self.interfaces)

    def robotPeriodic(self):
        self.indexerSubsystemInst.indexerPeriodic(self.interfaces)
        self.ioInst.robotPeriodic(self.interfaces)
        self.controllerManagerInst.controllerManagerSmartDashboard(self.interfaces)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):
        self.controllerManagerInst.controllerManagerPeriodic(self.interfaces)
        self.ioInst.teleopPeriodic(self.interfaces)
        self.intake.teleopPeriodic(self.interfaces)

if __name__ == "__main__":
    wpilib.run(MyRobot)