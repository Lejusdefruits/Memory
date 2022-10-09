def initialisation_plateau_de_jeu(longueur, largeur):
    from random import shuffle
    """
    Cette fonction va créer un plateau de jeu constitué de cartes aléatoirement placées sur le plateau. Cette fonction prend en argument 'largeur' et 'longueur', 
        qui définiront respectement la largeur et la longueur du platerau de jeu et donc le nombre de cartes. 

    Parameters
    ----------
    longeur: Désigne la longueur du plateau
        type: int
    largeur: Désigne la largeur du plateau
        type: int


    Returns
    -------
        plateau_base: Le plateau généré aléatoirement en fonction des dimensions 'largeur' et 'hauteur'
            type: list


    Exemples
    --------
    >>>len(initialisation_plateau_de_jeu(5, 2))
    5
    >>>len(initialisation_plateau_de_jeu(4, 3)[0])
    3
    
    """

    # ============
    # ----Code----
    # ============


    #---Préconditions---
    assert type(largeur) == int
    assert type(longueur) == int
    assert largeur*longueur % 2 == 0

    liste_cartes = [i for i in range(int(longueur*largeur/2))]*2
    shuffle(liste_cartes)
    plateau_base = [[liste_cartes[j*i] for j in range(largeur)] for i in range(longueur)]

    #---Postconditions---
    assert type(plateau_base) == list

    return plateau_base

# =============================================================================
# test de la fonction
# =============================================================================
if __name__ == '__main__':
    import doctest
    doctest.testmod()