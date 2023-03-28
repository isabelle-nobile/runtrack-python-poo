class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.hauteur

    def get_hauteur(self):
        return self.hauteur

    def set_hauteur(self, hauteur):
        self.hauteur = hauteur

#Rectangle de 5 et 3
rectangle = Rectangle(5, 3)
perimetre = rectangle.perimetre()
surface = rectangle.surface()

print("Rectangle:")
print("Périmètre: ", perimetre)
print("Surface: ", surface)

#Rectangle de 10 et 6
rectangle.set_longueur(10)
rectangle.set_largeur(6)
print("\nNouveau Rectangle")
print("Longueur: ", rectangle.get_longueur())
print("Largeur: ", rectangle.get_largeur())

#Parallelepipede  de 6, 5 et 3
para = Parallelepipede(6, 5, 3)
perimetre = para.perimetre()
surface = para.surface()
volume = para.volume()

print("\nParallelepipede:")
print("Périmètre: ", perimetre)
print("La surface du parallélépipède est : ", surface)
print("Le volume du parallélépipède est : ", volume)

#Parallelepipede  de 7, 5 et 3
para.set_longueur(7)
para.set_largeur(4)
para.set_hauteur(3)

print("\nNouveau Parallelepipede:")
print("Longueur: ", para.get_longueur())
print("Largeur: ", para.get_largeur())
print("Hauteur: ", para.get_hauteur())

