import subprocess

def findParticle():
    if subprocess.call("udevadm info /dev/ttyACM0 | head -3 | tail -1", shell=True) == \
            "S: serial/by-id/usb-239a_Adafruit_Industries-if00":
        return "/dev/ttyACM0"
    else:
        return "/dev/ttyACM1"
findParticle()