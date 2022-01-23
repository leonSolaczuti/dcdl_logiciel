from tkinter import *

def affiche(tirage):
    fenetre = Tk()
    str = 'Premier tirage :\n\n' + tirage
    label = Label(fenetre, text=str)
    label.pack()
    fenetre.mainloop()