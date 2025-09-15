from JeuHanoi import Jeu_Hanoi

class GameHandler:

    def __init__(self):
        self.alreadySeen = []

    def nombre_situation(self, jeu):
        return jeu.getPics().tostring()

    def pic_vide(self, jeu, index):
        # Return false if there is at least one palet on it
        return jeu.getPicValue(index) == 0

    def regle_jeu(self, jeu, start, end):
        if self.pic_vide(jeu, start):
            return False
        if start == end:
            return False

        if jeu.getHighest(start) > jeu.getHighest(end):
            if jeu.getHighest(end) == 0:
                return True
            return False

        return True

        # Logique pour gérer les règles du jeu
        # Ajouter ici la vérification des autres règles de déplacement
        pass

    def effectue_deplacement(self, jeu, start, end):
        # Prendre la highest de start 
        # La mettre "le plus haut de end" 
        value = jeu.getHighest(start)
        
        jeu.deletePalet(start)
        jeu.addPalet(value, end)
        
        self.alreadySeen.append(self.nombre_situation(jeu))

    def situation_non_vue(self, jeu, start, end):
        self.mon_jeu = Jeu_Hanoi()
        self.mon_jeu.pic = jeu.getPics()
        
        self.effectue_deplacement(self.mon_jeu, start, end)
        
        if self.nombre_situation(self.mon_jeu) in self.alreadySeen:
            return False
        return True

