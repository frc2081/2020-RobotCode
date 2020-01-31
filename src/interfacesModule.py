import wpilib

class interfaces:
    #driver controller
    dTurn = 0
    dMoveX = 0
    dMoveY = 0
    dBallIntake = False
    #self.dBallOther = False
    dClimbRelease = False
    dClimbWinch = 0

    #mechanism controller
    mSpinnyRaise = False
    mSpinnyPhase1 = False
    mSpinnyPhase2 = False
    mShootAgainstWall = False
    mShootStartLine = False
    mShootStartLineAuto = False
    mShootTrench = False
    mShootTrenchAuto = False
    mReverseIndexer = False
    mStartShooter = 0

    def __init__(self):
        pass

    def interfacesInit(self):
        pass
