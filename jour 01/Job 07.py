class Livre:
    def __init__(self, auteur, nombre_pages, titre):
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__titre = titre

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


livre = Livre('Mr Inconnu', 20,'La programmation pour les nuls')

print("auteur :", livre.get_auteur())
print("nombre de pages :", livre.get_nombre_pages())
print("titre :", livre.get_titre())


livre.set_auteur('Miss Inconnu')
livre.set_nombre_pages(42)
livre.set_titre('La programmtion pour les nuls 2')


print("Nouveau auteur :", livre.get_auteur())
print("Nouveau Nombre de pages:", livre.get_nombre_pages())
print("Nouveau titre:", livre.get_titre())

