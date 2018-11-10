from src import serialSend
from src import pgp

cipher = pgp.encrypt("hello World", "testUser1")
serialSend.send("/dev/tty0", cipher)

