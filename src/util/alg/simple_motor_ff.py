class SimpleMotorFeedforward:
	def __init__(self, ks, kv, ka):
		self.ks = ks
		self.kv = kv
		self.ka = ka

	def calculate(self, voltage) -> float:
		return self.ks + self.kv * voltage + self.ka * voltage * voltage