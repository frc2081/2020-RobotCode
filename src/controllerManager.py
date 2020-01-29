import wpilib

class controllerManager:
    def controllerInit(self):

        self.driveController = wpilib.XboxController(0)
        self.mechanismController = wpilib.XboxController(1)

        #driver controller
        self.dTurn = 0
        self.dMoveX = 0
        self.dMoveY = 0
        self.dBallIntake = False
        #self.dBallOther = False
        self.dClimbRelease = False
        self.dClimbWinch = 0

        #mechanism controller
        self.mSpinnyRaise = False
        self.mSpinnyPhase1 = False
        self.mSpinnyPhase2 = False
        self.mShootAgainstWall = False
        self.mShootStartLine = False
        self.mShootStartLineAuto = False
        self.mShootTrench = False
        self.mShootTrenchAuto = False
        self.mReverseIndexer = False
        self.mStartShooter = 0

        wpilib.SmartDashboard.putNumber("swerve turn command", self.dTurn)
        wpilib.SmartDashboard.putNumber("swerve move X command", self.dMoveX)
        wpilib.SmartDashboard.putNumber("swerve move Y command", self.dMoveY)
        wpilib.SmartDashboard.putBoolean("ball intake command", self.dBallIntake)
        wpilib.SmartDashboard.putBoolean("climb release command", self.dClimbRelease)
        wpilib.SmartDashboard.putNumber("climb winch command", self.dClimbWinch)
        wpilib.SmartDashboard.putBoolean("raise spinny wheel command", self.mSpinnyRaise)
        wpilib.SmartDashboard.putBoolean("spinny phase 1 command", self.mSpinnyPhase1)
        wpilib.SmartDashboard.putBoolean("spinny phase 2 command", self.mSpinnyPhase2)
        wpilib.SmartDashboard.putBoolean("shoot against wall command", self.mShootAgainstWall)
        wpilib.SmartDashboard.putBoolean("shoot from start line command", self.mShootStartLine)
        wpilib.SmartDashboard.putBoolean("shoot from start line auto command", self.mShootStartLineAuto)
        wpilib.SmartDashboard.putBoolean("shoot from trench command", self.mShootTrench)
        wpilib.SmartDashboard.putBoolean("shoot from trench auto command", self.mShootTrenchAuto)
        wpilib.SmartDashboard.putBoolean("reverse indexer command", self.mReverseIndexer)
        wpilib.SmartDashboard.putNumber("begin spinning the shooter command", self.mStartShooter)

    def controllerManagerPeriodic(self):
        #drive controller
        self.dTurn = self.driveController.getX(wpilib.XboxController.Hand.kRightHand)
        self.dMoveX = self.driveController.getX(wpilib.XboxController.Hand.kLeftHand)
        self.dMoveY = self.driveController.getY(wpilib.XboxController.Hand.kLeftHand)
        self.dBallIntake = self.driveController.getAButton()
        #self.dBallOther = 
        if self.driveController.getBumper(wpilib.XboxController.Hand.kLeftHand) & self.driveController.getStartButton():
            self.dClimbRelease = True
        else:
            self.dClimbRelease = False
        self.dClimbWinch = self.driveController.getTriggerAxis(wpilib.XboxController.Hand.kLeftHand)
        

        #mechanism controller
        self.mSpinnyRaise = self.mechanismController.getBumper(wpilib.XboxController.Hand.kLeftHand)
        self.mSpinnyPhase1 = self.mechanismController.getBackButton()
        self.mSpinnyPhase2 = self.mechanismController.getStartButton()
        self.mShootAgainstWall = self.mechanismController.getAButton()
        if self.mechanismController.getBButton() and not (self.mechanismController.getBumper(wpilib.XboxController.Hand.kRightHand)):
            self.mShootStartLine = True
        else:
            self.mShootStartLine = False
        if self.mechanismController.getBButton() & self.mechanismController.getBumper(wpilib.XboxController.Hand.kRightHand):
            self.mShootStartLineAuto = True
        else:
            self.mShootStartLineAuto = False
        if self.mechanismController.getYButton() and not self.mechanismController.getBumper(wpilib.XboxController.Hand.kRightHand):
            self.mShootTrench = True
        else:
            self.mShootTrench = False
        if self.mechanismController.getYButton() & self.mechanismController.getBumper(wpilib.XboxController.Hand.kRightHand):
            self.mShootTrenchAuto = True
        else:
            self.mShootTrenchAuto = False
        self.mReverseIndexer = self.mechanismController.getXButton()
        self.mStartShooter = self.mechanismController.getTriggerAxis(wpilib.XboxController.Hand.kRightHand)
    def controllerManagerSmartDashboard(self):
        wpilib.SmartDashboard.putNumber("swerve turn command", self.dTurn)
        wpilib.SmartDashboard.putNumber("swerve move X command", self.dMoveX)
        wpilib.SmartDashboard.putNumber("swerve move Y command", self.dMoveY)
        wpilib.SmartDashboard.putBoolean("ball intake command", self.dBallIntake)
        wpilib.SmartDashboard.putBoolean("climb release command", self.dClimbRelease)
        wpilib.SmartDashboard.putNumber("climb winch command", self.dClimbWinch)
        wpilib.SmartDashboard.putBoolean("raise spinny wheel command", self.mSpinnyRaise)
        wpilib.SmartDashboard.putBoolean("spinny phase 1 command", self.mSpinnyPhase1)
        wpilib.SmartDashboard.putBoolean("spinny phase 2 command", self.mSpinnyPhase2)
        wpilib.SmartDashboard.putBoolean("shoot against wall command", self.mShootAgainstWall)
        wpilib.SmartDashboard.putBoolean("shoot from start line command", self.mShootStartLine)
        wpilib.SmartDashboard.putBoolean("shoot from start line auto command", self.mShootStartLineAuto)
        wpilib.SmartDashboard.putBoolean("shoot from trench command", self.mShootTrench)
        wpilib.SmartDashboard.putBoolean("shoot from trench auto command", self.mShootTrenchAuto)
        wpilib.SmartDashboard.putBoolean("reverse indexer command", self.mReverseIndexer)
        wpilib.SmartDashboard.putNumber("begin spinning the shooter command", self.mStartShooter)