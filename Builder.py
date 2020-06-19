from Factories import*


# Nuestro constructor
class Builder():
    def get_sprites(self): pass
    def set_sprites(self): pass


# Nuestro constructor concreto

class jugUnoBuilder():
    def __init__(self):
        self.factory = jugadorUnoFactory()

    def get_sprites(self):
        return [self.factory.moveFront(),
                self.factory.moveBack(),
                self.factory.moveLeft(),
                self.factory.moveRight()] 


class GokuBuilder():
    def __init__(self):
        self.factory = GokuSpritesFactory()

    def get_sprites(self):
        return [self.factory.moveLeft(),
                self.factory.moveRight(),
                self.factory.power()]
