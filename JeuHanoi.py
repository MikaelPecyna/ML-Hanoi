import numpy as np

class JeuHanoi:
    def printJeu(self):
        print("\nÉtat du jeu :")
        for niveau in range(2, -1, -1):
            ligne = []
            for pic in range(3):
                if self.nombre_palet[pic] > niveau:
                    val = self.pic[pic, niveau]
                    ligne.append(str(val))
                else:
                    ligne.append("|")
            print("  ".join(ligne))
        print("--- --- ---")
        print(" 0   1   2 ")
    def __init__(self):
        self.pic = np.zeros([3,3],dtype=np.int_)
        self.nombre_palet = np.zeros(3,dtype=np.int_)
        pass

    def getHighest(self, indice_pic):

        n = self.nombre_palet[indice_pic]
        if n == 0:
            return 0
        return self.pic[indice_pic, n-1]

    def removeHighest(self, indice_pic):
        n = self.nombre_palet[indice_pic]
        if n == 0:
            return 0
        val = self.pic[indice_pic, n-1]
        self.pic[indice_pic, n-1] = 0
        self.nombre_palet[indice_pic] -= 1
        return val

    def addPalet(self, indice_pic, valeur):
        n = self.nombre_palet[indice_pic]
        self.pic[indice_pic, n] = valeur
        self.nombre_palet[indice_pic] += 1
