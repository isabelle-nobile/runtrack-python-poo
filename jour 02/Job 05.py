import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius ** 2

#Rectangle de 5 et 3 / Cercle de 2
rectangle = Rectangle(6, 7)
cercle = Cercle(8)

print("Aire du rectangle :", rectangle.aire())
print("Aire du cercle :", cercle.aire())
