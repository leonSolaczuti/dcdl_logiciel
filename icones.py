from loadConsVoy import loadCons, loadVoy, genereTirageLettres
from classe import *
from tkinter import *
import tkinter as tk
import time
from random import *
import tkinter.font as tkFont
import pygame
from motUtilisateur import *
from data import *
#from datetime import timedelta, datetime, date, time

class Icones:
    def __init__(self, Mafenetre):
        self.fen = Mafenetre
        self.boutons_tirage = []
        self.boutons_reponse = []
        self.triangle = []
        self.bouton_effacer = Button(Mafenetre)
        self.bouton_raz = Button(Mafenetre)
        self.bouton_next = Button(Mafenetre)
        self.bouton_solutions = Button(Mafenetre)
        self.chrono = Label(Mafenetre)
        self.bouton_top = Button(Mafenetre)
        self.bouton_valider = Button(Mafenetre)
        self.boutons_lettres = []
        self.boutons_chiffres = []
        self.boutons_nbVoyelles = []
        self.score = Label(Mafenetre)
        self.tops = Label(Mafenetre)
        self.boutons_aleatoire = []
        self.bouton_lancement_lettres = []
        self.bouton_lancement_chiffres = []
        self.position_actuelle_chiffres = []
        self.bouton_changer = Button(Mafenetre)
        self.boutons_lancement_nbLettres = []
        self.reglage_temps = []
        self.bareme_chiffres = []
        self.boutons_son = []
        self.boutons_temporisation = []
        self.boutons_sauvegarde = Button(Mafenetre)
        self.bouton_rajouts = Button(Mafenetre)
        self.labels_rajouts = []
        self.sabot_chiffres = Button(self.fen)
        self.sabot_lettres = Button(self.fen)

    def Lancement_tirage_lettres(self, tirage, don, chrono, motUtilisateur):
        # if don.nbLettres==10:
        #     self.fen.geometry('900x430')
        # else:
        self.fen.title('Tirage')
        tirage.ajuste_tirage_prepares(don)  # on ne garde que les tirages préparés qui ont le bon nombre de
        # lettres ou plaques
        def maFonc(event):
            if don.type_actuel == 'lettres':
                lettre_a_ajouter = event.char.upper()
                if tirage.valide:
                    idx_dans_tirage = []
                    if len(self.boutons_tirage):
                        for ii in range(len(self.boutons_tirage)):
                            if self.boutons_tirage[ii].cget('bg') == don.proprietes.couleur_bg_defaut:
                                if self.boutons_tirage[ii].cget('text').upper() == lettre_a_ajouter:
                                    idx_dans_tirage.append(ii)
                    if len(idx_dans_tirage):
                        idx_dans_tirage = idx_dans_tirage[0]
                        motUtilisateur.AddLettre(tirage, idx_dans_tirage, self, don)
                else:
                    self.AddLettre(tirage, lettre_a_ajouter)


        def maFonc_del(event):
            if don.type_actuel == 'lettres':
                if tirage.valide:
                    motUtilisateur.DelLettre(tirage, self, don)
                else:
                    self.DelLettre(tirage)

        def maFonc_valide(event):
            if don.type_actuel == 'lettres':
                if tirage.valide:
                    motUtilisateur.ValideReponse(tirage, don, self, chrono)
                else:
                    self.ValideTirage(tirage, chrono)

        self.fen.geometry('954x430')
        don.type_actuel = 'lettres'
        nbLettres = don.nbLettres
        # SI TEST EN LETTRES SEULEMENT SUPPRIMER LA LIGNE SUIVANTE
        self.Del_boutons_lancement()
        self.Set_boutons_lettres(tirage, self.fen, don, chrono)
        self.Set_chrono(chrono, don)
        self.Set_triangle(nbLettres, don)
        self.Set_boutons_tirage(tirage, motUtilisateur, nbLettres, don)
        self.Set_score(don)
        self.Set_tops(don)
        self.Set_bouton_top(tirage, don)
        self.Set_bouton_effacer(tirage, motUtilisateur, don)
        self.Set_bouton_raz(tirage, motUtilisateur, don)
        self.Set_bouton_valider(tirage, motUtilisateur, don, chrono)
        self.Set_bouton_solutions(tirage, don)
        self.Set_bouton_next(tirage, motUtilisateur, don, chrono)
        self.Set_boutons_aleatoire(don)
        self.Set_boutons_nbVoyelles(tirage, don)
        self.Set_boutons_sauvegarde(tirage, don)
        self.fen.bind("<a>", maFonc)
        self.fen.bind("<b>", maFonc)
        self.fen.bind("<c>", maFonc)
        self.fen.bind("<d>", maFonc)
        self.fen.bind("<e>", maFonc)
        self.fen.bind("<f>", maFonc)
        self.fen.bind("<g>", maFonc)
        self.fen.bind("<h>", maFonc)
        self.fen.bind("<i>", maFonc)
        self.fen.bind("<j>", maFonc)
        self.fen.bind("<k>", maFonc)
        self.fen.bind("<l>", maFonc)
        self.fen.bind("<m>", maFonc)
        self.fen.bind("<n>", maFonc)
        self.fen.bind("<o>", maFonc)
        self.fen.bind("<p>", maFonc)
        self.fen.bind("<q>", maFonc)
        self.fen.bind("<r>", maFonc)
        self.fen.bind("<s>", maFonc)
        self.fen.bind("<t>", maFonc)
        self.fen.bind("<u>", maFonc)
        self.fen.bind("<v>", maFonc)
        self.fen.bind("<w>", maFonc)
        self.fen.bind("<x>", maFonc)
        self.fen.bind("<y>", maFonc)
        self.fen.bind("<z>", maFonc)
        self.fen.bind("<A>", maFonc)
        self.fen.bind("<B>", maFonc)
        self.fen.bind("<C>", maFonc)
        self.fen.bind("<D>", maFonc)
        self.fen.bind("<E>", maFonc)
        self.fen.bind("<F>", maFonc)
        self.fen.bind("<G>", maFonc)
        self.fen.bind("<H>", maFonc)
        self.fen.bind("<I>", maFonc)
        self.fen.bind("<J>", maFonc)
        self.fen.bind("<K>", maFonc)
        self.fen.bind("<L>", maFonc)
        self.fen.bind("<M>", maFonc)
        self.fen.bind("<N>", maFonc)
        self.fen.bind("<O>", maFonc)
        self.fen.bind("<P>", maFonc)
        self.fen.bind("<Q>", maFonc)
        self.fen.bind("<R>", maFonc)
        self.fen.bind("<S>", maFonc)
        self.fen.bind("<T>", maFonc)
        self.fen.bind("<U>", maFonc)
        self.fen.bind("<V>", maFonc)
        self.fen.bind("<W>", maFonc)
        self.fen.bind("<X>", maFonc)
        self.fen.bind("<Y>", maFonc)
        self.fen.bind("<Z>", maFonc)
        self.fen.bind("<BackSpace>", maFonc_del)
        self.fen.bind("<Return>", maFonc_valide)
        self.Set_bouton_changer_lettres(tirage, motUtilisateur, don, chrono)

    def Lancement_tirage_lettres2(self, tirage, don, chrono, motUtilisateur):
        # if don.nbLettres==10:
        #     self.fen.geometry('900x430')
        # else:
        def maFonc(event):
            if don.type_actuel == 'lettres':
                lettre_a_ajouter = event.char.upper()
                if tirage.valide:
                    idx_dans_tirage = []
                    if len(self.boutons_tirage):
                        for ii in range(len(self.boutons_tirage)):
                            if self.boutons_tirage[ii].cget('bg') == don.proprietes.couleur_bg_defaut:
                                if self.boutons_tirage[ii].cget('text').upper() == lettre_a_ajouter:
                                    idx_dans_tirage.append(ii)
                    if len(idx_dans_tirage):
                        idx_dans_tirage = idx_dans_tirage[0]
                        motUtilisateur.AddLettre(tirage, idx_dans_tirage, self, don)
                else:
                    self.AddLettre(tirage, lettre_a_ajouter)

        def maFonc_del(event):
            if don.type_actuel == 'lettres':
                if tirage.valide:
                    motUtilisateur.DelLettre(tirage, self, don)
                else:
                    self.DelLettre(tirage)

        def maFonc_valide(event):
            if don.type_actuel == 'lettres':
                if tirage.valide:
                    motUtilisateur.ValideReponse(tirage, don, self, chrono)
                else:
                    self.ValideTirage(tirage, chrono)

        chrono.reset_lettres()
        self.fen.geometry('954x430')
        don.type_actuel = 'lettres'
        nbLettres = don.nbLettres
        self.Del_boutons_chiffres()
        # SI TEST EN LETTRES SEULEMENT SUPPRIMER LA LIGNE SUIVANTE
        self.Set_boutons_lettres(tirage, self.fen, don, chrono)
        self.Set_boutons_sauvegarde(tirage, don)
        self.Set_chrono(chrono, don)
        self.Set_triangle(nbLettres, don)
        self.Set_boutons_tirage(tirage, motUtilisateur, nbLettres, don)
        self.Set_score(don)
        self.Set_tops(don)
        self.Set_bouton_top(tirage, don)
        self.Set_bouton_effacer(tirage, motUtilisateur, don)
        self.Set_bouton_raz(tirage, motUtilisateur, don)
        self.Set_bouton_valider(tirage, motUtilisateur, don, chrono)
        self.Set_bouton_solutions(tirage, don)
        self.Set_bouton_next(tirage, motUtilisateur, don, chrono)
        self.Set_boutons_aleatoire(don)
        self.Set_boutons_nbVoyelles(tirage, don)
        self.fen.bind("<a>", maFonc)
        self.fen.bind("<b>", maFonc)
        self.fen.bind("<c>", maFonc)
        self.fen.bind("<d>", maFonc)
        self.fen.bind("<e>", maFonc)
        self.fen.bind("<f>", maFonc)
        self.fen.bind("<g>", maFonc)
        self.fen.bind("<h>", maFonc)
        self.fen.bind("<i>", maFonc)
        self.fen.bind("<j>", maFonc)
        self.fen.bind("<k>", maFonc)
        self.fen.bind("<l>", maFonc)
        self.fen.bind("<m>", maFonc)
        self.fen.bind("<n>", maFonc)
        self.fen.bind("<o>", maFonc)
        self.fen.bind("<p>", maFonc)
        self.fen.bind("<q>", maFonc)
        self.fen.bind("<r>", maFonc)
        self.fen.bind("<s>", maFonc)
        self.fen.bind("<t>", maFonc)
        self.fen.bind("<u>", maFonc)
        self.fen.bind("<v>", maFonc)
        self.fen.bind("<w>", maFonc)
        self.fen.bind("<x>", maFonc)
        self.fen.bind("<y>", maFonc)
        self.fen.bind("<z>", maFonc)
        self.fen.bind("<A>", maFonc)
        self.fen.bind("<B>", maFonc)
        self.fen.bind("<C>", maFonc)
        self.fen.bind("<D>", maFonc)
        self.fen.bind("<E>", maFonc)
        self.fen.bind("<F>", maFonc)
        self.fen.bind("<G>", maFonc)
        self.fen.bind("<H>", maFonc)
        self.fen.bind("<I>", maFonc)
        self.fen.bind("<J>", maFonc)
        self.fen.bind("<K>", maFonc)
        self.fen.bind("<L>", maFonc)
        self.fen.bind("<M>", maFonc)
        self.fen.bind("<N>", maFonc)
        self.fen.bind("<O>", maFonc)
        self.fen.bind("<P>", maFonc)
        self.fen.bind("<Q>", maFonc)
        self.fen.bind("<R>", maFonc)
        self.fen.bind("<S>", maFonc)
        self.fen.bind("<T>", maFonc)
        self.fen.bind("<U>", maFonc)
        self.fen.bind("<V>", maFonc)
        self.fen.bind("<W>", maFonc)
        self.fen.bind("<X>", maFonc)
        self.fen.bind("<Y>", maFonc)
        self.fen.bind("<Z>", maFonc)
        self.fen.bind("<BackSpace>", maFonc_del)
        self.fen.bind("<Return>", maFonc_valide)
        self.Set_bouton_changer_lettres(tirage, motUtilisateur, don, chrono)

    def Del_boutons_chiffres(self):
        for ii in self.boutons_tirage:
            ii.destroy()
        self.bouton_effacer.destroy()
        self.bouton_raz.destroy()
        self.bouton_next.destroy()
        self.bouton_solutions.destroy()
        self.chrono.destroy()
        self.bouton_top.destroy()
        self.bouton_valider.destroy()
        for ii in self.boutons_chiffres:
            ii.destroy()
        self.score.destroy()
        self.tops.destroy()
        for ii in self.boutons_aleatoire:
            ii.destroy()
        for ii in self.boutons_nbVoyelles:
            ii.destroy()
        Mafenetre = self.fen
        self.bouton_changer.destroy()
        self.boutons_tirage = []
        self.boutons_reponse = []
        self.triangle = []
        self.bouton_effacer = Button(Mafenetre)
        self.bouton_raz = Button(Mafenetre)
        self.bouton_next = Button(Mafenetre)
        self.bouton_solutions = Button(Mafenetre)
        self.chrono = Label(Mafenetre)
        self.bouton_top = Button(Mafenetre)
        self.bouton_valider = Button(Mafenetre)
        self.boutons_lettres = []
        self.boutons_chiffres = []
        self.boutons_nbVoyelles = []
        self.score = Label(Mafenetre)
        self.tops = Label(Mafenetre)
        self.boutons_aleatoire = []
        self.bouton_lancement_lettres = []
        self.bouton_lancement_chiffres = []
        self.position_actuelle_chiffres = []
        self.bouton_changer = Button(Mafenetre)

    def Del_boutons_Lettres(self):
        for ii in self.boutons_tirage:
            ii.destroy()
        for ii in self.boutons_reponse:
            ii.destroy()
        for ii in self.triangle:
            ii.destroy()
        self.bouton_effacer.destroy()
        self.bouton_raz.destroy()
        self.bouton_next.destroy()
        self.bouton_solutions.destroy()
        self.chrono.destroy()
        self.bouton_top.destroy()
        self.bouton_valider.destroy()
        for ii in self.boutons_lettres:
            ii.destroy()
        self.score.destroy()
        self.tops.destroy()
        for ii in self.boutons_aleatoire:
            ii.destroy()
        for ii in self.boutons_nbVoyelles:
            ii.destroy()
        Mafenetre = self.fen
        self.bouton_changer.destroy()

        self.boutons_tirage = []
        self.boutons_reponse = []
        self.triangle = []
        self.bouton_effacer = Button(Mafenetre)
        self.bouton_raz = Button(Mafenetre)
        self.bouton_next = Button(Mafenetre)
        self.bouton_solutions = Button(Mafenetre)
        self.chrono = Label(Mafenetre)
        self.bouton_top = Button(Mafenetre)
        self.bouton_valider = Button(Mafenetre)
        self.boutons_lettres = []
        self.boutons_chiffres = []
        self.boutons_nbVoyelles = []
        self.score = Label(Mafenetre)
        self.tops = Label(Mafenetre)
        self.boutons_aleatoire = []
        self.position_actuelle_chiffres = []
        self.bouton_changer = Button(Mafenetre)

    def Lancement_tirage_chiffres(self, tirage, don, chrono, motUtilisateur):
        self.fen.title('Tirage')
        chrono.reset_chiffres()
        don.type_actuel = 'chiffres'
        # if don.nbLettres==10:
        #     self.fen.geometry('900x430')
        # else:
        tirage.ajuste_tirage_prepares(don) # on ne garde que les tirages préparés qui ont le bon nombre de
        # lettres ou plaques
        self.fen.geometry('954x430')
        # que au départ, lors du choix entre chiffres et lettres
        self.Del_boutons_lancement()
        self.Set_boutons_chiffres(tirage, self.fen, don, chrono)
        self.Set_boutons_sauvegarde(tirage, don)
        self.Set_chrono(chrono, don)
        self.Set_score(don)
        self.Set_tops(don)
        motUtilisateur.Init_plaques_possibles(don.nbPlaquesChiffres)
        self.Set_boutons_tirage_chiffres(tirage, motUtilisateur, don)
        self.Set_bouton_next_chiffres(tirage, motUtilisateur, don, chrono)
        self.Set_boutons_aleatoire(don)
        self.Set_bouton_solutions_chiffres(tirage, don)
        self.Set_bouton_effacer_chiffres(tirage, motUtilisateur, don)
        self.Set_bouton_top_chiffres(tirage, don)
        self.Set_bouton_raz_chiffres(tirage, motUtilisateur, don)
        self.Set_bouton_valider_chiffres(tirage, motUtilisateur, don, chrono)
        self.Set_boutons_nbGrossesPlaques(tirage, don)
        self.Set_bouton_changer_chiffres(tirage, motUtilisateur, don, chrono)



        # motUtilisateur.AddLettre(tirage, c, self, don)

    def Lancement_tirage_chiffres2(self, tirage, don, chrono, motUtilisateur):
        don.type_actuel = 'chiffres'
        # que au départ, lors du choix entre chiffres et lettres
        self.Del_boutons_Lettres()
        self.Set_boutons_chiffres(tirage, self.fen, don, chrono)
        self.Set_chrono(chrono, don)
        self.Set_boutons_sauvegarde(tirage, don)
        self.Set_score(don)
        self.Set_tops(don)
        motUtilisateur.Init_plaques_possibles(don.nbPlaquesChiffres)
        self.Set_boutons_tirage_chiffres(tirage, motUtilisateur, don)
        self.Set_bouton_next_chiffres(tirage, motUtilisateur, don, chrono)
        self.Set_boutons_aleatoire(don)
        self.Set_bouton_solutions_chiffres(tirage, don)
        self.Set_bouton_effacer_chiffres(tirage, motUtilisateur, don)
        self.Set_bouton_top_chiffres(tirage, don)
        self.Set_bouton_raz_chiffres(tirage, motUtilisateur, don)
        self.Set_bouton_valider_chiffres(tirage, motUtilisateur, don, chrono)
        self.Set_boutons_nbGrossesPlaques(tirage, don)
        self.Set_bouton_changer_chiffres(tirage, motUtilisateur, don, chrono)

    def Increment_position_actuelle_chiffres(self, don):
        if don.nbPlaquesChiffres == 6:
            idx = [13,14,15,17,18,19,20,22,23,24,25,27,28,29,30,32,33,34,35,37]
            if self.position_actuelle_chiffres in idx:
                idx2 = idx.index(self.position_actuelle_chiffres)
                if idx2 < len(idx)-1:
                    self.position_actuelle_chiffres = idx[idx2+1]

    def Get_increment_position_actuelle_chiffres(self, don):
        if don.nbPlaquesChiffres == 6:
            idx = [13,14,15,17,18,19,20,22,23,24,25,27,28,29,30,32,33,34,35,37]
            if self.position_actuelle_chiffres in idx:
                idx2 = idx.index(self.position_actuelle_chiffres)
                if idx2 < len(idx)-1:
                    return idx[idx2+1]
                else:
                    return idx[idx2]


    def Decrement_position_actuelle_chiffres(self, don):
        if don.nbPlaquesChiffres == 6:
            idx = [13,14,15,17,18,19,20,22,23,24,25,27,28,29,30,32,33,34,35,37]
            if self.position_actuelle_chiffres in idx:
                idx2 = idx.index(self.position_actuelle_chiffres)
                if idx2 > 0:
                    self.position_actuelle_chiffres = idx[idx2-1]

    def Get_decrement_position_actuelle_chiffres(self, don):
        if don.nbPlaquesChiffres == 6:
            idx = [13,14,15,17,18,19,20,22,23,24,25,27,28,29,30,32,33,34,35,37]
            if self.position_actuelle_chiffres in idx:
                idx2 = idx.index(self.position_actuelle_chiffres)
                if idx2 > 0:
                    return idx[idx2-1]
                else:
                    return idx[idx2]




    def Del_boutons_lancement(self):
        self.bouton_lancement_lettres.destroy()
        self.bouton_lancement_chiffres.destroy()
        self.bouton_rajouts.destroy()
        self.sabot_chiffres.destroy()
        self.sabot_lettres.destroy()
        for ii in range(len(self.boutons_lancement_nbLettres)):
            self.boutons_lancement_nbLettres[ii].destroy()
        for ii in self.reglage_temps:
            ii.destroy()
        for ii in self.bareme_chiffres:
            ii.destroy()
        for ii in self.boutons_son:
            ii.destroy()
        for ii in self.boutons_temporisation:
            ii.destroy()


    def AddLettre(self, tirage, lettre):
        if tirage.valide==0:
            tirage.AddLettre(lettre)
            self.boutons_tirage[len(tirage.tirage)-1].configure(text=lettre.upper())

    def AddChiffre(self, tirage, chiffre):
        if tirage.valide==0 and chiffre!=0:
            if len(tirage.tirage_chiffres) < tirage.nbChiffres:
                tirage.AddChiffre(chiffre)
                self.boutons_tirage[len(tirage.tirage_chiffres) - 1].configure(text=str(tirage.tirage_chiffres[-1]))
            elif len(tirage.objectif_chiffres) < 4:
                idx_boutons_tirage = [6, 7, 8, 38] # labels pour les milliers, centaines, dizaines et unités
                if chiffre < 10:
                    tirage.objectif_chiffres.append(chiffre)
                    self.boutons_tirage[idx_boutons_tirage[len(tirage.objectif_chiffres)-1]].configure(
                        text=str(chiffre))
                elif chiffre == 10:
                    if len(tirage.objectif_chiffres) > 0:
                        tirage.objectif_chiffres.append(0)
                        self.boutons_tirage[idx_boutons_tirage[len(tirage.objectif_chiffres)-1]].configure(
                            text=str(chiffre))
            # elif len(tirage.objectif_chiffres) < 3:
            #     if chiffre < 10:
            #         tirage.objectif_chiffres.append(chiffre)
            #         self.boutons_tirage[5 + len(tirage.objectif_chiffres)].configure(text=str(chiffre))
            #     elif chiffre == 10:
            #         if len(tirage.objectif_chiffres) > 0:
            #             tirage.objectif_chiffres.append(0)
            #             self.boutons_tirage[5 + len(tirage.objectif_chiffres)].configure(text=str(0))


    def DelLettre(self, tirage):
        tirage.DelLettre()
        self.boutons_tirage[len(tirage.tirage)].configure(text='')
        self.triangle[len(tirage.tirage)].configure(text='')

    def DelChiffre(self, tirage):
        if len(tirage.objectif_chiffres):
            idx_labels_totalATrouver = [6, 7, 8, 38]
            tirage.objectif_chiffres = tirage.objectif_chiffres[:-1]
            self.boutons_tirage[idx_labels_totalATrouver[len(tirage.objectif_chiffres)]].configure(text='')
        else:
            tirage.DelChiffre()
            self.boutons_tirage[len(tirage.tirage_chiffres)].configure(text='')

    def ValideTirage(self, tirage, chrono):
        if len(tirage.tirage)>=2:
            tirage.GenereFin()
            chrono.reset_lettres()
            for ii in range(0, len(self.boutons_tirage)):
                self.boutons_tirage[ii].configure(text=tirage.tirage[ii])
                self.triangle[ii].configure(text=tirage.tirage[ii])
                self.boutons_tirage[ii].update()
            chrono.actif = 1
            chrono.val_actuelle += 1
            self.chrono.configure(text=chrono.val_actuelle)
            tirage.valide = 1

    def ValideTirage_chiffres(self, tirage, chrono, don):
        tirage.GenereFin_chiffres(don)
        chrono.reset_chiffres()
        for ii in range(0, don.nbPlaquesChiffres):
            self.boutons_tirage[ii].configure(text=tirage.tirage_chiffres[ii])
        cible = str(tirage.tirage_chiffres[-1])
        idx_labels_totalATrouver = [6, 7, 8, 38]
        for ii in range(0, len(str(don.borneMax))):
            self.boutons_tirage[idx_labels_totalATrouver[ii]].configure(text=cible[ii])
        chrono.actif = 1
        chrono.val_actuelle += 1
        self.chrono.configure(text=chrono.val_actuelle)
        tirage.valide = 1

    def Lancement(self, tirage, don, chrono, motUtilisateur):
        # boutons affichés lors du lancement du programme uniquement
        self.bouton_lancement_lettres = Button(self.fen)
        self.bouton_lancement_lettres.configure(font=("Helvetica", 30), text="Lettres",
                                                bg=don.proprietes.couleur_fond_lettres)
        self.bouton_lancement_lettres.place(x=150, y=50, anchor=CENTER, width=200, height=50)
        self.bouton_lancement_lettres.configure(command=lambda: self.Lancement_tirage_lettres(tirage,
                                                                don, chrono, motUtilisateur))

        self.bouton_lancement_chiffres = Button(self.fen)
        self.bouton_lancement_chiffres.configure(font=("Helvetica", 30), text="Chiffres",
                                                 bg=don.proprietes.couleur_fond_lettres)
        self.bouton_lancement_chiffres.place(x=150, y=110, anchor=CENTER, width=200, height=50)
        self.bouton_lancement_chiffres.configure(command=lambda: self.Lancement_tirage_chiffres(tirage,
                                                                don, chrono, motUtilisateur))


        self.bouton_rajouts = Button(self.fen)
        self.bouton_rajouts.configure(font=("Helvetica", 30), text="Rajouts", bg='gainsboro')
        self.bouton_rajouts.place(x=390, y=50, anchor=CENTER, width=200, height=50)
        self.bouton_rajouts.configure(command=lambda: self.lancementRajouts(don))


        # nombre de lettres
        self.boutons_lancement_nbLettres.append(Label(self.fen))
        self.boutons_lancement_nbLettres[0].configure(font=("Helvetica", 20), text="nombre\nde lettres",
                                                 bg=don.proprietes.couleur_fond)
        self.boutons_lancement_nbLettres[0].place(x=350, y=115, anchor=CENTER)

        val_nbl = ['11','10']
        val_nbl1 = StringVar(self.fen)
        val_nbl1.set(val_nbl[0])
        self.boutons_lancement_nbLettres.append(OptionMenu(self.fen, val_nbl1, *val_nbl))
        self.boutons_lancement_nbLettres[-1].configure(font=('Helvetica', 20))
        self.boutons_lancement_nbLettres[-1].place(x=465, y=115, anchor=CENTER, width=70, height=35)
        def callback_nbl(*args):
            don.nbLettres = int(val_nbl1.get())
        val_nbl1.trace("w", callback_nbl)


        # son actif ou non
        self.boutons_son.append(Label(self.fen))
        self.boutons_son[0].configure(font=("Helvetica", 20), text="son",
                                                      bg=don.proprietes.couleur_fond)
        self.boutons_son[0].place(x=540, y=310, anchor=CENTER)

        val_son_0 = ['actif', 'inactif']
        val_son = StringVar(self.fen)
        val_son.set(val_son_0[0])
        self.boutons_son.append(OptionMenu(self.fen, val_son, *val_son_0))
        self.boutons_son[-1].configure(font=('Helvetica', 16))
        self.boutons_son[-1].place(x=540, y=345, anchor=CENTER, width=90, height=35)

        def callback_son(*args):
            if val_son.get() == 'actif':
                don.son_actif = 1
            else:
                don.son_actif = 0
        val_son.trace("w", callback_son)

        # temporisation
        self.boutons_temporisation.append(Label(self.fen))
        self.boutons_temporisation[0].configure(font=("Helvetica", 20), text="temporisation",
                                      bg=don.proprietes.couleur_fond)
        self.boutons_temporisation[0].place(x=690, y=310, anchor=CENTER)

        val_tempo_0 = ['0', '0.5', '1', '1.5', '2']
        val_tempo = StringVar(self.fen)
        val_tempo.set(val_tempo_0[0])
        self.boutons_son.append(OptionMenu(self.fen, val_tempo, *val_tempo_0))
        self.boutons_son[-1].configure(font=('Helvetica', 16))
        self.boutons_son[-1].place(x=690, y=345, anchor=CENTER, width=90, height=35)
        def callback_tempo(*args):
            don.tempo = float(val_tempo.get())

        val_tempo.trace("w", callback_tempo)


        # temps de réflexion
        OptionList_lettres = ['15','20','25','30','35','40','45','50','55','60']
        variable_lettres = StringVar(self.fen)
        variable_lettres.set(OptionList_lettres[5])
        OptionList_chiffres = ['15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
        variable_chiffres = StringVar(self.fen)
        variable_chiffres.set(OptionList_chiffres[5])

        x0_reglages = 650
        y0_reglages = 40

        self.reglage_temps.append(Label(self.fen))
        self.reglage_temps[0].place(x=x0_reglages, y=y0_reglages, anchor=CENTER, width=250, height=50)
        self.reglage_temps[0].configure(font=("Helvetica", 20), text="temps de réflexion",
                                        bg=don.proprietes.couleur_fond)

        self.reglage_temps.append(Label(self.fen))
        self.reglage_temps[1].place(x=x0_reglages-60, y=y0_reglages+40, anchor=CENTER, width=120, height=50)
        self.reglage_temps[1].configure(font=("Helvetica", 20), text="lettres", bg=don.proprietes.couleur_fond)

        self.reglage_temps.append(Label(self.fen))
        self.reglage_temps[2].place(x=x0_reglages+60, y=y0_reglages+40, anchor=CENTER, width=120, height=50)
        self.reglage_temps[2].configure(font=("Helvetica", 20), text="chiffres", bg=don.proprietes.couleur_fond)

        self.reglage_temps.append(OptionMenu(self.fen, variable_lettres, *OptionList_lettres))
        self.reglage_temps[3].configure(font=('Helvetica', 20))
        self.reglage_temps[3].place(x=x0_reglages-60, y=y0_reglages+80, anchor=CENTER, width=80, height=40)
        def callback_lettres(*args):
            chrono.val_lettres = int(variable_lettres.get())
        variable_lettres.trace("w", callback_lettres)

        self.reglage_temps.append(OptionMenu(self.fen, variable_chiffres, *OptionList_chiffres))
        self.reglage_temps[4].configure(font=('Helvetica', 20))
        self.reglage_temps[4].place(x=x0_reglages+60, y=y0_reglages+80, anchor=CENTER, width=80, height=40)
        def callback_chiffres(*args):
            chrono.val_chiffres = int(variable_chiffres.get())
        variable_chiffres.trace("w", callback_chiffres)

        y0_reglages = y0_reglages-10

        # temps d'écriture
        OptionList_ecrit_lettres = ['5', '10', '15', '20']
        variable_ecrit_lettres = StringVar(self.fen)
        variable_ecrit_lettres.set(OptionList_ecrit_lettres[1])
        OptionList_ecrit_chiffres = ['5', '10', '15', '20', '25', '30']
        variable_ecrit_chiffres = StringVar(self.fen)
        variable_ecrit_chiffres.set(OptionList_ecrit_chiffres[3])

        self.reglage_temps.append(Label(self.fen))
        self.reglage_temps[5].place(x=x0_reglages, y=y0_reglages+150, anchor=CENTER, width=250, height=50)
        self.reglage_temps[5].configure(font=("Helvetica", 20), text="temps d'écriture",
                                        bg=don.proprietes.couleur_fond)

        self.reglage_temps.append(Label(self.fen))
        self.reglage_temps[6].place(x=x0_reglages - 60, y=y0_reglages + 190, anchor=CENTER, width=120, height=50)
        self.reglage_temps[6].configure(font=("Helvetica", 20), text="lettres", bg=don.proprietes.couleur_fond)

        self.reglage_temps.append(Label(self.fen))
        self.reglage_temps[7].place(x=x0_reglages + 60, y=y0_reglages + 190, anchor=CENTER, width=120, height=50)
        self.reglage_temps[7].configure(font=("Helvetica", 20), text="chiffres", bg=don.proprietes.couleur_fond)

        self.reglage_temps.append(OptionMenu(self.fen, variable_ecrit_lettres, *OptionList_ecrit_lettres))
        self.reglage_temps[8].configure(font=('Helvetica', 20))
        self.reglage_temps[8].place(x=x0_reglages - 60, y=y0_reglages + 230, anchor=CENTER, width=80, height=40)

        def callback_ecrit_lettres(*args):
            chrono.val_ecriture_lettres = int(variable_ecrit_lettres.get())
        variable_ecrit_lettres.trace("w", callback_ecrit_lettres)

        self.reglage_temps.append(OptionMenu(self.fen, variable_ecrit_chiffres, *OptionList_ecrit_chiffres))
        self.reglage_temps[9].configure(font=('Helvetica', 20))
        self.reglage_temps[9].place(x=x0_reglages + 60, y=y0_reglages + 230, anchor=CENTER, width=80, height=40)
        def callback_ecrit_chiffres(*args):
            chrono.val_ecriture_chiffres = int(variable_ecrit_chiffres.get())
        variable_ecrit_chiffres.trace("w", callback_ecrit_chiffres)

        # barème chiffres
        x0_bareme = 250
        y0_bareme = 170

        dx1 = -210
        dx2 = -150
        dx3 = -90
        dx4 = -30
        dx5 = 30
        dx6 = 90
        dx7 = 150
        dx8 = 210
        dx9 = -15
        dx10 = 25
        dx11 = 300
        dx12 = 340

        dy1 = 40
        dy2 = 70
        dy3 = 100
        dy4 = 130
        dy5 = 160
        dy6 = 190
        dy7 = 230
        dy8 = 260

        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[0].place(x=x0_bareme-100, y=y0_bareme, anchor=CENTER, width=250, height=50)
        self.bareme_chiffres[0].configure(font=("Helvetica", 20), text="Barème chiffres", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme +dx1, y=y0_bareme+dy1, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="CB", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx1, y=y0_bareme + dy2, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 1", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx1, y=y0_bareme + dy3, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 2", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx1, y=y0_bareme + dy4, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 3", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx1, y=y0_bareme + dy5, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 4", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx1, y=y0_bareme + dy6, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 5", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx3, y=y0_bareme + dy1, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 6", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx3, y=y0_bareme + dy2, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 7", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx3, y=y0_bareme + dy3, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 8", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx3, y=y0_bareme + dy4, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 9", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx3, y=y0_bareme + dy5, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 10", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx3, y=y0_bareme + dy6, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 11", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx5, y=y0_bareme + dy1, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 12", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx5, y=y0_bareme + dy2, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 13", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx5, y=y0_bareme + dy3, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 14", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx5, y=y0_bareme + dy4, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 15", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx5, y=y0_bareme + dy5, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 16", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx5, y=y0_bareme + dy6, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 17", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx7, y=y0_bareme + dy1, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 18", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx7, y=y0_bareme + dy2, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 19", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx7, y=y0_bareme + dy3, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="± 20", bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx7, y=y0_bareme + dy4, anchor=CENTER)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="21+", bg=don.proprietes.couleur_fond)

        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx9, y=y0_bareme + dy7, anchor=E)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="meilleure approche",
                                           bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx9, y=y0_bareme + dy8, anchor=E)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="2ème meilleure approche",
                                           bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx11, y=y0_bareme + dy7, anchor=E)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="3ème meilleure approche",
                                           bg=don.proprietes.couleur_fond)
        self.bareme_chiffres.append(Label(self.fen))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx11, y=y0_bareme + dy8, anchor=E)
        self.bareme_chiffres[-1].configure(font=("Helvetica", 15), text="4ème meilleure approche",
                                           bg=don.proprietes.couleur_fond)

        bareme_liste = ['complément à 10', 'tournoi Nantes', 'manuel']
        variable_liste_baremes = StringVar(self.fen)
        variable_liste_baremes.set(bareme_liste[2])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_liste_baremes, *bareme_liste))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + 120, y=y0_bareme, anchor=CENTER, width=200, height=30)
        def callback_bareme_liste(*args):
            don.bareme_chiffres.valeur[0] = int(variable_CB.get())
            if variable_liste_baremes.get() == 'complément à 10':
                variable_CB.set('10')
                variable_1.set('9')
                variable_2.set('8')
                variable_3.set('7')
                variable_4.set('6')
                variable_5.set('5')
                variable_6.set('4')
                variable_7.set('3')
                variable_8.set('2')
                variable_9.set('1')
                variable_10.set('1')
                variable_11.set('1')
                variable_12.set('1')
                variable_13.set('1')
                variable_14.set('1')
                variable_15.set('1')
                variable_16.set('1')
                variable_17.set('1')
                variable_18.set('1')
                variable_19.set('1')
                variable_20.set('1')
                variable_21.set('1')
                variable_approche1.set('≥ 7')
                variable_approche2.set('≥ 5')
                variable_approche3.set('≥ 3')
                variable_approche4.set('≥ 2')
                don.bareme_chiffres.Set_bareme('C10')
            if variable_liste_baremes.get() == 'tournoi Nantes':
                variable_CB.set('10')
                variable_1.set('9')
                variable_2.set('8')
                variable_3.set('7')
                variable_4.set('7')
                variable_5.set('6')
                variable_6.set('6')
                variable_7.set('5')
                variable_8.set('5')
                variable_9.set('4')
                variable_10.set('4')
                variable_11.set('3')
                variable_12.set('3')
                variable_13.set('2')
                variable_14.set('2')
                variable_15.set('2')
                variable_16.set('2')
                variable_17.set('2')
                variable_18.set('2')
                variable_19.set('2')
                variable_20.set('2')
                variable_21.set('0')
                variable_approche1.set('≥ 7')
                variable_approche2.set('≥ 4')
                variable_approche3.set('≥ 2')
                variable_approche4.set('≥ 0')
                don.bareme_chiffres.Set_bareme('NANTES')
        variable_liste_baremes.trace("w", callback_bareme_liste)

        bareme_CB = ['11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
        bareme_0 = ['11', '10', '9']
        variable_CB = StringVar(self.fen)
        variable_CB.set(bareme_0[1])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_CB, *bareme_0))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme +dx2, y=y0_bareme + dy1, anchor=CENTER, width=55, height=30)
        def callback_bareme_CB(*args):
            don.bareme_chiffres.valeur[0] = int(variable_CB.get())
        variable_CB.trace("w", callback_bareme_CB)

        variable_1 = StringVar(self.fen)
        variable_1.set(bareme_CB[2])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_1, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx2, y=y0_bareme + dy2, anchor=CENTER, width=55, height=30)
        def callback_bareme_1(*args):
            don.bareme_chiffres.valeur[1] = int(variable_1.get())
        variable_1.trace("w", callback_bareme_1)

        variable_2 = StringVar(self.fen)
        variable_2.set(bareme_CB[3])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_2, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx2, y=y0_bareme + dy3, anchor=CENTER, width=55, height=30)
        def callback_bareme_2(*args):
            don.bareme_chiffres.valeur[2] = int(variable_2.get())
        variable_2.trace("w", callback_bareme_2)

        variable_3 = StringVar(self.fen)
        variable_3.set(bareme_CB[4])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_3, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx2, y=y0_bareme + dy4, anchor=CENTER, width=55, height=30)
        def callback_bareme_3(*args):
            don.bareme_chiffres.valeur[3] = int(variable_3.get())
        variable_3.trace("w", callback_bareme_3)

        variable_4 = StringVar(self.fen)
        variable_4.set(bareme_CB[5])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_4, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx2, y=y0_bareme + dy5, anchor=CENTER, width=55, height=30)
        def callback_bareme_4(*args):
            don.bareme_chiffres.valeur[4] = int(variable_4.get())
        variable_4.trace("w", callback_bareme_4)

        variable_5 = StringVar(self.fen)
        variable_5.set(bareme_CB[6])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_5, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx2, y=y0_bareme + dy6, anchor=CENTER, width=55, height=30)
        def callback_bareme_5(*args):
            don.bareme_chiffres.valeur[5] = int(variable_5.get())
        variable_5.trace("w", callback_bareme_5)

        variable_6 = StringVar(self.fen)
        variable_6.set(bareme_CB[7])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_6, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx4, y=y0_bareme + dy1, anchor=CENTER, width=55, height=30)
        def callback_bareme_6(*args):
            don.bareme_chiffres.valeur[6] = int(variable_6.get())
        variable_6.trace("w", callback_bareme_6)

        variable_7 = StringVar(self.fen)
        variable_7.set(bareme_CB[8])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_7, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx4, y=y0_bareme + dy2, anchor=CENTER, width=55, height=30)
        def callback_bareme_7(*args):
            don.bareme_chiffres.valeur[7] = int(variable_7.get())
        variable_7.trace("w", callback_bareme_7)

        variable_8 = StringVar(self.fen)
        variable_8.set(bareme_CB[9])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_8, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx4, y=y0_bareme + dy3, anchor=CENTER, width=55, height=30)
        def callback_bareme_8(*args):
            don.bareme_chiffres.valeur[8] = int(variable_8.get())
        variable_8.trace("w", callback_bareme_8)

        variable_9 = StringVar(self.fen)
        variable_9.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_9, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx4, y=y0_bareme + dy4, anchor=CENTER, width=55, height=30)
        def callback_bareme_9(*args):
            don.bareme_chiffres.valeur[9] = int(variable_9.get())
        variable_9.trace("w", callback_bareme_9)

        variable_10 = StringVar(self.fen)
        variable_10.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_10, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx4, y=y0_bareme + dy5, anchor=CENTER, width=55, height=30)
        def callback_bareme_10(*args):
            don.bareme_chiffres.valeur[10] = int(variable_10.get())
        variable_10.trace("w", callback_bareme_10)

        variable_11 = StringVar(self.fen)
        variable_11.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_11, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx4, y=y0_bareme + dy6, anchor=CENTER, width=55, height=30)
        def callback_bareme_11(*args):
            don.bareme_chiffres.valeur[11] = int(variable_11.get())
        variable_11.trace("w", callback_bareme_11)

        variable_12 = StringVar(self.fen)
        variable_12.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_12, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx6, y=y0_bareme + dy1, anchor=CENTER, width=55, height=30)
        def callback_bareme_12(*args):
            don.bareme_chiffres.valeur[12] = int(variable_12.get())
        variable_12.trace("w", callback_bareme_12)

        variable_13 = StringVar(self.fen)
        variable_13.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_13, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx6, y=y0_bareme + dy2, anchor=CENTER, width=55, height=30)
        def callback_bareme_13(*args):
            don.bareme_chiffres.valeur[13] = int(variable_13.get())
        variable_13.trace("w", callback_bareme_13)

        variable_14 = StringVar(self.fen)
        variable_14.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_14, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx6, y=y0_bareme + dy3, anchor=CENTER, width=55, height=30)
        def callback_bareme_14(*args):
            don.bareme_chiffres.valeur[14] = int(variable_14.get())
        variable_14.trace("w", callback_bareme_14)

        variable_15 = StringVar(self.fen)
        variable_15.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_15, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx6, y=y0_bareme + dy4, anchor=CENTER, width=55, height=30)
        def callback_bareme_15(*args):
            don.bareme_chiffres.valeur[15] = int(variable_15.get())
        variable_15.trace("w", callback_bareme_15)

        variable_16 = StringVar(self.fen)
        variable_16.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_16, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx6, y=y0_bareme + dy5, anchor=CENTER, width=55, height=30)
        def callback_bareme_16(*args):
            don.bareme_chiffres.valeur[16] = int(variable_16.get())
        variable_16.trace("w", callback_bareme_16)

        variable_17 = StringVar(self.fen)
        variable_17.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_17, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx6, y=y0_bareme + dy6, anchor=CENTER, width=55, height=30)
        def callback_bareme_17(*args):
            don.bareme_chiffres.valeur[17] = int(variable_17.get())
        variable_17.trace("w", callback_bareme_17)

        variable_18 = StringVar(self.fen)
        variable_18.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_18, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx8, y=y0_bareme + dy1, anchor=CENTER, width=55, height=30)
        def callback_bareme_18(*args):
            don.bareme_chiffres.valeur[18] = int(variable_18.get())
        variable_18.trace("w", callback_bareme_18)

        variable_19 = StringVar(self.fen)
        variable_19.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_19, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx8, y=y0_bareme + dy2, anchor=CENTER, width=55, height=30)
        def callback_bareme_19(*args):
            don.bareme_chiffres.valeur[19] = int(variable_19.get())
        variable_19.trace("w", callback_bareme_19)

        variable_20 = StringVar(self.fen)
        variable_20.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_20, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx8, y=y0_bareme + dy3, anchor=CENTER, width=55, height=30)
        def callback_bareme_20(*args):
            don.bareme_chiffres.valeur[20] = int(variable_20.get())
        variable_20.trace("w", callback_bareme_20)

        variable_21 = StringVar(self.fen)
        variable_21.set(bareme_CB[10])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_21, *bareme_CB))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx8, y=y0_bareme + dy4, anchor=CENTER, width=55, height=30)
        def callback_bareme_21(*args):
            don.bareme_chiffres.valeur[21] = int(variable_21.get())
        variable_21.trace("w", callback_bareme_21)

        bareme_approche = ['11','≥ 10','≥ 9','≥ 8','≥ 7']
        variable_approche1 = StringVar(self.fen)
        variable_approche1.set(bareme_approche[4])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_approche1, *bareme_approche))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx10, y=y0_bareme + dy7, anchor=CENTER, width=72, height=30)
        def callback_bareme_approche1(*args):
            if variable_approche1.get() == '11':
                don.bareme_chiffres.approches[0] = 11
            elif variable_approche1.get() == '≥ 10':
                don.bareme_chiffres.approches[0] = 10
            elif variable_approche1.get() == '≥ 9':
                don.bareme_chiffres.approches[0] = 9
            elif variable_approche1.get() == '≥ 8':
                don.bareme_chiffres.approches[0] = 8
            elif variable_approche1.get() == '≥ 7':
                don.bareme_chiffres.approches[0] = 7
        variable_approche1.trace("w", callback_bareme_approche1)

        bareme_approche2 = ['≥ 6', '≥ 5', '≥ 4', '≥ 3', '≥ 2', '≥ 1', '≥ 0']
        variable_approche2 = StringVar(self.fen)
        variable_approche2.set(bareme_approche2[1])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_approche2, *bareme_approche2))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx10, y=y0_bareme + dy8, anchor=CENTER, width=72, height=30)
        def callback_bareme_approche2(*args):
            if variable_approche2.get() == '≥ 6':
                don.bareme_chiffres.approches[1] = 6
            elif variable_approche2.get() == '≥ 5':
                don.bareme_chiffres.approches[1] = 5
            elif variable_approche2.get() == '≥ 4':
                don.bareme_chiffres.approches[1] = 4
            elif variable_approche2.get() == '≥ 3':
                don.bareme_chiffres.approches[1] = 3
            elif variable_approche2.get() == '≥ 2':
                don.bareme_chiffres.approches[1] = 2
            elif variable_approche2.get() == '≥ 1':
                don.bareme_chiffres.approches[1] = 1
            elif variable_approche2.get() == '≥ 0':
                don.bareme_chiffres.approches[1] = 0
        variable_approche2.trace("w", callback_bareme_approche2)

        variable_approche3 = StringVar(self.fen)
        variable_approche3.set(bareme_approche2[3])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_approche3, *bareme_approche2))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx12, y=y0_bareme + dy7, anchor=CENTER, width=72, height=30)
        def callback_bareme_approche3(*args):
            if variable_approche3.get() == '≥ 6':
                don.bareme_chiffres.approches[2] = 6
            elif variable_approche3.get() == '≥ 5':
                don.bareme_chiffres.approches[2] = 5
            elif variable_approche3.get() == '≥ 4':
                don.bareme_chiffres.approches[2] = 4
            elif variable_approche3.get() == '≥ 3':
                don.bareme_chiffres.approches[2] = 3
            elif variable_approche3.get() == '≥ 2':
                don.bareme_chiffres.approches[2] = 2
            elif variable_approche3.get() == '≥ 1':
                don.bareme_chiffres.approches[2] = 1
            elif variable_approche3.get() == '≥ 0':
                don.bareme_chiffres.approches[2] = 0
        variable_approche3.trace("w", callback_bareme_approche3)

        variable_approche4 = StringVar(self.fen)
        variable_approche4.set(bareme_approche2[4])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_approche4, *bareme_approche2))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=x0_bareme + dx12, y=y0_bareme + dy8, anchor=CENTER, width=72, height=30)
        def callback_bareme_approche4(*args):
            if variable_approche4.get() == '≥ 6':
                don.bareme_chiffres.approches[3] = 6
            elif variable_approche4.get() == '≥ 5':
                don.bareme_chiffres.approches[3] = 5
            elif variable_approche4.get() == '≥ 4':
                don.bareme_chiffres.approches[3] = 4
            elif variable_approche4.get() == '≥ 3':
                don.bareme_chiffres.approches[3] = 3
            elif variable_approche4.get() == '≥ 2':
                don.bareme_chiffres.approches[3] = 2
            elif variable_approche4.get() == '≥ 1':
                don.bareme_chiffres.approches[3] = 1
            elif variable_approche4.get() == '≥ 0':
                don.bareme_chiffres.approches[3] = 0
        variable_approche4.trace("w", callback_bareme_approche4)

        self.sabot_chiffres = Button(self.fen)
        self.sabot_chiffres.place(x=x0_bareme + 450, y=y0_bareme + dy7 - 5, anchor=CENTER)
        self.sabot_chiffres.configure(font=("Helvetica", 15), text="sabot chiffres")
        self.sabot_chiffres.configure(command=lambda: self.Change_sabot_chiffres(don))

        self.sabot_lettres = Button(self.fen)
        self.sabot_lettres.place(x=x0_bareme + 450, y=y0_bareme + dy7 + 40, anchor=CENTER)
        self.sabot_lettres.configure(font=("Helvetica", 15), text="sabot lettres")
        self.sabot_lettres.configure(command=lambda: self.Change_sabot_Lettres(don))

    def Change_sabot_Lettres(self, don):
        voyelles = 'AEIOUY'
        consonnes = 'BCDFGHJKLMNPQRSTVWXZ'
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        def print_name(event):
            don.Analyse_sabot_chiffres(entree.get(), bouton_warning)
            # print(entree.get())

        fenetre = tk.Tk()
        fenetre.geometry('600x600')
        fenetre.title('Sabot lettres')

        boutons_txt = []
        boutons_val = []
        value = []

        x = [100, 280, 460]
        y = [100, 150, 200, 250, 300, 350, 400, 450, 500]
        for ii in range(len(alphabet)):
            boutons_txt.append(Label(fenetre))
            i = ii % len(y)
            j = int((ii-i)/len(y))
            boutons_txt[-1].place(x=x[j], y=y[i], anchor=E)
            boutons_txt[-1].configure(text=alphabet[ii]+' : ', font=("Helvetica", 20))

            nb = 0
            if alphabet[ii] in voyelles:
                for jj in range(len(don.listeVoy)):
                    if don.listeVoy[jj]==alphabet[ii]:
                        nb += 1
            elif alphabet[ii] in consonnes:
                for jj in range(len(don.listeCons)):
                    if don.listeCons[jj]==alphabet[ii]:
                        nb += 1
            else:
                nb = 31415
            value.append(tk.StringVar(fenetre))
            cha = str(nb)
            value[-1].set(cha)
            boutons_val.append(Entry(fenetre, textvariable=value[-1]))
            boutons_val[-1].place(x=x[j]+5, y=y[i]-18, width=52, height=35)
            boutons_val[-1].configure(font=("Helvetica", 20))

        bouton_valider = Button(fenetre)
        bouton_valider.place(x=100, y=560, width=115, height=42, anchor=CENTER)
        bouton_valider.configure(font=("Helvetica", 20), text='valider')
        bouton_valider.configure(command=lambda: don.Analyse_sabot_lettres(alphabet, consonnes,
                                                                           voyelles, boutons_val, bouton_warn,
                                                                           fenetre))
        bouton_warn = Label(fenetre)
        bouton_warn.place(x=180, y=560, anchor=W)
        bouton_warn.configure(text='', font=("Helvetica", 15), fg='red')

        label_type = Label(fenetre)
        label_type.place(x=170, y=40, anchor=CENTER)
        label_type.configure(text='Type de sabot :', font=("Helvetica", 20))

        typeSabots = ['Le Francophone', 'manuel']
        var_typeSabot = StringVar(fenetre)
        var_typeSabot.set(typeSabots[0])
        bouton_typeSabot = OptionMenu(fenetre, var_typeSabot, *typeSabots)
        bouton_typeSabot.configure(font=('Helvetica', 20))
        bouton_typeSabot.place(x=400, y=40, anchor=CENTER, width=250, height=50)

        def callback_typeSabot(*args):
            valeurs_francophone = [42, 8, 16, 20, 94, 8, 8, 6, 40, 2, 1, 26, 14, 34, 33, 14, 6, 32, 36, 30,
                                   34, 10, 1, 4, 2, 2]
            if var_typeSabot.get() == 'Le Francophone':
                for ii in range(26):
                    value[ii].set(str(valeurs_francophone[ii]))
                print(len(valeurs))
            print('toto')
        var_typeSabot.trace("w", callback_typeSabot)

        fenetre.mainloop()

    def Change_sabot_chiffres(self, don):
        def print_name(event):
            don.Analyse_sabot_chiffres(entree.get(), bouton_warning, fenetre)
            # print(entree.get())

        fenetre = tk.Tk()
        # fenetre.geometry('800x100')
        fenetre.geometry('800x200')
        fenetre.title('Sabot chiffres')
        value = tk.StringVar(fenetre)
        cha = ''
        for ii in range(len(don.listeChiffres)):
            if ii==0:
                cha = cha + str(don.listeChiffres[ii])
            else:
                cha = cha +', ' + str(don.listeChiffres[ii])

        value.set(cha)
        #entree = tk.Entry(fenetre)
        entree = tk.Entry(fenetre, textvariable=value)
        entree.place(x=30, y=10, width=630, height=35)
        entree.configure(font=("Helvetica", 14))

        # On lie la fonction à l'Entry
        # La fonction sera exécutée à chaque fois que l'utilisateur appuie sur "Entrée"
        entree.bind("<Return>", print_name)

        bouton_warning = Label(fenetre)
        bouton_warning.place(x=30, y=70, anchor=W)
        bouton_warning.configure(text='', font=("Helvetica", 15), fg='red')

        bouton_valider = Button(fenetre)
        bouton_valider.place(x=735, y=30, width=100, height=35, anchor=CENTER)
        bouton_valider.configure(font=("Helvetica", 16), text='valider')
        bouton_valider.configure(command=lambda: don.Analyse_sabot_chiffres(entree.get(), bouton_warning,
                                                                        entree_min.get(), entree_max.get(),
                                                                            bouton_warning_minmax, fenetre))

        # minimum à trouver
        label_min = Label(fenetre)
        label_min.place(x=120, y=110, anchor=CENTER)
        label_min.configure(text='minimum à trouver', font=("Helvetica", 15))

        value_min = tk.StringVar(fenetre)
        cha_min = str(don.borneMin)
        value_min.set(cha_min)
        entree_min = tk.Entry(fenetre, textvariable=value_min)
        entree_min.place(x=120, y=150, width=60, height=38, anchor=CENTER)
        entree_min.configure(font=("Helvetica", 18))

        # maximum à trouver
        label_max = Label(fenetre)
        label_max.place(x=330, y=110, anchor=CENTER)
        label_max.configure(text='maximum à trouver', font=("Helvetica", 15))

        value_max = tk.StringVar(fenetre)
        cha_max = str(don.borneMax)
        value_max.set(cha_max)
        entree_max = tk.Entry(fenetre, textvariable=value_max)
        entree_max.place(x=330, y=150, width=60, height=38, anchor=CENTER)
        entree_max.configure(font=("Helvetica", 18))

        bouton_warning_minmax = Label(fenetre)
        bouton_warning_minmax.place(x=450, y=140, anchor=W)
        bouton_warning_minmax.configure(text='', font=("Helvetica", 15), fg='red', justify=LEFT)

        # On lie la fonction à l'Entry
        # La fonction sera exécutée à chaque fois que l'utilisateur appuie sur "Entrée"
        # entree.bind("<Return>", print_name)

        fenetre.mainloop()


    def Set_boutons_chiffres(self, tirage, fen, don, chrono):
        # boutons en haut à droite
        tx = don.geom.taille_x
        if len(self.boutons_chiffres) == 0:
            liste_chiffres = sorted(set(don.listeChiffres))
            while len(liste_chiffres) < 15:
                liste_chiffres.append(0)
            for ii in range(0, len(liste_chiffres)):
                self.boutons_chiffres.append(Button(fen))
                if liste_chiffres[ii]==0:
                    self.boutons_chiffres[ii].configure(font=("Helvetica", 18),
                                                        text='.',
                                                        bg=don.proprietes.couleur_bg_select)
                else:
                    self.boutons_chiffres[ii].configure(font=("Helvetica", 18),
                                                   text=str(liste_chiffres[ii]),
                                                   bg=don.proprietes.couleur_bg_select)
                posX = ii % 7
                posY = (ii-posX)/7
                self.boutons_chiffres[ii].place(x=tx - 310 + 46 * posX,
                                               y=27 + 46 * posY,
                                               anchor=CENTER, width=45, height=45)
            # bouton annuler
            self.boutons_chiffres.append(Button(fen))
            self.boutons_chiffres[-1].place(x=tx - 310 + 46 * 2,
                                           y=27 + 46 * 2,
                                           anchor=CENTER, width=45*3, height=45)
            self.boutons_chiffres[-1].configure(font=("Helvetica", 18), text='annuler',
                                               bg=don.proprietes.couleur_bg_select)

            # bouton valider
            self.boutons_chiffres.append(Button(fen))
            self.boutons_chiffres[-1].place(x=tx - 310 + 46 * 5,
                                           y=27 + 46 * 2,
                                           anchor=CENTER, width=45 * 3, height=45)
            self.boutons_chiffres[-1].configure(font=("Helvetica", 18), text='valider',
                                               bg=don.proprietes.couleur_bg_select)










    def Set_boutons_lettres(self, tirage, fen, don, chrono):
        tx = don.geom.taille_x
        if len(self.boutons_lettres) == 0:
            liste_lettres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.'
            for ii in range(0, len(liste_lettres)):
                self.boutons_lettres.append(Button(fen))
                self.boutons_lettres[ii].configure(font=("Helvetica", 18),
                                                   text=liste_lettres[ii],
                                                   bg=don.proprietes.couleur_bg_select)
                posX = ii % 8
                posY = (ii-posX)/8
                self.boutons_lettres[ii].place(x=tx - 290 + 35 * posX,
                                               y=20 + 35 * posY,
                                               anchor=CENTER, width=34, height=34)
            # bouton annuler
            self.boutons_lettres.append(Button(fen))
            self.boutons_lettres[-1].place(x=tx - 290 + 35 * 3.75,
                                           y=20 + 35 * 3,
                                           anchor=CENTER, width=34*2.5, height=34)
            self.boutons_lettres[-1].configure(font=("Helvetica", 17), text='annuler',
                                               bg=don.proprietes.couleur_bg_select)

            # bouton valider
            self.boutons_lettres.append(Button(fen))
            self.boutons_lettres[-1].place(x=tx - 290 + 35 * 6.25,
                                           y=20 + 35 * 3,
                                           anchor=CENTER, width=34 * 2.5, height=34)
            self.boutons_lettres[-1].configure(font=("Helvetica", 18), text='valider',
                                               bg=don.proprietes.couleur_bg_select)


    def Set_chrono(self, chrono, don):

        posX = don.geom.posX
        posY = don.geom.posY
        self.chrono.configure(text=chrono.val_disp, relief=FLAT, font=("Helvetica", 26), fg="red")
        self.chrono.configure(bg=don.proprietes.couleur_fond)
        self.chrono.place(x=posX, y=posY, anchor=CENTER, width=70, height=32)

    def Set_triangle(self, nbLettres, don):

        x0 = don.geom.x0
        y0 = don.geom.y0
        dx = don.geom.dx
        dy = don.geom.dy
        var_dw = don.geom.var_dw
        var_dh = don.geom.var_dh
        for ii in range(0, nbLettres):
            self.triangle.append(Label(self.fen))
            self.triangle[ii].configure(relief=FLAT, font=("Helvetica", 32))
            self.triangle[ii].configure(bg=don.proprietes.couleur_fond)
        if nbLettres == 10:
            self.triangle[0].place(x=x0, y=y0, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[1].place(x=x0 - 0.5 * dx, y=y0 + dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[2].place(x=x0 + 0.5 * dx, y=y0 + dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[3].place(x=x0 - dx, y=y0 + 2 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[4].place(x=x0, y=y0 + 2 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[5].place(x=x0 + dx, y=y0 + 2 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[6].place(x=x0 - 1.5 * dx, y=y0 + 3 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[7].place(x=x0 - 0.5 * dx, y=y0 + 3 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[8].place(x=x0 + 0.5 * dx, y=y0 + 3 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[9].place(x=x0 + 1.5 * dx, y=y0 + 3 * dy, anchor=CENTER, width=var_dw, height=var_dh)
        if nbLettres == 11:
            self.triangle[0].place(x=x0 - 0.5 * dx, y=y0, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[1].place(x=x0 + 0.5 * dx, y=y0, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[2].place(x=x0 - 0.5 * dx, y=y0 + dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[3].place(x=x0 + 0.5 * dx, y=y0 + dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[4].place(x=x0 - dx, y=y0 + 2 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[5].place(x=x0, y=y0 + 2 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[6].place(x=x0 + dx, y=y0 + 2 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[7].place(x=x0 - 1.5 * dx, y=y0 + 3 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[8].place(x=x0 - 0.5 * dx, y=y0 + 3 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[9].place(x=x0 + 0.5 * dx, y=y0 + 3 * dy, anchor=CENTER, width=var_dw, height=var_dh)
            self.triangle[10].place(x=x0 + 1.5 * dx, y=y0 + 3 * dy, anchor=CENTER, width=var_dw, height=var_dh)

    def Set_boutons_tirage(self, tirage, motUtilisateur, nbLettres, don):

        for ii in range(0, nbLettres):
            b = Button(self.fen, text='', font=("Helvetica", 30), bg=don.proprietes.couleur_bg_defaut)
            self.boutons_reponse.append(b)
            self.boutons_reponse[ii].place(x=60 + 54 * ii, y=110, anchor=CENTER, width=50, height=50)

            b = Button(self.fen, text='', font=("Helvetica", 30), bg=don.proprietes.couleur_bg_defaut)
            self.boutons_tirage.append(b)
            self.boutons_tirage[ii].place(x=60 + 54 * ii, y=30, anchor=CENTER, width=50, height=50)
        for ii in range(0, nbLettres):
            self.boutons_tirage[ii].configure(command=lambda c=ii: motUtilisateur.AddLettre(tirage, c, self, don))

    def Set_boutons_tirage_chiffres(self, tirage, compteUtilisateur, don):
        # inclut à la fois le tirage et la solution donnée par l'utilisateur : plus simple à cause des plaques résultat
        #  qui sont réutilisées comme des plaques de tirage

        for ii in range(0, don.nbPlaquesChiffres):
            posX = ii % 3
            posY = (ii-posX)/3

            b = Button(self.fen, text='', font=("Helvetica", 34), bg=don.proprietes.couleur_bg_defaut)
            self.boutons_tirage.append(b)
            self.boutons_tirage[ii].place(x=50 + 90 * posX, y=40 + 70 * posY, anchor=CENTER, width=80, height=60)
            # self.boutons_tirage[ii].configure(command=lambda c=ii: motUtilisateur.AddChiffre(tirage, c, self, don))
        # ajout du total à trouver
        for ii in range(0, 3):
            b = Label(self.fen, text='', font=("Helvetica", 48))
            self.boutons_tirage.append(b)
            self.boutons_tirage[ii+don.nbPlaquesChiffres].place(x=50 + 70 * (3.7 + 0.55*ii),
                                                                y=40 + 70 * 0.5, anchor=CENTER)
            self.boutons_tirage[ii+don.nbPlaquesChiffres].configure(bg=don.proprietes.couleur_fond)
        # ajout des signes des opérations
        b = Button(self.fen, text='+', font=("Helvetica", 32), bg=don.proprietes.couleur_bg_defaut)
        b.configure(command=lambda c=len(self.boutons_tirage): compteUtilisateur.AddChiffre(tirage, c, self, don))
        self.boutons_tirage.append(b)
        self.boutons_tirage[-1].place(x=50 + 90 * 4.7, width=55, height=55,
                                      y=40 + 0.05*70, anchor=CENTER)
        b = Button(self.fen, text='-', font=("Helvetica", 32), bg=don.proprietes.couleur_bg_defaut)
        b.configure(command=lambda c=len(self.boutons_tirage): compteUtilisateur.AddChiffre(tirage, c, self, don))
        self.boutons_tirage.append(b)
        self.boutons_tirage[-1].place(x=50 + 90 * 5.5, width=55, height=55,
                                      y=40 + 0.05*70, anchor=CENTER)
        b = Button(self.fen, text='x', font=("Helvetica", 32), bg=don.proprietes.couleur_bg_defaut)
        b.configure(command=lambda c=len(self.boutons_tirage): compteUtilisateur.AddChiffre(tirage, c, self, don))
        self.boutons_tirage.append(b)
        self.boutons_tirage[-1].place(x=50 + 90 * 4.7, width=55, height=55,
                                      y=40 + 0.95*70, anchor=CENTER)
        b = Button(self.fen, text='/', font=("Helvetica", 32), bg=don.proprietes.couleur_bg_defaut)
        b.configure(command=lambda c=len(self.boutons_tirage): compteUtilisateur.AddChiffre(tirage, c, self, don))
        self.boutons_tirage.append(b)
        self.boutons_tirage[-1].place(x=50 + 90 * 5.5, width=55, height=55,
                                      y=40 + 0.95*70, anchor=CENTER)
        for ii in range(0, don.nbPlaquesChiffres):
            self.boutons_tirage[ii].configure(command=lambda c=ii: compteUtilisateur.AddChiffre(tirage, c, self, don))
        nb_plaques_tirage_reel = len(self.boutons_tirage)
        # ajout des opérations
        y0 = 190
        for ii in range(0, 5):
            b = Label(self.fen, text='', font=("Helvetica", 28))
            self.boutons_tirage.append(b)
            self.boutons_tirage[-1].place(x=50, y=y0 + 50 * ii, anchor=CENTER)
            self.boutons_tirage[-1].configure(bg=don.proprietes.couleur_fond)

            b = Label(self.fen, text='', font=("Helvetica", 28))
            self.boutons_tirage.append(b)
            self.boutons_tirage[-1].place(x=125, y=y0 + 50 * ii, anchor=CENTER)
            self.boutons_tirage[-1].configure(bg=don.proprietes.couleur_fond)

            b = Label(self.fen, text='', font=("Helvetica", 28))
            self.boutons_tirage.append(b)
            self.boutons_tirage[-1].place(x=200, y=y0 + 50 * ii, anchor=CENTER)
            self.boutons_tirage[-1].configure(bg=don.proprietes.couleur_fond)

            b = Label(self.fen, text='', font=("Helvetica", 28))
            self.boutons_tirage.append(b)
            self.boutons_tirage[-1].place(x=275, y=y0 + 50 * ii, anchor=CENTER)
            self.boutons_tirage[-1].configure(bg=don.proprietes.couleur_fond)

            b = Button(self.fen, text='', font=("Helvetica", 28))
            self.boutons_tirage.append(b)
            self.boutons_tirage[-1].place(x=360, y=y0 + 50 * ii, anchor=CENTER, width=110, height=50)
            self.boutons_tirage[-1].configure(
                command=lambda c=len(self.boutons_tirage)-1: compteUtilisateur.AddChiffre(tirage, c, self, don))
        self.boutons_tirage[-1].configure(command=[])

        # ajout d'une quatrième plaque pour le total à trouver
        b = Label(self.fen, text='', font=("Helvetica", 48))
        self.boutons_tirage.append(b)
        self.boutons_tirage[-1].place(x=50 + 70 * (3.7 + 0.55 * 3), y=40 + 70 * 0.5, anchor=CENTER)
        self.boutons_tirage[-1].configure(bg=don.proprietes.couleur_fond)

    def Set_score(self, don):

        taille_x = don.geom.taille_x
        cha = 'score : ' + str(don.score) + ' / ' + str(don.total)
        self.score.configure(text=cha,
                               font=("Helvetica", 20),
                               fg='blue', bg=don.proprietes.couleur_fond)
        self.score.place(x=0.62 * taille_x, y=250, anchor=CENTER)

    def Set_tops(self, don):

        taille_x = don.geom.taille_x
        cha = 'Tops : ' + str(don.nbTops) + ' / ' + str(don.nbTirages)
        self.tops.configure(text=cha,
                              font=("Helvetica", 20),
                              fg='blue', bg=don.proprietes.couleur_fond)
        self.tops.place(x=0.87 * taille_x, y=250, anchor=CENTER)

    def Set_bouton_top(self, tirage, don):

        taille_x = don.geom.taille_x
        # self.bouton_top.configure(text='top',
        #                           bg=don.proprietes.couleur_fond_boutons6,
        #                           font=("Helvetica", 20),
        #                           command=lambda: printTop(tirage, don, self))
        self.bouton_top.configure(text='top',
                                    bg=don.proprietes.couleur_bg_select,
                                    font=("Helvetica", 20))
        self.bouton_top.place(x=0.8 * taille_x - 65, y=300, anchor=CENTER, width=130, height=45)

    def Set_bouton_top_chiffres(self, tirage, don):
        taille_x = don.geom.taille_x
        # self.bouton_top.configure(text='top',
        #                             bg=don.proprietes.couleur_fond_boutons6,
        #                             font=("Helvetica", 20),
        #                             command=lambda: printTop_chiffres(tirage, don, self))
        self.bouton_top.configure(text='top',
                                  bg=don.proprietes.couleur_bg_select,
                                  font=("Helvetica", 20))
        self.bouton_top.place(x=0.8 * taille_x - 65, y=300, anchor=CENTER, width=130, height=45)

    def Set_bouton_effacer(self, tirage, motUtilisateur, don):

        taille_x = don.geom.taille_x
        # self.bouton_effacer.configure(text='effacer',
        #                                 bg=don.proprietes.couleur_fond_boutons6,
        #                                 font=("Helvetica", 20),
        #                                 command=lambda: motUtilisateur.DelLettre(tirage, self, don))
        self.bouton_effacer.configure(text='effacer',
                                        bg=don.proprietes.couleur_bg_select,
                                        font=("Helvetica", 20))
        self.bouton_effacer.place(x=0.6 * taille_x, y=350, anchor=CENTER, width=100, height=45)

    def Set_bouton_effacer_chiffres(self, tirage, motUtilisateur, don):

        taille_x = don.geom.taille_x
        # self.bouton_effacer.configure(text='effacer',
        #                                 bg=don.proprietes.couleur_fond_boutons6,
        #                                 font=("Helvetica", 20),
        #                                 command=lambda: motUtilisateur.DelChiffre(self, don))
        self.bouton_effacer.configure(text='effacer',
                                      bg=don.proprietes.couleur_bg_select,
                                      font=("Helvetica", 20))
        self.bouton_effacer.place(x=0.6 * taille_x, y=350, anchor=CENTER, width=100, height=45)

    def Set_bouton_raz(self, tirage, motUtilisateur, don):

        taille_x = don.geom.taille_x
        self.bouton_raz.configure(text='RAZ',
                                  font=("Helvetica", 20),
                                  bg=don.proprietes.couleur_bg_select)
        self.bouton_raz.place(x=0.6 * taille_x, y=400, anchor=CENTER, width=100, height=45)

    def Set_bouton_raz_chiffres(self, tirage, motUtilisateur, don):

        taille_x = don.geom.taille_x
        self.bouton_raz.configure(text='RAZ',
                                  font=("Helvetica", 20),
                                  bg=don.proprietes.couleur_bg_select)
        self.bouton_raz.place(x=0.6 * taille_x, y=400, anchor=CENTER, width=100, height=45)

    def Set_bouton_valider(self, tirage, motUtilisateur, don, chrono):

        taille_x = don.geom.taille_x
        self.bouton_valider.configure(text='valider',
                                      font=("Helvetica", 20),
                                      bg=don.proprietes.couleur_bg_select, borderwidth=4)
        self.bouton_valider.place(x=0.6 * taille_x, y=300, anchor=CENTER, width=100, height=45)

    def Set_bouton_valider_chiffres(self, tirage, motUtilisateur, don, chrono):

        taille_x = don.geom.taille_x
        self.bouton_valider.configure(text='valider',
                                      font=("Helvetica", 20),
                                      bg=don.proprietes.couleur_bg_select, borderwidth=4)
        self.bouton_valider.place(x=0.6 * taille_x, y=300, anchor=CENTER, width=100, height=45)

    def Set_bouton_solutions(self, tirage, don):

        taille_x = don.geom.taille_x
        # self.bouton_solutions.configure(text='solutions',
        #                                 font=("Helvetica", 20),
        #                                 bg=don.proprietes.couleur_fond_boutons6,
        #                                 command=lambda: solveur(tirage, don))
        self.bouton_solutions.configure(text='solutions',
                                      font=("Helvetica", 20),
                                      bg=don.proprietes.couleur_bg_select)
        self.bouton_solutions.place(x=0.8 * taille_x + 70, y=300, anchor=CENTER, width=120, height=45)

    def Set_bouton_solutions_chiffres(self, tirage, don):

        taille_x = don.geom.taille_x
        # self.bouton_solutions.configure(text='solutions',
        #                                 font=("Helvetica", 20),
        #                                 bg=don.proprietes.couleur_fond_boutons6,
        #                                 command=lambda: solveur_chiffres(tirage, don))
        self.bouton_solutions.configure(text='solutions',
                                      font=("Helvetica", 20),
                                      bg=don.proprietes.couleur_bg_select)
        self.bouton_solutions.place(x=0.8 * taille_x + 70, y=300, anchor=CENTER, width=120, height=45)

    def Set_bouton_next(self, tirage, motUtilisateur, don, chrono):

        taille_x = don.geom.taille_x
        self.bouton_next.configure(text='nouveau tirage',
                                 font=("Arial", 20),
                                 bg=don.proprietes.couleur_fond_boutons6,
                                 command=lambda: lancement_tirage_suivant(don, tirage, motUtilisateur,
                                                                          self, chrono))
        self.bouton_next.place(x=0.8 * taille_x + 0, y=350, anchor=CENTER, width=260, height=45)

    def Set_bouton_next_chiffres(self, tirage, motUtilisateur, don, chrono):

        taille_x = don.geom.taille_x
        self.bouton_next.configure(text='nouveau tirage',
                                 font=("Arial", 20),
                                 bg=don.proprietes.couleur_fond_boutons6,
                                 command=lambda: lancement_tirage_suivant_chiffres(don, tirage, motUtilisateur,
                                                                          self, chrono))
        self.bouton_next.place(x=0.8 * taille_x + 0, y=350, anchor=CENTER, width=260, height=45)

    def Set_bouton_changer_chiffres(self, tirage, motUtilisateur, don, chrono):
        # pour passer des chiffres aux lettres

        taille_x = don.geom.taille_x
        self.bouton_changer.configure(text='lettres',
                                 font=("Arial", 20),
                                 bg=don.proprietes.couleur_changer,
                                 command=lambda: self.Lancement_tirage_lettres2(tirage, don, chrono, motUtilisateur))
        self.bouton_changer.place(x=0.8 * taille_x + 0, y=400, anchor=CENTER, width=260, height=45)

    def Set_bouton_changer_lettres(self, tirage, motUtilisateur, don, chrono):
        # pour passer des lettres aux chiffres

        taille_x = don.geom.taille_x
        self.bouton_changer.configure(text='chiffres',
                                 font=("Arial", 20),
                                 bg=don.proprietes.couleur_changer,
                                 command=lambda: self.Lancement_tirage_chiffres2(tirage, don, chrono, motUtilisateur))
        self.bouton_changer.place(x=0.8 * taille_x + 0, y=400, anchor=CENTER, width=260, height=45)

    def Set_boutons_aleatoire(self, don):

        dy_voyelles = don.geom.dy_voyelles
        y_voyelles = don.geom.y_voyelles
        taille_x = don.geom.taille_x

        liste_aleatoire = ['aléatoire', 'préparé', 'manuel']
        variable_aleatoire = StringVar(self.fen)
        if don.prepare == 1:
            variable_aleatoire.set(liste_aleatoire[1])
        elif don.manuel == 1:
            variable_aleatoire.set(liste_aleatoire[2])
        else:
            variable_aleatoire.set(liste_aleatoire[0])
        self.bareme_chiffres.append(OptionMenu(self.fen, variable_aleatoire, *liste_aleatoire))
        self.bareme_chiffres[-1].configure(font=('Helvetica', 15))
        self.bareme_chiffres[-1].place(x=0.59 * taille_x, y=y_voyelles - 0.1 * dy_voyelles,
                                       anchor=CENTER, width=130, height=35)
        def callback_aleatoire(*args):
            if variable_aleatoire.get() == 'aléatoire':
                don.aleatoire = 1
                don.prepare = 0
                don.manuel = 0
            if variable_aleatoire.get() == 'manuel':
                don.aleatoire = 0
                don.prepare = 0
                don.manuel = 1
            if variable_aleatoire.get() == 'préparé':
                don.aleatoire = 0
                don.prepare = 1
                don.manuel = 0
        variable_aleatoire.trace("w", callback_aleatoire)

    def Set_boutons_sauvegarde(self, tirage, don):
        dy_voyelles = don.geom.dy_voyelles
        y_voyelles = don.geom.y_voyelles
        taille_x = don.geom.taille_x

        self.boutons_sauvegarde.configure(font=('Helvetica', 15), text='Sauvegarde',
                                           bg=don.proprietes.couleur_bg_select,
                                           command=lambda: tirage.sauvegarde(self, don))
        self.boutons_sauvegarde.place(x=0.59 * taille_x, y=y_voyelles + 1 * dy_voyelles,
                                       anchor=CENTER, width=130, height=35)



    def Set_boutons_nbVoyelles(self, tirage, don):

        dy_voyelles = don.geom.dy_voyelles
        y_voyelles = don.geom.y_voyelles
        taille_x = don.geom.taille_x
        self.boutons_nbVoyelles.append(Label(self.fen))
        self.boutons_nbVoyelles[0].configure(text='voyelles :',
                                               font=("Helvetica", 20), bg=don.proprietes.couleur_fond)
        self.boutons_nbVoyelles[0].place(x=0.82 * taille_x, y=y_voyelles + 0.5 * dy_voyelles, anchor=E)

        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='2',
                                                bg=don.proprietes.couleur_fond_nbVoy,
                                                font=("Helvetica", 20),
                                                command=lambda: don.SetSetNbVoy(2, self, 'fixe'))
        self.boutons_nbVoyelles[-1].place(x=0.84 * taille_x, y=y_voyelles, anchor=CENTER, width=34, height=34)
        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='3',
                                                bg=don.proprietes.couleur_fond_nbVoy,
                                                font=("Helvetica", 20),
                                                command=lambda: don.SetSetNbVoy(3, self, 'fixe'))
        self.boutons_nbVoyelles[-1].place(x=0.88 * taille_x, y=y_voyelles, anchor=CENTER, width=34, height=34)
        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='4',
                                                bg=don.proprietes.couleur_fond_nbVoy,
                                                font=("Helvetica", 20),
                                                command=lambda: don.SetSetNbVoy(4, self, 'fixe'))
        self.boutons_nbVoyelles[-1].place(x=0.92 * taille_x, y=y_voyelles, anchor=CENTER, width=34, height=34)
        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='5',
                                                bg=don.proprietes.couleur_fond_nbVoy,
                                                font=("Helvetica", 20),
                                                command=lambda: don.SetSetNbVoy(5, self, 'fixe'))
        self.boutons_nbVoyelles[-1].place(x=0.96 * taille_x, y=y_voyelles, anchor=CENTER, width=34, height=34)
        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='6',
                                                bg=don.proprietes.couleur_fond_nbVoy,
                                                font=("Helvetica", 20),
                                                command=lambda: don.SetSetNbVoy(6, self, 'fixe'))
        self.boutons_nbVoyelles[-1].place(x=0.84 * taille_x, y=y_voyelles + dy_voyelles, anchor=CENTER, width=34,
                                            height=34)
        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='7',
                                                bg=don.proprietes.couleur_fond_nbVoy,
                                                font=("Helvetica", 20),
                                                command=lambda: don.SetSetNbVoy(7, self, 'fixe'))
        self.boutons_nbVoyelles[-1].place(x=0.88 * taille_x, y=y_voyelles + dy_voyelles, anchor=CENTER, width=34,
                                            height=34)
        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='8',
                                                bg=don.proprietes.couleur_fond_nbVoy,
                                                font=("Helvetica", 20),
                                                command=lambda: don.SetSetNbVoy(8, self, 'fixe'))
        self.boutons_nbVoyelles[-1].place(x=0.92 * taille_x, y=y_voyelles + dy_voyelles, anchor=CENTER, width=34,
                                            height=34)
        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='?',
                                                bg=don.proprietes.couleur_nbVoy,
                                                font=("Helvetica", 20),
                                                command=lambda: don.SetSetNbVoy(314, self))
        self.boutons_nbVoyelles[-1].place(x=0.96 * taille_x, y=y_voyelles + dy_voyelles, anchor=CENTER, width=34,
                                            height=34)

    def Set_boutons_nbGrossesPlaques(self, tirage, don):

        dy_voyelles = don.geom.dy_voyelles
        y_voyelles = don.geom.y_voyelles
        taille_x = don.geom.taille_x
        self.boutons_nbVoyelles.append(Label(self.fen))
        self.boutons_nbVoyelles[0].configure(text='grosses\nplaques',
                                               font=("Helvetica", 20), bg=don.proprietes.couleur_fond)
        self.boutons_nbVoyelles[0].place(x=0.75 * taille_x, y=y_voyelles + 0.5 * dy_voyelles, anchor=CENTER)

        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='0',
                                                bg=don.proprietes.couleur_fond_nbVoy,
                                                font=("Helvetica", 20),
                                                command=lambda: self.Set_nb_grosses_plaques(0, don))
        self.boutons_nbVoyelles[-1].place(x=0.84 * taille_x, y=y_voyelles, anchor=CENTER, width=34, height=34)

        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='1',
                                              bg=don.proprietes.couleur_fond_nbVoy,
                                              font=("Helvetica", 20),
                                              command=lambda: self.Set_nb_grosses_plaques(1, don))
        self.boutons_nbVoyelles[-1].place(x=0.88 * taille_x, y=y_voyelles, anchor=CENTER, width=34, height=34)

        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='2',
                                              bg=don.proprietes.couleur_fond_nbVoy,
                                              font=("Helvetica", 20),
                                              command=lambda: self.Set_nb_grosses_plaques(2, don))
        self.boutons_nbVoyelles[-1].place(x=0.92 * taille_x, y=y_voyelles, anchor=CENTER, width=34, height=34)

        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='3',
                                              bg=don.proprietes.couleur_fond_nbVoy,
                                              font=("Helvetica", 20),
                                              command=lambda: self.Set_nb_grosses_plaques(3, don))
        self.boutons_nbVoyelles[-1].place(x=0.96 * taille_x, y=y_voyelles, anchor=CENTER, width=34, height=34)

        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='4',
                                              bg=don.proprietes.couleur_fond_nbVoy,
                                              font=("Helvetica", 20),
                                              command=lambda: self.Set_nb_grosses_plaques(4, don))
        self.boutons_nbVoyelles[-1].place(x=0.84 * taille_x, y=y_voyelles + dy_voyelles,
                                          anchor=CENTER, width=34, height=34)

        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='5',
                                              bg=don.proprietes.couleur_fond_nbVoy,
                                              font=("Helvetica", 20),
                                              command=lambda: self.Set_nb_grosses_plaques(5, don))
        self.boutons_nbVoyelles[-1].place(x=0.88 * taille_x, y=y_voyelles + dy_voyelles,
                                          anchor=CENTER, width=34, height=34)

        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='6',
                                              bg=don.proprietes.couleur_fond_nbVoy,
                                              font=("Helvetica", 20),
                                              command=lambda: self.Set_nb_grosses_plaques(6, don))
        self.boutons_nbVoyelles[-1].place(x=0.92 * taille_x, y=y_voyelles + dy_voyelles,
                                          anchor=CENTER, width=34, height=34)

        self.boutons_nbVoyelles.append(Button(self.fen))
        self.boutons_nbVoyelles[-1].configure(text='?',
                                              bg=don.proprietes.couleur_nbVoy,
                                              font=("Helvetica", 20),
                                              command=lambda: self.Set_nb_grosses_plaques(314, don))
        self.boutons_nbVoyelles[-1].place(x=0.96 * taille_x, y=y_voyelles + dy_voyelles,
                                          anchor=CENTER, width=34, height=34)

    def Set_nb_grosses_plaques(self, val, don):
        don.Set_nb_grosses_plaques(val)
        if val==314:
            idxBouton = 8
        else:
            idxBouton = val+1
        for ii in range(1,9):
            if ii == idxBouton:
                self.boutons_nbVoyelles[ii].configure(bg=don.proprietes.couleur_nbVoy)
            else:
                self.boutons_nbVoyelles[ii].configure(bg=don.proprietes.couleur_fond_nbVoy)

    def lancementRajouts(self, don):
        rajout = Rajout()
        Mafenetre = tk.Tk()
        Mafenetre.title('Rajouts')
        don.init_rajouts()

        def modif(don, idx):
            don.rajoutsActifs[idx-1] = 1-don.rajoutsActifs[idx-1]

        cha = str('700x220')
        Mafenetre.geometry(cha)
        self.labels_rajouts = []
        for ii in range(10):
            self.labels_rajouts.append(Label(Mafenetre))
            self.labels_rajouts[-1].place(x=50+ii*66, y=75, anchor=CENTER, width=60, height=60)
            self.labels_rajouts[-1].configure(bg='antiquewhite', font=("Helvetica", 36),
                                                  text='', borderwidth=0.5, relief="solid")
        bouton1 = Checkbutton(Mafenetre)
        var1 = tk.BooleanVar()
        var1.set(True)
        bouton1.place(x=140, y=160, anchor=CENTER)
        bouton1.configure(font=("Helvetica", 36), text='+1', variable=var1, command=lambda: modif(don,1))
        bouton1.select()

        bouton2 = Checkbutton(Mafenetre)
        var2 = tk.BooleanVar()
        var2.set(True)
        bouton2.place(x=350, y=160, anchor=CENTER)
        bouton2.configure(font=("Helvetica", 36), text='+2', variable=var2, command=lambda: modif(don,2))
        bouton2.select()

        bouton3 = Checkbutton(Mafenetre)
        var3 = tk.BooleanVar()
        var3.set(True)
        bouton3.place(x=560, y=160, anchor=CENTER)
        bouton3.configure(font=("Helvetica", 36), text='+3', variable=var3, command=lambda: modif(don, 3))

        def rajouts_addLettre(event):
            lettre_a_ajouter = event.char.upper()
            if len(rajout.base) < rajout.max_nbLettres:
                self.labels_rajouts[len(rajout.base)].configure(text=lettre_a_ajouter)
                rajout.base = rajout.base + lettre_a_ajouter

        def rajout_delLettre(event):
            if len(rajout.base):
                rajout.base = rajout.base[:-1]
                self.labels_rajouts[len(rajout.base)].configure(text='')

        def rajout_valide(event):
            if len(rajout.base):
                rajout.Cherche_solutions(don)

        Mafenetre.bind("<a>", rajouts_addLettre)
        Mafenetre.bind("<b>", rajouts_addLettre)
        Mafenetre.bind("<c>", rajouts_addLettre)
        Mafenetre.bind("<d>", rajouts_addLettre)
        Mafenetre.bind("<e>", rajouts_addLettre)
        Mafenetre.bind("<f>", rajouts_addLettre)
        Mafenetre.bind("<g>", rajouts_addLettre)
        Mafenetre.bind("<h>", rajouts_addLettre)
        Mafenetre.bind("<i>", rajouts_addLettre)
        Mafenetre.bind("<j>", rajouts_addLettre)
        Mafenetre.bind("<k>", rajouts_addLettre)
        Mafenetre.bind("<l>", rajouts_addLettre)
        Mafenetre.bind("<m>", rajouts_addLettre)
        Mafenetre.bind("<n>", rajouts_addLettre)
        Mafenetre.bind("<o>", rajouts_addLettre)
        Mafenetre.bind("<p>", rajouts_addLettre)
        Mafenetre.bind("<q>", rajouts_addLettre)
        Mafenetre.bind("<r>", rajouts_addLettre)
        Mafenetre.bind("<s>", rajouts_addLettre)
        Mafenetre.bind("<t>", rajouts_addLettre)
        Mafenetre.bind("<u>", rajouts_addLettre)
        Mafenetre.bind("<v>", rajouts_addLettre)
        Mafenetre.bind("<w>", rajouts_addLettre)
        Mafenetre.bind("<x>", rajouts_addLettre)
        Mafenetre.bind("<y>", rajouts_addLettre)
        Mafenetre.bind("<z>", rajouts_addLettre)
        Mafenetre.bind("<A>", rajouts_addLettre)
        Mafenetre.bind("<B>", rajouts_addLettre)
        Mafenetre.bind("<C>", rajouts_addLettre)
        Mafenetre.bind("<D>", rajouts_addLettre)
        Mafenetre.bind("<E>", rajouts_addLettre)
        Mafenetre.bind("<F>", rajouts_addLettre)
        Mafenetre.bind("<G>", rajouts_addLettre)
        Mafenetre.bind("<H>", rajouts_addLettre)
        Mafenetre.bind("<I>", rajouts_addLettre)
        Mafenetre.bind("<J>", rajouts_addLettre)
        Mafenetre.bind("<K>", rajouts_addLettre)
        Mafenetre.bind("<L>", rajouts_addLettre)
        Mafenetre.bind("<M>", rajouts_addLettre)
        Mafenetre.bind("<N>", rajouts_addLettre)
        Mafenetre.bind("<O>", rajouts_addLettre)
        Mafenetre.bind("<P>", rajouts_addLettre)
        Mafenetre.bind("<Q>", rajouts_addLettre)
        Mafenetre.bind("<R>", rajouts_addLettre)
        Mafenetre.bind("<S>", rajouts_addLettre)
        Mafenetre.bind("<T>", rajouts_addLettre)
        Mafenetre.bind("<U>", rajouts_addLettre)
        Mafenetre.bind("<V>", rajouts_addLettre)
        Mafenetre.bind("<W>", rajouts_addLettre)
        Mafenetre.bind("<X>", rajouts_addLettre)
        Mafenetre.bind("<Y>", rajouts_addLettre)
        Mafenetre.bind("<Z>", rajouts_addLettre)
        Mafenetre.bind("<BackSpace>", rajout_delLettre)
        Mafenetre.bind("<Return>", rajout_valide)

        Mafenetre.mainloop()



def Lancement_tirage_lettres(icones, tirage, don, chrono, motUtilisateur):
    nbLettres = don.nbLettres
    icones.Del_boutons_lancement()
    icones.Set_boutons_lettres(tirage, self.fen, don, chrono)
    icones.Set_chrono(chrono, don)
    icones.Set_triangle(nbLettres, don)
    icones.Set_boutons_tirage(tirage, motUtilisateur, nbLettres)
    icones.Set_score(don)
    icones.Set_tops(don)
    icones.Set_bouton_top(tirage, don)
    icones.Set_bouton_effacer(tirage, motUtilisateur, don)
    icones.Set_bouton_raz(tirage, motUtilisateur, don)
    icones.Set_bouton_valider(tirage, motUtilisateur, don, chrono)
    icones.Set_bouton_solutions(tirage, don)
    icones.Set_bouton_next(tirage, motUtilisateur, don, chrono)
    icones.Set_boutons_aleatoire(don)
    icones.Set_boutons_nbVoyelles(tirage, don)

def lancement_tirage_suivant(don, tirage, motUtilisateur, icones, chrono):

    # activation des boutons s'ils ne l'étaient pas déjà auparavant
    icones.bouton_valider.configure(bg=don.proprietes.couleur_fond_boutons6, borderwidth=4,
                     command=lambda: motUtilisateur.ValideReponse(tirage, don, icones, chrono))
    icones.bouton_raz.configure(bg=don.proprietes.couleur_fond_boutons6,
                              command=lambda: motUtilisateur.DelLettreRAZ(icones, don))
    icones.bouton_effacer.configure(bg=don.proprietes.couleur_fond_boutons6,
                                  command=lambda: motUtilisateur.DelLettre(tirage, icones, don))
    icones.bouton_solutions.configure(bg=don.proprietes.couleur_fond_boutons6,
                                    command=lambda: solveur(tirage, don))
    icones.bouton_top.configure(bg=don.proprietes.couleur_fond_boutons6,
                              command=lambda: printTop(tirage, don, icones))
    liste_lettres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.'
    for ii in range(0, len(liste_lettres)):
        icones.boutons_lettres[ii].configure(bg=don.proprietes.couleur_fond_lettres,
                                           command=lambda c=ii: icones.AddLettre(tirage, liste_lettres[c]))
    icones.boutons_lettres[-2].configure(bg=don.proprietes.couleur_fond_lettres,
                                       command=lambda: icones.DelLettre(tirage))

    # bouton valider
    icones.boutons_lettres[-1].configure(bg=don.proprietes.couleur_fond_lettres,
                                        command=lambda: icones.ValideTirage(tirage, chrono))


    # remise à zéro de la proposition
    motUtilisateur.Reset()
    motUtilisateur.possible_de_valider = 1
    chrono.reset_lettres()
    icones.chrono.configure(text='')
    if not don.prepare:
        icones.boutons_sauvegarde.configure(bg=don.proprietes.couleur_bg_defaut)
    tirage.valide = 0

    # remise à zéro
    for ii in range(0, len(icones.boutons_tirage)):
        icones.boutons_tirage[ii].configure(text='')
        icones.boutons_reponse[ii].configure(text='')
        icones.triangle[ii].configure(text='')
        icones.triangle[ii].configure(fg='black')
        icones.boutons_tirage[ii].configure(bg=don.proprietes.couleur_bg_defaut)
        icones.boutons_reponse[ii].configure(bg=don.proprietes.couleur_bg_defaut)
    for ii in range(1, len(icones.boutons_nbVoyelles)):
        icones.boutons_nbVoyelles[ii].configure(bg=don.proprietes.couleur_fond_nbVoy)
    icones.bouton_top.configure(text='top')

    # affichage du nouveau tirage
    if don.aleatoire or don.prepare:
        don.SetNbVoy(don.nbVoy)
        if don.nbVoyAleatoire:
            icones.boutons_nbVoyelles[-1].configure(bg=don.proprietes.couleur_nbVoy)
        icones.boutons_nbVoyelles[don.nbVoy-1].configure(bg=don.proprietes.couleur_nbVoy)
        if don.aleatoire:
            tirage.Genere(don)
        else: # tirage préparé
            icones.boutons_sauvegarde.configure(bg=don.proprietes.couleur_bg_select)
            tirage.Genere_prepa_lettres(don)
        for ii in range(0, len(icones.boutons_tirage)):
            icones.boutons_tirage[ii].configure(text=tirage.tirage[ii])
            icones.triangle[ii].configure(text=tirage.tirage[ii])
            if don.son_actif:
                time.sleep(1.2)
            time.sleep(don.tempo)
            icones.boutons_tirage[ii].update()
            if don.son_actif:
                pygame.mixer.init()
                cha = 'sons/' + tirage.tirage[ii].upper() + '.mp3'
                pygame.mixer.music.load(cha)
                pygame.mixer.music.play()
        chrono.actif = 1
        chrono.val_actuelle += 1
        icones.chrono.configure(text=chrono.val_actuelle)
        if don.son_actif:
            time.sleep(1.5)
            pygame.mixer.music.load('sons/DEBCHRON.mp3')
            pygame.mixer.music.play()
        time.sleep(don.tempo)
        tirage.valide = 1
    elif don.manuel:
        tirage.Reinit()

def lancement_tirage_suivant_chiffres(don, tirage, motUtilisateur, icones, chrono):
    # activation des boutons s'ils ne l'étaient pas déjà auparavant
    icones.bouton_valider.configure(bg=don.proprietes.couleur_fond_boutons6,
                                  command=lambda: motUtilisateur.ValideReponse_chiffres(tirage, don, icones, chrono))
    icones.bouton_raz.configure(bg=don.proprietes.couleur_fond_boutons6,
                              command=lambda: motUtilisateur.DelChiffreRAZ(icones, don))
    icones.bouton_effacer.configure(bg=don.proprietes.couleur_fond_boutons6,
                                  command=lambda: motUtilisateur.DelChiffre(icones, don))
    icones.bouton_solutions.configure(bg=don.proprietes.couleur_fond_boutons6,
                                    command=lambda: solveur_chiffres(tirage, don))
    icones.bouton_top.configure(bg=don.proprietes.couleur_fond_boutons6,
                              command=lambda: printTop_chiffres(tirage, don, icones))
    # activations des plaques chiffres en haut à droite
    liste_chiffres = sorted(set(don.listeChiffres))
    while len(liste_chiffres)<15:
        liste_chiffres.append(0)
    # liste_chiffres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100, 42]
    for ii in range(0, max(15, len(liste_chiffres))):
        icones.boutons_chiffres[ii].configure(bg=don.proprietes.couleur_fond_lettres,
                                            command=lambda c=ii: icones.AddChiffre(tirage, liste_chiffres[c]))
    # bouton annuler
    icones.boutons_chiffres[-2].configure(bg=don.proprietes.couleur_fond_lettres,
                                          command=lambda: icones.DelChiffre(tirage))
    # bouton valider
    icones.boutons_chiffres[-1].configure(bg=don.proprietes.couleur_fond_lettres,
                                        command=lambda: icones.ValideTirage_chiffres(tirage, chrono, don))


    # RAZ de la proposition de l'utilisateur
    motUtilisateur.DelChiffreRAZ(icones, don)
    motUtilisateur.possible_de_valider = 1
    motUtilisateur.proposition = []
    icones.position_actuelle_chiffres = 13
    icones.bouton_top.configure(text='top')
    if not don.prepare:
        icones.boutons_sauvegarde.configure(bg=don.proprietes.couleur_bg_defaut)
    chrono.reset_chiffres()
    icones.chrono.configure(text='')
    tirage.valide = 0
    # remise à zéro
    for ii in range(0, len(icones.boutons_tirage)):
        if ii not in [9,10,11,12]:
            icones.boutons_tirage[ii].configure(text='')
            icones.boutons_tirage[ii].configure(bg=don.proprietes.couleur_bg_defaut)
        # on met le fond en blanc lors du lancement du tirage (pendant que les plaques sont enoncees)
        if ii in [6,7,8,38,13,14,15,16,18,19,20,21,23,24,25,26,28,29,30,31,33,34,35,36]:
            icones.boutons_tirage[ii].configure(bg=don.proprietes.couleur_fond)
    # lancement du nouveau tirage
    if don.aleatoire or don.prepare:
        if don.aleatoire:
            tirage.Genere_chiffres(don)
        else: # tirage préparé
            icones.boutons_sauvegarde.configure(bg=don.proprietes.couleur_bg_select)
            tirage.Genere_prepa_chiffres(don)
        # +++ mise à jour des icônes
        for ii in range(0,len(tirage.tirage_chiffres)-1):
            icones.boutons_tirage[ii].configure(text=str(tirage.tirage_chiffres[ii]))
            icones.boutons_tirage[ii].update()

            if don.son_actif:
                pygame.mixer.init()
                if tirage.tirage_chiffres[ii] in [1,2,3,4,5,6,7,8,9,10,25,50,75,100]:
                    cha = 'sons/' + str(tirage.tirage_chiffres[ii]) + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                else: # cas d'une plaque exotique
                    num_str = str(tirage.tirage_chiffres[ii])
                    if len(num_str)<4:
                        if len(num_str) == 3:
                            centaines = num_str[0]
                        else:
                            centaines = []
                            reste = num_str
                        if centaines == '1':
                            cha = 'sons/100.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.5)
                        elif centaines in ['23456789']:
                            cha = 'sons/' + centaines + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.5)
                            cha = 'sons/100.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.8)
                        if int(reste) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                          25,
                                          30, 31,
                                          40, 41, 50, 51,
                                          60, 61, 70, 71, 75, 80, 81, 91]:
                            cha = 'sons/' + str(int(reste)) + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                        elif reste[0] == '2':
                            cha = 'sons/20.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.7)
                            cha = 'sons/' + reste[1] + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                        elif reste[0] == '3':
                            cha = 'sons/30.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.7)
                            cha = 'sons/' + reste[1] + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                        elif reste[0] == '4':
                            cha = 'sons/40.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.7)
                            cha = 'sons/' + reste[1] + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                        elif reste[0] == '5':
                            cha = 'sons/50.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.7)
                            cha = 'sons/' + reste[1] + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                        elif reste[0] == '6':
                            cha = 'sons/60.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.7)
                            cha = 'sons/' + reste[1] + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                        elif reste[0] == '7':
                            cha = 'sons/60.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.7)
                            cha = 'sons/' + str(10 + int(reste[1])) + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                        elif reste[0] == '8':
                            cha = 'sons/80.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.7)
                            cha = 'sons/' + reste[1] + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                        elif reste[0] == '9':
                            cha = 'sons/80.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                            time.sleep(0.7)
                            cha = 'sons/' + str(10 + int(reste[1])) + '.mp3'
                            pygame.mixer.music.load(cha)
                            pygame.mixer.music.play()
                time.sleep(1.1)
            time.sleep(don.tempo)

        total_a_trouver_str = str(tirage.tirage_chiffres[-1])
        propr = Proprietes()
        # possibilité d'aller au-delà de 999 avec icones.boutons_tirage[38] pour le chiffre des unités
        if len(total_a_trouver_str) == 4:
            icones.boutons_tirage[don.nbPlaquesChiffres].configure(text=total_a_trouver_str[0], bg=propr.couleur_fond)
            icones.boutons_tirage[don.nbPlaquesChiffres].update()
            icones.boutons_tirage[don.nbPlaquesChiffres+1].configure(text=total_a_trouver_str[1], bg=propr.couleur_fond)
            icones.boutons_tirage[don.nbPlaquesChiffres+1].update()
            icones.boutons_tirage[don.nbPlaquesChiffres+2].configure(text=total_a_trouver_str[2], bg=propr.couleur_fond)
            icones.boutons_tirage[don.nbPlaquesChiffres+2].update()
            icones.boutons_tirage[38].configure(text=total_a_trouver_str[3], bg=propr.couleur_fond)
            icones.boutons_tirage[38].update()
            milliers = total_a_trouver_str[0]
            if don.son_actif:
                if milliers in '23456789':
                    cha = 'sons/' + milliers + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.5)
                cha = 'sons/1000.mp3'
                pygame.mixer.music.load(cha)
                pygame.mixer.music.play()
                time.sleep(0.5)
            centaines = total_a_trouver_str[1]
            if don.son_actif:
                if centaines == '1':
                    cha = 'sons/100.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.5)
                elif centaines in '23456789':
                    cha = 'sons/' + centaines + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.5)
                    cha = 'sons/100.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.8)
                reste = total_a_trouver_str[2:]
                if int(reste) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 30,
                                  31,
                                  40, 41, 50, 51,
                                  60, 61, 70, 71, 75, 80, 81, 91]:
                    cha = 'sons/' + str(int(reste)) + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '2':
                    cha = 'sons/20.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '3':
                    cha = 'sons/30.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '4':
                    cha = 'sons/40.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '5':
                    cha = 'sons/50.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '6':
                    cha = 'sons/60.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '7':
                    cha = 'sons/60.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + str(10 + int(reste[1])) + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '8':
                    cha = 'sons/80.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '9':
                    cha = 'sons/80.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + str(10 + int(reste[1])) + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()

        elif len(total_a_trouver_str) == 3:
            for ii in range(0, len(total_a_trouver_str)):
                icones.boutons_tirage[don.nbPlaquesChiffres + ii].configure(text=total_a_trouver_str[ii],
                                                                            bg=propr.couleur_fond)
                icones.boutons_tirage[ii].update()
            centaines = total_a_trouver_str[0]
            if don.son_actif:
                if centaines == '1':
                    cha = 'sons/100.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.5)
                else:
                    cha = 'sons/' + centaines + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.5)
                    cha = 'sons/100.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.8)
                reste = total_a_trouver_str[1:]
                if int(reste) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 30,
                                  31,
                                  40, 41, 50, 51,
                                  60, 61, 70, 71, 75, 80, 81, 91]:
                    cha = 'sons/' + str(int(reste)) + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '2':
                    cha = 'sons/20.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '3':
                    cha = 'sons/30.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '4':
                    cha = 'sons/40.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '5':
                    cha = 'sons/50.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '6':
                    cha = 'sons/60.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '7':
                    cha = 'sons/60.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + str(10 + int(reste[1])) + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '8':
                    cha = 'sons/80.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + reste[1] + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                elif reste[0] == '9':
                    cha = 'sons/80.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()
                    time.sleep(0.7)
                    cha = 'sons/' + str(10 + int(reste[1])) + '.mp3'
                    pygame.mixer.music.load(cha)
                    pygame.mixer.music.play()

        chrono.actif = 1
        chrono.val_actuelle += 1
        time.sleep(don.tempo)
        icones.chrono.configure(text=chrono.val_actuelle)
        if don.son_actif:
            time.sleep(1)
            pygame.mixer.music.load('sons/DEBCHRON.mp3')
            pygame.mixer.music.play()
    elif don.manuel:
        tirage.Reinit()



def printTop(tirage, don, icones):
    if len(tirage.sol_complet) == 0:
        tirage.Solveur(don)
    cha = 'top : ' + str(tirage.top) + ' L'
    icones.bouton_top.configure(text=cha)

def printTop_chiffres(tirage, don, icones):
    if len(tirage.sol_complet) == 0:
        tirage.Solveur_chiffres(don)
    meilleure_solution = eval(tirage.sol_basique[0])
    cible = tirage.tirage_chiffres[-1]
    if meilleure_solution == cible:
        cha = 'top : CB'
    else:
        cha = 'top : ± ' + str(abs(cible-meilleure_solution))
    icones.bouton_top.configure(text=cha)

def solveur(tirage, don):
    if len(tirage.sol_complet) == 0:
        tirage.Solveur(don)
    tirage.Affiche_solutions()

def solveur_chiffres(tirage, don):
    if len(tirage.sol_complet) == 0:
        tirage.Solveur_chiffres(don)
    tirage.Affiche_solutions_chiffres(don)

def select_aleatoire(don):
    don.aleatoire = 1 - don.aleatoire



class Rajout:
    def __init__(self):
        self.base = ''
        self.max_nbLettres = 10
        self.base_min = ''
        self.solution_rajout1 = []
        self.lettre_rajout1 = []
        self.def_rajout1 = []

    def Get_base_min(self):
        self.base_min = ordreAlpha(self.base.lower())

    # RAJOUTS
    def Cherche_solutions(self,don):
        def rajout_FoncF2(event):
            root_rajouts_f2 = tk.Tk()
            root_rajouts_f2.title('Définitions')
            S_f2 = tk.Scrollbar(root_rajouts_f2)
            T_f2 = tk.Text(root_rajouts_f2, height=20, width=80, font=(don.police_solution, don.taille_solution))
            S_f2.pack(side=tk.RIGHT, fill=tk.Y)
            T_f2.pack(side=tk.LEFT, fill=tk.Y)
            S_f2.config(command=T_f2.yview)
            T_f2.config(yscrollcommand=S_f2.set)
            quote_f2 = cha2
            T_f2.insert(tk.END, quote_f2)
            tk.mainloop()

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.Get_base_min()
        tirages1 = []
        longueur_base = len(self.base)

        if don.rajoutsActifs[0]:
            for ll in alphabet:
                tirages1.append(ordreAlpha(self.base_min + ll))

            # rajouts +1
            dico1 = don.dico[longueur_base - 1]
            listeIdx = []
            for possible in tirages1:
                listeIdx1 = []
                for ii in range(len(dico1.alpha)):
                    if dico1.alpha[ii] == possible:
                        listeIdx1.append(ii)
                listeIdx.append(listeIdx1)

            # récupération des mots (basiques et complets) et des définitions
            sol_basique1 = []
            sol_complet1 = []
            sol_def1 = []
            for ii in range(len(listeIdx)):
                bt = []  # basique temporaire
                ct = []
                dt = []
                if len(listeIdx[ii]):
                    for jj in range(len(listeIdx[ii])):
                        bt.append(dico1.basique[listeIdx[ii][jj]])
                        ct.append(dico1.complet[listeIdx[ii][jj]])
                        dt.append(dico1.definitions[listeIdx[ii][jj]])
                sol_basique1.append(bt)
                sol_complet1.append(ct)
                sol_def1.append(dt)


        # rajouts +2
        if don.rajoutsActifs[1]:
            if longueur_base < 10:
                tirages2 = []
                rajout2 = []
                dico2 = don.dico[longueur_base]
                for ll1 in range(0, len(alphabet)):
                    for ll2 in range(ll1, len(alphabet)):
                        tirages2.append(ordreAlpha(self.base_min + alphabet[ll1] + alphabet[ll2]))
                        rajout2.append(alphabet[ll1].upper() + alphabet[ll2].upper())

                listeIdx2 = []
                for possible in tirages2:
                    listeIdx21 = []
                    for ii in range(len(dico2.alpha)):
                        if dico2.alpha[ii] == possible:
                            listeIdx21.append(ii)
                    listeIdx2.append(listeIdx21)
                sol_basique2 = []
                sol_complet2 = []
                sol_def2 = []
                for ii in range(len(listeIdx2)):
                    bt = []  # basique temporaire
                    ct = []
                    dt = []
                    if len(listeIdx2[ii]):
                        for jj in range(len(listeIdx2[ii])):
                            bt.append(dico2.basique[listeIdx2[ii][jj]])
                            ct.append(dico2.complet[listeIdx2[ii][jj]])
                            dt.append(dico2.definitions[listeIdx2[ii][jj]])
                    sol_basique2.append(bt)
                    sol_complet2.append(ct)
                    sol_def2.append(dt)

        # rajouts +2
        if don.rajoutsActifs[2]:
            if longueur_base < 9:
                tirages3 = []
                rajout3 = []
                dico3 = don.dico[longueur_base+1]
                for ll1 in range(0, len(alphabet)):
                    for ll2 in range(ll1, len(alphabet)):
                        for ll3 in range(ll2, len(alphabet)):
                            tirages3.append(ordreAlpha(self.base_min + alphabet[ll1] + alphabet[ll2] + alphabet[ll3]))
                            rajout3.append(alphabet[ll1].upper() + alphabet[ll2].upper() + alphabet[ll3].upper())

                listeIdx3 = []
                for possible in tirages3:
                    listeIdx31 = []
                    for ii in range(len(dico3.alpha)):
                        if dico3.alpha[ii] == possible:
                            listeIdx31.append(ii)
                    listeIdx3.append(listeIdx31)
                sol_basique3 = []
                sol_complet3 = []
                sol_def3 = []
                for ii in range(len(listeIdx3)):
                    bt = []  # basique temporaire
                    ct = []
                    dt = []
                    if len(listeIdx3[ii]):
                        for jj in range(len(listeIdx3[ii])):
                            bt.append(dico3.basique[listeIdx3[ii][jj]])
                            ct.append(dico3.complet[listeIdx3[ii][jj]])
                            dt.append(dico3.definitions[listeIdx3[ii][jj]])
                    sol_basique3.append(bt)
                    sol_complet3.append(ct)
                    sol_def3.append(dt)




        #-----------------------------
        # rajouter une mise dans l'ordre alpha ?
        #-----------------------------

        cha = '' # solutions
        cha2 = '' # définitions
        if don.rajoutsActifs[0]:
            for ii in range(len(sol_complet1)):
                if len(sol_complet1[ii]):
                    cha = cha + self.base + ' + ' + alphabet[ii].upper() + ' : '
                    for jj in range(len(sol_complet1[ii])):
                        if len(sol_def1[ii][jj]):
                            cha2 = cha2 + self.base + ' + ' + alphabet[ii].upper() + ' : ' + \
                                   sol_complet1[ii][jj] + ' : ' + \
                                   sol_def1[ii][jj] + '\n'
                        cha = cha + sol_complet1[ii][jj]
                        if jj < len(sol_complet1[ii]) - 1:
                            cha = cha + ', '
                    cha = cha + '\n'
            cha = cha + '\n'

        if don.rajoutsActifs[1] and longueur_base < 10:
            for ii in range(len(sol_complet2)):
                if len(sol_complet2[ii]):
                    cha = cha + self.base + ' + ' + rajout2[ii].upper() + ' : '
                    for jj in range(len(sol_complet2[ii])):
                        if len(sol_def2[ii][jj]):
                            cha2 = cha2 + self.base + ' + ' + rajout2[ii].upper() + ' : ' + \
                                   sol_complet2[ii][jj] + ' : ' + \
                                   sol_def2[ii][jj] + '\n'
                        cha = cha + sol_complet2[ii][jj]
                        if jj < len(sol_complet2[ii]) - 1:
                            cha = cha + ', '
                    cha = cha + '\n'
            cha = cha + '\n'

        if don.rajoutsActifs[2] and longueur_base < 9:
            for ii in range(len(sol_complet3)):
                if len(sol_complet3[ii]):
                    cha = cha + self.base + ' + ' + rajout3[ii].upper() + ' : '
                    for jj in range(len(sol_complet3[ii])):
                        if len(sol_def3[ii][jj]):
                            cha2 = cha2 + self.base + ' + ' + rajout3[ii].upper() + ' : ' + \
                                   sol_complet3[ii][jj] + ' : ' + \
                                   sol_def3[ii][jj] + '\n'
                        cha = cha + sol_complet3[ii][jj]
                        if jj < len(sol_complet3[ii]) - 1:
                            cha = cha + ', '
                    cha = cha + '\n'

        root = tk.Tk()
        root.title('Solutions')
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=20, width=80, font=('consolas', 20))
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = cha
        T.insert(tk.END, quote)
        root.bind("<F2>", rajout_FoncF2)
        tk.mainloop()


