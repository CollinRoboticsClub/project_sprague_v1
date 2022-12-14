from constants import schedule_consts
from mpu6050 import mpu6050
import math

class Gyro:
	def __init__(self):
		self.mpu = mpu6050(0x68, bus=1)
		self.heading = 0

	def setup(self):
		pass

	def periodic(self):
		self.heading += math.degrees(self.mpu.get_gyro_data()['z']) * schedule_consts.DT_SECONDS
		
	def get_heading(self):
		return self.heading