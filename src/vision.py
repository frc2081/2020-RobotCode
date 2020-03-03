from cscore import CameraServer

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    usb1 = cs.startAutomaticCapture(dev=0)
    usb2 = cs.startAutomaticCapture(dev=1)

    usb1.setResolution(160, 120)
    usb2.setResolution(160, 120)

    usb1.setFPS(10)
    usb2.setFPS(10)

    cs.waitForever()