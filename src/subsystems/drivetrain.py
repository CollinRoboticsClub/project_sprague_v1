from subsystems.gyro import Gyro
from subsystems.smart_motor import SmartMotor
from constants import pins

class Drivetrain:
	def __init__(self):
		self.gyro = Gyro()
		self.left_motor = SmartMotor(pins.ENA, pins.IN1, pins.IN2, pins.LEFT_ENCODER)
		self.right_motor = SmartMotor(pins.ENB, pins.IN4, pins.IN3, pins.RIGHT_ENCODER) # flip direction by swapping IN pins

	def setup(self):
		self.gyro.setup()
		self.left_motor.setup()
		self.right_motor.setup()

	def periodic(self):
		self.gyro.periodic()
		self.left_motor.periodic()
		self.right_motor.periodic()
	
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
