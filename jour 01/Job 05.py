class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def get_age(self):
        return self.age

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

    def get_prenom(self):
        return self.prenom

animal = Animal()

print("L'âge de l'animal :", animal.get_age())

animal.vieillir()
print("L'âge de l'animal :", animal.get_age())

animal.nommer("Luna")
print("L'animal se nomme", animal.get_prenom())
