import RPi.GPIO as GPIO
from util.alg.pid_controller import PIDController

# TODO: idle mode https://www.dprg.org/l298n-motor-driver-board-drive-modes/
class SmartMotor:
	def __init__(self, enable_pin, in1_pin, in2_pin):
		self.enable_pin = enable_pin
		self.in1_pin = in1_pin
		self.in2_pin = in2_pin

		self.cur_direction = 0
		self.encoder_ticks = 0

	def setup(self):
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(self.enable_pin, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.in1_pin, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.in2_pin, GPIO.OUT, initial=GPIO.LOW)

		self.pwm = GPIO.PWM(self.enable_pin, 1000)
		self.pwm.start(0)

		GPIO.setup(self.encoder_pin, GPIO.IN)
		GPIO.add_event_detect(self.encoder_pin, GPIO.BOTH, callback=self.encoder_tick_callback)

	def set_output(self, velocity):
		"""
		Velocity from -1 to 1 pls.
		"""

		self.cur_direction = 1 if velocity > 0 else -1

		if velocity > 0:
			GPIO.output(self.in1_pin, GPIO.HIGH)
			GPIO.output(self.in2_pin, GPIO.LOW)
		else:
			GPIO.output(self.in1_pin, GPIO.LOW)
			GPIO.output(self.in2_pin, GPIO.HIGH)

		self.pwm.ChangeDutyCycle(abs(velocity) * 100)

	def set_velocity(self, velocity):
		"""
		Velocity in RPM.
		"""
		pass

	def encoder_tick_callback(self, channel):
		self.encoder_ticks += 1 * self.cur_direction