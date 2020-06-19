import pygame
from pygame.sprite import Sprite
from pygame import*
import time


class Character(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.direction = 1
        self.cont = 0
        self.speed = 20
        

    def defPositions(self, auxPosX, auxPosY):
        self.posX = auxPosX
        self.posY = auxPosY
# Se establecen los sprites y la imagen [1][0] sera la primera en dibujarse, ya que 1 y 0 son los primeros
# valores por defecto

    def set_sprites(self, images):
        self.graphics = images
        self.image = self.graphics[self.direction][self.cont]
        #self.rect = self.sprite.get_rect()

    def moveRight(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_RIGHT]:
            self.posX += self.speed
            time.sleep(0.06)
            self.direction = 1

    def moveLeft(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            self.posX -= self.speed
            time.sleep(0.06)
            self.direction = 0

    

    def doPower(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_SPACE]:
            self.direction = 2
            time.sleep(0.09)

    # Esta clase es la que ayuda a cambiar los sprites de los peronajes segun el movimiento
    def changeSprite(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_RIGHT] or pressed[K_LEFT] or pressed[K_SPACE] or pressed[K_UP]:
            try:
                self.image = self.graphics[self.direction][self.cont]
                self.cont += 1
                self.cont %= len(self.graphics[self.direction])
            except IndexError:
                self.cont = 0
        else:
            self.cont = 0
            self.image = self.graphics[self.direction][0]

    # Este metodo reune todos los movimientos, los cuales le dan info. al metodo changeSprite y asi se puedan actualizar
    # los sprites segun el movimiento
    def update(self):
        self.doPower()
        self.moveRight()
        self.moveLeft()
        self.changeSprite()
        

    def drawCharacter(self, screen):
        screen.blit(self.image, (self.posX, self.posY))
