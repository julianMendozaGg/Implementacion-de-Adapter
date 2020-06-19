# Esta es nuestra clase de fabricas, ya que usamos el patron Abstract Factory
from Products import *

# Farica abstracta que tiene como metodos mover izq y mover der


class AbstractFactory():
    def moveLeft(self): pass
    def moveRight(self): pass
    def moveDown(self): pass
    def moveUp(self): pass
    def power(self): pass


# Fabrica concreta que produce sprites de cada personaje


class GokuSpritesFactory(AbstractFactory):

    def moveLeft(self):
        left= leftGoku()
        return left.get_sprites()
    
    def moveRight(self):
        right = rightGoku()
        return right.get_sprites()
    

    def power(self):
        power = powerGoku()
        return power.get_sprites()

class jugadorUnoFactory(AbstractFactory):
   
    def moveLeft(self): 
        left = leftJugUno()
        return left.get_sprites()

    def moveRight(self): 
        right = rightJugUno()
        return right.get_sprites()

    def moveFront(self):
        front = frontJugUno()
        return front.get_sprites()
    
    def moveBack(self):
        back = backJugUno()
        return back.get_sprites()