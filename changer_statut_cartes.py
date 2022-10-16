def changer_statut_cartes(etat_cartes, infos_carte):
    """
    Cette fonction prend en argument l'etat de chaque carte présente sur le plateau de jeu et modifie celui de la carte indiquée dans 'infos_carte'

    Parameters
    ----------
    etat_cartes: liste où les cartes sont rangées dans l'ordre aléatoire définit au préalable, peut_être soit face visible, devinée ou retournée
        type: list
    infos_carte: p-uplet de données contennant la position de la carte et son nouvel état(face visible, devinée ou retournée)
        type: tuple

    Returns
    -------
    nouvel_etat_cartes: la liste précédente modifiée avec les nouvelles informations de la carte


    Exemples
    --------

    >>> changer_statut_cartes([['face visible', 'devinée'], ['devinée', 'retournée']], ((0, 0), 'retournée'))
    [['retournée', 'devinée'], ['devinée', 'retournée']]

    >>> changer_statut_cartes([['face visible', 'retournée'], ['retournée', 'retournée']], ((1, 1), 'face visible'))
    [['face visible', 'retournée'], ['retournée', 'face visible']]


    """

    # ============
    # ----Code----
    # ============


    #---Préconditions---
    assert type(etat_cartes) == list
    assert len(etat_cartes) != 0
    assert type(infos_carte) == tuple
    
    nouvel_etat_cartes = etat_cartes
    nouvel_etat_cartes[infos_carte[0][0]][infos_carte[0][1]] = infos_carte[1]

    #---Postconditions---
    assert type(nouvel_etat_cartes) == list
    assert len(nouvel_etat_cartes) != 0
    
    return nouvel_etat_cartes


# =============================================================================
# test de la fonction
# =============================================================================
if __name__ == '__main__':
    import doctest
    doctest.testmod()