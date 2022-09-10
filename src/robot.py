import ischedule, signal, time

import RPi.GPIO as GPIO

from subsystems.drivetrain import Drivetrain

from constants import schedule_consts

class Robot:
	def __init__(self):
		self.drivetrain = Drivetrain()
		self.start_time = 0

	def run(self):
		self.setup()

		signal.signal(signal.SIGINT, self.stop)

		ischedule.schedule(self.periodic, interval=schedule_consts.DT_SECONDS)

		try:
			ischedule.run_loop()
		finally:
			self.stop()

	def setup(self):
		self.drivetrain.setup()
		self.start_time = time.time()
	
	def periodic(self):
		elapsed_time = time.time() - self.start_time
		if elapsed_time < 2:
			self.drivetrain.arcade_drive(0.5, 0)
		elif elapsed_time < 4:
			#Turn right
			self.drivetrain.arcade_drive(0, 0.5)
		elif elapsed_time < 6:
			self.drivetrain.arcade_drive(0.5, 0)
		elif elapsed_time < 8:
			#Turn left
			self.drivetrain.arcade_drive(0, -0.5)
		else:
			# reset the timer to repeat the sequence
			self.start_time = time.time()

		self.drivetrain.periodic()

	def stop(self):
		GPIO.cleanup()