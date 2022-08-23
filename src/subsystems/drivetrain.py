from gyro import Gyro
from smart_motor import SmartMotor
from constants import pins

class Drivetrain:
	def __init__(self):
		self.gyro = Gyro()
		self.left_motor = SmartMotor(pins.ENA, pins.IN1, pins.IN2)
		self.right_motor = SmartMotor(pins.ENB, pins.IN3, pins.IN4)

	def setup(self):
		self.gyro.setup()
		self.left_motor.setup()
		self.right_motor.setup()

	def periodic(self):
		self.left_motor.set_output(1)
		self.right_motor.set_output(1)

		self.gyro.periodic()
