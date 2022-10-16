def afficher_plateu_de_jeu(etats_cartes, liste_cartes):
    """
    Cette fonction affiche dans la console les cartes n'ayant pas comme état 'retournée' et prend donc en argument la liste des cartes et leur etat
    
    Parameters
    ----------
    etat_cartes: liste où les cartes sont rangées dans l'ordre aléatoire définit au préalable, peut_être soit face visible, devinée ou retournée
        type: list
    liste_cartes: la liste de cartes rangées dans l'ordre aléatoire définit au début de partie
        type: list
    """
    
    # ============
    # ----Code----
    # ============
    
    
    #---Préconditions---


    liste_a_afficher = liste_cartes
    for i in range(len(liste_cartes)):
        for j in range(len(liste_cartes[0])):
            if etats_cartes[i][j] == 'retournée':
                liste_a_afficher[i][j] = 'X'


    for element in liste_a_afficher:
        print(element)