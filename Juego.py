import pygame
import sys
from pygame.locals import *
from random import randint
from Products import *
import time
import Character
from Director import *
from Builder import *
from Character import *
import loadImages


class Juego():
     
    i=0
    width = 900
    height = 600
    colour = (227,166,162)
    empezar = True
    opc = 0
            

    pygame.init()                
    posX=100
    posY=250
    posTup = (posX,posY)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Prueba")
    speed=20

    while opc != 1 and opc !=2:
        print ("Para elegir tu personaje ingresa:")
        print ("1-->Personaje Adaptado \n 2---> Personaje por defecto")
        opc = int(input())

    auxDirector = Director() 
    if opc == 1:
        auxDirector.setBuilder(jugUnoBuilder())
    elif opc == 2:
        auxDirector.setBuilder(GokuBuilder())

    charac = auxDirector.getChar(opc)
    charac.defPositions(posX,posY)
    jugando =True
    background = loadImages.load("background/mexBack.jpeg")
            
    while empezar:        
        for i in pygame.event.get():
            if i.type == QUIT:
                pygame.quit()
                empezar = False
                sys.exit()
                
        screen.blit(background,(0,0))
        charac.update()
        charac.drawCharacter(screen)
        pygame.display.update()
        
         
        
        
        




