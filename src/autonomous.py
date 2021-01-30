import interfacesModule
import robot

class autonomousDrive:
    #array for inputs
    #currently represents 10 seconds of inputs at 1 change every 1/4 second
    #**THIS WILL SPIN REALLY FAST**
    #left stick X; left stick Y; right stick X (rudder)
    autonomousInputs = [
        #1
        [0, 0, 0],
        [0, 0, 0.1],
        [0, 0, 0.2],
        [0, 0, 0.3],
        #2
        [0, 0, 0.4],
        [0, 0, 0.5],
        [0, 0, 0.6],
        [0, 0, 0.7],
        #3
        [0, 0, 0.8],
        [0, 0, 0.9],
        [0, 0, 1],
        [0, 0, 1],
        #4
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        #5
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        #6
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        #7
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
        #8
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 0.9],
        [0, 0, 0.8],
        #9
        [0, 0, 0.7],
        [0, 0, 0.6],
        [0, 0, 0.5],
        [0, 0, 0.4],
        #10
        [0, 0, 0.3],
        [0, 0, 0.2],
        [0, 0, 0.1],
        [0, 0, 0],
        #leave last one blank to ensure the robot stops moving at the end of the code
        [0, 0, 0],
        ]

    def autonomousDrive(self, interfaces):
            pass