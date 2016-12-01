

from pygame import *
from pygame.sprite import *
from random import *
from pygame.locals import Rect, DOUBLEBUF, QUIT, K_ESCAPE, KEYDOWN, K_DOWN, \
    K_LEFT, K_UP, K_RIGHT, KEYUP, K_LCTRL, K_RETURN, FULLSCREEN
import sys
import pygame

DELAY = 3000;           

background = (0,0,0)   

X_MAX=900
Y_MAX=900

LEFT, RIGHT, UP, DOWN = 0, 1, 3, 4
START, STOP = 0, 1

everything = pygame.sprite.Group() 

class Hoop(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("Hoop.bmp").convert_alpha()
        self.rect = self.image.get_rect(center=(450,450))

    
    def move(self):
        randX = randint(0, 800)
        randY = randint(0, 600)
        self.rect.center = (randX,randY)
        move_final= self.rect.center

class Fire(Sprite):
    def __init__(self, group):
        Sprite.__init__(self)
        self.image = image.load("fire.bmp").convert_alpha()
        self.rect = self.image.get_rect()
        self.add(group)
  
    def appear(self):
        randX = randint(0, 800)
        randY = randint(0, 600)
        self.rect.center = (randX,randY)
        move_final= self.rect.center
        appear_final= self.rect.copy()



class Helicopter(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load("helicopter.bmp"))
        self.images.append(pygame.image.load("helicopter2.bmp"))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

        self.rect.center = (X_MAX/2, Y_MAX - 40)
        self.dx=self.dy=0
        self.in_position=False
        self.autopilot= False

    def update(self):
        self.image = self.images[self.index]
        self.index += 1
        if self.index >= len(self.images):
            self.index=0
        self.image = self.images[self.index]

        x,y= self.rect.center

        if not self.autopilot:
            self.rect.center = x + self.dx, y + self.dy

        else:
            if not self.in_position:
                if x != X_MAX/2:
                    x += (abs(X_MAX/2 - x)/(X_MAX/2 - x)) * 2
                if y != Y_MAX - 100:
                    y += (abs(Y_MAX - 100 - y)/(Y_MAX - 100 - y)) * 2

                if x == X_MAX/2 and y == Y_MAX - 100:
                    self.in_position = True
            else:
                y -= self.velocity
                self.velocity *= 1.5
                if y <= 0:
                    y = -30
            self.rect.center = x, y

    def move(self, direction, operation):
        v = 15
        if operation == START:
            if direction in (UP, DOWN):
                self.dy = {UP: -v,
                           DOWN: v}[direction]

            if direction in (LEFT, RIGHT):
                self.dx = {LEFT: -v,
                           RIGHT: v}[direction]

        if operation == STOP:
            if direction in (UP, DOWN):
                self.dy = 0
            if direction in (LEFT, RIGHT):
                self.dx = 0

    def hit(self, target):
        return self.rect.colliderect(target)
    
    def dead(self, death):
        if self.rect.colliderect(death):
            self.kill()
            



def main():
    game_over=False
    init()

    screen = display.set_mode((X_MAX, Y_MAX))
    display.set_caption("Hit the hoops and don't touch the fire")




    f = font.Font(None, 36)

    heli = Helicopter()
    target = Hoop()
    obstical=pygame.sprite.Group()
    heli.add(everything)
    sprites = RenderPlain(heli, target, obstical)

    score = 0
    time.set_timer(USEREVENT + 1, DELAY)
    clock=pygame.time.Clock()

    Fire([sprites, obstical])


    while True:
        if not game_over: 
            mixer.Sound("heli_sound.wav").play()
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit()   
            if not game_over:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_DOWN:
                        heli.move(DOWN, START)
                    if event.key == K_LEFT:
                        heli.move(LEFT, START)
                    if event.key == K_RIGHT:
                        heli.move(RIGHT, START)
                    if event.key == K_UP:
                        heli.move(UP, START)                         
                          
                if event.type == KEYUP:
                    if event.key == K_DOWN:
                        heli.move(DOWN, STOP)
                    if event.key == K_LEFT:
                        heli.move(LEFT, STOP)
                    if event.key == K_RIGHT:
                        heli.move(RIGHT, STOP)
                        if event.key == K_UP:
                            heli.move(UP, STOP)
                elif event.type == USEREVENT +1:
                    target.move()

                
                hit_fire = pygame.sprite.spritecollide(heli, obstical, True)
                if hit_fire:
                    game_over = True
                    break

                if heli.hit(target):
                    Fire([sprites, obstical])
                    target.move()
                    score +=1

                    for i in obstical:
                        i.appear()

                    time.set_timer(USEREVENT + 1, DELAY)

       
        if game_over == True:
        
            
            # print (text)
            print ("hi")
            mixer.Sound("heli_sound.wav").stop() 
            mixer.Sound("fail.wav").play() 
             
            print ('hello')
            
           
            screen.fill(background)
            final_text= f.render("GAME OVER!! Score {}".format(str(score)), False, (250, 250, 0))
            text= screen.blit(final_text, (400, 400))           
            
            sprites.update()
            sprites.draw(screen)
            display.update()
            

        screen.fill(background)
        t = f.render("Score = " + str(score), False, (250,250,0))
        screen.blit(t, (400, 0))       

        sprites.update()
        sprites.draw(screen)
        display.update()


main()

