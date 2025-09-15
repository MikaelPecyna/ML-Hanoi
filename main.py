#!/bin/python3

from JeuHanoi import Jeu_Hanoi
from GameHandler import GameHandler
jeu = Jeu_Hanoi() 

#init de la partie au début
jeu.nombre_palet[0] = 3
jeu.pic[0,0] = 3
jeu.pic[0,1] = 2
jeu.pic[0,2] = 1

#init de la partie finale voulu => Condition d'arret 
jeu_final = Jeu_Hanoi()

jeu_final.pic[2,0] = 3
jeu_final.pic[2,1] = 2
jeu_final.pic[2,2] = 1

gh = GameHandler()

turn = 0 
#while gh.nombre_situation(jeu) != gh.nombre_situation(jeu_final):
while(turn < 5):
	
    
    
    # Règle 1 : déplacer du pic 0 vers pic 1 si possible
    if gh.regle_jeu(jeu, 0, 1) and gh.situation_non_vue(jeu, 0, 1):
        print("REGLE 1 : Déplacement du pic 0 vers pic 1")
        gh.effectue_deplacement(jeu, 0, 1)
    
    # Règle 2 : déplacer du pic 1 vers pic 2 si possible
    elif gh.regle_jeu(jeu, 1, 2) and gh.situation_non_vue(jeu, 1, 2):
        print("REGLE 2 : Déplacement du pic 1 vers pic 2")
        
        
    # Règle 3 : déplacer du pic 2 vers pic 1 si possible
    elif gh.regle_jeu(jeu, 2, 1) and gh.situation_non_vue(jeu, 2, 1):
        print("REGLE 3 : Déplacement du pic 2 vers pic 1")
        gh.effectue_deplacement(jeu, 2, 1)
    
    # Règle 4 : déplacer du pic 1 vers pic 0 si possible
    elif gh.regle_jeu(jeu, 1, 0) and gh.situation_non_vue(jeu, 1, 0):
        print("REGLE 4 : Déplacement du pic 1 vers pic 0")
        gh.effectue_deplacement(jeu, 1, 0)
    
    else: 
        print("Erreur")
    
    # Incrémentation du compteur de tours
    turn += 1

print("finit")
