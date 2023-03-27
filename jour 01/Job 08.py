class Livre:
    def __init__(self, auteur, nombre_pages, titre):
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__titre = titre
        self.__disponible = True

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_auteur(self):
        return self.__auteur

    def set_nombre_pages(self, nombre):
        if nombre >= 0:
            self.__nombre_pages = int(nombre)
            return self.__nombre_pages
        else:
            print("Ce n'est pas un nombre entier positif")


    def get_nombre_pages(self):
        return self.__nombre_pages
    
    def set_titre(self, titre):
        self.__titre = titre

    def get_titre(self):
        return self.__titre
    
    def set_disponible(self, disponible):
        self.__disponible = disponible

    def get_disponible(self):
        return self.__disponible
    
    def verification(self):
        if self.__disponible == True:
            return True
        else: 
            return False
    
    def emprunter(self):
        if self.verification() == True:
            return True
        else:
            return False
    
    def rendre(self):
        if self.emprunter() == True:
            return False
        else:
            return True

    

            


livre = Livre('Mr Inconnu', 20,'La programmation pour les nuls')

print("auteur :", livre.get_auteur())
print("nombre de pages :", livre.get_nombre_pages())
print("titre :", livre.get_titre())
print("Disponible:" , livre.verification())
print("Empruntable:", livre.emprunter())
print("Rendre:", livre.rendre())

livre.set_disponible(False)
print("Disponible:", livre.get_disponible())

