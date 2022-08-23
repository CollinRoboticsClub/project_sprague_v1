class Pose2d:
	"""
		Represents a two-dimensional position.
		
		Units: meters and radians.
		
		Conventions:
			forward: +x
			right: +y
			clockwise: +theta
	"""
	x = 0.0
	y = 0.0
	theta = 0.0

	def __init__(self, x=0.0, y=0.0, theta=0.0):
		self.x = x
		self.y = y
		self.theta = theta
	
	def reset(self):
		self.x = 0.0
		self.y = 0.0
		self.theta = 0.0