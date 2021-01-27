import wpilib

import interfacesModule
import ioModule
import controllerManager
import DriveManager
import indexerSubsystem
import intakeSubSystem
import autonomousDrive

class MyRobot(wpilib.TimedRobot):

    #This is an example comment

    autoTimer = 0
    #^started at 0
    autoTimerQuarterSecond = 0
    #^comment for symmetry
    autoSpoolTime = 100
    #^started at 100
    autoShootTime = 500
    #^started at 500
    autoDriveTime = 530
    #^started at 600
    autoShooterTopSpd = 300
    #^started at 700
    autoShooterBotSpd = -3800
    #^started at -1800
    autoDriveX = -.5
    #^started at .5    
    autoDriveY = 0
    #^started at 0

    autoMode = 0 # 0 = 10 foot shot, 1 = shot against wall

    def robotInit(self):

        wpilib.CameraServer.launch('vision.py:main')
        self.interfaces = interfacesModule.interfaces()
        self.interfaces.interfacesInit()       
         
        self.ioInst = ioModule.io(self.interfaces)

        self.driveManagerInst = DriveManager.DriveManager()
        self.driveManagerInst.DriveManagerInit(self.interfaces)

        self.controllerManagerInst = controllerManager.controllerManager()
        self.controllerManagerInst.controllerInit(self.interfaces)

        self.indexer = indexerSubsystem.indexerSystem(self.interfaces) 

        self.intake = intakeSubSystem.intakeSystem(self.interfaces)
        self.intake.init(self.interfaces)

    def robotPeriodic(self):   
        self.ioInst.robotPeriodic(self.interfaces)

    def autonomousInit(self):
        
        self.autoTimer = 0
        #Configure Auto mode
        #shot from 10 foot line
        if(self.autoMode == 0):
            self.autoSpoolTime = 100
            self.autoShootTime = 500
            self.autoDriveTime = 530
            self.autoDriveX = .5    
            self.autoDriveY = 0
            self.autoShooterTopSpd = self.interfaces.shooterSpdTopLongShot
            self.autoShooterBotSpd = self.interfaces.shooterSpdBotLongShot

        #Stationary shot against wall
        elif(self.autoMode == 1):
            self.autoSpoolTime = 100
            self.autoShootTime = 500
            self.autoDriveTime = 530
            self.autoDriveX = 0 
            self.autoDriveY = 0
            self.autoShooterTopSpd = self.interfaces.shooterSpdBotWallShot
            self.autoShooterBotSpd = self.interfaces.shooterSpdBotWallShot


    def autonomousPeriodic(self):
        self.autoTimer += 1

        if(self.autoTimer % 12.5 == 0):
            if(self.autoTimerQuarterSecond < len(self.autonomousDrive.autonomousInputs)):
                self.autoTimerQuarterSecond = self.autoTimer / 12.5
                #update every quarter second, assuming it already updates every 50ms, or 20/s
                #limits the timer increase so that it doesn't try to access a value beyond what is in the list
            self.interfaces.dMoveX = self.autonomousDrive.autonomousInputs[autoTimerQuarterSecond][1]
            self.interfaces.dMoveY = self.autonomousDrive.autonomousInputs[autoTimerQuarterSecond][2]
            self.interfaces.dTurn = self.autonomousDrive.autonomousInputs[autoTimerQuarterSecond][3]

        """
        if(self.autoTimer < self.autoShootTime):
            self.interfaces.indexerManMode = True
            self.interfaces.indexerManPower = 0
            self.interfaces.shooterManTopDesSpd = self.autoShooterTopSpd
            self.interfaces.shooterManBotDesSpd = self.autoShooterBotSpd
            self.interfaces.dMoveY = 0
            self.interfaces.dMoveX = 0

        if((self.autoTimer < self.autoShootTime) and (self.autoTimer > self.autoSpoolTime)):
            self.interfaces.indexerManPower = -.25
            

        if((self.autoTimer > self.autoShootTime) and (self.autoTimer < self.autoDriveTime)):
            self.interfaces.dMoveY = self.autoDriveX
            self.interfaces.dMoveX = self.autoDriveY
            self.interfaces.indexerManMode = False
            self.interfaces.indexerManPower = 0
            self.interfaces.shooterManTopDesSpd = 0
            self.interfaces.shooterManBotDesSpd = 0

        if(self.autoTimer > self.autoDriveTime):
            self.interfaces.dMoveX = 0
            self.interfaces.dMoveY = 0
        """

        self.driveManagerInst.DriveManagerPeriodic(self.interfaces)
        self.intake.teleopPeriodic(self.interfaces)
        self.ioInst.teleopPeriodic(self.interfaces)

    def teleopInit(self):
        
        self.ioInst.teleopInit(self.interfaces)
        self.indexer.teleopInit(self.interfaces)

    def teleopPeriodic(self):
        
        self.controllerManagerInst.controllerManagerPeriodic(self.interfaces)
        self.driveManagerInst.DriveManagerPeriodic(self.interfaces)

        self.intake.teleopPeriodic(self.interfaces)
        self.indexer.teleopPeriodic(self.interfaces)
        self.ioInst.teleopPeriodic(self.interfaces)

if __name__ == "__main__":
    wpilib.run(MyRobot)