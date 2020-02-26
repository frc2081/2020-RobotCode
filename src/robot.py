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
    autoShooterTopSpd = 700
    autoShooterBotSpd = -1800
    autoDriveX = .5    
    autoDriveY = 0

    autoMode = 0 # 0 = 10 foot shot, 1 = shot against wall

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

    def autonomousInit(self):
        self.autoTimer = 0
        #Configure Auto mode
        #shot from 10 foot line
        if(self.autoMode == 0):
            self.autoSpoolTime = 100
            self.autoShootTime = 500
            self.autoDriveTime = 600
            self.autoDriveX = .5    
            self.autoDriveY = 0
            self.autoShooterTopSpd = 700
            self.autoShooterBotSpd = -1800

        #Stationary shot against wall
        elif(self.autoMode == 1):
            self.autoSpoolTime = 100
            self.autoShootTime = 500
            self.autoDriveTime = 600
            self.autoDriveX = 0 
            self.autoDriveY = 0
            self.autoShooterTopSpd = 200
            self.autoShooterBotSpd = -1600
        pass

    def autonomousPeriodic(self):
        self.autoTimer = self.autoTimer + 1

        self.interfaces.shooterManTopDesSpd = self.autoShooterTopSpd
        self.interfaces.shooterManBotDesSpd = self.autoShooterBotSpd
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