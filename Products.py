import loadImages
# Esta es nustra clase productos donde cada prducto concreto nos retorna una lista de sprites del personaje

# Producto Abstracto left


class left():
    def get_sprites(self): pass



class leftGoku(left):
    def get_sprites(self):
        return[loadImages.load("gokuSprites/GI1.png"),
               loadImages.load("gokuSprites/GI2.png"),
               loadImages.load("gokuSprites/GI3.png"),
               loadImages.load("gokuSprites/GI4.png"),
               loadImages.load("gokuSprites/GI5.png"),
               loadImages.load("gokuSprites/GI6.png"),
               loadImages.load("gokuSprites/GN.png")]

class leftJugUno(left):
    def get_sprites(self):
        return [loadImages.load('imagenes/I0.png'),
                loadImages.load('imagenes/I1.png'),
                loadImages.load('imagenes/I2.png'),
                loadImages.load('imagenes/I3.png')]

# Producto Abstracto right


class right():
    def get_sprites(self): pass



class rightGoku(right):
    def get_sprites(self):
        return[loadImages.load("gokuSprites/GD1.png"),
               loadImages.load("gokuSprites/GD2.png"),
               loadImages.load("gokuSprites/GD3.png"),
               loadImages.load("gokuSprites/GD4.png"),
               loadImages.load("gokuSprites/GD5.png"),
               loadImages.load("gokuSprites/GD6.png"),
               loadImages.load("gokuSprites/GN.png")]

class rightJugUno(right):
    def get_sprites(self):
        return [loadImages.load('imagenes/D0.png'),
                loadImages.load('imagenes/D1.png'),
                loadImages.load('imagenes/D2.png'),
                loadImages.load('imagenes/D3.png')]

# Producto Abstracto power


class power():
    def get_sprites(self): pass



class powerGoku(power):
    def get_sprites(self):
        return[loadImages.load("gokuSprites/GP1.png"),
               loadImages.load("gokuSprites/GP2.png"),
               loadImages.load("gokuSprites/GP3.png"),
               loadImages.load("gokuSprites/GP4.png"),
               loadImages.load("gokuSprites/GP5.png"),
               loadImages.load("gokuSprites/GP6.png"),
               loadImages.load("gokuSprites/GP7.png"),
               loadImages.load("gokuSprites/GP8.png")]

class front():
    def get_sprites(self): pass

class frontJugUno(front):
    def get_sprites(self):
        return[]

class back():
    def get_sprites(self): pass

class backJugUno(back):
    def get_sprites(self):
        return[]
