from __future__ import print_function, division
from pygame import *
from colors import *
from funcs import *
from screen import Screen, S

from pos import Pos

init()

class Trace(object):

	"""
		Remember points, and join them with straight lines
	"""

	def __init__(self, **kwargs):
		self.pos = []
		self.color = kwargs.get('color', black)

		self.index = -1

	def add(self, x, y=None):
		if y == None and len(x) == 2:
			x, y = x
		try:
			self.pos[-1]
		except IndexError:
			pass
		else:
			size = 1
			self.fillup(self.pos[-1], (x, y), size)
		self.pos.append((x, y))
		self.clean()
		return self

	def fillup(self, first, second, fillup_width, fillup_height=None):
		if fillup_height is None: fillup_height = fillup_width
		first = Pos(first)
		second = Pos(second)

		width = abs(first.x - second.x)
		height = abs(first.y - second.y)

		if width >= height:
			if width == 0:
				return self
			steps = int(width / fillup_width)
			if steps == 0: return self
			xref = first.x
			y = first.y
			if first.y < second.y:
				y_to_add = height / steps
			else:
				y_to_add = -(height / steps)
				
			for i in range(steps + 1):
				x = i * fillup_width * (-1 if first.x > second.x else 1) + xref
				self.pos.append((x, int(round(y))))
				y += y_to_add
		else:
			if height == 0:
				return self
			steps = int(height / fillup_height)
			if steps == 0: return self
			yref = first.y
			x = first.x
			if first.x < second.x:
				x_to_add = width / steps
			else:
				x_to_add = -(width / steps)
			for i in range(steps + 1):
				y = i * fillup_height * (-1 if first.y > second.y else 1) + yref
				self.pos.append((int(round(x)), y))
				x += x_to_add

		return self

	def clean(self):
		new = [(0, 0)]
		for pos in self.pos:
			if pos != new[-1]:
				new.append(pos)
		new.pop(0)
		self.pos = new

	def render(self):
		for x, y in self.pos:
			draw.circle(Screen.screen, self.color, (x, y), 2)
		return self

	def clear(self):
		try:
			self.pos[-1]
		except IndexError:
			self.pos = [(0, 0)]
		else:
			self.pos = [self.pos[-1]]
		print('-----')
		return self

	def get(self):
		try:
			return self.pos.pop(0)
		except IndexError:
			return False

