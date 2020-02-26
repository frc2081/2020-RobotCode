import wpilib

import interfacesModule
import ioModule
import controllerManager
import DriveManager
import indexerSubsystem
import intakeSubSystem

class MyRobot(wpilib.TimedRobot):

    autoTimer = 0
    autoSpoolTime = 100
    autoShootTime = 500
    autoDriveTime = 600
    autoDriveX = .5    
    autoDriveY = 0

    def robotInit(self):

        wpilib.CameraServer.launch()
        self.interfaces = interfacesModule.interfaces()
        self.interfaces.interfacesInit()       
         
        self.ioInst = ioModule.io(self.interfaces)

        self.driveManagerInst = DriveManager.DriveManager()
        self.driveManagerInst.DriveManagerInit(self.interfaces)

        self.controllerManagerInst = controllerManager.controllerManager()
        self.controllerManagerInst.controllerInit(self.interfaces)

        self.indexerSubsystemInst = indexerSubsystem.indexer() 
        self.indexerSubsystemInst.indexerInit(self.interfaces)

        self.intake = intakeSubSystem.intakeSystem(self.interfaces)
        self.intake.init(self.interfaces)

    def robotPeriodic(self):
        pass
       
        self.ioInst.robotPeriodic(self.interfaces)
        #self.controllerManagerInst.controllerManagerSmartDashboard(self.interfaces)

    def autonomousInit(self):
        self.autoTimer = 0
        pass

    def autonomousPeriodic(self):
        self.autoTimer = self.autoTimer + 1

        self.interfaces.shooterManTopDesSpd = 700
        self.interfaces.shooterManBotDesSpd = -1800
        self.interfaces.dMoveY = 0
        self.interfaces.dMoveX = 0

        while((self.autoTimer < self.autoShootTime) and (self.autoTimer > self.autoSpoolTime)):
            self.interfaces.indexerManMode = True
            self.interfaces.indexerManPower = -.25

        while((self.autoTimer > self.autoShootTime) and (self.autoTimer < self.autoDriveTime)):
            self.interfaces.dMoveY = self.autoDriveX
            self.interfaces.dMoveX = self.autoDriveY
            self.interfaces.indexerManMode = False
            self.interfaces.indexerManPower = 0
            self.interfaces.shooterManTopDesSpd = 0
            self.interfaces.shooterManBotDesSpd = 0

    def teleopInit(self):
        pass
        self.ioInst.teleopInit(self.interfaces)

    def teleopPeriodic(self):
        pass
        self.controllerManagerInst.controllerManagerPeriodic(self.interfaces)
        self.driveManagerInst.DriveManagerPeriodic(self.interfaces)
        self.intake.teleopPeriodic(self.interfaces)
        self.ioInst.teleopPeriodic(self.interfaces)

if __name__ == "__main__":
    wpilib.run(MyRobot)