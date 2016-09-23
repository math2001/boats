from __future__ import print_function, division
from pygame import *
from colors import *
from funcs import *
from screen import Screen, S

from trace import Trace

init()

class Boat(object):

	def __init__(self, color):

		"""
			is focus is True when the user is setting the position.
		"""

		self.color = color
		self.surf = self.__generate_surf()
		self.rect = self.surf.get_rect(center=Screen.rect.center)

		self.trace = None

		self.speed = [0, 0]

		self.test_speed = [0, 0]

		self.laps = 0

		self.is_focus = False

	def update(self):
		self.laps += 1
		if self.is_focus:
			self.trace.add(mouse.get_pos())


		if self.laps % 5 == 0:

			if self.trace is not None and self.is_focus is False:
				pos = self.trace.get()
				if pos is False:
					self.trace = None
				else:
					self.speed = pos[0] - self.rect.centerx, pos[1] - self.rect.centery
					self.rect.center = pos
			else:
				self.rect.move_ip(self.speed)

	def __generate_surf(self):
		surf = Surface((50, 20))
		surf.fill(grey)
		color = Surface((25, 7))
		color.fill(self.color)
		surf.blit(color, color.get_rect(center=surf.get_rect().center))
		return surf

	def render(self):
		if self.trace is not None:
			self.trace.render()
		Screen.screen.blit(self.surf, self.rect)

	def focus(self):
		self.trace = Trace()
		self.is_focus = True
		return self

	def unfocus(self):
		self.is_focus = False
		return self
