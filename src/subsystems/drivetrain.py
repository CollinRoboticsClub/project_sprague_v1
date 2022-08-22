from gyro import Gyro
from smart_motor import SmartMotor

class Drivetrain:
	def __init__(self):
		self.gyro = Gyro()

	def setup(self):
		self.gyro.setup()

	def periodic(self):
		self.gyro.periodic()