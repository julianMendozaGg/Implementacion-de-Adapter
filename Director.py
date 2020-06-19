from Factories import *
from Character import *
from JugadorAdapter import*
class Director():
    __builder = None

    def setBuilder(self, builder):
        self.__builder= builder
    
    def getChar(self,num):
        self.definedCharacter=self.defineCharacter(num)
        self.definedCharacter.set_sprites(self.__builder.get_sprites())
        return self.definedCharacter

    def defineCharacter(self,num):
        if num == 1:
            self.jugador = JugadorAdapter()
            return self.jugador
        elif num == 2:
            self.charac = Character()
            return self.charac

    
