#!/bin/python3

from JeuHanoi import Jeu_Hanoi
from GameHandler import GameHandler

# Initialisation du jeu
jeu = Jeu_Hanoi() 

# Initialisation de la partie au début
jeu.nombre_palet[0] = 3
jeu.pic[0,0] = 3
jeu.pic[0,1] = 2
jeu.pic[0,2] = 1

# Initialisation de la partie finale (condition d'arrêt)
jeu_final = Jeu_Hanoi()
jeu_final.pic[2,0] = 3
jeu_final.pic[2,1] = 2
jeu_final.pic[2,2] = 1

gh = GameHandler()

turn = 0

print("================ Version Début ================")
jeu.printJeu()
print("===============================================")

# Boucle de jeu avec un nombre maximum de tours







while turn < 2:

    # Vérification des règles avant de tenter un déplacement
    # Règle 1 : déplacer du pic 0 vers pic 1 si possible
    regle_1 = gh.regle_jeu(jeu, 0, 1)
    situation_1 = gh.situation_non_vue(jeu, 0, 1)
    print(f"Règle 1 - regle_jeu: {regle_1}, situation_non_vue: {situation_1}")
    
    if regle_1 and situation_1:
        print("REGLE 1 : Déplacement du pic 0 vers pic 1")
        gh.effectue_deplacement(jeu, 0, 1)
        jeu.printJeu()
    
    # Règle 2 : déplacer du pic 1 vers pic 2 si possible
    regle_2 = gh.regle_jeu(jeu, 1, 2)
    situation_2 = gh.situation_non_vue(jeu, 1, 2)
    print(f"Règle 2 - regle_jeu: {regle_2}, situation_non_vue: {situation_2}")
    
    if regle_2 and situation_2:
        print("REGLE 2 : Déplacement du pic 1 vers pic 2")
        gh.effectue_deplacement(jeu, 1, 2)
        
        
    # Règle 3 : déplacer du pic 2 vers pic 1 si possible
    regle_3 = gh.regle_jeu(jeu, 2, 1)
    situation_3 = gh.situation_non_vue(jeu, 2, 1)
    print(f"Règle 3 - regle_jeu: {regle_3}, situation_non_vue: {situation_3}")
    
    if regle_3 and situation_3:
        print("REGLE 3 : Déplacement du pic 2 vers pic 1")
        gh.effectue_deplacement(jeu, 2, 1)
    
    # Règle 4 : déplacer du pic 1 vers pic 0 si possible
    regle_4 = gh.regle_jeu(jeu, 1, 0)
    situation_4 = gh.situation_non_vue(jeu, 1, 0)
    print(f"Règle 4 - regle_jeu: {regle_4}, situation_non_vue: {situation_4}")
    
    if regle_4 and situation_4:
        print("REGLE 4 : Déplacement du pic 1 vers pic 0")
        gh.effectue_deplacement(jeu, 1, 0)
    
    else: 
        print("Erreur")
    
    # Afficher l'état actuel du jeu à chaque tour
    jeu.printJeu()
    
    # Incrémentation du compteur de tours
    turn += 1

print("================ Version Finale ================")
jeu.printJeu()
print("================================================")

