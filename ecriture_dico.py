from classe import *
from loadConsVoy import *
from affichage import *
import tkinter as tk
import time
import tkinter.font as tkFont
import pygame
from icones import *
from tirage import *
import numpy
from motUtilisateur import *
#from datetime import timedelta, datetime, date, time


nbLettres = 11
nbVoy = 5 # par défaut

# Chargement des données
don = Data()
don.SetNbLettres(nbLettres, nbVoy)
don.LoadDico()

basique = []
complet = []

for ii in range(len(don.dico)):
    for jj in range(len(don.dico[ii].basique)):
        basique.append(don.dico[ii].basique[jj])
        complet.append(don.dico[ii].complet[jj])

idx = sorted(range(len(basique)), key=lambda k: basique[k])
cha = ''
for ii in idx:
    cha = cha + complet[ii] + '\n\n'

f = open("dictionnaire.txt", "a")
f.write(cha)
f.close()

# res_list = [i for i in range(len(don.dico[idx_dico].alpha)) if
#                             don.dico[idx_dico].alpha[i] == prop_sort]



