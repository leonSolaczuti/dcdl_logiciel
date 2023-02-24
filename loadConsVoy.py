# loadConvVoy.py
# chargement des fichiers de voyelles et consonnes

import random

def genereTiragePrepaLettres(prepa):
    r = random.randint(0, len(prepa) - 1)
    tirage = prepa[r]
    return tirage

def genereTirageLettres(nbLettres,nbVoy,listeCons,listeVoy):
    idxVoy = []
    idxCons = []
    testVoy = 0
    testCons = 0

    nbLettresReste = nbLettres
    nbVoyReste = nbVoy

    tirage = ''
    cons = list(listeCons)
    voy = list(listeVoy)

    for ii in range(0,nbLettres):
        # voyelle ou consonne ?
        r = random.randint(1, nbLettresReste)
        if r <= nbVoyReste:
            testVoy = 1
            testCons = 0
            nbVoyReste = nbVoyReste-1
        else:
            testVoy = 0
            testCons = 1
        nbLettresReste = nbLettresReste-1

        # ajout de la lettre au tirage
        if testVoy:
            a = random.randint(0, len(voy)-1)
            tirage = tirage+voy[a]
            del(voy[a])
        elif testCons:
            a = random.randint(0, len(cons) - 1)
            tirage = tirage + cons[a]
            del(cons[a])
    return tirage

def genereTiragePrepaChiffres(prepa):
    r = random.randint(0, len(prepa) - 1)
    tirage = []
    l = prepa[r].split(' ')
    for ii in l:
        tirage.append(int(ii))
    return tirage

def genereTirageChiffres(nbPlaques, listePlaques, borneMin, borneMax, *args):
    nbGrossesPlaques = 314
    tirage = []
    if args:
        nbGrossesPlaques = args[0]
    # appelée par Genere_chiffres (tirage.py)
    if nbGrossesPlaques==314:
        copie_plaques = list(listePlaques)
        nbPlaquesReste = len(copie_plaques)
        # plaques
        for ii in range(0, nbPlaques):
            r = random.randint(0, nbPlaquesReste - 1)
            tirage.append(copie_plaques[r])
            nbPlaquesReste += -1
            del (copie_plaques[r])
        # compte à trouver
        tirage.append(random.randint(borneMin, borneMax))
        return tirage
    else:
        liste_grosses_plaques = []
        liste_petites_plaques = []
        for ii in range(0,len(listePlaques)):
            if listePlaques[ii]>=10:
                liste_grosses_plaques.append(listePlaques[ii])
            else:
                liste_petites_plaques.append(listePlaques[ii])
        nbPetitesPlaquesReste = len(liste_petites_plaques)
        nbGrossesPlaquesReste = len(liste_grosses_plaques)

        nb10 = 0 # pour garder les plaques 10 dans les petites plaques si elles n'ont pas déjà été utilisées
        if nbGrossesPlaques:
            for ii in range(0, nbGrossesPlaques):
                if nbGrossesPlaquesReste:
                    r = random.randint(0, nbGrossesPlaquesReste - 1)
                    tirage.append(liste_grosses_plaques[r])
                    nbGrossesPlaquesReste += -1
                    del (liste_grosses_plaques[r])
            for ii in range(0,len(tirage)):
                if tirage[ii] == 10:
                    nb10 += 1

        nbPetitesPlaques = nbPlaques - len(tirage)
        nb10_init = 0
        for ii in range(0, len(listePlaques)):
            if listePlaques[ii] == 10:
                nb10_init += 1
        nb10 = nb10_init - nb10
        nbPetitesPlaquesReste += nb10
        if nb10:
            for ii in range(0, nb10):
                liste_petites_plaques.append(10)

        for ii in range(0, nbPetitesPlaques):
            r = random.randint(0, nbPetitesPlaquesReste - 1)
            tirage.append(liste_petites_plaques[r])
            nbPetitesPlaquesReste += -1
            del (liste_petites_plaques[r])

        # compte à trouver
        tirage.append(random.randint(borneMin, borneMax))
        return tirage

