import wpilib
import indexerSubsystem
class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.indexerInst = indexerSubsystem.indexer()
        self.indexerInst.indexerInit()

    def teleopPeriodic(self):
        self.indexerInst.indexerPeriodic()        

if __name__ == "__main__":
    wpilib.run(MyRobot)