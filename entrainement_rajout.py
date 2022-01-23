import tkinter as tk
import numpy
from tkinter import *
import random
import tkinter.font as tkFont

def loadTirages(nomFichier, nomOublis):
    fichier = open(nomFichier, "r")
    liste = []
    for line in fichier.readlines():
        temp = line.strip().split('|')
        if len(temp) == 2:
            temp2 = temp[0].split('(')
            temp3 = temp2[1].split(')')
            tirage = temp2[0].strip()
            nbLettres = temp3[0]
            solutions = temp[1].strip()
            liste.append([tirage, nbLettres, solutions])
    fichier.close()

    try:
        fichier2 = open(nomOublis, "r")
        liste2 = []
        for line in fichier2.readlines():
            temp = line.strip().split('|')
            if len(temp) == 2:
                temp2 = temp[0].split('(')
                temp3 = temp2[1].split(')')
                tirage = temp2[0].strip()
                nbLettres = temp3[0]
                solutions = temp[1].strip()
                liste.append([tirage, nbLettres, solutions])
        fichier2.close()
    except:
        a = 1
    return liste

class listeTirages():
    def __init__(self):
        self.complet = []
        self.recents = []
        self.tres_recents = []
        self.oublis = []

def loadTirages_evoluee(nomFichier, nomOublis):
    fichier = open(nomFichier, "r")
    liste = []
    for line in fichier.readlines():
        temp = line.strip().split('|')
        if len(temp) == 2:
            tirage = temp[0].strip()
            nbLettres = 0
            solutions = temp[1].strip()
            liste.append([tirage, nbLettres, solutions])
    fichier.close()

    listeTresRecents = []
    listeRecents = []
    listeOublis = []
    if len(liste)>48:
        for ii in range(0,48):
            listeTresRecents.append(liste[len(liste)-1-ii])
    if len(liste)>240:
        for ii in range(0,240):
            listeRecents.append(liste[len(liste)-1-ii])


    try:
        fichier2 = open(nomOublis, "r")
        liste2 = []
        for line in fichier2.readlines():
            temp = line.strip().split('|')
            if len(temp) == 2:
                tirage = temp[0].strip()
                nbLettres = 0
                solutions = temp[1].strip()
                listeOublis.append([tirage, nbLettres, solutions])
                liste.append([tirage, nbLettres, solutions])
        fichier2.close()
    except:
        a = 1

    liste_Tirages = listeTirages()
    liste_Tirages.complet = liste
    liste_Tirages.recents = listeRecents
    liste_Tirages.tres_recents = listeTresRecents
    liste_Tirages.oublis = listeOublis
    return liste_Tirages
    # return liste, listeTresRecents, listeRecents, listeOublis

class etat:
    def __init__(self):
        etat.valeur = 0
        etat.tirage = ''
        etat.nbLettres = 0
        etat.solution = ''
        etat.fen = []
        etat.sauvegardePossible = 1
        etat.nb = 0

def lancementTirage(tirages, labels, etat, T, label_nb):
    if etat.valeur == 0:
        etat.nb += 1
        etat.sauvegardePossible = 1
        for ii in labels:
            ii.configure(text='')

        if not isinstance(tirages, list):
            r = random.randint(1,100)
            pascontent = 1
            if r<=20:
                if len(tirages.tres_recents):
                    r = random.randint(1, len(tirages.tres_recents))
                    tirage = tirages.tres_recents[r - 1][0]
                    nbLettres = tirages.tres_recents[r - 1][1]
                    solution = tirages.tres_recents[r - 1][2]
                    pascontent = 0
            elif r<=40:
                if len(tirages.recents):
                    r = random.randint(1, len(tirages.recents))
                    tirage = tirages.recents[r - 1][0]
                    nbLettres = tirages.recents[r - 1][1]
                    solution = tirages.recents[r - 1][2]
                    pascontent = 0
            elif r<=50:
                if len(tirages.oublis):
                    r = random.randint(1, len(tirages.oublis))
                    tirage = tirages.oublis[r - 1][0]
                    nbLettres = tirages.oublis[r - 1][1]
                    solution = tirages.oublis[r - 1][2]
                    pascontent = 0
            if pascontent:
                r = random.randint(1, len(tirages.complet))
                tirage = tirages.complet[r - 1][0]
                nbLettres = tirages.complet[r - 1][1]
                solution = tirages.complet[r - 1][2]
        else:
            n = len(tirages)
            r = random.randint(1, n)
            tirage = tirages[r - 1][0]
            nbLettres = tirages[r - 1][1]
            solution = tirages[r - 1][2]
        x = [280]
        y = [60]
        namefont = "Helvetica"
        fontsize = 32
        etat.tirage = tirage
        etat.nbLettres = nbLettres
        etat.solution = solution

        # affichage du nombre de tirages
        label_nb.configure(text=str(etat.nb))

        # value = tk.StringVar(etat.fen)
        # value.set('')
        T.delete('1.0', END)
        # T.configure(text='')
        # T.configure(textvariable=value)

        labels[0].place(x=x[0], y=y[0], anchor=CENTER)
        labels[0].configure(font=(namefont, fontsize), text=tirage)
    else:
        cha = etat.solution
        # value = tk.StringVar(etat.fen)
        # value.set(cha)
        # T.configure(text=cha)
        T.insert(INSERT, cha)
    etat.valeur = 1 - etat.valeur  # pour un passage au nouveau tirage ou l'affichage des solutions




def ajoutOubli(etat, fichierOublis):
    if etat.sauvegardePossible:
        f = open(fichierOublis, "a")
        cha = etat.tirage + ' | ' + etat.solution + '\n'
        f.write(cha)
        f.close()
    etat.sauvegardePossible = 0



indice = etat()

nomFichier = "listeRajouts.txt"
fichierOublis = "listeRajoutsOublies.txt"
listeTirages = loadTirages_evoluee(nomFichier, fichierOublis)


fenetre = tk.Tk()
indice.fen = fenetre
fenetre.title('entraînement rajouts')
fenetre.geometry('800x230')
labels_lettres = []

labels_lettres.append(Label(fenetre))

valider = Button(fenetre)
valider.configure(font=("Helvetica", 25), text="ok")
valider.place(x=700, y=40, anchor=CENTER, width=150, height=50)
valider.configure(command=lambda: lancementTirage(listeTirages, labels_lettres, indice, T, label_nb))

oublis = Button(fenetre)
oublis.configure(font=("Helvetica", 25), text="ajouter")
oublis.place(x=700, y=100, anchor=CENTER, width=150, height=50)
oublis.configure(command=lambda: ajoutOubli(indice, fichierOublis))


label_nb = Label(fenetre)
label_nb.configure(font=("Helvetica", 25), text=str(indice.nb), fg='red')
label_nb.place(x=600, y=20, anchor=CENTER)

value = tk.StringVar(fenetre)
# cha = ''
# value.set(cha)
T = tk.Text(fenetre)
T.insert(INSERT, '')
T.place(x=20, y=140, width=760, height=60)
T.configure(font=("Helvetica", 14))


def ajoutOubli_event(event):
    ajoutOubli(indice, fichierOublis)

def lancementTirage_event(event):
    lancementTirage(listeTirages, labels_lettres, indice, T, label_nb)

fenetre.bind("<Return>", lancementTirage_event)
fenetre.bind("<p>", ajoutOubli_event)

lancementTirage(listeTirages, labels_lettres, indice, T, label_nb)


fenetre.mainloop()