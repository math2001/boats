from __future__ import print_function, division
from pygame import *
from colors import *
from funcs import *
from screen import Screen, S

from rect_ import Rect as cRect

from trace import Trace
from harbor import Harbor
from boat import Boat


init()


screen = display.set_mode((500, 500))
Screen.init()

harbor = Harbor(color=orange)

boats = [Boat(orange)]

main = True

surf = Surface((50, 50))
surf.fill(red)

while main:
	screen.fill(-1)
	for e in event.get():
		if e.type == QUIT:
			main = False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				main = False

		if e.type == MOUSEBUTTONDOWN:
			for boat in boats:
				if boat.rect.collidepoint(e.pos):
					boat.focus()
					break
		if e.type == MOUSEBUTTONUP:
			for boat in boats:
				boat.unfocus()


	harbor.render()
	# Screen.screen.blit(surf, (0.7, 0.7))
	Screen.screen.blit(surf, cRect(0, 0, 50, 50))
	for boat in boats:
		boat.update()
		boat.render()
	display.flip()


quit()