def verifier_fin(etat_cartes):
    """
    Cette fonction prend en argument l'état de toutes les cartes présentes sur le plateau de jeu et renvoie True si le jeu est fini
        et donc que touts les couples de cartes ont étés trouvés, False sinon.

    Parameters
    ----------
    etat_cartes: liste où les cartes sont rangées dans l'ordre aléatoire définit au préalable, peut_être soit face visible, devinée ou retournée
        type: dict


    Returns
    -------
    response: response contient True si l'etat de toutes les cartes se trouve être devinée, False sinon.
        type: bool


    Exemples
    --------

    >>>verifier_fin(["face visible", "devinée", "devinée", "retournée"])
    False
    >>>verifier_fin(["devinée", "devinée", "devinée", "devinée"])
    True



    """

    # ============
    # ----Code----
    # ============


    #---Préconditions---
    assert type(etat_cartes) == list
    assert len(etat_cartes) != 0

    #---Postconditions---
    assert type(response) == bool


# =============================================================================
# test de la fonction
# =============================================================================
if __name__ == '__main__':
    import doctest
    doctest.testmod()