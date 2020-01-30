import wpilib

class interfaces:

    def interfacesInit(self):
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