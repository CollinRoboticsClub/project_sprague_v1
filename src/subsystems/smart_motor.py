from enum import Enum
import RPi.GPIO as GPIO
from util.alg.pid_controller import PIDController
from util import ezmath

class SmartMotor:
	class IdleMode(Enum):
		BRAKE = 0
		COAST = 1

	def __init__(self, enable_pin, in1_pin, in2_pin, encoder_pin,  idle_mode: IdleMode = IdleMode.BRAKE):
		self.enable_pin = enable_pin
		self.in1_pin = in1_pin
		self.in2_pin = in2_pin
		self.encoder_pin = encoder_pin
		self.idle_mode = idle_mode

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

	def periodic(self):
		pass

	def set_output(self, velocity):
		"""
		Velocity from -1 to 1 pls.
		"""

		velocity = ezmath.clamp(velocity, -1, 1)
		self.cur_direction = 1 if velocity > 0 else -1

		pwm_output = abs(velocity) * 100

		if velocity > 0:
			GPIO.output(self.in1_pin, GPIO.HIGH)
			GPIO.output(self.in2_pin, GPIO.LOW)
		elif velocity < 0:
			GPIO.output(self.in1_pin, GPIO.LOW)
			GPIO.output(self.in2_pin, GPIO.HIGH)
		else:
			if self.idle_mode == SmartMotor.IdleMode.BRAKE:
				GPIO.output(self.in1_pin, GPIO.HIGH)
				GPIO.output(self.in2_pin, GPIO.HIGH)
				pwm_output = 100
			else:
				GPIO.output(self.in1_pin, GPIO.LOW)
				GPIO.output(self.in2_pin, GPIO.LOW)

		self.pwm.ChangeDutyCycle(pwm_output)

	def set_velocity(self, velocity):
		"""
		Velocity in RPM.
		"""
		pass

	def encoder_tick_callback(self, channel):
		self.encoder_ticks += 1 * self.cur_direction