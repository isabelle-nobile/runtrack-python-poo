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
        return "J'ai {00} ans.".format(self.age)
    
class Professeur:
    def __init__(self, matiereEnseignée) -> None:
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        return "Le cours va commencer"
    
personne = Personne()
eleve = Eleve()
print(eleve.affichageAge())
