import math

class TrapezoidProfile:
	def __init__(self, max_vel, time_to_max_v, goal, dt):
		self.max_vel = max_vel
		self.time_to_max_v = time_to_max_v
		self.goal = goal
		self.dt = dt
		self.t_rec, self.x_rec, self.v_rec, self.a_rec = self.generate_trapezoid_profile(max_vel, time_to_max_v, dt, goal)
		self.i = 0

	def get(self):
		return self.t_rec[self.i], self.x_rec[self.i], self.v_rec[self.i], self.a_rec[self.i]

	def next(self):
		self.i += 1
		return self.get()

	def reset(self):
		self.i = 0

	def is_done(self):
		return self.i >= len(self.t_rec)
	

	def generate_trapezoid_profile(max_v , time_to_max_v , dt , goal):
		""" 
		From Controls Engineering in FIRST Robotics Competition, by Tyler Veness
		Creates a trapezoid profile with the given constraints.
		Returns:
		t_rec -- list of timestamps
		x_rec -- list of positions at each timestep
		v_rec -- list of velocities at each timestep
		a_rec -- list of accelerations at each timestep
		Keyword arguments :
		max_v -- maximum velocity of profile
		time_to_max_v -- time from rest to maximum velocity
		dt -- timestep
		goal -- final position when the profile is at rest
		"""
		t_rec = [0.0]
		x_rec = [0.0]
		v_rec = [0.0]
		a_rec = [0.0]
		a = max_v / time_to_max_v
		time_at_max_v = goal / max_v - time_to_max_v
		# If profile is short
		if max_v * time_to_max_v > goal:
			time_to_max_v = math.sqrt(goal / a)
			time_from_max_v = time_to_max_v
			time_total = 2.0 * time_to_max_v
			profile_max_v = a * time_to_max_v
		else:
			time_from_max_v = time_to_max_v + time_at_max_v
			time_total = time_from_max_v + time_to_max_v
			profile_max_v = max_v
		while t_rec [-1] < time_total :
			t = t_rec [-1] + dt
			t_rec.append(t)
		if t < time_to_max_v :
			# Accelerate up
			a_rec.append(a)
			v_rec.append(a * t)
		elif t < time_from_max_v :
			# Maintain max velocity
			a_rec.append (0.0)
			v_rec.append( profile_max_v )
		elif t < time_total :
			# Accelerate down
			decel_time = t - time_from_max_v
			a_rec.append(-a)
			v_rec.append( profile_max_v - a * decel_time )
		else:
			a_rec.append (0.0)
			v_rec.append (0.0)
			x_rec.append(x_rec [-1] + v_rec [-1] * dt)
		return t_rec , x_rec , v_rec , a_rec