import wpilib
import interfacesModule
import robot

class controllerManager:

    def controllerInit(self, interfaces):

        self.driveController = wpilib.XboxController(0)
        self.mechanismController = wpilib.XboxController(1)

    def controllerManagerPeriodic(self, interfaces):
        #drive controller
        interfaces.dTurn = self.driveController.getX(wpilib.XboxController.Hand.kRightHand)
        interfaces.dMoveX = self.driveController.getX(wpilib.XboxController.Hand.kLeftHand)
        interfaces.dMoveY = self.driveController.getY(wpilib.XboxController.Hand.kLeftHand)
        interfaces.dBallIntake = self.driveController.getAButton()

        #interfaces.dTurn = (interfaces.dTurn * abs(interfaces.dTurn) * (abs(interfaces.dTurn) / 2))
        interfaces.dTurn = (interfaces.dTurn ** 5)
        interfaces.dMoveX = interfaces.dMoveX * abs(interfaces.dMoveX)
        interfaces.dMoveY = interfaces.dMoveY * abs(interfaces.dMoveY)

        #When in winch mode, slow the drivetrain way down to make lining up the hook easier
        if(self.driveController.getStartButton()):
            interfaces.dMoveX = interfaces.dMoveX / 6
            interfaces.dMoveY = interfaces.dMoveY / 6      
            interfaces.dTurn = interfaces.dTurn / 2

        #Add deadband
        deadBand = 0.04
        if(abs(interfaces.dMoveX) < deadBand):
            interfaces.dMoveX = 0
        if(abs(interfaces.dMoveY) < deadBand):
            interfaces.dMoveY = 0
        if(abs(interfaces.dTurn) < deadBand):
            interfaces.dTurn = 0

        #Hold start button to enable the winch, driver triggers to raise or lower it
        if self.driveController.getStartButton():
            interfaces.dClimbWinchPower = -self.driveController.getTriggerAxis(wpilib.XboxController.Hand.kLeftHand)
            if(self.driveController.getBumper(wpilib.XboxController.Hand.kRightHand)):
                interfaces.dClimbRaisePower = .4
            elif(self.driveController.getBumper(wpilib.XboxController.Hand.kLeftHand)):
                interfaces.dClimbRaisePower = -.6
            else:
                interfaces.dClimbRaisePower = 0
        else:
            interfaces.dClimbWinchPower = 0
            interfaces.dClimbRaisePower = 0

        #mechanism controller
        interfaces.mIndexerAdvance = self.mechanismController.getAButtonPressed()
        interfaces.mIndexerReverse = self.mechanismController.getBButtonPressed()

        #indexer and shooter manual control
        interfaces.indexerManMode = self.mechanismController.getBackButton()
        if(interfaces.indexerManMode):
            #if(self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kLeftHand) > .1):
                #interfaces.indexerManPower = .15
            #elif(self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kRightHand) > .1):
                #interfaces.indexerManPower = -.15
            interfaces.indexerManPower = self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kLeftHand) - self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kRightHand)
            #else:
                #interfaces.indexerManPower = 0

            #Wall Shot
            if(self.mechanismController.getAButtonPressed()):
                interfaces.shooterManTopDesSpd = interfaces.shooterSpdTopWallShot
                interfaces.shooterManBotDesSpd = interfaces.shooterSpdBotWallShot
            
            #10 foot shot
            elif(self.mechanismController.getBButtonPressed()):
                interfaces.shooterManTopDesSpd = interfaces.shooterSpdTopLongShot
                interfaces.shooterManBotDesSpd = interfaces.shooterSpdBotLongShot
        else: 

            if(self.mechanismController.getXButtonPressed()):
                interfaces.shooterManTopDesSpd = interfaces.shooterSpdTopWallShot
                interfaces.shooterManBotDesSpd = interfaces.shooterSpdBotWallShot
            #10 foot shot
            elif(self.mechanismController.getYButtonPressed()):
                interfaces.shooterManTopDesSpd = interfaces.shooterSpdTopLongShot
                interfaces.shooterManBotDesSpd = interfaces.shooterSpdBotLongShot
            elif(self.mechanismController.getStartButtonPressed()):
                interfaces.shooterManTopDesSpd = 0
                interfaces.shooterManBotDesSpd = 0


        interfaces.intakeReverse = self.driveController.getBackButton()

    def controllerManagerSmartDashboard(self, interfaces):
        wpilib.SmartDashboard.putNumber("swerve turn command", interfaces.dTurn)
        wpilib.SmartDashboard.putNumber("swerve move X command", interfaces.dMoveX)
        wpilib.SmartDashboard.putNumber("swerve move Y command", interfaces.dMoveY)
        wpilib.SmartDashboard.putBoolean("ball intake command", interfaces.dBallIntake)
        wpilib.SmartDashboard.putNumber("climb winch command", interfaces.dClimbWinchPower)
        wpilib.SmartDashboard.putBoolean("raise spinny wheel command", interfaces.mSpinnyRaise)
        wpilib.SmartDashboard.putBoolean("spinny phase 1 command", interfaces.mSpinnyPhase1)
        wpilib.SmartDashboard.putBoolean("spinny phase 2 command", interfaces.mSpinnyPhase2)
        wpilib.SmartDashboard.putBoolean("shoot against wall command", interfaces.mShootAgainstWall)
        wpilib.SmartDashboard.putBoolean("shoot from start line command", interfaces.mShootStartLine)
        wpilib.SmartDashboard.putBoolean("shoot from start line auto command", interfaces.mShootStartLineAuto)
        wpilib.SmartDashboard.putBoolean("shoot from trench command", interfaces.mShootTrench)
        wpilib.SmartDashboard.putBoolean("shoot from trench auto command", interfaces.mShootTrenchAuto)
        wpilib.SmartDashboard.putBoolean("reverse indexer command", interfaces.mReverseIndexer)
        wpilib.SmartDashboard.putNumber("begin spinning the shooter command", interfaces.mStartShooter)
        wpilib.SmartDashboard.putNumber("Indexer Manual Power", interfaces.indexerManPower)