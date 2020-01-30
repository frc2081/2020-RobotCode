import wpilib
import interfacesModule
import robot

class controllerManager:
    def controllerInit(self):

        self.driveController = wpilib.XboxController(0)
        self.mechanismController = wpilib.XboxController(1)

        wpilib.SmartDashboard.putNumber("swerve turn command", self.interfaces.dTurn)
        wpilib.SmartDashboard.putNumber("swerve move X command", interfaces.dMoveX)
        wpilib.SmartDashboard.putNumber("swerve move Y command", interfaces.dMoveY)
        wpilib.SmartDashboard.putBoolean("ball intake command", interfaces.dBallIntake)
        wpilib.SmartDashboard.putBoolean("climb release command", interfaces.dClimbRelease)
        wpilib.SmartDashboard.putNumber("climb winch command", interfaces.dClimbWinch)
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

    def controllerManagerPeriodic(self, interfaces):
        #drive controller
        interfaces.dTurn = self.driveController.getX(wpilib.XboxController.Hand.kRightHand)
        interfaces.dMoveX = self.driveController.getX(wpilib.XboxController.Hand.kLeftHand)
        interfaces.dMoveY = self.driveController.getY(wpilib.XboxController.Hand.kLeftHand)
        interfaces.dBallIntake = self.driveController.getAButton()
        #self.dBallOther = 
        if self.driveController.getBumper(wpilib.XboxController.Hand.kLeftHand) & self.driveController.getStartButton():
            interfaces.dClimbRelease = True
        else:
            interfaces.dClimbRelease = False
        interfaces.dClimbWinch = self.driveController.getTriggerAxis(wpilib.XboxController.Hand.kLeftHand)
        

        #mechanism controller
        interfaces.mSpinnyRaise = self.mechanismController.getBumper(wpilib.XboxController.Hand.kLeftHand)
        interfaces.mSpinnyPhase1 = self.mechanismController.getBackButton()
        interfaces.mSpinnyPhase2 = self.mechanismController.getStartButton()
        interfaces.mShootAgainstWall = self.mechanismController.getAButton()
        if self.mechanismController.getBButton() and not (self.mechanismController.getBumper(wpilib.XboxController.Hand.kRightHand)):
            interfaces.mShootStartLine = True
        else:
            interfaces.mShootStartLine = False
        if self.mechanismController.getBButton() & self.mechanismController.getBumper(wpilib.XboxController.Hand.kRightHand):
            interfaces.mShootStartLineAuto = True
        else:
            interfaces.mShootStartLineAuto = False
        if self.mechanismController.getYButton() and not self.mechanismController.getBumper(wpilib.XboxController.Hand.kRightHand):
            interfaces.mShootTrench = True
        else:
            interfaces.mShootTrench = False
        if self.mechanismController.getYButton() & self.mechanismController.getBumper(wpilib.XboxController.Hand.kRightHand):
            interfaces.mShootTrenchAuto = True
        else:
            interfaces.mShootTrenchAuto = False
        interfaces.mReverseIndexer = self.mechanismController.getXButton()
        interfaces.mStartShooter = self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kRightHand)
    def controllerManagerSmartDashboard(self, interfaces):
        wpilib.SmartDashboard.putNumber("swerve turn command", interfaces.dTurn)
        wpilib.SmartDashboard.putNumber("swerve move X command", interfaces.dMoveX)
        wpilib.SmartDashboard.putNumber("swerve move Y command", interfaces.dMoveY)
        wpilib.SmartDashboard.putBoolean("ball intake command", interfaces.dBallIntake)
        wpilib.SmartDashboard.putBoolean("climb release command", interfaces.dClimbRelease)
        wpilib.SmartDashboard.putNumber("climb winch command", interfaces.dClimbWinch)
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