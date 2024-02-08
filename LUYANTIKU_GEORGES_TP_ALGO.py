# LUYANTIKU GEORGES
# G2/ Génie Civil

                                 # TP D'ALGORITHMIQUE ET PROGRAMMATION

# Définition de la classe Fraction
class Fraction:
    # Constructeur de la classe
    def __init__(self, num, den):
        # On vérifie que le dénominateur est un entier strictement positif
        assert isinstance(den, int) and den > 0, "Le dénominateur doit être un entier strictement positif"
        # On simplifie la fraction en utilisant le plus grand commun diviseur
        pgcd = self.pgcd(num, den)
        self.num = num // pgcd # Attribut privé num
        self.den = den // pgcd # Attribut privé den
    
    # Méthode pour calculer le plus grand commun diviseur de deux nombres
    def pgcd(self, a, b):
        # Algorithme d'Euclide
        while b != 0:
            a, b = b, a % b
        return a
    
    # Méthode spéciale pour afficher la fraction
    def __str__(self):
        # Si le dénominateur vaut 1, on affiche seulement le numérateur
        if self.den == 1:
            return str(self.num)
        # Sinon, on affiche le numérateur et le dénominateur séparés par un slash
        else:
            return str(self.num) + "/" + str(self.den)
    
    # Méthode spéciale pour comparer deux fractions
    def __eq__(self, other):
        # On vérifie que l'autre objet est une instance de la classe Fraction
        if isinstance(other, Fraction):
            # On compare les numérateurs et les dénominateurs
            return self.num == other.num and self.den == other.den
        # Sinon, on renvoie False
        else:
            return False

# Création des instances F1, F2, F3 et F4
F1 = Fraction(3, 4)
F2 = Fraction(-8, 1)
F3 = Fraction(2, 3)
F4 = Fraction(21, 28)

# Affichage des instances
print(F1) # 3/4
print(F2) # -8
print(F3) # 2/3
print(F4) # 3/4

# Tests de la méthode spéciale eq
print(F1 == F4) # True
print(F2 == F3) # False
print(F1 == 0.75) # False
