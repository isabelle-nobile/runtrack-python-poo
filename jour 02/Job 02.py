class Personne:
    def __init__(self) -> None:
        self.age = 14

    def afficherAge(self):
        return self.age
    
    def bonjour(self):
        return "Hello"
    
    def modifierAge(self, n_age):
        self.age = n_age
    

class Eleve(Personne):
    def allerEnCours(self):
        return "Je vais en cours"
    
    def affichageAge(self):
        return "J'ai {} ans.".format(self.age)
    
class Professeur(Personne):
    def __init__(self, matiereEnseignée) -> None:
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        return "Le cours va commencer"
    
#Instancie 
personne = Personne()
eleve = Eleve()
professeur = Professeur("Histoire")

#Eleve de 15 ans
print(personne.bonjour())
print(eleve.allerEnCours())
eleve.modifierAge(15)
print(eleve.affichageAge())

#Professeur de 40 ans
professeur.modifierAge(40)
print(professeur.bonjour())
print(professeur.enseigner())