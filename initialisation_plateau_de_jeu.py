def initialisation_plateau_de_jeu(longueur, largeur):

    #---Import des modules---
    from random import shuffle

    """
    Cette fonction va créer un plateau de jeu constitué de cartes aléatoirement placées sur le plateau. Cette fonction prend en argument 'largeur' et 'longueur',
        qui définiront respectement la largeur et la longueur du plateau de jeu et donc le nombre de cartes pour renvoyer 'plateau_base' et 'etat_cartes'. 

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
        etat_cartes: Une liste contennant l'etat de chaque carte(face visible, devinée ou retournée)
            type: list

    """

    # ============
    # ----Code----
    # ============

    #---Préconditions---
    assert type(largeur) == int
    assert type(longueur) == int
    assert largeur*longueur % 2 == 0

    liste_cartes = [i for i in range(int(longueur * largeur / 2))] * 2
    shuffle(liste_cartes)
    plateau_base = [[liste_cartes[i+j] for j in range(largeur)] for i in range(len(liste_cartes), largeur)]
    etat_cartes = [['retournée' for j in range(largeur)] for i in range(0, len(liste_cartes), largeur)]

    #---Postconditions---
    assert type(plateau_base) == list
    assert type(etat_cartes) == list

    assert len(plateau_base) == longueur
    assert len(plateau_base[0]) == largeur

    assert len(etat_cartes) == longueur
    assert len(etat_cartes[0]) == largeur

    #---Returns---
    return plateau_base, etat_cartes

# =============================================================================
# test de la fonction
# =============================================================================
if __name__ == '__main__':
    import doctest
    doctest.testmod()