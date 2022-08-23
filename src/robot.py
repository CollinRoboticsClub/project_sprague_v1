import ischedule, signal

import RPi.GPIO as GPIO

from subsystems.drivetrain import Drivetrain

from constants import schedule_consts

class Robot:
	def __init__(self):
		self.drivetrain = Drivetrain()

	def run(self):
		self.setup()

		signal.signal(signal.SIGINT, self.stop)

		ischedule.schedule(self.periodic, schedule_consts.DT_SECONDS)

		try:
			ischedule.run_loop()
		finally:
			self.stop()

	def setup(self):
		self.drivetrain.setup()
	
	def periodic(self):
		self.drivetrain.periodic()

	def stop(self):
		GPIO.cleanup()