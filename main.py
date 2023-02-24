from classe import *
from loadConsVoy import *
import tkinter as tk
import time
import tkinter.font as tkFont
import pygame
from icones import *
from tirage import *
import numpy
from motUtilisateur import *
#from datetime import timedelta, datetime, date, time

# from solveur_compte import *

nbLettres = 11
nbVoy = 5 # par défaut

# Chargement des données
don = Data()
don.SetNbLettres(nbLettres, nbVoy)
don.LoadDico()

duree_totale = 40
duree_ecriture_lettres = 10

pt_total = 0
top_total = 0

def testf():
    global chrono, icones, don
    if chrono.actif:
        chrono.decrement()
        icones.chrono.configure(text=chrono.val_actuelle)
    if abs(chrono.val_actuelle - chrono.val_ecriture) < 0.5:
        if don.son_actif:
            pygame.mixer.init()
            pygame.mixer.music.load('sons/ECRIVEZ.mp3')
            pygame.mixer.music.play()
    if chrono.fini:
        if don.son_actif:
            pygame.mixer.music.load('sons/GONG.mp3')
            pygame.mixer.music.play()
            if don.type_actuel=='chiffres':
                tirage.Solveur_chiffres(don)
            else:
                tirage.Solveur(don)
    Mafenetre.after(1000, testf)
#





chrono = Chrono(duree_totale)
Mafenetre = tk.Tk()
Mafenetre.title('Le Confiné')

cha = str(don.geom.taille_x0) + 'x' + str(don.geom.taille_y0)
Mafenetre.geometry(cha)

tirage = Tirage(don)
motUtilisateur = MotUtilisateur()

icones = Icones(Mafenetre)
icones.Lancement(tirage, don, chrono, motUtilisateur)
#icones.Lancement_tirage_lettres(tirage, don, chrono, motUtilisateur)

listePlaques = [1,2,3,4,5,6,7,8,9,10,25,50,75,100,1,2,3,4,5,6,7,8,9,10]

testf()
Mafenetre.configure(bg=don.proprietes.couleur_fond)
Mafenetre.mainloop()




