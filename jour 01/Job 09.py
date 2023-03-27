class Student:
    def __init__(self, nom, prenom, numero_etudiants):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiants = numero_etudiants
        self.__nombre_credit = 0
        self.__level = self.__studentEval()

    def add_credits(self, credit):
        if credit >= 0:
            self.__nombre_credit = int(credit)
            return self.__nombre_credit
        else: 
            print(" Ce n'est un nombre entier positif")
        
    def set_nom(self, nom):
        self.__nom = nom

    def get_nom(self):
        return self.__nom
    
    def set_prenom(self, prenom):
        self.__prenom = prenom

    def get_prenom(self):
        return self.__prenom
    
    def set_nombre_credit(self, nombre_credit):
        self.__nombre_credit = nombre_credit

    def get_nombre_credit(self):
        return self.__nombre_credit
    
    def __studentEval(self):
        if self.__nombre_credit >= 90:
            return 'Excellent'
        elif self.__nombre_credit >= 80:
            return 'Très bien'
        elif self.__nombre_credit >= 70:
            return 'Bien'
        elif self.__nombre_credit >= 60:
            return 'Passable'
        elif self.__nombre_credit <= 60:
            return 'Insuffisant'
        else: 
            return False
        
    def studentinfo(self):
        return f'Nom : {self.__nom}\nPrenom : {self.__prenom}\nId : {self.__numero_etudiants}\nNiveau : {self.__level}'


etudiant = Student("John", "Doe", 145)
prenom = etudiant.get_nom()
nom = etudiant.get_prenom()
e_credits = etudiant.add_credits(30)

print(f'Le nombre de credits de {prenom} {nom} est de {e_credits} points')

info = etudiant.studentinfo()
print(info)
