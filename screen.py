import pygame
from pygame.locals import *

pygame.init()

class S:
	""" A class way quicker to type. See Screee::init """

class Screen:

	@staticmethod
	def init():
		""" 
			A static method to use the SAME rect all the time. 
			Like this, it is way easier to change it when the user resize the screen
		"""
		S.s = Screen.screen = pygame.display.get_surface()
		S.r = Screen.rect  = Screen.screen.get_rect()
