print ('Amanda McLeod')
print('42936051')

import random
import pygame
from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN
from pygame.locals import *
from pygame.sprite import *

DELAY=100



class Hoop(pygame.sprite.Sprite):
  def __init__(self):
    self.size = 150
    self.colour = (0, 0, 255)
    self.thickness = 1
    
    Sprite.__init__(self)
        self.rect = self.image.get_rect()

	def move(self):
		randX = randint(0, 600)
    	randY = randint(0, 400)
    	self.rect.center = (randX,randY)
    	move_final= self.rect.center


	def display(self):
  		pygame.draw.circle(self, self.colour, self.move, self.size, self.thickness)


class Monster(pygame.sprite.Sprite): 
	def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("helicpter.gif").convert()
        self.rect = self.image.get_rect()

    

class Helicopter(pygame.sprite.Sprite):
	def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("helicpter.gif").convert()
        self.rect = self.image.get_rect()
        self.score=0
        self.dx=self.dy

    def move(self, movement):
    	v=10
		if movement in (UP, DOWN):
			self.dy = {UP: -v,
                       DOWN: v}[direction]

        if movement in (LEFT, RIGHT):
            self.dx = {LEFT: -v,
                       RIGHT: v}[direction]
    def collision (self, hoop):
    	self.score +=1
    	return self.rect.colliderect(target)



   

  		


def main():
	pygame.init()
	target=Hoop()
	heli= Helicopter()    

	timer=pygame.time.Clock()

	game_over = False 
	screen= pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Move the Helicopter through as many hoops as possible before time runs out.")

	background = pygame.Surface(screen.get_size())
	background.fill((250, 250, 250))

	
	fon = pygame.font.Font(None, 36)
	screen.blit(background, (0, 0))
	pygame.display.flip()

	while True:
		clock.tick=30
		mixer.Sound(#song).play()
    	e = event.poll()
    	if e.type == QUIT:
        	quit()
        	break



if __name__ == '__main__': main()
