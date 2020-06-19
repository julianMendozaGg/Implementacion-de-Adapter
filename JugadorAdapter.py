from Target import *
from jugador import *


class JugadorAdapter(Target):

    def __init__(self):
        Sprite.__init__(self)
        self.auxJugador = Jugador()
        self.velocidad = self.auxJugador.velocidad
        self.sentido = self.auxJugador.sentido
        self.cont = self.auxJugador.cont

    def set_sprites(self,sprites):
        self.auxJugador.set_sprites(sprites)

    def defPositions(self, auxposX, auxPosY):
        self.posX = auxPosY
        self.posY = auxPosY

    def moveRight(self):
        self.auxJugador.mover_derecha()
        

    def moveLeft(self):
        self.auxJugador.mover_izquierda()
        

    def changeSprite(self):
        self.auxJugador.update()

    def update(self):
        self.moveLeft()
        self.moveRight()
        self.changeSprite()
        

    def drawCharacter(self, screen):
        self.auxJugador.draw(screen)
