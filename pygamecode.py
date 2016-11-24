print ('Amanda McLeod')
print('42936051')

import random
import pygame
from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN
from pygame.locals import *
from pygame.sprite import *

DELAY=100



class Hoop(Sprite):
  def __init__(self):
    randX = randint(0, 600)
    randY = randint(0, 400)
    self.rect.center = (randX,randY)
    self.size = 150
    self.colour = (0, 0, 255)
    self.thickness = 1
    
    Sprite.__init__(self)
        self.rect = self.image.get_rect()

	def display(self):
  		pygame.draw.circle(screen, self.colour, self.rect.center, self.size, self.thickness)



class Helicopter(Sprite):
	def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("helicpter.gif").convert()
        self.rect = self.image.get_rect()

    def move(self):

        

  		


def main():
	pygame.init()
	game_over = False 
	screen= pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Move the Helicopter with the Up and Down arrows and don't hit the walls.")

	background = pygame.Surface(screen.get_size())
	background.fill((250, 250, 250))

	
	fon = pygame.font.Font(None, 36)
	screen.blit(background, (0, 0))
	pygame.display.flip()

	while True:
    	e = event.poll()
    	if e.type == QUIT:
        	quit()
        	break



if __name__ == '__main__': main()
