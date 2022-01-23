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
            temp2 = temp[0].split('(')
            temp3 = temp2[1].split(')')
            tirage = temp2[0].strip()
            nbLettres = temp3[0]
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
                temp2 = temp[0].split('(')
                temp3 = temp2[1].split(')')
                tirage = temp2[0].strip()
                nbLettres = temp3[0]
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
        x = [75, 110, 145, 180, 215, 250, 285]
        y = [50, 120, 190, 260]
        namefont = "Helvetica"
        fontsize = 42
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

        if len(tirage) == 10:
            labels[0].place(x=x[3], y=y[0], anchor=CENTER)
            labels[0].configure(font=(namefont, fontsize), text=tirage[0])

            labels[1].place(x=x[2], y=y[1], anchor=CENTER)
            labels[1].configure(font=(namefont, fontsize), text=tirage[1])

            labels[2].place(x=x[4], y=y[1], anchor=CENTER)
            labels[2].configure(font=(namefont, fontsize), text=tirage[2])

            labels[3].place(x=x[1], y=y[2], anchor=CENTER)
            labels[3].configure(font=(namefont, fontsize), text=tirage[3])

            labels[4].place(x=x[3], y=y[2], anchor=CENTER)
            labels[4].configure(font=(namefont, fontsize), text=tirage[4])

            labels[5].place(x=x[5], y=y[2], anchor=CENTER)
            labels[5].configure(font=(namefont, fontsize), text=tirage[5])

            labels[6].place(x=x[0], y=y[3], anchor=CENTER)
            labels[6].configure(font=(namefont, fontsize), text=tirage[6])

            labels[7].place(x=x[2], y=y[3], anchor=CENTER)
            labels[7].configure(font=(namefont, fontsize), text=tirage[7])

            labels[8].place(x=x[4], y=y[3], anchor=CENTER)
            labels[8].configure(font=(namefont, fontsize), text=tirage[8])

            labels[9].place(x=x[6], y=y[3], anchor=CENTER)
            labels[9].configure(font=(namefont, fontsize), text=tirage[9])

            labels[10].place(x=x[0] -40, y=y[0]-5, anchor=CENTER)
            labels[10].configure(font=(namefont, int(0.7*fontsize)), text=etat.nbLettres)

            labels[11].place(x=x[0], y=y[0]-50, anchor=CENTER)
            labels[11].configure(font=(namefont, fontsize), text='')
        if len(tirage) == 11:
            labels[0].place(x=x[2], y=y[0], anchor=CENTER)
            labels[0].configure(font=(namefont, fontsize), text=tirage[0])

            labels[1].place(x=x[4], y=y[0], anchor=CENTER)
            labels[1].configure(font=(namefont, fontsize), text=tirage[1])

            labels[2].place(x=x[2], y=y[1], anchor=CENTER)
            labels[2].configure(font=(namefont, fontsize), text=tirage[2])

            labels[3].place(x=x[4], y=y[1], anchor=CENTER)
            labels[3].configure(font=(namefont, fontsize), text=tirage[3])

            labels[4].place(x=x[1], y=y[2], anchor=CENTER)
            labels[4].configure(font=(namefont, fontsize), text=tirage[4])

            labels[5].place(x=x[3], y=y[2], anchor=CENTER)
            labels[5].configure(font=(namefont, fontsize), text=tirage[5])

            labels[6].place(x=x[5], y=y[2], anchor=CENTER)
            labels[6].configure(font=(namefont, fontsize), text=tirage[6])

            labels[7].place(x=x[0], y=y[3], anchor=CENTER)
            labels[7].configure(font=(namefont, fontsize), text=tirage[7])

            labels[8].place(x=x[2], y=y[3], anchor=CENTER)
            labels[8].configure(font=(namefont, fontsize), text=tirage[8])

            labels[9].place(x=x[4], y=y[3], anchor=CENTER)
            labels[9].configure(font=(namefont, fontsize), text=tirage[9])

            labels[10].place(x=x[6], y=y[3], anchor=CENTER)
            labels[10].configure(font=(namefont, fontsize), text=tirage[10])

            labels[11].place(x=x[0] - 40, y=y[0]-5, anchor=CENTER)
            labels[11].configure(font=(namefont, int(0.7*fontsize)), text=etat.nbLettres)
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
        cha = etat.tirage + ' (' + etat.nbLettres + ') | ' + etat.solution + '\n'
        f.write(cha)
        f.close()
    etat.sauvegardePossible = 0



indice = etat()

nomFichier = "listeTirages.txt"
fichierOublis = "oublis.txt"
# listeTirages = loadTirages(nomFichier, fichierOublis)
listeTirages = loadTirages_evoluee(nomFichier, fichierOublis)


fenetre = tk.Tk()
indice.fen = fenetre
fenetre.title('entraînement tirages')
fenetre.geometry('360x500')
labels_lettres = []
for ii in range(12):
    labels_lettres.append(Label(fenetre))

valider = Button(fenetre)
valider.configure(font=("Helvetica", 25), text="ok")
valider.place(x=90, y=340, anchor=CENTER, width=150, height=50)
valider.configure(command=lambda: lancementTirage(listeTirages, labels_lettres, indice, T, label_nb))

oublis = Button(fenetre)
oublis.configure(font=("Helvetica", 25), text="ajouter")
oublis.place(x=270, y=340, anchor=CENTER, width=150, height=50)
oublis.configure(command=lambda: ajoutOubli(indice, fichierOublis))

label_nb = Label(fenetre)
label_nb.configure(font=("Helvetica", 25), text=str(indice.nb), fg='red')
label_nb.place(x=330, y=20, anchor=CENTER)

value = tk.StringVar(fenetre)
# cha = ''
# value.set(cha)
T = tk.Text(fenetre)
T.insert(INSERT, '')
T.place(x=20, y=398, width=320, height=95)
T.configure(font=("Helvetica", 14))


def ajoutOubli_event(event):
    ajoutOubli(indice, fichierOublis)

def lancementTirage_event(event):
    lancementTirage(listeTirages, labels_lettres, indice, T, label_nb)

fenetre.bind("<Return>", lancementTirage_event)
fenetre.bind("<p>", ajoutOubli_event)

lancementTirage(listeTirages, labels_lettres, indice, T, label_nb)


        # root.bind("<F2>", maFoncF2)


# labels_lettres.place(x=50 + ii * 66, y=75, anchor=CENTER, width=60, height=60)
#     self.labels_rajouts[-1].configure(bg='antiquewhite', font=("Helvetica", 36),
#                                       text='', borderwidth=0.5, relief="solid")
#
#         bouton1 = Checkbutton(Mafenetre)
#         var1 = tk.BooleanVar()
#         var1.set(True)
#         bouton1.place(x=140, y=160, anchor=CENTER)
#         bouton1.configure(font=("Helvetica", 36), text='+1', variable=var1, command=lambda: modif(don,1))
#         bouton1.select()

  # Mafenetre.bind("<Z>", rajouts_addLettre)
  #       Mafenetre.bind("<BackSpace>", rajout_delLettre)
  #       Mafenetre.bind("<Return>", rajout_valide)

fenetre.mainloop()