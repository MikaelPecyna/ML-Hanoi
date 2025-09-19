from JeuHanoi import JeuHanoi
from utils import *

jeu = JeuHanoi()
jeu.nombre_palet[0] = 3
jeu.pic[0,0] = 3
jeu.pic[0,1] = 2
jeu.pic[0,2] = 1





Jeu_final = JeuHanoi()
Jeu_final.nombre_palet[2] = 3
Jeu_final.pic[2,0] = 3
Jeu_final.pic[2,1] = 2
Jeu_final.pic[2,2] = 1




def main():
    turn = 0
    situation_deja_vue = []
    value_final = nombre_situation(Jeu_final)
    while nombre_situation(jeu) != value_final:
        if(regle_jeu(jeu, 0,1) and situation_non_vue(jeu, 0, 1, situation_deja_vue)):
            effectue_deplacement(jeu, 0,1, situation_deja_vue)
        elif(regle_jeu(jeu, 1,2) and situation_non_vue(jeu, 1, 2, situation_deja_vue)):
            effectue_deplacement(jeu, 1,2, situation_deja_vue)
        elif(regle_jeu(jeu, 2,1) and situation_non_vue(jeu, 2, 1, situation_deja_vue)):
            effectue_deplacement(jeu, 2,1, situation_deja_vue)
        elif(regle_jeu(jeu, 1,0) and situation_non_vue(jeu, 1, 0, situation_deja_vue)):
            effectue_deplacement(jeu, 1,0, situation_deja_vue)
        turn +=1
        print("\n\n------[", turn , "]------", )
        jeu.printJeu()

if __name__ == '__main__':
    main()