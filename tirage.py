from loadConsVoy import *
from affichage import *
import tkinter as tk
import time
from random import *
import tkinter.font as tkFont
import pygame
from icones import *
from motUtilisateur import *
from data import *
from classe import *

class Tirage:
    def __init__(self, don):
        self.type = "lettre"
        self.tirage = ''
        self.tirageMin = ''
        self.nbLettres = don.nbLettres
        self.sol_basique = []
        self.sol_complet = []
        self.sol_definitions = []
        self.top = 0
        self.tirage_chiffres = []
        self.objectif_chiffres = []
        self.nbChiffres = don.nbPlaquesChiffres
        self.tirage_etendu = []
        self.liste_possibles_chiffres = []
        self.valide = 0
        self.tirages_prepares_lettres = lecture_tirages_prepares('lettres', don.fichier_prepa_l)
        self.tirages_prepares_chiffres = lecture_tirages_prepares('chiffres', don.fichier_prepa_c)

    def Reinit(self):
        self.sol_basique = []
        self.sol_complet = []
        self.sol_definitions = []
        self.tirage_chiffres = []
        self.objectif_chiffres = []
        self.tirage = ''
        self.tirageMin = ''
        self.liste_possibles_chiffres = []
        self.liste_approches = []
        self.valide = 0

    def AddLettre(self, lettre):
        if len(self.tirage) < self.nbLettres:
            self.tirage = self.tirage + lettre.upper()
            self.tirageMin = self.tirageMin + lettre.lower()

    def AddChiffre(self, chiffre):
        if len(self.tirage_chiffres) < self.nbChiffres:
            self.tirage_chiffres.append(int(chiffre))

    def DelLettre(self):
        if len(self.tirage) > 0:
            self.tirage = self.tirage[:-1]
            self.tirageMin = self.tirageMin[:-1]

    def DelChiffre(self):
        if len(self.tirage_chiffres) > 0:
            self.tirage_chiffres = self.tirage_chiffres[:-1]

    def Genere(self, don, *args):
        self.tirage = []
        self.tirageMin = []
        self.nbLettres = don.nbLettres
        self.sol_basique = []
        self.sol_complet = []
        self.sol_definitions = []
        if len(args) == 0:
            self.tirage = genereTirageLettres(don.nbLettres, don.nbVoy, don.listeCons, don.listeVoy)
            self.tirageMin = self.tirage.lower()
            # mise dans l'ordre alphabétique, sinon les combinaisons de lettres ne correspondent pas à celles,
            # ordonnées, du dico
            self.tirageMin = ordreAlpha(self.tirage.lower())
            self.valide = 1
        # le tirage est imposé
        elif len(args) == 1:
            self.tirage = args[0]
            self.nbLettres = len(args[0])
            self.tirageMin = self.tirage.lower()
            self.tirageMin = ordreAlpha(self.tirage.lower())

    def Genere_prepa_lettres(self, don):
        self.tirage = []
        self.tirageMin = []
        self.nbLettres = don.nbLettres
        self.sol_basique = []
        self.sol_complet = []
        self.sol_definitions = []

        self.tirage = genereTiragePrepaLettres(self.tirages_prepares_lettres).strip()
        self.tirageMin = self.tirage.lower()
        # mise dans l'ordre alphabétique, sinon les combinaisons de lettres ne correspondent pas à celles,
        # ordonnées, du dico
        self.tirageMin = ordreAlpha(self.tirage.lower())
        self.valide = 1

    def ajuste_tirage_prepares(self, don):
        new_l = []
        new_c = []
        if len(self.tirages_prepares_lettres):
            for ii in self.tirages_prepares_lettres:
                if len(ii)==don.nbLettres+1:
                    new_l.append(ii)
        if len(self.tirages_prepares_chiffres):
            for ii in self.tirages_prepares_chiffres:
                decoupe = ii.split(' ')
                if len(decoupe) == don.nbPlaquesChiffres+1:
                    if int(decoupe[-1]) <= don.borneMax and int(decoupe[-1]) >= don.borneMin:
                        new_c.append(ii)
        self.tirages_prepares_lettres = new_l
        self.tirages_prepares_chiffres = new_c


    def Genere_chiffres(self, don, *args):
        # appelée par lancement_tirage_suivant_chiffres (icones.py)
        self.tirage_chiffres = []
        self.sol_basique = []
        self.sol_complet = []
        self.liste_possibles_chiffres = []
        self.liste_approches = []
        if len(args) == 0:
            self.tirage_chiffres = genereTirageChiffres(don.nbPlaquesChiffres, don.listeChiffres,
                                               don.borneMin, don.borneMax, don.nb_grosses_plaques)
           # self.tirage_etendu = self.tirage_chiffres[:-1]
        # le tirage est imposé
        elif len(args) == 1:
            self.tirage_chiffres = args[0]
           # self.tirage_etendu = self.tirage_chiffres[:-1]

    def Genere_prepa_chiffres(self, don):
        # appelée par lancement_tirage_suivant_chiffres (icones.py)
        self.tirage_chiffres = []
        self.sol_basique = []
        self.sol_complet = []
        self.liste_possibles_chiffres = []
        self.liste_approches = []

        if len(self.tirages_prepares_chiffres):
            self.tirage_chiffres = genereTiragePrepaChiffres(self.tirages_prepares_chiffres)
        else:
            self.tirage_chiffres = genereTirageChiffres(don.nbPlaquesChiffres, don.listeChiffres,
                                                        don.borneMin, don.borneMax, don.nb_grosses_plaques)

    def GenereFin(self):
        self.tirageMin = self.tirage.lower()
        while len(self.tirage)<self.nbLettres:
            self.tirage = self.tirage + '.'
            self.tirageMin = self.tirageMin + '.'
        self.valide = 1

    def GenereFin_chiffres(self, don):
        if len(self.tirage_chiffres) < don.nbPlaquesChiffres:
            nbPlaques_reste = don.nbPlaquesChiffres - len(self.tirage_chiffres)
            finTirage = genereTirageChiffres(nbPlaques_reste,
                                             don.listeChiffres,
                                             don.borneMin, don.borneMax)
            for ii in range(0,len(finTirage)):
                self.tirage_chiffres.append(finTirage[ii])
        elif len(self.objectif_chiffres) == len(str(don.borneMax)):
            if len(str(don.borneMax))==3:
                cible = 100 * int(self.objectif_chiffres[0]) + 10 * int(self.objectif_chiffres[1]) \
                        + int(self.objectif_chiffres[2])
            else:
                cible = 1000 * int(self.objectif_chiffres[0]) + 100 * int(self.objectif_chiffres[1]) \
                        + 10 * int(self.objectif_chiffres[2]) + int(self.objectif_chiffres[3])
            self.tirage_chiffres.append(cible)
        elif len(self.objectif_chiffres) == 0:
            finTirage = genereTirageChiffres(1, don.listeChiffres,
                                             don.borneMin, don.borneMax)
            self.tirage_chiffres.append(finTirage[-1])
        elif len(self.objectif_chiffres) == 1:
            if len(str(don.borneMax)) == 3:
                finTirage = genereTirageChiffres(1, don.listeChiffres, 1, 99)
                cible = 100 * int(self.objectif_chiffres[0]) + finTirage[-1]
                self.tirage_chiffres.append(cible)
            elif len(str(don.borneMax)) == 4:
                finTirage = genereTirageChiffres(1, don.listeChiffres, 1, 999)
                cible = 1000 * int(self.objectif_chiffres[0]) + finTirage[-1]
                self.tirage_chiffres.append(cible)
        elif len(self.objectif_chiffres) == 2:
            if len(str(don.borneMax)) == 3:
                finTirage = genereTirageChiffres(1, don.listeChiffres, 1, 9)
                cible = 100 * int(self.objectif_chiffres[0]) + 10 * int(self.objectif_chiffres[1]) + finTirage[-1]
                self.tirage_chiffres.append(cible)
            elif len(str(don.borneMax)) == 4:
                finTirage = genereTirageChiffres(1, don.listeChiffres, 1, 99)
                cible = 1000 * int(self.objectif_chiffres[0]) + 100 * int(self.objectif_chiffres[1]) + finTirage[-1]
                self.tirage_chiffres.append(cible)
        elif len(self.objectif_chiffres) == 3:
            if len(str(don.borneMax)) == 4:
                finTirage = genereTirageChiffres(1, don.listeChiffres, 1, 9)
                cible = 1000 * int(self.objectif_chiffres[0]) + 100 * int(self.objectif_chiffres[1]) + \
                        10 * int(self.objectif_chiffres[2]) + finTirage[-1]
                self.tirage_chiffres.append(cible)
        self.valide = 1

    def Affiche(self):
        print('PREMIER TIRAGE')
        print(self.tirage)
        affiche(self.tirage)

    def GUI_Tirage(self, don):
        #ch = ''
        #for ii in range(0, len(self.tirage)):
        #    ch = ch + self.tirage[ii] + ' '
        #w = tk.Label(master, text=ch, font=("Helvetica", 40))
        #w.pack()
        #w.mainloop()
        # BoutonLancer = Button(Mafenetre, text ='Lancer', command = NouveauLance)
        # BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)

        Mafenetre = tk.Tk()
        Mafenetre.title('Tirage')
        Mafenetre.geometry("600x250")

        Bouton = []
        motUtilisateur = MotUtilisateur()

        boutons_reponse = []
        for ii in range(0, len(self.tirage)):
            b = Button(Mafenetre, text='', font=("Helvetica", 30), bg=self.couleur_bg_defaut)
            boutons_reponse.append(b)
            # b.configure(command=lambda c=ii: motUtilisateur.AddLettre(self, c, Bouton[c]))
            boutons_reponse[ii].place(x=60 + 54 * ii, y=110, anchor=CENTER, width=50, height=50)

        for ii in range(0, len(self.tirage)):
            b = Button(Mafenetre, text=self.tirage[ii], font=("Helvetica", 30), bg=self.couleur_bg_defaut)
            Bouton.append(b)
            b.configure(command=lambda c=ii: motUtilisateur.AddLettre(self, c, Bouton[c], boutons_reponse))
            #Bouton.append(Button(Mafenetre, text=self.tirage[ii], font=("Helvetica", 30),
            #                    command=lambda c=ii: motUtilisateur.AddLettre(self.tirage[c])))
            Bouton[ii].place(x=60+54*ii, y=30, anchor=CENTER, width=50, height=50)

        BoutonErase = Button(Mafenetre, text='effacer', font=("Helvetica", 20),
                              command=lambda: motUtilisateur.DelLettre(self, Bouton, boutons_reponse))
        BoutonErase.place(relx=0.2, y=200, anchor=CENTER)

        BoutonRAZ = Button(Mafenetre, text='RAZ', font=("Helvetica", 20),
                             command=lambda: motUtilisateur.DelLettreRAZ(self, Bouton, boutons_reponse))
        BoutonRAZ.place(relx=0.4, y=200, anchor=CENTER)

        BoutonSolutions = Button(Mafenetre, text='voir les solutions', font=("Helvetica", 20),
                              command=lambda: solveur(self, don))
        BoutonSolutions.place(relx=0.75, y=200, anchor=CENTER)
        Mafenetre.maj_temps_restant()
        Mafenetre.mainloop()

    def Affiche_solutions(self):
        #fenetre = tk.Tk()
        #scrollbar = tk.Scrollbar
        #fenetre.option_add('*font', ('', 20))
        #helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')

        def maFoncF2(event):
            root_f2 = tk.Tk()
            root_f2.title('Définitions')
            S_f2 = tk.Scrollbar(root_f2)
            T_f2 = tk.Text(root_f2, height=22, width=88, font=('consolas', 16))
            S_f2.pack(side=tk.RIGHT, fill=tk.Y)
            T_f2.pack(side=tk.LEFT, fill=tk.Y)
            S_f2.config(command=T_f2.yview)
            T_f2.config(yscrollcommand=S_f2.set)
            quote_f2 = ch2
            T_f2.insert(tk.END, quote_f2)
            tk.mainloop()

        ch = 'Tirage :\n\n' + self.tirage + '\n\nSolutions : \n\n'
        ch2 = ''
        for ii in range(0, len(self.sol_complet)):
            nb_lettres_disp = len(self.sol_complet)-ii-1
            if len(self.sol_complet[nb_lettres_disp]) > 0:
                ch = ch + str(len(self.sol_basique[nb_lettres_disp][0])) + " lettres : "
                if len(self.sol_complet[nb_lettres_disp]) > 1:
                    ch = ch + "(" + str(len(self.sol_complet[nb_lettres_disp])) + " mots) "
                    for jj in range(0,len(self.sol_complet[nb_lettres_disp])):
                        if len(self.sol_definitions[nb_lettres_disp][jj]):
                            ch2 = ch2 + self.sol_complet[nb_lettres_disp][jj] + ' : ' \
                            + self.sol_definitions[nb_lettres_disp][jj] + '\n'
                        ch = ch + self.sol_complet[nb_lettres_disp][jj]
                        if jj<len(self.sol_complet[nb_lettres_disp])-1:
                            ch = ch + ', '
                    #ch = ch + self.sol_complet[nb_lettres_disp][jj+1]
                else:
                    if len(self.sol_definitions[nb_lettres_disp][0]):
                        ch2 = ch2 + self.sol_complet[nb_lettres_disp][0] + ' : ' \
                        + self.sol_definitions[nb_lettres_disp][0] + '\n'
                    ch = ch + "(" + str(len(self.sol_complet[nb_lettres_disp])) + " mot) "
                    ch = ch + self.sol_complet[nb_lettres_disp][0]
                ch = ch + '\n\n'

        root = tk.Tk()
        root.title('Solutions')
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=20, width=80, font=('consolas', 20))
        #T = tk.Text(root, height=36, width=100)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = ch
        T.insert(tk.END, quote)
        root.bind("<F2>", maFoncF2)
        tk.mainloop()

    def Affiche_solutions_chiffres(self, don):
        cible = self.tirage_chiffres[-1]
        nbPt = []
        for ii in range(len(self.liste_approches)):
            t, u = don.bareme_chiffres.Appli_bareme(self.liste_possibles_chiffres,
                                                    abs(self.liste_approches[ii][0]-cible))
            nbPt.append(t)


        ch = 'Tirage :\n\n' + str(self.tirage_chiffres) + '\n\n'
        ch = ch + '--------------------------------------------\n\n'
        if len(self.liste_approches[0])==1:
            ch = ch + '     meilleure solution : ' + str(self.liste_approches[0][0]) + \
                 '      (' + str(nbPt[0]) +' points)\n'
        else:
            ch = ch + '     meilleure solution : ' + str(self.liste_approches[0][0]) + ', ' + \
                str(self.liste_approches[0][1]) + ' (' + str(nbPt[0]) +' points)\n'

        for ii in range(1, len(self.liste_approches)):
            if len(self.liste_approches[ii]) == 1:
                if nbPt[ii] > 1:
                    ch = ch + str(ii+1) + 'ème meilleure solution : ' + str(self.liste_approches[ii][0]) + \
                         '      (' + str(nbPt[ii]) + ' points)\n'
                else:
                    ch = ch + str(ii+1) + 'ème meilleure solution : ' + str(self.liste_approches[ii][0]) + \
                         '      (' + str(nbPt[ii]) + ' point)\n'
            else:
                if nbPt[ii] > 1:
                    ch = ch + str(ii+1) + 'ème meilleure solution : ' + str(self.liste_approches[ii][0]) + ', ' + \
                         str(self.liste_approches[ii][1]) + ' (' + str(nbPt[ii]) + ' points)\n'
                else:
                    ch = ch + str(ii + 1) + 'ème meilleure solution : ' + str(self.liste_approches[ii][0]) + ', ' + \
                         str(self.liste_approches[ii][1]) + ' (' + str(nbPt[ii]) + ' point)\n'

        ch = ch + '\n--------------------------------------------\n\n'
        init_nb_lettres = self.sol_complet[0]
        ch_temp = str(init_nb_lettres)
        ch = ch + ch_temp + ' plaques :\n\n'
        for ii in range(0, len(self.sol_basique)):
            if self.sol_complet[ii] != init_nb_lettres:
                init_nb_lettres = self.sol_complet[ii]
                ch = ch + '\n\n' + str(init_nb_lettres) + ' plaques :\n\n'
            ch_temp = self.sol_basique[ii]

            # on remplace les * par des ×
            ch_temp_modif = ch_temp.replace('*', '×')

            # pour enlever les parenthèses inutiles autour de la solution
            ch = ch + ch_temp_modif
            ch = ch + ' = ' + str(int(eval(ch_temp))) + '\n'
        root = tk.Tk()
        root.title('Solutions')
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=20, width=80, font=('consolas', 20))
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote = ch
        T.insert(tk.END, quote)
        tk.mainloop()

    def Affiche_solutions_console(self):
        print('Solutions')
        print('')

        print('2 lettres')
        chaine = 'nombre de mots : ' + str(len(self.sol_complet[0]))
        print(chaine)
        print(self.sol_complet[0])
        print('')

        print('3 lettres')
        chaine = 'nombre de mots : ' + str(len(self.sol_complet[1]))
        print(chaine)
        print(self.sol_complet[1])
        print('')

        print('4 lettres')
        chaine = 'nombre de mots : ' + str(len(self.sol_complet[2]))
        print(chaine)
        print(self.sol_complet[2])
        print('')

        print('5 lettres')
        chaine = 'nombre de mots : ' + str(len(self.sol_complet[3]))
        print(chaine)
        print(self.sol_complet[3])
        print('')

        print('6 lettres')
        chaine = 'nombre de mots : ' + str(len(self.sol_complet[4]))
        print(chaine)
        print(self.sol_complet[4])
        print('')

        print('7 lettres')
        chaine = 'nombre de mots : ' + str(len(self.sol_complet[5]))
        print(chaine)
        print(self.sol_complet[5])
        print('')

        print('8 lettres')
        chaine = 'nombre de mots : ' + str(len(self.sol_complet[6]))
        print(chaine)
        print(self.sol_complet[6])
        print('')

        print('9 lettres')
        chaine = 'nombre de mots : ' + str(len(self.sol_complet[7]))
        print(chaine)
        print(self.sol_complet[7])
        print('')

        print('10 lettres')
        chaine = 'nombre de mots : ' + str(len(self.sol_complet[8]))
        print(chaine)
        print(self.sol_complet[8])
        print('')

    def Solveur(self, don):
        # recherche des nombres de lettres possibles pour les dicos chargés
        nb_lettres_dico = []
        for ii in range(0, len(don.dico)):
            nb_lettres_dico.append(don.dico[ii].nbLettres)
        # recherche des solutions pour chaque nombre de lettres si le dico correspondant est chargé
        self.tirageMin = ordreAlpha(self.tirage.lower())
        for ii in range(2, self.nbLettres+1):
            if ii in nb_lettres_dico:
                idx_dico = nb_lettres_dico.index(ii)
                listeComb = []
                if ii == 2:
                    for i1 in range(0, self.nbLettres - 1):
                        for i2 in range(i1 + 1, self.nbLettres):
                            str = self.tirageMin[i1] + self.tirageMin[i2]
                            listeComb.append(str)
                if ii == 3:
                    for i1 in range(0, self.nbLettres - 2):
                        for i2 in range(i1 + 1, self.nbLettres-1):
                            for i3 in range(i2 + 1, self.nbLettres):
                                str = self.tirageMin[i1] + self.tirageMin[i2] + self.tirageMin[i3]
                                listeComb.append(str)
                if ii == 4:
                    for i1 in range(0, self.nbLettres - 3):
                        for i2 in range(i1 + 1, self.nbLettres-2):
                            for i3 in range(i2 + 1, self.nbLettres-1):
                                for i4 in range(i3 + 1, self.nbLettres):
                                    str = self.tirageMin[i1] + self.tirageMin[i2] + self.tirageMin[i3] \
                                          + self.tirageMin[i4]
                                    listeComb.append(str)

                if ii == 5:
                    for i1 in range(0, self.nbLettres - 4):
                        for i2 in range(i1 + 1, self.nbLettres - 3):
                            for i3 in range(i2 + 1, self.nbLettres - 2):
                                for i4 in range(i3 + 1, self.nbLettres-1):
                                    for i5 in range(i4 + 1, self.nbLettres):
                                        str = self.tirageMin[i1] + self.tirageMin[i2] + self.tirageMin[i3] \
                                            + self.tirageMin[i4] + self.tirageMin[i5]
                                        listeComb.append(str)

                if ii == 6:
                    for i1 in range(0, self.nbLettres - 5):
                        for i2 in range(i1 + 1, self.nbLettres - 4):
                            for i3 in range(i2 + 1, self.nbLettres - 3):
                                for i4 in range(i3 + 1, self.nbLettres-2):
                                    for i5 in range(i4 + 1, self.nbLettres-1):
                                        for i6 in range(i5 + 1, self.nbLettres):
                                            str = self.tirageMin[i1] + self.tirageMin[i2] + self.tirageMin[i3] \
                                                + self.tirageMin[i4] + self.tirageMin[i5] + self.tirageMin[i6]
                                            listeComb.append(str)

                if ii == 7:
                    for i1 in range(0, self.nbLettres - 6):
                        for i2 in range(i1 + 1, self.nbLettres - 5):
                            for i3 in range(i2 + 1, self.nbLettres - 4):
                                for i4 in range(i3 + 1, self.nbLettres-3):
                                    for i5 in range(i4 + 1, self.nbLettres-2):
                                        for i6 in range(i5 + 1, self.nbLettres-1):
                                            for i7 in range(i6 + 1, self.nbLettres):
                                                str = self.tirageMin[i1] + self.tirageMin[i2] + self.tirageMin[i3] \
                                                    + self.tirageMin[i4] + self.tirageMin[i5] + self.tirageMin[i6] \
                                                    + self.tirageMin[i7]
                                                listeComb.append(str)

                if ii == 8:
                    for i1 in range(0, self.nbLettres - 7):
                        for i2 in range(i1 + 1, self.nbLettres - 6):
                            for i3 in range(i2 + 1, self.nbLettres - 5):
                                for i4 in range(i3 + 1, self.nbLettres-4):
                                    for i5 in range(i4 + 1, self.nbLettres-3):
                                        for i6 in range(i5 + 1, self.nbLettres-2):
                                            for i7 in range(i6 + 1, self.nbLettres-1):
                                                for i8 in range(i7 + 1, self.nbLettres):
                                                    str = self.tirageMin[i1] + self.tirageMin[i2] \
                                                        + self.tirageMin[i3] + self.tirageMin[i4] \
                                                        + self.tirageMin[i5] + self.tirageMin[i6] \
                                                        + self.tirageMin[i7] + self.tirageMin[i8]
                                                    listeComb.append(str)

                if ii == 9:
                    for i1 in range(0, self.nbLettres - 8):
                        for i2 in range(i1 + 1, self.nbLettres - 7):
                            for i3 in range(i2 + 1, self.nbLettres - 6):
                                for i4 in range(i3 + 1, self.nbLettres-5):
                                    for i5 in range(i4 + 1, self.nbLettres-4):
                                        for i6 in range(i5 + 1, self.nbLettres-3):
                                            for i7 in range(i6 + 1, self.nbLettres-2):
                                                for i8 in range(i7 + 1, self.nbLettres-1):
                                                    for i9 in range(i8 + 1, self.nbLettres):
                                                        str = self.tirageMin[i1] + self.tirageMin[i2] \
                                                            + self.tirageMin[i3] + self.tirageMin[i4] \
                                                            + self.tirageMin[i5] + self.tirageMin[i6] \
                                                            + self.tirageMin[i7] + self.tirageMin[i8] \
                                                            + self.tirageMin[i9]
                                                        listeComb.append(str)

                if ii == 10:
                    for i1 in range(0, self.nbLettres - 9):
                        for i2 in range(i1 + 1, self.nbLettres - 8):
                            for i3 in range(i2 + 1, self.nbLettres - 7):
                                for i4 in range(i3 + 1, self.nbLettres-6):
                                    for i5 in range(i4 + 1, self.nbLettres-5):
                                        for i6 in range(i5 + 1, self.nbLettres-4):
                                            for i7 in range(i6 + 1, self.nbLettres-3):
                                                for i8 in range(i7 + 1, self.nbLettres-2):
                                                    for i9 in range(i8 + 1, self.nbLettres-1):
                                                        for i10 in range(i9 + 1, self.nbLettres):
                                                            str = self.tirageMin[i1] + self.tirageMin[i2] \
                                                                + self.tirageMin[i3] + self.tirageMin[i4] \
                                                                + self.tirageMin[i5] + self.tirageMin[i6] \
                                                                + self.tirageMin[i7] + self.tirageMin[i8] \
                                                                + self.tirageMin[i9] + self.tirageMin[i10]
                                                            listeComb.append(str)

                if ii == 11:
                    for i1 in range(0, self.nbLettres - 10):
                        for i2 in range(i1 + 1, self.nbLettres - 9):
                            for i3 in range(i2 + 1, self.nbLettres - 8):
                                for i4 in range(i3 + 1, self.nbLettres-7):
                                    for i5 in range(i4 + 1, self.nbLettres-6):
                                        for i6 in range(i5 + 1, self.nbLettres-5):
                                            for i7 in range(i6 + 1, self.nbLettres-4):
                                                for i8 in range(i7 + 1, self.nbLettres-3):
                                                    for i9 in range(i8 + 1, self.nbLettres-2):
                                                        for i10 in range(i9 + 1, self.nbLettres-1):
                                                            for i11 in range(i10 + 1, self.nbLettres):
                                                                str = self.tirageMin[i1] + self.tirageMin[i2] \
                                                                    + self.tirageMin[i3] + self.tirageMin[i4] \
                                                                    + self.tirageMin[i5] + self.tirageMin[i6] \
                                                                    + self.tirageMin[i7] + self.tirageMin[i8] \
                                                                    + self.tirageMin[i9] + self.tirageMin[i10] \
                                                                    + self.tirageMin[i11]
                                                                listeComb.append(str)
                # on retire les doublons
                listeComb2 = list(set(listeComb))
                listeComb2.sort()
                # recherche dans le dictionnaire pour chaque combinaison de lettres
                sol_alpha_t = []
                sol_complet_t = []
                sol_basique_t = []
                sol_basique = []
                sol_complet = []
                sol_def_t = []
                sol_def = []
                for idx_comb in range(0, len(listeComb2)):
                    res_list = [i for i in range(len(don.dico[idx_dico].alpha)) if
                                        don.dico[idx_dico].alpha[i] == listeComb2[idx_comb]]
                    if len(res_list) > 0:
                        for jj in range(0, len(res_list)):
                            sol_alpha_t.append(don.dico[idx_dico].alpha[res_list[jj]])
                            sol_basique_t.append(don.dico[idx_dico].basique[res_list[jj]])
                            sol_complet_t.append(don.dico[idx_dico].complet[res_list[jj]])
                            sol_def_t.append(don.dico[idx_dico].definitions[res_list[jj]])
                # rangement dans l'ordre alphabétique
                s = sol_basique_t
                ss = sorted(range(len(s)), key=lambda k: s[k])
                for jj in range(0, len(ss)):
                    sol_basique.append(sol_basique_t[ss[jj]])
                    sol_complet.append(sol_complet_t[ss[jj]])
                    sol_def.append(sol_def_t[ss[jj]])
                self.sol_basique.append(sol_basique)
                self.sol_complet.append(sol_complet)
                self.sol_definitions.append(sol_def)
                top = 0
        for jj in range(0, len(self.sol_basique)):
            if len(self.sol_basique[jj]) > 0:
                top = max(top, len(self.sol_basique[jj][0]))
        self.top = top

    def Solveur_chiffres(self,don):
        x = []
        for ii in range(0,len(self.tirage_chiffres)-1):
            plaque = []
            plaque.append(self.tirage_chiffres[ii])
            x.append(plaque)
        liste_possibilites = test_solveur4(x)
        # toto=test_solveur3([[10], [3], [1], [5], [8], [5]])

        # on enlève les []
        liste_possibilites.val = [i for i in liste_possibilites.val if i or i == 0]
        liste_possibilites.cha = [i for i in liste_possibilites.cha if i]
        liste_possibilites.nbPlaques = [i for i in liste_possibilites.nbPlaques if i]

        # rangement dans l'ordre croissant
        zz = sorted(range(len(liste_possibilites.val)), key=lambda k: liste_possibilites.val[k])
        zz2 = [liste_possibilites.val[i] for i in zz] # valeurs en int
        zz3 = [liste_possibilites.cha[i] for i in zz] # valeurs en char avec les opérations
        zz4 = [liste_possibilites.nbPlaques[i] for i in zz]  # nb plaques
        cible = self.tirage_chiffres[-1]
        distance = [abs(i - cible) for i in zz2]

        idx_distance_ordonnee = sorted(range(len(distance)), key=lambda k: distance[k])

        # récupération de la liste des approches (pour affichage avec les solutions)
        liste_approches0 = []
        liste_approches  = []
        for ii in idx_distance_ordonnee:
            liste_approches0.append(zz2[ii])
        idx_app = 0
        while len(liste_approches) < 5:
            valt = []
            eloi = abs(liste_approches0[idx_app] - cible)
            idx_app2 = 0
            eloi2 = abs(liste_approches0[idx_app + idx_app2] - cible)
            while eloi2 == eloi:
                if liste_approches0[idx_app + idx_app2] not in valt:
                    valt.append(liste_approches0[idx_app + idx_app2])
                idx_app2 += 1
                eloi2 = abs(liste_approches0[idx_app + idx_app2] - cible)
            idx_app += idx_app2
            valt.sort()
            liste_approches.append(valt)

        self.liste_approches = liste_approches
        ttemp = sorted(set(distance))
        self.liste_possibles_chiffres = ttemp[0:9] # éloignements en valeur absolue, pour application du barème
        # (à fusionner avec self.liste_approches ? )
        solution = []
        nbPlaques = []
        solution.append(zz3[idx_distance_ordonnee[0]])
        nbPlaques.append(zz4[idx_distance_ordonnee[0]])
        ii = 1
        while zz2[idx_distance_ordonnee[ii]] == zz2[idx_distance_ordonnee[0]]:
            solution.append(zz3[idx_distance_ordonnee[ii]])
            nbPlaques.append(zz4[idx_distance_ordonnee[ii]])
            ii += 1
        yy = sorted(range(len(nbPlaques)), key=lambda k: nbPlaques[k])
        yy2 = [nbPlaques[i] for i in yy]
        yy1 = [solution[i] for i in yy]

        new_y1 = []
        new_y2 = []
        for i in range(0,len(yy1)):
            if yy1[i] not in new_y1:
                new_y1.append(yy1[i])
                new_y2.append(yy2[i])

        for ii in range(0,len(new_y1)):
            temp = ''
            for jj in range(1, len(new_y1[ii])-1):
                temp = temp + new_y1[ii][jj]
            new_y1[ii] = temp

        for ii in range(0, len(new_y1)):
            new_y1[ii] = get_chaine_simplifiee(new_y1[ii]).strip()

        basique = []
        plaques = []
        for ii in range(0, len(new_y1)):
            if ii == 0:
                basique.append(new_y1[0])
                plaques.append(new_y2[0])
            else:
                ajout = 1
                for jj in range(0, len(basique)):
                    if new_y1[ii] == basique[jj]:
                        ajout = 0
                if ajout == 1:
                    basique.append(new_y1[ii])
                    plaques.append(new_y2[ii])

        # new_y1 : liste des solutions
        # new_y2 : nombres de plaques


        self.sol_basique = basique
        self.sol_complet = plaques

    def sauvegarde(self, icones, don):
        if don.type_actuel == 'lettres':
            if len(self.tirage) == don.nbLettres:
                if icones.boutons_sauvegarde.cget('bg') == don.proprietes.couleur_bg_defaut:
                    fichier = open(don.fichier_prepa_l, "a")
                    fichier.write('\n')
                    fichier.write(self.tirage)
                    fichier.close()
                    icones.boutons_sauvegarde.configure(bg=don.proprietes.couleur_bg_select)
        if don.type_actuel == 'chiffres':
            if len(self.tirage_chiffres) == don.nbPlaquesChiffres+1:
                if icones.boutons_sauvegarde.cget('bg') == don.proprietes.couleur_bg_defaut:
                    fichier = open(don.fichier_prepa_c, "a")
                    fichier.write('\n')
                    cha = str(self.tirage_chiffres[0])
                    for ii in range(1, len(self.tirage_chiffres)):
                        cha = cha + ' ' + str(self.tirage_chiffres[ii])
                    fichier.write(cha)
                    fichier.close()
                    icones.boutons_sauvegarde.configure(bg=don.proprietes.couleur_bg_select)

def ordreAlpha(chaine):
    liste = []
    for ii in range(0, len(chaine)):
        liste.append(chaine[ii])
    liste.sort()
    newListe = ''
    for ii in range(0, len(chaine)):
        newListe = newListe + liste[ii]
    return newListe

def test_solveur4(x):
    val = valeurrr()
    for ii in range(2,len(x)+1):
        if ii == 2:
            for jj1 in range(0,len(x)-1):
                for jj2 in range(jj1+1, len(x)):
                    x_temp = []
                    x_temp.append(x[jj1])
                    x_temp.append(x[jj2])
                    val_temp = test_solveur3(x_temp)
                    for kk in range(0,len(val_temp.val)):
                        val.val.append(val_temp.val[kk])
                        val.cha.append(val_temp.cha[kk])
                        if val_temp.val[kk]:
                            val.nbPlaques.append(ii)
                        else:
                            val.nbPlaques.append([])
        if ii == 3:
            for jj1 in range(0,len(x)-2):
                for jj2 in range(jj1+1, len(x)-1):
                    for jj3 in range(jj2 + 1, len(x)):
                        x_temp = []
                        x_temp.append(x[jj1])
                        x_temp.append(x[jj2])
                        x_temp.append(x[jj3])
                        val_temp = test_solveur3(x_temp)
                        for kk in range(0,len(val_temp.val)):
                            val.val.append(val_temp.val[kk])
                            val.cha.append(val_temp.cha[kk])
                            if val_temp.val[kk]:
                                val.nbPlaques.append(ii)
                            else:
                                val.nbPlaques.append([])
        if ii == 4:
            for jj1 in range(0,len(x)-3):
                for jj2 in range(jj1+1, len(x)-2):
                    for jj3 in range(jj2 + 1, len(x)-1):
                        for jj4 in range(jj3 + 1, len(x)):
                            x_temp = []
                            x_temp.append(x[jj1])
                            x_temp.append(x[jj2])
                            x_temp.append(x[jj3])
                            x_temp.append(x[jj4])
                            val_temp = test_solveur3(x_temp)
                            for kk in range(0,len(val_temp.val)):
                                val.val.append(val_temp.val[kk])
                                val.cha.append(val_temp.cha[kk])
                                if val_temp.val[kk]:
                                    val.nbPlaques.append(ii)
                                else:
                                    val.nbPlaques.append([])
        if ii == 5:
            for jj1 in range(0,len(x)-4):
                for jj2 in range(jj1+1, len(x)-3):
                    for jj3 in range(jj2 + 1, len(x)-2):
                        for jj4 in range(jj3 + 1, len(x)-1):
                            for jj5 in range(jj4 + 1, len(x)):
                                x_temp = []
                                x_temp.append(x[jj1])
                                x_temp.append(x[jj2])
                                x_temp.append(x[jj3])
                                x_temp.append(x[jj4])
                                x_temp.append(x[jj5])
                                val_temp = test_solveur3(x_temp)
                                for kk in range(0,len(val_temp.val)):
                                    val.val.append(val_temp.val[kk])
                                    val.cha.append(val_temp.cha[kk])
                                    if val_temp.val[kk]:
                                        val.nbPlaques.append(ii)
                                    else:
                                        val.nbPlaques.append([])
        if ii == 6:
            for jj1 in range(0,len(x)-5):
                for jj2 in range(jj1+1, len(x)-4):
                    for jj3 in range(jj2 + 1, len(x)-3):
                        for jj4 in range(jj3 + 1, len(x)-2):
                            for jj5 in range(jj4 + 1, len(x)-1):
                                for jj6 in range(jj5 + 1, len(x)):
                                    x_temp = []
                                    x_temp.append(x[jj1])
                                    x_temp.append(x[jj2])
                                    x_temp.append(x[jj3])
                                    x_temp.append(x[jj4])
                                    x_temp.append(x[jj5])
                                    x_temp.append(x[jj6])
                                    val_temp = test_solveur3(x_temp)
                                    for kk in range(0,len(val_temp.val)):
                                        val.val.append(val_temp.val[kk])
                                        val.cha.append(val_temp.cha[kk])
                                        if val_temp.val[kk]:
                                            val.nbPlaques.append(ii)
                                        else:
                                            val.nbPlaques.append([])
    return val



def test_solveur3(x):
    valeurs = valeurrr()
    if len(x)==1:
        valeurs.val.append(x[0][0])
        valeurs.cha.append(str(x[0][0]))
    if len(x)==2:
        for ii in range(0,len(x[0])):
            for jj in range(0,len(x[1])):
                if isinstance(x[0][ii], int) and isinstance(x[1][jj], int):
                    valeurs.val.append(x[0][ii]+x[1][jj])
                    valeurs.cha.append("(%s + %s)" % (x[0][ii], x[1][jj]))

                    # on ne garde pas s'il y a une multiplication par 1
                    if x[0][ii] == 1 or x[1][jj] == 1:
                        valeurs.val.append([])
                        valeurs.cha.append([])
                    else:
                        valeurs.val.append(x[0][ii] * x[1][jj])
                        valeurs.cha.append("(%s * %s)" % (x[0][ii], x[1][jj]))

                    if x[0][ii] - x[1][jj] > 0:
                        valeurs.val.append(x[0][ii] - x[1][jj])
                        valeurs.cha.append("(%s - %s)" % (x[0][ii], x[1][jj]))
                    elif x[1][jj] - x[0][ii] > 0:
                        valeurs.val.append(x[1][jj] - x[0][ii])
                        valeurs.cha.append("(%s - %s)" % (x[1][jj], x[0][ii]))
                    else:
                        valeurs.val.append([])
                        valeurs.cha.append([])

                    if x[0][ii] == 1 or x[1][jj] == 1:
                        valeurs.val.append([])
                        valeurs.cha.append([])
                    else:
                        if not x[0][ii] % x[1][jj]:
                            valeurs.val.append(x[0][ii] // x[1][jj])
                            valeurs.cha.append("(%s / %s)" % (x[0][ii], x[1][jj]))
                        elif not x[1][jj] % x[0][ii]:
                            valeurs.val.append(x[1][jj] // x[0][ii])
                            valeurs.cha.append("(%s / %s)" % (x[1][jj], x[0][ii]))
                        else:
                            valeurs.val.append([])
                            valeurs.cha.append([])
                else:
                    valeurs.val.append([])
                    valeurs.val.append([])
                    valeurs.val.append([])
                    valeurs.val.append([])
                    valeurs.cha.append([])
                    valeurs.cha.append([])
                    valeurs.cha.append([])
                    valeurs.cha.append([])
    else:
        # obtention des partitions de x en 2 parties
        # la première partie est d'une taille inférieure ou égale à la seconde
        liste_parties = partiesliste_2(x)
        for ii in range(0,(len(liste_parties))):
            w1 = liste_parties[ii][0]
            w2 = liste_parties[ii][1]
            val1 = test_solveur3(w1)
            val2 = test_solveur3(w2)

            for kk in range(0, len(val1.val)):
                for jj in range(0, len(val2.val)):
                    if isinstance(val1.val[kk], int) and isinstance(val2.val[jj], int):
                        valeurs.val.append(val1.val[kk] + val2.val[jj])
                        valeurs.cha.append("(%s + %s)" % (val1.cha[kk], val2.cha[jj]))

                        if val1.val[kk] == 1 or val2.val[jj] == 1:
                            valeurs.val.append([])
                            valeurs.cha.append([])
                        else:
                            valeurs.val.append(val1.val[kk] * val2.val[jj])
                            valeurs.cha.append("(%s * %s)" % (val1.cha[kk], val2.cha[jj]))

                        if val1.val[kk] - val2.val[jj] > 0:
                            valeurs.val.append(val1.val[kk] - val2.val[jj])
                            valeurs.cha.append("(%s - %s)" % (val1.cha[kk], val2.cha[jj]))
                        elif val2.val[jj] - val1.val[kk] > 0:
                            valeurs.val.append(val2.val[jj] - val1.val[kk])
                            valeurs.cha.append("(%s - %s)" % (val2.cha[jj], val1.cha[kk]))
                        else:
                            valeurs.val.append([])
                            valeurs.cha.append([])

                        if val2.val[jj]>1 and val1.val[kk]>1:
                            # >1 à la fois pour éviter les 0, mais aussi pour empêcher des divisions inutiles par 1
                            if not val1.val[kk] % val2.val[jj]:
                                valeurs.val.append(val1.val[kk] // val2.val[jj])
                                valeurs.cha.append("(%s / %s)" % (val1.cha[kk], val2.cha[jj]))
                            elif not val2.val[jj] % val1.val[kk]:
                                valeurs.val.append(val2.val[jj] // val1.val[kk])
                                valeurs.cha.append("(%s / %s)" % (val2.cha[jj], val1.cha[kk]))
                            else:
                                valeurs.val.append([])
                                valeurs.cha.append([])
                        else:
                            valeurs.val.append([])
                            valeurs.cha.append([])
                    else:
                        valeurs.val.append([])
                        valeurs.val.append([])
                        valeurs.val.append([])
                        valeurs.val.append([])
                        valeurs.cha.append([])
                        valeurs.cha.append([])
                        valeurs.cha.append([])
                        valeurs.cha.append([])
    return valeurs


def partiesliste_2(seq):
    # obtention de l'ensemble des partitions en exactement deux parties d'une
    liste_parties = []
    for ii in range(1,1+(len(seq))//2):
        if ii == 1:
            for jj in range(0,len(seq)):
                par1 = []
                par2 = []
                par1.append(seq[jj])
                len_par2 = len(seq)-len(par1)
                if len(par1) != len_par2:
                    for kk in range(0,len(seq)):
                        if kk != jj:
                            par2.append(seq[kk])
                    par = []
                    par.append(par1)
                    par.append(par2)
                    liste_parties.append(par)
                elif jj < len(seq)-1:
                    for kk in range(jj+1,len(seq)):
                        par2.append(seq[kk])
                    par = []
                    par.append(par1)
                    par.append(par2)
                    liste_parties.append(par)
        if ii == 2:
            for jj1 in range(0,len(seq)-1):
                for jj2 in range(jj1+1,len(seq)):
                    par1 = []
                    par2 = []
                    par1.append(seq[jj1])
                    par1.append(seq[jj2])
                    idxj = []
                    idxj.append(jj1)
                    idxj.append(jj2)
                    len_par2 = len(seq) - len(par1)
                    if len(par1) != len_par2:
                        for kk in range(0,len(seq)):
                            if kk not in idxj:
                                par2.append(seq[kk])
                        par = []
                        par.append(par1)
                        par.append(par2)
                        liste_parties.append(par)
                    elif jj1 < len(seq) - 1:
                        for kk in range(jj1+1,len(seq)):
                            if kk not in idxj:
                                par2.append(seq[kk])
                        par = []
                        if len(par2)==len(par1):
                            par.append(par1)
                            par.append(par2)
                            liste_parties.append(par)

        if ii == 3:
            for jj1 in range(0,len(seq)-2):
                for jj2 in range(jj1+1,len(seq)-1):
                    for jj3 in range(jj2+1, len(seq)):
                        par1 = []
                        par2 = []
                        par1.append(seq[jj1])
                        par1.append(seq[jj2])
                        par1.append(seq[jj3])
                        idxj = []
                        idxj.append(jj1)
                        idxj.append(jj2)
                        idxj.append(jj3)
                        len_par2 = len(seq) - len(par1)
                        if len(par1) != len_par2:
                            for kk in range(0,len(seq)):
                                if kk not in idxj:
                                    par2.append(seq[kk])
                            par = []
                            par.append(par1)
                            par.append(par2)
                            liste_parties.append(par)
                        elif jj1 < len(seq) - 1:
                            for kk in range(jj1 + 1, len(seq)):
                                if kk not in idxj:
                                    par2.append(seq[kk])
                            par = []
                            if len(par2) == len(par1):
                                par.append(par1)
                                par.append(par2)
                                liste_parties.append(par)
    return liste_parties

class valeurrr:
    def __init__(self):
        self.val = []
        self.cha = []
        self.nbPlaques = []

def lecture_tirages_prepares(l_ou_c, nomFichier):
    list = []
    if l_ou_c in ['lettres', 'chiffres']:
        try:
            fichier = open(nomFichier, "r")
            for line in fichier:
                if '|' in line:
                    v = line.split('|')
                    tir = v[0]
                else:
                    tir = line
                if l_ou_c == 'lettres':
                    if '(' in tir:
                        w = tir.split('(')
                        list.append(w[0])
                    else:
                        list.append(tir)
                else:
                    list.append(tir)
        except IOError:
            cha = "le fichier de tirages préparés de " + l_ou_c + " n'a pas pu être chargé."
            print(cha)
    return list



