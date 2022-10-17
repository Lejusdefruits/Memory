#---Import des modules---
from afficher_plateau_de_jeu import afficher_plateau_de_jeu
from changer_statut_cartes import changer_statut_cartes
from IHM_choix_joueur import IHM_choix_joueur
from initialisation_plateau_de_jeu import initialisation_plateau_de_jeu
from retourner_cartes_non_devinees import retourner_cartes_non_devinees
from verifier_egalite_cartes import verifier_egalite_cartes
from verifier_fin import verifier_fin


longeur, largeur = 4, 4
tour = 0
liste_cartes, etat_cartes = initialisation_plateau_de_jeu(longeur, largeur)

condition = True
while condition:
    print(liste_cartes)
    tour += 1
    afficher_plateau_de_jeu(etat_cartes, liste_cartes)
    print(liste_cartes)
    coordonnees_carte_a_retourner = IHM_choix_joueur(longeur, largeur)
    etat_cartes = changer_statut_cartes(etat_cartes, (coordonnees_carte_a_retourner, 'face visible'))
    if tour % 2 == 0:
        afficher_plateau_de_jeu(etat_cartes, liste_cartes)
        if verifier_fin(etat_cartes): condition = False
        if verifier_egalite_cartes(etat_cartes, liste_cartes)[0]:
            for i in range(2):
                changer_statut_cartes(etat_cartes, (verifier_egalite_cartes(etat_cartes, liste_cartes)[i][1], verifier_egalite_cartes(etat_cartes, liste_cartes)[i][2], 'face visible'))
            else:
                etat_cartes = retourner_cartes_non_devinees(etat_cartes)