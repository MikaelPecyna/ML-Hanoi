class GameHandler: 
    
    def __init__(self): 
        alreadySeen = []
        pass

    def situation_non_vue(self, jeu, start, end):
        return 

    def nombre_situation(self, jeu):
        #Return l'id de la situation
        pass


    def calc_situation(self, jeu, start, end):
        


    def pic_vide(self, jeu, index):
        # Return false if there is at least one palet on it
        return jeu.getPicValue(index) == 0

    def regle_jeu(self, jeu, start; end):
        # Return true if the move is possible 
        if(jeu.getHighestPalet(start) == 0): #Si il n'y a pas de palet sur le pic de depart => false 
            return False 
        elif(jeu.getHighestPalet(start) > jeu.getHighestPale(end):
                return False 
        else:
            return True 
