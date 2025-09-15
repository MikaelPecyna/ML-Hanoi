import numpy as np

class Jeu_Hanoi:
    def __init__(self):
        # Initialisation de la matrice pic (3 tours avec 3 niveaux possibles)
        self.pic = np.zeros([3, 3], dtype=np.int)  # Matrice 3x3 pour les tours et les palets
        self.nombre_palet = np.zeros(3, dtype=np.int)  # Nombre de palets sur chaque tour

    def getPicValue(self, index):
        # Retourne le nombre de palets sur la tour d'index donné
        return self.nombre_palet[index]
        
    def getPics(self):
        # Retourne la matrice pic qui contient les palets sur chaque tour
        return self.pic

    def getHighest(self, index):
        for i in range(2, -1, -1):  # Parcours de la colonne de la tour spécifiée
            if self.pic[index][i] != 0:  # Si un palet est trouvé (non nul)
                return self.pic[index][i]  # Retourne la valeur du palet le plus haut
        return 0  # Retourne 0 si aucun palet n'est trouvé sur la tour
        
    def addPalet(self, value, index):
        self.pic[index][self.nombre_palet[index]] = value
        self.nombre_palet[index] += 1  # Met à jour le nombre de palets sur la tour
        
    def deletePalet(self, index):
        # Supprime le palet du sommet de la tour
        self.pic[index][self.nombre_palet[index] - 1] = 0
        self.nombre_palet[index] -= 1  # Diminue le nombre de palets sur la tour
        
    def printJeu(self):
        print(self.pic)

