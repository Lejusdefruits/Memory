def IHM_choix_joueur(longueur, largeur):
    """
    Cette fonction demande au joueur de choisir une carte à retourner,
        prend en argument la longueur et la largeur du plateau pour vérifier si les coordonnées qu'entre le joueur existent

    Parameters
    ----------
    longeur: Désigne la longueur du plateau
        type: int
    largeur: Désigne la largeur du plateau
        type: int

    Returns
    -------
    emplacement_carte_choisie: Un tableau avec les coordonnées de la longueur et la largeur de la carte choisit par le joueur

    """

    # ============
    # ----Code----
    # ============
    emplacement_x_carte_choisie = -1
    emplacement_y_carte_choisie = -1

    while emplacement_x_carte_choisie < 0 or emplacement_x_carte_choisie > longueur or emplacement_y_carte_choisie < 0 or emplacement_y_carte_choisie > largeur:
        emplacement_x_carte_choisie = int(input("choisir la ligne de la carte choisie :"))
        emplacement_y_carte_choisie = int(input("choisir la colonne de la carte choisie :"))
        if emplacement_x_carte_choisie < 0 or emplacement_x_carte_choisie > longueur or emplacement_y_carte_choisie < 0 or emplacement_y_carte_choisie > largeur:
            print("Les coordonnées ne sont pas valides, veuillez réessayer \n")
    emplacement_carte_choisie = emplacement_x_carte_choisie, emplacement_y_carte_choisie

    #---Postconditions---
    assert emplacement_x_carte_choisie >= 0 and emplacement_x_carte_choisie <= longueur
    assert emplacement_y_carte_choisie >= 0 and emplacement_y_carte_choisie <= largeur
    assert type(emplacement_x_carte_choisie) == int
    assert type(emplacement_y_carte_choisie) == int
    assert type(emplacement_carte_choisie) == tuple

    #---Returns---
    return emplacement_carte_choisie

# =============================================================================
# test de la fonction
# =============================================================================
if __name__ == '__main__':
    IHM_choix_joueur(5, 5)