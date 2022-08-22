import ischedule

import RPi.GPIO as GPIO

from subsystems.drivetrain import Drivetrain

from constants import schedule_consts, pins
# todo: ground l298n and pi together

class Robot:
	def __init__(self):
		self.drivetrain = Drivetrain()

	def run(self):
		self.setup()
		ischedule.schedule(self.periodic, schedule_consts.dt)
		ischedule.run_loop()

	def setup(self):
		GPIO.setmode(GPIO.BCM)

		self.drivetrain.setup()
	
	def periodic(self):
		try:
			self.drivetrain.periodic()
		except KeyboardInterrupt:
			GPIO.cleanup()