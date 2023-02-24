from unidecode import unidecode

nomFichierLu = 'd11_v0.txt'
nomFichierEcrit = 'd11_v0.dat'
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