from loadConsVoy import loadCons, loadVoy, genereTirageLettres
import tkinter as tk
import time
from random import *
import tkinter.font as tkFont
import pygame
from icones import *
from tirage import *
from data import *
from classe import *
#from datetime import timedelta, datetime, date, time

class MotUtilisateur:
    def __init__(self):
        self.proposition = ''
        self.idxProposition = []
        self.plaques_possibles_actuelles = []
        self.plaques_possibles_ensemble = []
        self.valide = 0
        self.possible_de_valider = 1

    def Reset(self):
        self.proposition = ''
        self.idxProposition = []
        self.plaques_possibles_actuelles = []
        self.plaques_possibles_ensemble = []
        self.valide = 0
        self.possible_de_valider = 1

    def Init_plaques_possibles(self,nbPlaquesChiffres):
        # appelée par Lancement_tirage_chiffres (icones.py)
        for ii in range(0, nbPlaquesChiffres):
            self.plaques_possibles_actuelles.append(ii)
        if nbPlaquesChiffres == 6:
            self.plaques_possibles_ensemble = [0,1,2,3,4,5,17,22,27,32,37]

    def AddLettre(self, tirage, idx, icones, don):
        if not idx in self.idxProposition:
            self.idxProposition.append(idx)
            self.proposition = self.proposition + tirage.tirage[idx]
            icones.boutons_tirage[idx].configure(bg=don.proprietes.couleur_bg_select)
            icones.boutons_reponse[len(self.proposition)-1].configure(text=tirage.tirage[idx])
            icones.triangle[idx].configure(fg=don.proprietes.couleur_triangle_select)

    def AddChiffre(self, tirage, idx, icones, don):
        # appelée par Set_boutons_tirage_chiffres (icones.py)
        # idx : idice de la plaque sur laquelle on a cliqué

        idx_symboles_operations = [14, 19, 24, 29, 34]
        idx_symboles_egal = [16, 21, 26, 31, 36]
        idx_plaques_initiales = [0, 1, 2, 3, 4, 5]
        idx_nouvelles_plaques = [17, 22, 27, 32, 37]
        idx_toutes_plaques = [0, 1, 2, 3, 4, 5, 17, 22, 27, 32, 37]
        idx_valeurs_sans_action = [13, 15, 18, 20, 23, 25, 28, 30, 33, 35]
        idx_symboles_operations_init = [9, 10, 11, 12]

        if idx in idx_symboles_operations_init:
            position_nouvelle = icones.position_actuelle_chiffres
            if position_nouvelle in idx_symboles_operations:
                txt = icones.boutons_tirage[idx].cget('text')
                icones.boutons_tirage[icones.position_actuelle_chiffres].configure(text=txt)
                icones.Increment_position_actuelle_chiffres(don)
        if idx in idx_toutes_plaques:
            if idx not in self.idxProposition:
                txt = icones.boutons_tirage[idx].cget('text')
                if txt:
                    position_nouvelle = icones.position_actuelle_chiffres
                    if position_nouvelle in idx_valeurs_sans_action:
                        self.idxProposition.append(idx)
                        icones.boutons_tirage[idx].configure(bg=don.proprietes.couleur_bg_select)
                        txt = icones.boutons_tirage[idx].cget('text')
                        icones.boutons_tirage[icones.position_actuelle_chiffres].configure(text=txt)
                        icones.Increment_position_actuelle_chiffres(don)
                    position_nouvelle = icones.position_actuelle_chiffres
                    if position_nouvelle in idx_nouvelles_plaques:
                        # ajout du signe =
                        icones.boutons_tirage[position_nouvelle - 1].configure(text='=')

                        # calcul de la nouvelle plaque
                        valeur1 = int(icones.boutons_tirage[position_nouvelle - 4].cget('text'))
                        valeur2 = int(icones.boutons_tirage[position_nouvelle - 2].cget('text'))
                        operateur = icones.boutons_tirage[position_nouvelle - 3].cget('text')
                        valeur3 = 314
                        if operateur == '+':
                            valeur3 = valeur1 + valeur2
                        elif operateur == 'x':
                            valeur3 = valeur1 * valeur2
                        elif operateur == '-':
                            if valeur1 >= valeur2:
                                valeur3 = valeur1 - valeur2
                            else:
                                valeur3 = ''
                                # à faire : rajouter un bruit
                        elif operateur == '/':
                            if not valeur1 % valeur2:
                                valeur3 = valeur1 // valeur2
                            else:
                                valeur3 = ''
                                # à faire : rajouter un bruit

                        # ajout de la nouvelle plaque
                        icones.boutons_tirage[icones.position_actuelle_chiffres].configure(text=str(valeur3))
                        icones.Increment_position_actuelle_chiffres(don)

    def DelLettre(self, tirage, icones, don):
        if len(self.proposition) > 0:
            idx2del = self.idxProposition[-1]
            icones.boutons_reponse[len(self.proposition)-1].configure(text='')
            self.proposition = self.proposition[:-1]
            self.idxProposition = self.idxProposition[:-1]
            icones.boutons_tirage[idx2del].configure(bg=don.proprietes.couleur_bg_defaut)
            icones.triangle[idx2del].configure(fg="black")

    def DelChiffre(self, icones, don):
        # appelée par Set_bouton_effacer_chiffres (icones.py)
        # recherche de la plaque non vide la plus grande
        idx_symboles_operations = [14, 19, 24, 29, 34]
        idx_symboles_egal = [16, 21, 26, 31, 36]
        idx_plaques_initiales = [0, 1, 2, 3, 4, 5]
        idx_nouvelles_plaques = [17, 22, 27, 32, 37]
        idx_toutes_plaques = [0, 1, 2, 3, 4, 5, 17, 22, 27, 32, 37]
        idx_valeurs_sans_action = [13, 15, 18, 20, 23, 25, 28, 30, 33, 35]
        idx_symboles_operations_init = [9, 10, 11, 12]
        # icones.boutons_tirage[icones.position_actuelle_chiffres].configure(text=str(valeur3))
        posActuelle = icones.position_actuelle_chiffres
        posPrecedente = icones.Get_decrement_position_actuelle_chiffres(don)

        # cas particulier : on est sur la dernière plaque, dans ce cas, le decrement pose problème car
        # on se décale directement sur la plaque précédente au lieu de supprimer la plaque voulue
        if posActuelle == idx_nouvelles_plaques[-1]:
            icones.boutons_tirage[posActuelle].configure(text='')
            icones.boutons_tirage[posActuelle - 1].configure(text='')
            icones.boutons_tirage[self.idxProposition[-1]].configure(bg=don.proprietes.couleur_bg_defaut)
            self.idxProposition = self.idxProposition[:-1]
            icones.Decrement_position_actuelle_chiffres(don)
            icones.boutons_tirage[posPrecedente].configure(text='')
        else:
            # si avant on était sur une plaque sans action : celle-ci disparaît et la plaque initiale redevient cliquable
            if posPrecedente in idx_valeurs_sans_action:
                if len(self.idxProposition) > 0:
                    icones.boutons_tirage[self.idxProposition[-1]].configure(bg=don.proprietes.couleur_bg_defaut)
                    self.idxProposition = self.idxProposition[:-1]
                    icones.Decrement_position_actuelle_chiffres(don)
                icones.boutons_tirage[posPrecedente].configure(text='')

            # si avant on était sur un symbole opérateur, celui-ci est effacé
            if posPrecedente in idx_symboles_operations:
                icones.Decrement_position_actuelle_chiffres(don)
                icones.boutons_tirage[posPrecedente].configure(text='')

            # si avant on était sur une nouvelle plaque :
            #    la nouvelle plaque disparaît
            #    le symbole = aussi
            #    la plaque précédente aussi
            if posPrecedente in idx_nouvelles_plaques:
                icones.boutons_tirage[self.idxProposition[-1]].configure(bg=don.proprietes.couleur_bg_defaut)
                icones.Decrement_position_actuelle_chiffres(don)
                icones.boutons_tirage[posPrecedente].configure(text='')
                icones.boutons_tirage[posPrecedente - 1].configure(text='')
                self.DelChiffre(icones, don)





        # premier cas : la plaque à retirer est une plaque sur laquelle on ne peut pas cliquer (13, 14, 15 ZB)


    def DelLettreRAZ(self, icones, don):
        self.proposition = ''
        if len(self.idxProposition) > 0:
            for ii in self.idxProposition:
                icones.boutons_tirage[ii].configure(bg=don.proprietes.couleur_bg_defaut)
                icones.triangle[ii].configure(fg="black")
            for ii in range(0,len(self.idxProposition)):
                icones.boutons_reponse[ii].configure(text='')
        self.idxProposition = []

    def DelChiffreRAZ(self, icones, don):
        self.proposition = []
        for i in range(0,25):
            self.DelChiffre(icones, don)
        # if len(self.idxProposition) > 0:
        #     for ii in self.idxProposition:
        #         icones.boutons_tirage[ii].configure(bg=don.proprietes.couleur_bg_defaut)
        #     for ii in range(0,len(self.idxProposition)):
        #         icones.boutons_reponse[ii].configure(text='')
        self.idxProposition = []

    def ValideReponse(self, tirage, don, icones, chrono):
        chrono.val_actuelle = -5
        if len(tirage.sol_basique) == 0:
            tirage.Solveur(don)
        if self.possible_de_valider:
            self.valide = 0
            prop = self.proposition.lower()
            prop_sort = ordreAlpha(prop)
            # recherche dans le dictionnaire pour chaque combinaison de lettres
            sol_alpha_t = []
            sol_complet_t = []
            sol_basique_t = []
            idx_dico = 314
            for ii in range(0, len(don.dico)):
                if len(don.dico[ii].alpha[0]) == len(prop):
                    idx_dico = ii
            if idx_dico<200:
                res_list = [i for i in range(len(don.dico[idx_dico].alpha)) if
                            don.dico[idx_dico].alpha[i] == prop_sort]
                if len(res_list) > 0:
                    for jj in range(0, len(res_list)):
                        sol_alpha_t.append(don.dico[idx_dico].alpha[res_list[jj]])
                        sol_basique_t.append(don.dico[idx_dico].basique[res_list[jj]])
                        sol_complet_t.append(don.dico[idx_dico].complet[res_list[jj]])
                    if prop in sol_basique_t:
                        self.valide = 1
            self.possible_de_valider = 0
            if self.valide:
                for ii in range(0, len(icones.boutons_reponse)):
                    icones.boutons_reponse[ii].configure(bg=don.proprietes.couleur_valide)
            else:
                for ii in range(0, len(icones.boutons_reponse)):
                    icones.boutons_reponse[ii].configure(bg=don.proprietes.couleur_faux)
            don.nbTirages += 1
            don.total += tirage.top
            if self.valide:
                don.score += len(prop)
                if len(prop) == tirage.top:
                    don.nbTops += 1
            chas = 'Score : ' + str(don.score) + ' / ' + str(don.total)
            chat = 'Tops : ' + str(don.nbTops) + ' / ' + str(don.nbTirages)
            icones.score.configure(text=chas)
            icones.tops.configure(text=chat)

    def ValideReponse_chiffres(self, tirage, don, icones, chrono):
        chrono.val_actuelle = -5
        if len(tirage.sol_basique) == 0:
            tirage.Solveur_chiffres(don)
        if self.possible_de_valider:
            self.valide = 0
            liste_totaux = [0]
            idxPlaques = []
            cible = tirage.tirage_chiffres[-1]
            distance_BC = 100000
            for ii in range(0,don.nbPlaquesChiffres-1):
                idxPlaques.append(self.plaques_possibles_ensemble[-ii-1])
            for ii in idxPlaques:
                if icones.boutons_tirage[ii].cget('text'):
                    distance_temp = abs(int(icones.boutons_tirage[ii].cget('text'))-cible)
                    if distance_temp < distance_BC:
                        distance_BC = distance_temp
            [nbPts, ptsTop] = don.bareme_chiffres.Appli_bareme(tirage.liste_possibles_chiffres, distance_BC)

            self.possible_de_valider = 0
            don.nbTirages += 1
            don.total += ptsTop
            don.score += nbPts
            if ptsTop == nbPts:
                don.nbTops += 1
            chas = 'Score : ' + str(don.score) + ' / ' + str(don.total)
            chat = 'Tops : ' + str(don.nbTops) + ' / ' + str(don.nbTirages)
            icones.score.configure(text=chas)
            icones.tops.configure(text=chat)


