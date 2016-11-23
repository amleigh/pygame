print ('Amanda McLeod')
print('42936051')

import pygame
from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN
from pygame.locals import *

#pygame.init()
X_MAX=800
Y_MAX=600

def main():
	screen= pygame.display.set_mode((X_MAX, Y_MAX))
	background = pygame.image.load("maze.png").convert()
	screen.blit(background, [0, 0])


main()
