import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        couleurs = ["Pique", "Coeur", "Trèfle", "Carreau"]
        valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
    
    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

class Main:
    def __init__(self):
        self.cartes = []

    def ajouter_carte(self, carte):
        self.cartes.append(carte)

    def calculer_total(self):
        total = 0
        as_compte = 0
        for carte in self.cartes:
            if carte.valeur == "As":
                as_compte += 1
            elif carte.valeur in ["Valet", "Dame", "Roi"]:
                total += 10
            else:
                total += int(carte.valeur)

        total += as_compte
        while total + 10 <= 21 and as_compte > 0:
            total += 10
            as_compte -= 1

        return total

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def afficher_main(self, cachee=False):
        print(f"Main de {self.nom}:")
        if cachee:
            print("Carte cachée")
            for carte in self.main[1:]:
                print(carte)
        else:
            for carte in self.main:
                print(carte)
        print(f"Total: {self.calculer_total()}")

    def calculer_total(self):
        return Jeu().calculer_total(self.main)

    def prendre_carte(self, jeu):
        self.distribuer_cartes(jeu, 1)

    def distribuer_cartes(self, jeu, nb_cartes):
        jeu.distribuer_cartes(self, nb_cartes)

    
