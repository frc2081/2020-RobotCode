class subSystemTwo:
    def __init__(self):
        pass
    
    def periodic(self, interfaces):
        print("subSystemTwo Periodic function called")
        interfaces.lDriveMotorPower = 1
