class subSystemOne:
    def __init__(self):
        pass
        
    def periodic(self, interfaces):
        print("subSystemOne Periodic function called")
        interfaces.lDriveMotorPower = .5