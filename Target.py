from abc import ABC, abstractmethod
import pygame
from pygame.sprite import Sprite
from pygame import *


class Target(ABC, Sprite):
    @abstractmethod
    def defPositions(self): pass

    @abstractmethod
    def moveRight(self): pass

    @abstractmethod
    def moveLeft(self): pass

    @abstractmethod
    def changeSprite(self): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def drawCharacter(self): pass

    @abstractmethod
    def set_sprites(self): pass
