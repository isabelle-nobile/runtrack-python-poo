class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50


    def set_marque(self, marque):
        self.__marque = marque

    def get_marque(self):
        return self.__marque

    def set_modele(self, modele):
        self.__modele = modele

    def get_modele(self):
        return self.__modele

    def set_annee(self, annee):
        self.__annee = annee

    def get_annee(self):
        return self.__annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_kilometrage(self):
        return self.__kilometrage

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    def get_en_marche(self):
        return self.__en_marche

    def demarrer(self):
        if self.__verifier_plein() > 5 :
            vroum_vroum = self.__en_marche = True
            return vroum_vroum
        else: 
            return False
    
    def arreter(self):
        vroum_vroum_stop = self.__en_marche = False
        return vroum_vroum_stop
    
    def __verifier_plein(self):
        return self.__reservoir
    
voiture = Voiture("BMW","I7", 2022, 5000,)

print("La voiture démarre:", voiture.demarrer())
print("Les informations de la voitures :\nMarque:", voiture.get_marque(),"\nModèle:", voiture.get_modele(),"\nAnnée:", voiture.get_annee(),"\nKilomètrage:", voiture.get_kilometrage())
print("La voiture est arreté:", voiture.arreter())