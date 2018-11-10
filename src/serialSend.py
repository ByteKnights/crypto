import serial


def send(port):
    s = serial.Serial(port)

    def sendData(self, data):
        s.write(data)
