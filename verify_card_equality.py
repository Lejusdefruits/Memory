def verify_card_equality(card1, card2):
    """
    Cette fonction prend en argument card1 et card2 pour vérifier si ces deux cartes sont les mêmes ou non,
        renvoie une variable 'answer', contenant True si les deux cartes sont mêmes et False dans le cas contraire.

    Parameters
    ----------
        card1: Le nombre que porte première carte
            type=int
        card2: Le nombre que porte seconde carte
            type=int

    Returns
    -------
        answer: La réponse si oui ou non card1 et card2 sont les mêmes, True si oui et False sinon
            type=bool


    Exemples
    --------
    >>> verify_card_equality(1, 1)
    True
    >>> verify_card_equality(1, 2)
    False

    """

    # ============
    # ----Code----
    # ============



    #---Préconditions---

    #---Postconditions---



# =============================================================================
# test de la fonction
# =============================================================================
if __name__ == '__main__':
    import doctest
    doctest.testmod()