import pygame
from pygame.sprite import Sprite
from pygame import *

class Jugador(Sprite):
    
    def __init__(self):
        Sprite.__init__(self)
        self.sentido = 3
        self.velocidad = 5
        self.cont = 0
    
    def set_sprites(self, sprites):
        self.imagenes = sprites
        self.image = self.imagenes[self.sentido][0]
        self.rect = self.image.get_rect()

    def update(self):
        self.image = self.imagenes[self.sentido][0]
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.sentido = 2
        elif teclas[K_RIGHT]:
            self.sentido = 3
        if teclas[K_LEFT] or teclas[K_RIGHT] or teclas[K_UP] or teclas[K_DOWN]:
            self.image = self.imagenes[self.sentido][self.cont]
            self.cont += 1
            self.cont %= 3

    def mover_derecha(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_RIGHT]:
            self.rect.x += self.velocidad

    def mover_izquierda(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.rect.x -= self.velocidad  
                    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,250))