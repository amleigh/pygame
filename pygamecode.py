print ('Amanda McLeod')
print('42936051')

import random
import pygame
import sys
from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN
from pygame.locals import *
from pygame.sprite import *



#everything=pygame.sprite.Group()

class Hoop(pygame.sprite.Sprite):
	def __init__(self):
	    pygame.sprite.Sprite.__init__(self)
	    self.image= pygame.image.load("Hoop.bmp")
	    self.rect=self.image.get_rect()

	    # self.size = 150
	    # self.colour = (51, 159, 255)
	    # self.thickness = 1
	    # self.image = pygame.Surface((50, 50))
	    # self.circle= pygame.draw.circle(self.image, self.colour, (400,600), self.size, self.thickness)
	    # self.rect = self.image.get_rect()

	def move(self):
		randX = randint(0, 500)
		randY = randint(0, 500)
		self.rect.center = (randX,randY)
		move_final= self.rect.center


	#def display(self):
		#pygame.draw.circle(self, self.colour, self.move, self.size, self.thickness)


class Fire(Sprite): 
	def __init__(self):
		Sprite.__init__(self)
		self.image = pygame.image.load("fire.bmp").convert_alpha()
		self.rect = self.image.get_rect()

	def appear(self):                                      
		randX = randint(0, 600)
		randY = randint(0, 400)
		self.rect.copy = (randX,randY)
		appear_final= self.rect.copy()


class Helicopter(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#pygame.display.set_mode((1,1), pygame.DOUBLEBUF)
		self.images = []
		self.images.append(pygame.image.load("helicopter.bmp"))
		self.images.append(pygame.image.load("helicopter2.bmp"))
		#self.image=pygame.image.load("helicopter.gif").convert_alpha()

		
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(5, 5, 64, 64)
		

		self.score=0
		self.dx=self.dy=50

	def update(self):
		self.image = self.images[self.index]
		self.index += 1
		if self.index >= len(self.images):
			self.index=0
		self.image = self.images[self.index]

	def move(self, movement):
		v=10
		if movement in (UP, DOWN):
			self.dy = {UP: -v, DOWN: v}[direction]

		if movement in (LEFT, RIGHT):
			self.dx = {LEFT: -v,RIGHT: v}[direction]

	def collision (self, hoop):
		self.score +=1
		return self.rect.colliderect(hoop)


	def dead(self, death):
		if self.rect.colliderect(death):
			self.kill()

   

  		


def main():
	
	pygame.init()
	pygame.font.init()
	pygame.mixer.init()

	screen= pygame.display.set_mode((1000, 900))
	pygame.display.set_caption("Move the Helicopter through as many hoops as possible before time runs out.")

	fon = pygame.font.Font(None, 36)

	target=Hoop()
	heli= Helicopter() 
	obstical=Fire()   
	#pygame.time.delay(10)

	timer=pygame.time.Clock()

	game_over = False 
	

	background = pygame.Surface(screen.get_size())
	background.fill((0, 0, 0))

	
	DELAY=10
	
	images=RenderPlain(heli, obstical, target)

	#images.draw(screen)

	screen.blit(background, (0, 0))
	#pygame.display.flip()
	timer.set_timer(USEREVENT + 1, DELAY)
	


	#pygame.mixer.music.play("heli_sound.wav")

	while True:
		timer.tick(45)

		for occurance in pygame.event.get():
			if occurance.type == QUIT:
				sys.exit()
			if occurance.type == KEYDOWN:
				if occurance.key == K_ESCAPE:
					sys.exit()
				if occurance.key == K_DOWN:
					heli.move(DOWN)
				if occurance.key == K_LEFT:
					heli.move(LEFT)
				if occurance.key == K_RIGHT:
					heli.move(RIGHT)
				if occurance.key == K_UP:
					heli.move(UP)
			if occurance.type == KEYUP:
				if occurance.key == K_DOWN:
					heli.move(DOWN)
				if occurance.key == K_LEFT:
					heli.move(LEFT)
				if occurance.key == K_RIGHT:
					heli.move(RIGHT)
					if occurance.key == K_UP:
						heli.move(UP)

		# if pygame.sprite.spritecollide(heli, obstical, True) == True:
		# 	heli.dead(obstical)
		# 	game_over=True
		# 	end_text= fon.render("GAME OVER!! Score {}".format(heli.collision.score), 1, (250, 250, 250))
		# 	text=screen.blit(end_text, (0, 0))
		# 	print(text)
		# 	sys.exit()

		# if pygame.sprite.spritecollide(heli, target, True) == True:
		# 	target.move()
		# 	heli.collision(target)
		# 	obstical.appear()
		# 	scoretext = fon.render("Score {0}".format(heli.collision.score), 1, (250, 250, 250))
		# 	screen.blit(scoretext, (0, 0))

		# if game_over == True:
		# 	final_text= fon.render("GAME OVER!! Score {}".format(heli.collision.score), 1, (250, 250, 250))
		# 	fin=screen.blit(final_text, (0, 0))
		# 	print (fin)

	
		images.update()
		images.draw(screen)
		pygame.display.flip()
#music for background and explosion 
#display score and time
#set scoer to zero to start
#set display on screen


if __name__ == '__main__': 
	main()
#main()
