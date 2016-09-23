from time import time as get_time

class Timer:
	""" Create a simple timer. """
	def __init__(self):
		self.time = get_time()

	def get(self):
		return get_time() - self.time

	def reset(self):
		self.time = get_time()
		return self.time