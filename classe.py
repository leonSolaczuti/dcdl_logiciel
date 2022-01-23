from loadConsVoy import loadCons, loadVoy, genereTirageLettres
from affichage import *
import tkinter as tk
import time
from random import *
import tkinter.font as tkFont
import pygame
from icones import *
from tirage import *
from motUtilisateur import *
from data import *
#from datetime import timedelta, datetime, date, time



class Chrono:
    def __init__(self,val_defaut):
        self.val_defaut = val_defaut
        self.val_lettres = 40
        self.val_chiffres = 40
        self.val_ecriture_lettres = 10
        self.val_ecriture_chiffres = 20

        self.val_actuelle = val_defaut
        self.val_ecriture = 10 # pour le tirage actuelle
        self.actif = 0
        self.val_disp = ''
        self.fini = 0 # pour le lancement, une seule fois, du gong
        self.ecriture = 0 # lancement, une seule fois, du écrivez

    def decrement(self):
        if self.val_actuelle>0:
            self.val_actuelle += -1
            if self.val_actuelle <= 0:
                self.fini = 1
        else:
            self.val_actuelle = 0
            self.fini = 0

    def reset(self):
        self.val_actuelle = self.val_defaut
        self.actif = 0
        self.val_disp = ''
        self.fini = 0  # pour le lancement, une seule fois, du gong
        self.ecriture = 0  # lancement, une seule fois, du écrivez

    def reset_chiffres(self):
        # reset AVANT un tirage de chiffres
        self.val_actuelle = self.val_chiffres
        self.val_ecriture = self.val_ecriture_chiffres
        self.val_disp = ''
        self.fini = 0  # pour le lancement, une seule fois, du gong
        self.ecriture = 0  # lancement, une seule fois, du écrivez
        self.actif = 0

    def reset_lettres(self):
        # reset AVANT un tirage de lettres
        self.val_actuelle = self.val_lettres
        self.val_ecriture = self.val_ecriture_lettres
        self.val_disp = ''
        self.fini = 0  # pour le lancement, une seule fois, du gong
        self.ecriture = 0  # lancement, une seule fois, du écrivez
        self.actif = 0



def callback(lettre):
    print(lettre)


def lancement_tirage_suivant_old(don, fenetre, tirage, motUtilisateur, boutons_tirage, boutons_reponse):
    motUtilisateur.DelLettreRAZ_old(tirage, boutons_tirage, boutons_reponse)
    tirage.Genere(don)
    for ii in range(0, len(boutons_tirage)):
        boutons_tirage[ii].configure(text='')
        boutons_reponse[ii].configure(text='')
    for ii in range(0, len(boutons_tirage)):
        boutons_tirage[ii].configure(text=tirage.tirage[ii])
        time.sleep(1.1)
        boutons_tirage[ii].update()
        pygame.mixer.init()
        cha = tirage.tirage[ii].upper() + '.WAV'
        son = pygame.mixer.Sound(cha)
        son.play()





