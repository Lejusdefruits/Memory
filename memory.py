#---Import des modules---
from afficher_plateu_de_jeu import afficher_plateu_de_jeu
from changer_statut_cartes import changer_statut_cartes
from IHM_choix_joueur import IHM_choix_joueur
from initialisation_plateau_de_jeu import initialisation_plateau_de_jeu
from retourner_cartes_non_devinees import retourner_cartes_non_devinees
from verifier_egalite_cartes import verifier_egalite_cartes
from verifier_fin import verifier_fin


class Game:
    def __int__(self):
        self.longeur, self.largeur = 4, 4
        self.tour = 0
        self.liste_cartes, self.etat_cartes = initialisation_plateau_de_jeu(self.longeur, self.largeur)
        self.loop()

    def loop(self):
        self.tour += 1
        afficher_plateu_de_jeu(self.liste_cartes, self.etat_cartes)
        self.coordonnees_carte_a_retourner = IHM_choix_joueur(self.longeur, self.largeur)
        self.etat_cartes = changer_statut_cartes(self.etat_cartes, (self.coordonnees_carte_a_retourner, 'retournée'))
        if self.tour % 2 == 0:
            verifier_fin(self.etat_cartes)
            if verifier_egalite_cartes(self.etat_cartes, self.liste_cartes)[0]:
                for i in range(2):
                    changer_statut_cartes(self.etat_cartes, (verifier_egalite_cartes(self.etat_cartes, self.liste_cartes)[i][1], verifier_egalite_cartes(self.etat_cartes, self.liste_cartes)[i][2], 'retournée'))
            else:
                self.etat_cartes = retourner_cartes_non_devinees(self.etat_cartes)

        self.loop()







Game()