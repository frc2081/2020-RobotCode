import interfacesModule
import robot

import math

class autonomousDrive:
    A = 0
    B = 0

    #for changing between using autonomousInputsVector and autonomousInputs
    #1 is yes, 0 is no
    #recommend 1 (yes)
    useVectorInputs = 1

    #arrays for inputs
    #currently represents 10 seconds of inputs at 1 change every 1/4 second

    """first is angle (0-360), second is stength (0-1, although -1 is valid)"""
    autonomousInputsVector = [
        #1
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #2
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #3
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #4
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #5
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #6
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #7
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #8
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #9
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #10
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        #leave last one blank to ensure the robot stops moving at the end of the code
        [0, 0],
        ]

    """left stick X; left stick Y; right stick X (rudder)"""
    autonomousInputs = [
        #1
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #2
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #3
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #4
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #5
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #6
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #7
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #8
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #9
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #10
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        #leave last one blank to ensure the robot stops moving at the end of the code
        [0, 0, 0],
        ]

    """rotation only"""
    autonomousInputsRudder = [
        #1
        0,
        0.1,
        0.2,
        0.3,
        #2
        0.4,
        0.5,
        0.6,
        0.7,
        #3
        0.8,
        0.9,
        1,
        1,
        #4
        1,
        1,
        1,
        1,
        #5
        1,
        1,
        1,
        1,
        #6
        1,
        1,
        1,
        1,
        #7
        1,
        1,
        1,
        1,
        #8
        1,
        1,
        0.9,
        0.8,
        #9
        0.7,
        0.6,
        0.5,
        0.4,
        #10
        0.3,
        0.2,
        0.1,
        0,
        #leave last one blank to ensure the robot stops moving at the end of the code
        0,
        ]

    def autonomousInit(self):
        if (self.useVectorInputs == 1):
            for i in range(len(self.autonomousInputs)):
                A = ((self.autonomousInputsVector[i][1]) * math.cos(self.autonomousInputsVector[i][0]))
                B = ((self.autonomousInputsVector[i][1]) * math.sin(self.autonomousInputsVector[i][0]))
                self.autonomousInputs[i][0] = self.autonomousInputsVector[i][self.A]
                self.autonomousInputs[i][1] = self.autonomousInputsVector[i][self.B]

        for e in range(len(self.autonomousInputs)):
            self.autonomousInputs[e][2] = self.autonomousInputsRudder[e]

    def __init__(self):
        pass

    def autonomousDrive(self, interfaces):
        pass