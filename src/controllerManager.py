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

        interfaces.dTurn = interfaces.dTurn * abs(interfaces.dTurn)
        interfaces.dMoveX = interfaces.dMoveX * abs(interfaces.dMoveX)
        interfaces.dMoveY = interfaces.dMoveY * abs(interfaces.dMoveY)

        #Add deadband
        deadBand = 0.08
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
                interfaces.dClimbRaisePower = -.4
            else:
                interfaces.dClimbRaisePower = 0
        else:
            interfaces.dClimbWinchPower = 0
            interfaces.dClimbRaisePower = 0

        #mechanism controller
        interfaces.mShootAgainstWall = self.mechanismController.getAButton()


        #indexer and shooter manual control
        interfaces.indexerManMode = self.mechanismController.getBackButton()
        if(interfaces.indexerManMode):
            if(self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kLeftHand) > .1):
                interfaces.indexerManPower = .25
            elif(self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kRightHand) > .1):
                interfaces.indexerManPower = -.25
            else:
                interfaces.indexerManPower = 0

            #interfaces.indexerManPower = self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kLeftHand) - self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kRightHand)
            if(self.mechanismController.getAButtonPressed()):
                interfaces.shooterManTopDesSpd = 200
                interfaces.shooterManBotDesSpd = -1600
 
            elif(self.mechanismController.getBButtonPressed()):
                interfaces.shooterManTopDesSpd = 700
                interfaces.shooterManBotDesSpd = -1800
        else:
            interfaces.shooterManTopDesSpd = 0
            interfaces.shooterManBotDesSpd = 0
            interfaces.indexerManPower = 0     
        
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