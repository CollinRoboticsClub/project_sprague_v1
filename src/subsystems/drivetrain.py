from subsystems.gyro import Gyro
from subsystems.smart_motor import SmartMotor
from constants import pins

class Drivetrain:
	def __init__(self):
		# self.gyro = Gyro()
		self.left_motor = SmartMotor(pins.ENA, pins.IN1, pins.IN2, pins.LEFT_ENCODER)
		self.right_motor = SmartMotor(pins.ENB, pins.IN3, pins.IN4, pins.RIGHT_ENCODER)

	def setup(self):
		# self.gyro.setup()
		self.left_motor.setup()
		self.right_motor.setup()

	def periodic(self):
		self.arcade_drive(1, 0)

		# self.gyro.periodic()
	
	def arcade_drive(self, speed, turn):
		"""
		Drive with arcade drive.
		"""
		self.left_motor.set_output(speed + turn)
		self.right_motor.set_output(speed - turn)

	def tank_drive(self, left_speed, right_speed):
		"""
		Drive with tank drive.
		"""
		self.left_motor.set_output(left_speed)
		self.right_motor.set_output(right_speed)
