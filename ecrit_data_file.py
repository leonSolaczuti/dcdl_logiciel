# pour ecrire un fichier .dat (ou .txt) avec les trois colonnes a partir d'une liste de mots
# utile surtout pour les entree chaque annee
# le fichier d'entree doit etre encode en ANSI (facile a faire avec notepad)

from unidecode import unidecode

nomFichierLu = 'entrees2026_gen.txt'
nomFichierEcrit = 'entrees2026_gen.dat'
fichierLu = open(nomFichierLu, "r")
fichierEcrit = open(nomFichierEcrit,'w')

for line in fichierLu:
    sans_accent0 = unidecode(line).lower()
    sans_accent = []
    for jj in range(len(sans_accent0)):
        if ord(sans_accent0[jj])>=97 and ord(sans_accent0[jj])<=122:
            sans_accent.append(sans_accent0[jj])
    ordre_alpha = sans_accent.copy()
    ordre_alpha.sort()
    for c in ordre_alpha:
        fichierEcrit.write(c)
    fichierEcrit.write(' ')
    for c in sans_accent:
        fichierEcrit.write(c)
    fichierEcrit.write(' ')
    fichierEcrit.write(line)
fichierLu.close()
fichierEcrit.close()