import math
import numpy as np

class TrapezoidProfile:
	""" 
	From Controls Engineering in FIRST Robotics Competition, by Tyler Veness
	Creates a trapezoid profile with the given constraints.
	Returns:
	self.t_rec -- list of timestamps
	self.x_rec -- list of positions at each timestep
	self.v_rec -- list of velocities at each timestep
	self.a_rec -- list of accelerations at each timestep
	Keyword arguments :
	max_v -- maximum velocity of profile
	time_to_max_v -- time from rest to maximum velocity
	dt -- timestep
	goal -- final position when the profile is at rest
	"""
	def __init__(self, max_v, time_to_max_v, goal, dt=0.01):
		self.max_vel = max_v
		self.time_to_max_v = time_to_max_v
		self.goal = goal
		self.dt = dt
		self.i = 0

		self.t_rec = [0.0]
		self.x_rec = [0.0]
		self.v_rec = [0.0]
		self.a_rec = [0.0]
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
		
		# Generate profile
		while self.t_rec [-1] < time_total :
			t = self.t_rec [-1] + dt
			self.t_rec.append(t)
		
			if t < time_to_max_v :
				# Accelerate up
				self.a_rec.append(a)
				self.v_rec.append(a * t)
			elif t < time_from_max_v :
				# Maintain max velocity
				self.a_rec.append (0.0)
				self.v_rec.append( profile_max_v )
			elif t < time_total :
				# Accelerate down
				decel_time = t - time_from_max_v
				self.a_rec.append(-a)
				self.v_rec.append( profile_max_v - a * decel_time )
			else:
				self.a_rec.append (0.0)
				self.v_rec.append (0.0)
				self.x_rec.append(self.x_rec [-1] + self.v_rec [-1] * dt)

		# return self.t_rec , self.x_rec , self.v_rec , self.a_rec

	def get_next_state(self):
		"""
		Returns the next state of the profile.
		"""
		if self.i < len(self.t_rec):
			vals = self.t_rec[self.i], self.v_rec[self.i], self.a_rec[self.i]
			self.i += 1
			return vals
		else:
			return None, None, None

	

if __name__ == "__main__":
	import matplotlib.pyplot as plt
	from matplotlib.animation import FuncAnimation

	print("Trapezoid Profile")
	max_v = float(input("Enter maximum velocity: "))
	time_to_max_v = float(input("Enter time to maximum velocity: "))
	goal = float(input("Enter goal: "))

	profile = TrapezoidProfile(max_v, time_to_max_v, goal)

	t_list = []
	v_list = []
	
	fig, ax = plt.subplots()
	xdata, ydata = [], []
	ln, = plt.plot([], [])

	def update(frame):
		t, v, a = profile.get_next_state()
		if t != None:
			t_list.append(t)
			v_list.append(v)
			ax.plot(t_list, v_list)
			ax.set_xlim(0, t_list[-1])
			ax.set_ylim(0, max(v_list))
			fig.canvas.draw()
			fig.canvas.flush_events()
			return ax,
		else:
			return None

	ani = FuncAnimation(fig, update, interval=0.1)
	plt.show()