def verifier_egalite_cartes(etat_cartes, liste_cartes):
    
    """
    Cette fonction prend en argument etat_cartes pour vérifier si les deux cartes face visible les mêmes ou non,
        renvoie une variable 'answer', contenant True si les deux cartes sont mêmes et False dans le cas contraire.

    Parameters
    ----------
    etat_cartes: Une liste contennant l'etat de chaque carte(face visible, devinée ou retournée) rangée dans l'ordre aléatoire définit au préalable
            type: list
    liste_cartes: La liste des cartes rangés dans l'ordre aléatoire définit au préalable
            type: list

    Returns
    -------
        answer: La réponse si oui ou non card1 et card2 sont les mêmes, True si oui et False sinon
            type=bool


    Exemples
    --------
    >>> verifier_egalite_cartes(1, 1)[0]
    True
    >>> verifier_egalite_cartes(1, 2)[0]
    False

    """

    # ============
    #----Code-----
    # ============
    
    
    #---Préconditions---
    assert type(etat_cartes) == list
    assert type(liste_cartes) == list

    cartes_face_visible = []
    for i in range(len(etat_cartes)):
        for j in range(len(etat_cartes[0])):
            if etat_cartes[i][j] == 'face visible':
                cartes_face_visible.append([liste_cartes[i][j], i, j])

    if cartes_face_visible[0][0] == cartes_face_visible[1][0]:  #les deux cartes retournée doivent être les mêmes
            answer = True
            
    else:
         answer = False  #si  les deux carte retournées ne sont pas les mêmes


    #---Postconditions---
    assert type(answer) == bool

    #---Returns---
    return answer, cartes_face_visible


# =============================================================================
# test de la fonction
# =============================================================================
if __name__ == '__main__':
    import doctest
    doctest.testmod()