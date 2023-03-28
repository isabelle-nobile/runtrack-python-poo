class Vehicule:
    def __init__(self, marque, modele, annee, prix) -> None:
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        return f'Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}'

    def démarrer(self):
        return "Attention, je roule."


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix) -> None:
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        return f'Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}\nNombres de portes : {self.portes}'

    def démarrer(self):
        return "Attention, je roule vroum vroum avec ma voiture."


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix) -> None:
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        return f'Marque : {self.marque}\nModèle : {self.modele}\nAnnée : {self.annee}\nPrix : {self.prix}\nNombres de roues : {self.roue}'

    def démarrer(self):
        return "Attention, je roule vroum vroum avec ma moto."


vehicule = Vehicule("Mercedes", "Classe A", 2020, 18500)
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)

# info vehicule
print("Vehicule: ")

print(vehicule.informationsVehicule())

# info voiture
print("\nVoiture: ")
print(voiture.informationsVehicule())
