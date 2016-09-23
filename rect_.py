from __future__ import print_function, division
from pygame import Rect as pRect, Surface, error
from funcs import *
import time

def is_function(thing):
	return type(die) == type(thing)

class Rect(object):

	""" 
		The target of recoding this classe is to support float position:
		r.left = 0.2
		print(r.lefti) # 0
		r.left += 0.5 -> 0.7
		print(r.lefti) # 1
	"""

	
	def __init__(self, left=None, top=None, width=None, height=None, **kwargs):
		self._width, self._height = width or kwargs.get('width', 0), height or kwargs.get('height', 0)

		self.__update(left or kwargs.get('left', 0), top or kwargs.get('top', 0))
		self.__name__ = kwargs.get('name', 'Anonymous')
		start = time.time()
		# add a getter for everything that round it
		for item in dir(self):
			if not type(getattr(self, item)) == type(self.__init__) and \
			   not item.startswith('set') and \
			   not item.startswith('get') and \
			   not item.startswith('_'):
				exec('def getinteger(self): return int(round(self.{0})) if type(self.{0}) not in '
					'(tuple, list) else [int(round(el)) for el in self.{0}]'.format(item))
				setattr(Rect, item + 'i', property(getinteger))

	def __update(self, x=None, y=None):
		if x is not None and y is not None:
			self._left, self._top = x, y

		self._right, self._bottom = self._width + self._left, self._height + self._top

		self._centerx, self._centery = self._left + int(self._width / 2), self._top + int(self._height / 2)

	def __to_pygame_rect(self, rect, errormessage="Need a pygame.Rect or these rects"):
		if type(rect) != pRect:
			if type(rect) != Rect:
				raise error(errormessage + " (got '{}')".format(type(rect)))

			rect = pRect(rect.left, rect.top, rect.width, rect.height)
		return rect

	def delete(self):
		raise Exception('You cannot delete attribute!')

	# --- left ---

	def getleft(self):
		return self._left

	def setleft(self, left):
		self.__update(left, self._top)

	# --- right ---

	def getright(self):
		return self._right

	def setright(self, right):
		self.__update(right - self._width, self._top)

	# --- top ---

	def gettop(self):
		return self._top

	def settop(self, top):
		self.__update(self._left, top)

	# --- bottom ---

	def getbottom(self):
		return self._bottom
	
	def setbottom(self, bottom):
		self.__update(self._left, bottom - self._height)

	# --- center ---

	def getcenter(self):
		return self._centerx, self._centery
	
	def setcenter(self, center):
		centerx, centery = center
		self.__update(centerx - int(self._width / 2), centery - int(self._height / 2))

	# --- centerx ---

	def getcenterx(self):
		return self._centerx
	
	def setcenterx(self, centerx):
		self.__update(centerx - int(self._width / 2), self._top)

	# --- centery ---

	def getcentery(self):
		return self._centery
	
	def setcentery(self, centery):
		self.__update(self._left, centery - int(self._width / 2))

	# --- width ---

	def getwidth(self):
		return self._width
	
	def setwidth(self, width):
		self._width = width
		self.__update(self._left, self._top)
	
	# --- height ---
	
	def getheight(self):
		return self._height
	
	def setheight(self, height):
		self._height = height
		self.__update(self._left, self._top)

	# --- size ---
	
	def getsize(self):
		return self._width, self._height
	
	def setsize(self, size):
		self._width, self._height = size
		self.__update(self._left, self._top)
	
	# --- topleft ---
	
	def gettopleft(self):
		return self._left, self._top
	
	def settopleft(self, topleft):
		self.__update(topleft[0], topleft[1])
	
	# --- topright ---
	
	def gettopright(self):
		return self._top, self._right
	
	def settopright(self, topright):
		self.__update(topright[0], topright[1] - self._width)

	# --- bottomleft ---
	
	def getbottomleft(self):
		return self._left, self._bottom
	
	def setbottomleft(self, bottomleft):
		self.__update(bottomleft[0], bottomleft[1] - self._height)
	
	# --- bottomright ---
	
	def getbottomright(self):
		return self._right, self._bottom
	
	def setbottomright(self, bottomright):
		self.__update(bottomright[0] - self._width, bottomright[1] - self._height)
	
	# --- midtop ---
	
	def getmidtop(self):
		return self._centerx, self._top
	
	def setmidtop(self, midtop):
		self.__update(midtop[0] - int(self._width / 2), midtop[1])

	# --- midbottom ---
	
	def getmidbottom(self):
		return self._centerx, self._bottom
	
	def setmidbottom(self, midbottom):
		self.__update(midbottom[0] - int(self._width / 2), midbottom[1] - self._height)

	# --- midleft ---
	
	def getmidleft(self):
		return self._left, self._centery
	
	def setmidleft(self, midleft):
		self.__update(midleft[0], midleft[1] - int(self._height / 2))
	
	# --- midright ---
	
	def getmidright(self):
		return self._left, self._centery
	
	def setmidright(self, midright):
		self.__update(midright[0] - self._width, midright[1] - int(self._height / 2))
	

	def get_pygame_rect(self):
		return pRect(self._left, self._top, self._width, self._height)


	# --- functions ---

	def collidepoint(self, point):
		return self.get_pygame_rect().collidepoint(point)

	def colliderect(self, rect):
		""" rect might be a navite rect, or these rect """
		return self.get_pygame_rect().colliderect(self.__to_pygame_rect(rect))

	def contains(self, rect):
		return self.get_pygame_rect().contains(self.__to_pygame_rect(rect))


	def copy(self):
		return Rect(left=self._left, top=self._top, width=self._width, height=self._height)

	def move(self, x, y):
		self._left += x
		self._right = y
		self.__update()
		return self


	# --- python native stuff ---

	def __str__(self):
		return '<rect({}, {}, {}, {})>'.format(self._left, self._top, self._width, self._height)

	def __repr__(self):
		return str(self)


	left   = property(getleft, setleft, delete)
	right  = property(getright, setright, delete)
	top    = property(gettop, settop, delete)
	bottom = property(getbottom, setbottom, delete)

	center  = property(getcenter, setcenter, delete)
	centerx = property(getcenterx, setcenterx, delete)
	centery = property(getcentery, setcentery, delete)

	width  = property(getwidth, setwidth, delete)
	height = property(getheight, setheight, delete)
	size   = property(getsize, setsize, delete)

	topleft     = property(gettopleft, settopleft, delete)
	topright    = property(gettopright, settopright, delete)
	bottomleft  = property(getbottomleft, setbottomleft, delete)
	bottomright = property(getbottomright, setbottomright, delete)

	midtop    = property(getmidtop, setmidtop, delete)
	midbottom = property(getmidbottom, setmidbottom, delete)
	midleft   = property(getmidleft, setmidleft, delete)
	midright  = property(getmidright, setmidright, delete)

	# alias

	x   = property(getleft, setleft, delete)
	y   = property(gettop, settop, delete)

def bidouille(r):
	r.midbottom = 50, 50.5
	print(r.lefti)

r = Rect(left=0, top=0, width=10, height=10)
r.left = 0.5
die(r.lefti)
# bidouille(r)
print(r)

r = pRect(0, 0, 10, 10)
# bidouille(r)
print(r)