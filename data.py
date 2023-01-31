from loadConsVoy import loadCons, loadVoy, genereTirageLettres
from affichage import *
import tkinter as tk
import time
from random import *
import tkinter.font as tkFont
import pygame
from icones import *
from tirage import *
from classe import *
from motUtilisateur import *
#from datetime import timedelta, datetime, date, time

class Data:
    def __init__(self):
        self.listeCons = 'BBBBBBBBCCCCCCCCCCCCCCCCDDDDDDDDDDDDDDDDDDDDFFFFFFFFGGGGGGGGHHHHHHJJKLLLLLLLLLLLLLLL' + \
            'LLLLLLLLLLLMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNPPPPPPPPPPPPPPQQQQQQRRRRRRRRRRRRRRRRRR' + \
            'RRRRRRRRRRRRRRSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTVVVVVVVVVVWXXXXZZ'
        self.listeVoy = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE' + \
            'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIOOOOOOOO' + \
            'OOOOOOOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUYY'
        self.nbLettres = 11
        self.nbVoy = []
        self.dico = []
        self.proprietes = Proprietes()
        self.aleatoire = 1
        self.prepare = 0
        self.manuel = 0
        self.nbVoyAleatoire = 1
        self.geom = Geometrie()
        self.listeChiffres = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100]
        self.score = 0
        self.total = 0
        self.nbTops = 0
        self.nbTirages = 0
        self.nbPlaquesChiffres = 6
        self.borneMin = 101
        self.borneMax = 999
        self.bareme_chiffres = Bareme()
        self.nb_grosses_plaques = 314
        self.type_actuel = ''
        self.son_actif = 1
        self.tempo = 0.6
        self.fichier_prepa_l = 'prepa_l.txt'
        self.fichier_prepa_c = 'prepa_c.txt'
        self.rajoutsActifs = [1,1,0] # rajouts+1, +2 et +3

    def Analyse_sabot_lettres(self, alphabet, consonnes, voyelles, boutons_val, bouton_warn, fen):
        print(alphabet)
        warn = 0
        liste_val_voy = []
        liste_val_cons = []
        cha_voy = ''
        cha_cons = ''
        for ii in range(len(alphabet)):
            if alphabet[ii] in consonnes:
                try:
                    liste_val_cons.append(int(boutons_val[ii].get()))
                    nb = int(boutons_val[ii].get())
                    for jj in range(nb):
                        cha_cons = cha_cons + alphabet[ii]
                except:
                    warn = 1
            if alphabet[ii] in voyelles:
                try:
                    liste_val_voy.append(int(boutons_val[ii].get()))
                    nb = int(boutons_val[ii].get())
                    for jj in range(nb):
                        cha_voy = cha_voy + alphabet[ii]
                except:
                    warn = 1
        if warn==0:
            if len(cha_cons)<11 or len(cha_voy)<11:
                warn = 2
        if warn==0:
            self.listeCons = cha_cons
            self.listeVoy = cha_voy
            bouton_warn.configure(text='')
            fen.destroy()
        elif warn==2:
            bouton_warn.configure(text='Il faut au moins 11 consonnes et 11 voyelles')
        elif warn==1:
            bouton_warn.configure(text='Les champs ne doivent comporter\n que des chiffres')


    def Analyse_sabot_chiffres(self, chaine, bouton_warning, val_min, val_max, warn_minmax, fen):
        u = 1
        w = 0

        # analyse du sabot
        ch0 = chaine.split(',')
        ch = []
        for ii in ch0:
            try:
                ch.append(int(ii))
            except:
                u = 0
                texte = "La sélection n'est pas valide : il faut au moins six nombres séparés par des virgules"
                bouton_warning.configure(text=texte)

        # analyse des valeurs min et max
        valmin = 0
        valmax = 0
        try:
            valmin = int(val_min)
            valmax = int(val_max)
            if valmin>valmax:
                w = 11
            if valmin<100:
                w = 12
            if valmax>9999:
                w = 13
        except:
            w = 10


        if len(ch) > 6 and u==1 and w==0:
            self.listeChiffres = ch
            self.borneMin = valmin
            self.borneMax = valmax
            bouton_warning.configure(text='')
            warn_minmax.configure(text='')
            fen.destroy()
        else:
            if u != 1:
                texte = "La sélection n'est pas valide : il faut au moins six nombres séparés par des virgules"
                bouton_warning.configure(text=texte)
            if w != 0:
                if w == 10:
                    texte = "Les min et max doivent être \ndes nombres"
                    warn_minmax.configure(text=texte)
                elif w == 11:
                    texte = "Le minimum à trouver doit être \ninférieur au maximum"
                    warn_minmax.configure(text=texte)
                elif w == 12:
                    texte = "Le minimum à trouver doit être \nau moins égal à 100"
                    warn_minmax.configure(text=texte)
                elif w == 13:
                    texte = "Le maximum à trouver doit être \nstrictement inférieur à 10000"
                    warn_minmax.configure(text=texte)



    def init_rajouts(self):
        self.rajoutsActifs = [1, 1, 0]  # rajouts+1, +2 et +3

    def Set_nb_grosses_plaques(self, val):
        self.nb_grosses_plaques = val

    def SetSetNbVoy(self, nbVoy, icones, *argv):
        self.SetNbVoy(nbVoy, *argv)
        for ii in range(1, len(icones.boutons_nbVoyelles)):
            icones.boutons_nbVoyelles[ii].configure(bg=self.proprietes.couleur_fond_nbVoy)
        if nbVoy < 9:
            icones.boutons_nbVoyelles[nbVoy - 1].configure(bg=self.proprietes.couleur_nbVoy)
        else:
            icones.boutons_nbVoyelles[-1].configure(bg=self.proprietes.couleur_nbVoy)

    def LoadDico(self):
        for i_nbl in range(2, self.nbLettres+1):
            dico_temp = Dico(i_nbl)
            dico_temp.ReadDico()
            self.dico.append(dico_temp)

    def SetNbLettres(self, nbLettres, *args):
        self.nbLettres = nbLettres
        if len(args):
            self.nbVoy = args[0]

    def SetSon(self, var):
        self.son_actif = var


    def SetNbVoy(self, nbVoy, *argv):
        if len(argv):
            self.nbVoyAleatoire = 0
        if nbVoy==314 or self.nbVoyAleatoire:
            self.nbVoyAleatoire = 1
            # si 10 L : 3V : 5% // 4V : 20% // 5V : 50% // 6V : 20% // 7V : 5%
            # si 11 L : 3V : 4% // 4V : 16% // 5V : 30% // 6V : 30% // 7V : 16% // 8V : 4%
            val = 100*random()
            if self.nbLettres == 11:
                if val<4:
                    self.nbVoy = 3
                elif val<20:
                    self.nbVoy = 4
                elif val < 50:
                    self.nbVoy = 5
                elif val<80:
                    self.nbVoy = 6
                elif val < 96:
                    self.nbVoy = 7
                else:
                    self.nbVoy = 8
            elif self.nbLettres == 10:
                if val < 5:
                    self.nbVoy = 3
                elif val < 25:
                    self.nbVoy = 4
                elif val < 75:
                    self.nbVoy = 5
                elif val < 95:
                    self.nbVoy = 6
                else:
                    self.nbVoy = 7
        else:
            self.nbVoy = nbVoy
            self.nbVoyAleatoire = 0


   # def LoadConsVoy(self):
        # self.listeCons = loadCons()
        # self.listeVoy = loadVoy()

class Geometrie:
    def __init__(self):
        self.nbLettres = 10
        self.taille_x0 = 780
        self.taille_y0 = 470
        self.taille_x = 954
        self.taille_y = 430
        # positions du chrono
        self.posX = 0.48 * self.taille_x
        self.posY = 200
        # position du triangle de lettres
        self.dx = 50
        self.dy = 50
        self.x0 = 200
        self.y0 = 215
        self.var_dw = 40
        self.var_dh = 34
        # position des nb voyelles
        self.y_voyelles = 175
        self.dy_voyelles = 36

class Proprietes:
    def __init__(self):
        self.couleur_bg_defaut = 'whitesmoke'
        self.couleur_bg_select = 'darkgrey'
        self.couleur_triangle_select = 'gray'
        self.couleur_valide = 'lightgreen'
        self.couleur_faux = 'indianred'
        self.couleur_fond_lettres = 'lightgoldenrodyellow'
        self.couleur_fond_nbVoy = 'paleturquoise'
        self.couleur_fond_boutons6 = 'paleturquoise'
        self.couleur_nbVoy = 'deepskyblue'
        self.couleur_boutons_lancement = 'white'
        self.couleur_changer = 'lightsalmon'
        self.couleur_fond = 'seashell'

class Dico:
    def __init__(self, nbL):
        self.nbLettres = nbL
        self.alpha = []
        self.basique = []
        self.complet = []
        self.definitions = []

    def ReadDico(self):
        if self.nbLettres == 2:
            fichier = open("lexique/2L.dat", "r")
        if self.nbLettres == 3:
            fichier = open("lexique/3L.dat", "r")
        if self.nbLettres == 4:
            fichier = open("lexique/4L.dat", "r")
        if self.nbLettres == 5:
            fichier = open("lexique/5L.dat", "r")
        if self.nbLettres == 6:
            fichier = open("lexique/6L.dat", "r")
        if self.nbLettres == 7:
            fichier = open("lexique/7L.dat", "r")
        if self.nbLettres == 8:
            fichier = open("lexique/8L.dat", "r")
        if self.nbLettres == 9:
            fichier = open("lexique/9L.dat", "r")
        if self.nbLettres == 10:
            fichier = open("lexique/10L.dat", "r")
        if self.nbLettres == 11:
            fichier = open("lexique/11L.dat", "r")
        list0 = []
        list1 = []
        list2 = []
        list3 = []
        for line in fichier:
            if ';' in line:
                v = line.split(';')
                u = v[0].split()
                list0.append(u[0])
                list1.append(u[1])
                mot_complet = u[2]
                if len(u) > 3:
                    for zz in range(3,len(u)):
                        mot_complet = mot_complet + ' ' + u[zz]
                list2.append(mot_complet)
                list3.append(v[1])
            else:
                u = line.split()
                list0.append(u[0])
                list1.append(u[1])
                mot_complet = u[2]
                if len(u) > 3:
                    for zz in range(3, len(u)):
                        mot_complet = mot_complet + ' ' + u[zz]
                list2.append(mot_complet)
                list3.append([])
        self.alpha = list0
        self.basique = list1
        self.complet = list2
        self.definitions = list3

class Bareme:
    def __init__(self, *args):
        self.valeur = []  # [0] pour le BC, [1] pour l'approche à 1, etc. jusqu'à 21
        self.approches = []  # points min pour les 4 meilleures approches
        if len(args):
            nom = args[0]
        else:
            nom = 'classique'
        if nom == 'classique':
            self.approches = [7, 5, 3, 2]
            for ii in range(0, 22):
                if ii < 10:
                    self.valeur.append(10 - ii)
                else:
                    self.valeur.append(1)

    def Set_bareme(self, nom):
        if nom == 'C10':
            for ii in range(0, 22):
                if ii < 10:
                    self.valeur.append(10 - ii)
                else:
                    self.valeur.append(1)
            self.approches = [7, 5, 3, 2]
        if nom == 'NANTES':
            self.valeur = [10, 9, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 0]
            self.approches = [7, 4, 2, 0]

    def Appli_bareme(self, liste_possibles_chiffres, distance_BC):
        ptsTop = self.approches[0]
        if liste_possibles_chiffres[0] < len(self.valeur):
            ptsTop = max(ptsTop, self.valeur[liste_possibles_chiffres[0]])
        else:
            ptsTop = max(ptsTop, self.valeur[-1])

        ptsUtil = 0
        for ii in range(0, min(len(liste_possibles_chiffres), len(self.approches))):
            if liste_possibles_chiffres[ii] == distance_BC:
                ptsUtil = max(ptsUtil, self.approches[ii])
        if distance_BC < len(self.valeur):
            ptsUtil = max(ptsUtil, self.valeur[distance_BC])
        else:
            ptsUtil = max(ptsUtil, self.valeur[-1])
        return (ptsUtil, ptsTop)



class calcul:
    # pour simplifier les calculs : retire les parenthèses inutiles, regroupe les sommes et les produits
    def __init__(self):
        self.operateur = ''
        self.elements = []
        self.valeurs = []
        self.valeur = []
        self.operateurs_inverse = []
        self.operateur_inverse = 0

    def Set_calcul(self,chaine):
        idx_ouvre = []
        idx_ferme = []
        niveau_parenthese = []
        operateurs = ['+','-','/','*']
        self.valeur = eval(chaine)
        for ii in range(0,len(chaine)):
            if ii==0:
                niveau_parenthese.append(0)
            if chaine[ii] == '(':
                idx_ouvre.append(ii)
                niveau_parenthese.append(niveau_parenthese[-1]+1)
            elif chaine[ii] == ')':
                idx_ferme.append(ii)
                if chaine[ii-1] == ')':
                    niveau_parenthese.append(niveau_parenthese[-1] - 1)
                else:
                    niveau_parenthese.append(niveau_parenthese[-1])
            elif ii > 0:
                if chaine[ii-1] == ')':
                    niveau_parenthese.append(niveau_parenthese[-1] - 1)
                else:
                    niveau_parenthese.append(niveau_parenthese[-1])
            else:
                niveau_parenthese.append(niveau_parenthese[-1])
        niveau_parenthese = niveau_parenthese[1:]
        for ii in range(0, len(chaine)):
            if niveau_parenthese[ii]==0:
                if chaine[ii] in operateurs:
                    self.operateur = chaine[ii]
                    idx_operateur = ii
        chaine1 = chaine[:idx_operateur].strip()
        chaine2 = chaine[idx_operateur+1:].strip()

        objet_chaine1 = 0
        objet_chaine2 = 0
        if chaine1[0]=='(' and chaine1[-1]==')':
            chaine1 = chaine1[1:-1]
            objet_chaine1 = 1
        if chaine2[0]=='(' and chaine2[-1]==')':
            chaine2 = chaine2[1:-1]
            objet_chaine2 = 1
        if objet_chaine1==0:
            self.elements.append(int(eval(chaine1)))
        else:
            temp = calcul()
            temp.Set_calcul(chaine1)
            self.elements.append(temp)
        if objet_chaine2==0:
            self.elements.append(int(eval(chaine2)))
        else:
            temp = calcul()
            temp.Set_calcul(chaine2)
            self.elements.append(temp)
        for ii in range(0,len(self.elements)):
            if isinstance(self.elements[ii], calcul):
                self.valeurs.append(self.elements[ii].valeur)
            else:
                self.valeurs.append(self.elements[ii])
            self.operateurs_inverse.append(1)
        self.operateur_inverse = 1

    def Eval(self):
        valeur = 3141592
        self.valeurs = []
        for ii in range(0, len(self.elements)):
            if isinstance(self.elements[ii], calcul):
                self.elements[ii].Eval()
                if self.operateurs_inverse[ii]==1:
                    self.valeurs.append(self.elements[ii].valeur)
                else:
                    self.valeurs.append(-self.elements[ii].valeur)
            else:
                self.valeurs.append(self.elements[ii])
        if self.operateur=='+':
            valeur = 0
            for ii in range(0, len(self.valeurs)):
                valeur = valeur + self.valeurs[ii]
        elif self.operateur=='-':
            valeur = self.valeurs[0] - self.valeurs[1]
        elif self.operateur=='*':
            valeur = 1
            for ii in range(0, len(self.valeurs)):
                if self.valeurs[ii]>0:
                    valeur = valeur * self.valeurs[ii]
                elif self.valeurs[ii]<0:
                    valeur = valeur // (-self.valeurs[ii])
        elif self.operateur=='/':
            valeur = self.valeurs[0] // self.valeurs[1]
        self.valeur = valeur


    def Del_operateurs_inverses(self):
        self.operateurs_inverse = []
        for operation in self.elements:
            if isinstance(operation, calcul):
                operation.Del_operateurs_inverses()
                self.operateurs_inverse.append(operation.operateur_inverse)
            else:
                self.operateurs_inverse.append(1)
        if self.operateur=='-':
            self.operateur = '+'
            self.valeurs[1] = -self.valeurs[1]
            if isinstance(self.elements[1], calcul):
                self.operateurs_inverse[1] = -1
                self.elements[1].operateur_inverse = -1
            else:
                self.elements[1] = -self.elements[1]

        if self.operateur=='/':
            self.operateur = '*'
            self.valeurs[1] = -self.valeurs[1]
            if isinstance(self.elements[1], calcul):
                self.operateurs_inverse[1] = -1
                self.elements[1].operateur_inverse = -1
            else:
                self.elements[1] = -self.elements[1]

    def Simplify2(self):
        copie_elements = self.elements.copy()
        copie_operateurs_inverse = self.operateurs_inverse.copy()
        if self.operateur == '+':
            for ii in range(0, len(self.elements)):
                if isinstance(self.elements[ii], calcul):
                    self.elements[ii].Simplify2()
                    if self.elements[ii].operateur=='+':

                        if isinstance(self.elements[ii].elements[0], calcul):
                            copie_elements[ii] = self.elements[ii].elements[0]
                            copie_operateurs_inverse[ii] = self.operateurs_inverse[ii] * self.elements[ii].operateurs_inverse[0]
                        else:
                            if self.operateurs_inverse[ii]==1:
                                copie_elements[ii] = self.elements[ii].elements[0]
                                copie_operateurs_inverse[ii] = 1
                            else:
                                copie_elements[ii] = -self.elements[ii].elements[0]
                                copie_operateurs_inverse[ii] = 1

                        for jj in range(1, len(self.elements[ii].elements)):
                            if isinstance(self.elements[ii].elements[jj], calcul):
                                copie_elements.append(self.elements[ii].elements[jj])
                                copie_operateurs_inverse.append(self.operateurs_inverse[ii] * self.elements[ii].operateurs_inverse[jj])
                            else:
                                if self.operateurs_inverse[ii]==1:
                                    copie_elements.append(self.elements[ii].elements[jj])
                                    copie_operateurs_inverse.append(1)
                                else:
                                    copie_elements.append(-self.elements[ii].elements[jj])
                                    copie_operateurs_inverse.append(1)

        if self.operateur == '*':
            for ii in range(0, len(self.elements)):
                if isinstance(self.elements[ii], calcul):
                    self.elements[ii].Simplify2()
                    if self.elements[ii].operateur == '*':

                        if isinstance(self.elements[ii].elements[0], calcul):
                            copie_elements[ii] = self.elements[ii].elements[0]
                            copie_operateurs_inverse[ii] = self.operateurs_inverse[ii] * self.elements[ii].operateurs_inverse[0]
                        else:
                            if self.operateurs_inverse[ii] == 1:
                                copie_elements[ii] = self.elements[ii].elements[0]
                                copie_operateurs_inverse[ii] = 1
                            else:
                                copie_elements[ii] = -self.elements[ii].elements[0]
                                copie_operateurs_inverse[ii] = 1

                        for jj in range(1, len(self.elements[ii].elements)):
                            if isinstance(self.elements[ii].elements[jj], calcul):
                                copie_elements.append(self.elements[ii].elements[jj])
                                copie_operateurs_inverse.append(self.operateurs_inverse[ii] * self.elements[ii].operateurs_inverse[jj])
                            else:
                                if self.operateurs_inverse[ii] == 1:
                                    copie_elements.append(self.elements[ii].elements[jj])
                                    copie_operateurs_inverse.append(1)
                                else:
                                    copie_elements.append(-self.elements[ii].elements[jj])
                                    copie_operateurs_inverse.append(1)

        self.elements = copie_elements
        self.operateurs_inverse = copie_operateurs_inverse
        self.Eval()


    def Range(self):
        for el in self.elements:
            if isinstance(el, calcul):
                el.Range()
        copie_el = self.elements.copy()
        copie_val = self.valeurs.copy()
        copie_inv = self.operateurs_inverse.copy()

        copie = self.valeurs.copy()
        idx = []

        # pour ne pas avoir une solution qui s'écrit 9*(7+2) et l'autre (7+2)*9
        while len(copie)>0:
            valMax = max(copie)
            idxTemp = []
            idxTemp2 = []
            valeur_associee = []
            idxTemp_del = []
            for ii in range(0, len(self.valeurs)):
                if self.valeurs[ii]==valMax:
                    idxTemp.append(ii)
            for ii in range(0, len(copie)):
                if copie[ii]==valMax:
                    idxTemp_del.append(ii)
            for idx0 in idxTemp:
                if isinstance(self.elements[idx0], calcul):
                    valeur_associee.append(self.elements[idx0].valeurs[1]-self.elements[idx0].valeurs[0])
                else:
                    valeur_associee.append(-12345)
            idx2 = sorted(range(len(valeur_associee)), key=lambda k: valeur_associee[k], reverse=True)
            for ii in range(0, len(idx2)):
                idx.append(idxTemp[idx2[ii]])
            for ii in range(0, len(idxTemp_del)):
                copie.remove(valMax)




        # idx = sorted(range(len(self.valeurs)), key=lambda k: self.valeurs[k], reverse=True)
        self.valeurs = []
        self.elements = []
        self.operateurs_inverse = []

        for ii in idx:
            self.valeurs.append(copie_val[ii])
            self.elements.append(copie_el[ii])
            self.operateurs_inverse.append(copie_inv[ii])

    def Get_chaine(self):
        cha = ''
        if self.operateur == '+':
            if isinstance(self.elements[0], calcul):
                cha = self.elements[0].Get_chaine()
            else:
                cha = str(self.valeurs[0])
            for ii in range(1, len(self.elements)):
                if isinstance(self.elements[ii], calcul):
                    cha0 = self.elements[ii].Get_chaine()
                    if self.operateurs_inverse[ii] == -1:
                        cha = cha + ' - ' + cha0
                    else:
                        cha = cha + ' + ' + cha0
                else:
                    if self.valeurs[ii] > 0:
                        cha = cha + ' + ' + str(self.valeurs[ii])
                    else:
                        cha = cha + ' - ' + str(-self.valeurs[ii])
        if self.operateur == '*':
            if isinstance(self.elements[0], calcul):
                cha = '(' + self.elements[0].Get_chaine() + ')'
            else:
                cha = str(self.valeurs[0])
            for ii in range(1, len(self.elements)):
                if isinstance(self.elements[ii], calcul):
                    cha0 = self.elements[ii].Get_chaine()
                    if self.operateurs_inverse[ii] == -1:
                        cha = cha + ' / (' + cha0 + ')'
                    else:
                        cha = cha + ' * (' + cha0 + ')'
                else:
                    if self.valeurs[ii] > 0:
                        cha = cha + ' * ' + str(self.valeurs[ii])
                    else:
                        cha = cha + ' / ' + str(-self.valeurs[ii])
        return(cha)








    def Simplify(self):
        if self.operateur == '+':
            element_save = self.elements.copy()
            for ii in range(0,len(element_save)):
                self.elements.pop(0)

            for ii in range(0, len(element_save)):
                if isinstance(element_save[ii], calcul):
                    if element_save[ii].operateur == '+':
                        for jj in range(0, len(element_save[ii].elements)):
                            self.elements.append(element_save[ii].elements[jj])
                    if element_save[ii].operateur == '*':
                        self.elements.append(element_save[ii])
                else:
                    self.elements.append(element_save[ii])
        if self.operateur == '*':
            element_save = self.elements.copy()
            for ii in range(0,len(element_save)):
                self.elements.pop(0)
            for ii in range(0, len(element_save)):
                if isinstance(element_save[ii], calcul):
                    if element_save[ii].operateur == '+':
                        self.elements.append(element_save[ii])
                    if element_save[ii].operateur == '*':
                        val = []
                        val0 = []
                        val1 = []
                        for jj in range(0, len(element_save[ii].elements)):
                            val.append(eval(element_save[ii].elements[jj]))
                            val1.append(element_save[ii].elements[jj])
                        idx = sorted(range(len(val)), key=lambda k: val[k])
                        for jj in range(0, len(val0)):
                            val1.append(val0[idx[jj]])
                        cha = val1[0]
                        for jj in range(1, len(val1)):
                            cha = cha + ' * ' + val1[jj]
                        self.elements.append(cha)
                else:
                    self.elements.append(element_save[ii])

def get_chaine_simplifiee(chaine):
    op = calcul()
    op.Set_calcul(chaine)
    op.Del_operateurs_inverses()
    op.Simplify2()
    op.Range()
    cha = op.Get_chaine()
    return cha




