from JeuHanoi import *

def nombre_situation(jeu) -> int:
    code = 0
    for pic in range(3):  # 3 pics
        triplet = [0, 0, 0]
        for i in range(jeu.nombre_palet[pic]):  
            disque = jeu.pic[pic, i] 
            triplet[disque - 1] = 1  
        triplet_val = (triplet[2] << 2) | (triplet[1] << 1) | triplet[0]
        code |= (triplet_val << (3 * (2 - pic)))  # pic0 = bits de poids fort
    return code

def pic_vide(jeu, i) -> bool :

    return jeu.nombre_palet[i] == 0

def regle_jeu(jeu, i1, i2) -> bool : 
    """
    Trois possibilité de non deplacement : 
    - Si i1 est vide 
    - Si i1 > i2 
    - Si i1 = i2 sauf si i2 = 0
    """
    if pic_vide(jeu, i1):
        return False
    if i1 == i2:
        return False
    disque_a_deplacer = jeu.getHighest(i1)
    disque_dest = jeu.getHighest(i2)
    if disque_dest == 0:
        return True
    if disque_a_deplacer < disque_dest:
        return True
    return False

def effectue_deplacement(jeu, i1, i2, situation_deja_vue):
    value = jeu.removeHighest(i1)
    jeu.addPalet(i2, value)
    situation_deja_vue.append(nombre_situation(jeu))

def situation_non_vue(jeu: JeuHanoi, p1: int, p2: int, situation_deja_vue: list) -> bool:
    """
    Modifie un nombre de 9 bits en se basant sur deux sections (p1 et p2)
    et vérifie si le nouveau nombre est déjà dans une liste.

    Args:
        jeu (JeuHanoi): Jeu avant le coup
        p1 (int): L'index de la première section (0, 1, ou 2).
        p2 (int): L'index de la deuxième section (0, 1, ou 2).
        situation_deja_vue (list): La liste des nombres déjà vus.

    Returns:
        bool: True si le nouveau nombre n'est pas dans la liste, False sinon.
    """
    # On calcule la situation après déplacement (simulation)
    jeu_copie = JeuHanoi()
    jeu_copie.pic = jeu.pic.copy()
    jeu_copie.nombre_palet = jeu.nombre_palet.copy()
    # On simule le déplacement
    if jeu_copie.nombre_palet[p1] == 0:
        return False  # déplacement impossible
    disque = jeu_copie.removeHighest(p1)
    jeu_copie.addPalet(p2, disque)
    code = nombre_situation(jeu_copie)
    if code in situation_deja_vue:
        return False
    return True

