def retourner_cartes_non_devinees(etat_cartes):
    """
    Cette fonction change l'état des deux cartes ayant l'état 'devinée' por leur mettre l'état 'retournée'
    Parameters
    ----------
    etat_cartes: Une liste contennant l'etat de chaque carte(face visible, devinée ou retournée)
            type: list

    Returns
    -------
    nouvel_etat_cartes: Une liste contennant l'etat de chaque carte(face visible, devinée ou retournée),
        en ayant retourné les deux cartes qui avaient l'état 'devinée'.
        type: list

    Exemples
    --------

    >>> retourner_cartes_non_devinees([['face visible', 'devinée'], ['devinée', 'face visible']])
    [['retournée', 'devinée'], ['devinée', 'retournée']]

    >>> retourner_cartes_non_devinees([['face visible', 'retournée'], ['face visible', 'retournée']])
    [['retournée', 'retournée'], ['retournée', 'retournée']]
    """

    # ============
    # ----Code----
    # ============

    # ---Préconditions---
    assert type(etat_cartes) == list
    assert len(etat_cartes) != 0

    nouvel_etat_cartes = etat_cartes

    for i in range(len(etat_cartes)):
        for j in range(len(etat_cartes[0])):
            if nouvel_etat_cartes[i][j] == 'face visible':
                nouvel_etat_cartes[i][j] = 'retournée'

    # ---Postconditions---
    assert type(nouvel_etat_cartes) == list
    assert len(nouvel_etat_cartes) == len(etat_cartes)

    print("\nLes 2 cartes retournées n'étaient pas les mêmes\n")
    timeout = input("Appuyez sur entrée pour continuer...")
    return nouvel_etat_cartes


if __name__ == '__main__':
    import doctest
    doctest.testmod()