#!/bin/python3
from JeuHanoi import Jeu_Hanoi
from GameHandler import GameHandler

def test_regle_jeu():
    # Création de l'instance de jeu
    jeu = Jeu_Hanoi()
    gh = GameHandler()
    
    # Initialisation des tours avec quelques palets
    jeu.addPalet(3, 0)  # Tour 0 : Palet de taille 3
    jeu.addPalet(2, 0)  # Tour 0 : Palet de taille 2
    jeu.addPalet(1, 0)  # Tour 0 : Palet de taille 1
    jeu.addPalet(3, 1)  # Tour 1 : Palet de taille 3
    jeu.addPalet(2, 1)  # Tour 1 : Palet de taille 2


    # Test 1 : Le pic de départ est vide (Tour 2 à Tour 0)
    print("Test 1 : Départ vide")
    result = gh.regle_jeu(jeu, 2, 0)  # Tour 2 à Tour 0 (vide, donc doit échouer)
    print(f"Résultat : {result} (doit être False)")
    
    # Test 2 : Le départ est le même que la destination
    print("\nTest 2 : Départ = Destination")
    result = gh.regle_jeu(jeu, 0, 0)  # Tour 0 à Tour 0 (doit échouer car même pic)
    print(f"Résultat : {result} (doit être False)")
    
    # Test 3 : Le palet du départ est plus grand que celui de la destination
    print("\nTest 3 : Palet départ > palet destination")
    result = gh.regle_jeu(jeu, 0, 2)  # Tour 0 (3) à Tour 2 (1) (doit échouer)
    print(f"Résultat : {result} (doit être True)")
    
    # Test 4 : Le palet du départ est plus petit que celui de la destination
    print("\nTest 4 : Palet départ < palet destination")
    result = gh.regle_jeu(jeu, 1, 0)  # Tour 2 (1) à Tour 0 (3) (doit réussir)
    print(f"Résultat : {result} (doit être True)")
    
    # Test 5 : Le pic de destination est vide
    print("\nTest 5 : Destination vide")
    result = gh.regle_jeu(jeu, 1, 2)  # Tour 1 (2) à Tour 2 (vide) (doit réussir)
    print(f"Résultat : {result} (doit être True)")

    # Test 6 : Le pic de destination est déjà occupé par un palet plus petit
    print("\nTest 6 : Destination occupée par un palet plus petit")
    result = gh.regle_jeu(jeu, 0, 2)  # Tour 0 (3) à Tour 2 (1) (doit échouer)
    print(f"Résultat : {result} (doit être True)")
    
    # Test 7 : Le pic de départ est vide, mais avec une destination valide (vide)
    print("\nTest 7 : Départ vide, destination valide")
    result = gh.regle_jeu(jeu, 2, 1)  # Tour 2 (vide) à Tour 1 (2) (doit échouer)
    print(f"Résultat : {result} (doit être False)")

    # Test 8 : Déplacement d'un petit palet sur un grand palet
    print("\nTest 8 : Petit palet sur grand palet")
    result = gh.regle_jeu(jeu, 2, 1)  # Tour 2 (1) à Tour 1 (2) (doit réussir)
    print(f"Résultat : {result} (doit être False)")

test_regle_jeu()
