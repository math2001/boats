from __future__ import print_function, division
from pygame import *
from colors import *
from funcs import *
from screen import Screen, S

init()

class Harbor(object):

	def __init__(self, **kwargs):
		self.color = kwargs.get('color', black)
		self.surf = self.__generate_surf(self.color)
		left, top = kwargs.get('pos', (0, 0))
		self.rect= self.surf.get_rect(left=left, top=top)

	def __generate_surf(self, color):
		surf = Surface((50, 50))
		surf.fill(-1)
		p = font.Font('fonts/luckiest-guy.ttf', 30).render('P', True, color)
		rect = p.get_rect(center=(25, 25))
		surf.blit(p, rect)
		return surf

	def render(self):
		Screen.screen.blit(self.surf, self.rect)