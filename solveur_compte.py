#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Create arithmetic expression approaching target value
# jill-jenn vie et christoph durr et jean-christophe filliatre - 2014-2017


# snip{
def arithm_expr_target(x, target):
    """ Create arithmetic expression approaching target value
    :param x: allowed constants
    :param target: target value
    :returns: string in form 'expression=value'
    :complexity: huge
    """
    soluce = ''
    n = len(x)
    expr = [{} for _ in range(1 << n)]  # expr[S][val] = string of expr. of value val using only values from set S
    for i in range(n):
        expr[1 << i] = {x[i]: str(x[i])}   # store singletons
    tout = (1 << n) - 1
    for S in range(3, tout + 1): # 3 = first number which is not a power of 2
        if expr[S] != {}:
            continue             # in that case S is a power of 2
        for L in range(1, S):    # decompose set S into non-empty sets L and R
            if L & S == L:
                R = S ^ L
                for vL in expr[L]:         # combine expressions from L
                    for vR in expr[R]:     # with expressions from R
                        eL = expr[L][vL]
                        eR = expr[R][vR]
                        expr[S][vL] = eL
                        if vL > vR:        # difference cannot become negative
                            expr[S][vL - vR] = "(%s-%s)" % (eL, eR)
                        if L < R:   # briser la symétrie
                            expr[S][vL + vR] = "(%s+%s)" % (eL, eR)
                            expr[S][vL * vR] = "(%s*%s)" % (eL, eR)
                        if vR != 0 and vL % vR == 0:  # only integer divisions
                            expr[S][vL // vR] = "\n(%s/%s)" % (eL, eR)
    # chercher expression la plus proche du but
    for dist in range(target + 1):
        for sign in [-1, +1]:
            val = target + sign * dist
            if val in expr[tout]:
                return "%s=%i" % (expr[tout][val], val)
                # soluce = soluce + '\n' + "%s=%i" % (expr[tout][val], val)
    # partie jamais atteinte si x contient des nombres entre 0 et but
    pass
# snip}

def test_solveur(x, target):
    valeurs = []
    if len(x)==2:
        for ii in range(0,len(x[0])):
            for jj in range(0,len(x[1])):
                if isinstance(x[0][ii], int) and isinstance(x[1][jj], int):
                    valeurs.append(x[0][ii]+x[1][jj])
                    valeurs.append(x[0][ii] * x[1][jj])
                    valeurs.append(abs(x[0][ii] - x[1][jj]))
                    if not x[0][ii] % x[1][jj]:
                        print(1)
                        valeurs.append(x[0][ii]//x[1][jj])
                    elif not x[1][jj] % x[0][ii]:
                        print(2)
                        valeurs.append(x[1][jj] // x[0][ii])
                    else:
                        valeurs.append([])
                else:
                    valeurs.append([])
                    valeurs.append([])
                    valeurs.append([])
                    valeurs.append([])
    else:
        for ii in range(0,len(x)):
            z = [a for i, a in enumerate(x) if i != ii]
            y = []
            y.append(x[ii])
            a = []
            a.append(y)
            w = []
            for jj in range(0,len(x)):
                if jj != ii:
                    w.append(x[jj])
            a.append(w)
            val = test_solveur(w,target)
            for kk in range(0, len(x[ii])):
                for jj in range(0, len(val)):
                    if isinstance(val[jj], int):
                        valeurs.append(x[ii][kk] + val[jj])
                        valeurs.append(x[ii][kk] * val[jj])
                        valeurs.append(abs(x[ii][kk] - val[jj]))
                        if val[jj]>0 and x[ii][kk]>0:
                            if not x[ii][kk] % val[jj]:
                                valeurs.append(x[ii][kk] // val[jj])
                            elif not val[jj] % x[ii][kk]:
                                valeurs.append(val[jj] // x[ii][kk])
                            else:
                                valeurs.append([])
                        else:
                            valeurs.append([])
                    else:
                        valeurs.append([])
                        valeurs.append([])
                        valeurs.append([])
                        valeurs.append([])
    return valeurs

class valeurrr:
    def __init__(self):
        self.val = []
        self.cha = []

def test_solveur2(x, target):
    valeurs = valeurrr()
    if len(x)==2:
        for ii in range(0,len(x[0])):
            for jj in range(0,len(x[1])):
                if isinstance(x[0][ii], int) and isinstance(x[1][jj], int):
                    valeurs.val.append(x[0][ii]+x[1][jj])
                    valeurs.cha.append("(%s+%s)" % (x[0][ii], x[1][jj]))
                    valeurs.val.append(x[0][ii] * x[1][jj])
                    valeurs.cha.append("(%s*%s)" % (x[0][ii], x[1][jj]))
                    valeurs.val.append(abs(x[0][ii] - x[1][jj]))
                    valeurs.cha.append("(%s-%s)" % (x[0][ii], x[1][jj]))
                    if not x[0][ii] % x[1][jj]:
                        valeurs.val.append(x[0][ii]//x[1][jj])
                        valeurs.cha.append("(%s/%s)" % (x[0][ii], x[1][jj]))
                    elif not x[1][jj] % x[0][ii]:
                        valeurs.val.append(x[1][jj] // x[0][ii])
                        valeurs.cha.append("(%s/%s)" % (x[0][ii], x[1][jj]))
                    else:
                        valeurs.val.append([])
                        valeurs.cha.append([])
                else:
                    valeurs.val.append([])
                    valeurs.val.append([])
                    valeurs.val.append([])
                    valeurs.val.append([])
                    valeurs.cha.append([])
                    valeurs.cha.append([])
                    valeurs.cha.append([])
                    valeurs.cha.append([])
    else:
        for ii in range(0,len(x)):
            w = []
            for jj in range(0,len(x)):
                if jj != ii:
                    w.append(x[jj])
            val = test_solveur2(w,target)
            for kk in range(0, len(x[ii])):
                for jj in range(0, len(val.val)):
                    if isinstance(val.val[jj], int):
                        valeurs.val.append(x[ii][kk] + val.val[jj])
                        valeurs.cha.append("(%s+%s)" % (x[ii][kk], val.cha[jj]))
                        valeurs.val.append(x[ii][kk] * val.val[jj])
                        valeurs.cha.append("(%s*%s)" % (x[ii][kk], val.cha[jj]))
                        valeurs.val.append(abs(x[ii][kk] - val.val[jj]))
                        valeurs.cha.append("(%s-%s)" % (x[ii][kk], val.cha[jj]))
                        if val.val[jj]>0 and x[ii][kk]>0:
                            if not x[ii][kk] % val.val[jj]:
                                valeurs.val.append(x[ii][kk] // val.val[jj])
                                valeurs.cha.append("(%s/%s)" % (x[ii][kk], val.cha[jj]))
                            elif not val.val[jj] % x[ii][kk]:
                                valeurs.val.append(val.val[jj] // x[ii][kk])
                                valeurs.cha.append("(%s/%s)" % (x[ii][kk], val.cha[jj]))
                            else:
                                valeurs.val.append([])
                                valeurs.cha.append([])
                        else:
                            valeurs.val.append([])
                            valeurs.cha.append([])
                    else:
                        valeurs.val.append([])
                        valeurs.val.append([])
                        valeurs.val.append([])
                        valeurs.val.append([])
                        valeurs.cha.append([])
                        valeurs.cha.append([])
                        valeurs.cha.append([])
                        valeurs.cha.append([])
    return valeurs

def test_solveur3(x):
    valeurs = valeurrr()
    if len(x)==1:
        valeurs.val.append(x[0][0])
        valeurs.cha.append(str(x[0][0]))
    if len(x)==2:
        for ii in range(0,len(x[0])):
            for jj in range(0,len(x[1])):
                if isinstance(x[0][ii], int) and isinstance(x[1][jj], int):
                    valeurs.val.append(x[0][ii]+x[1][jj])
                    valeurs.cha.append("(%s + %s)" % (x[0][ii], x[1][jj]))
                    valeurs.val.append(x[0][ii] * x[1][jj])
                    valeurs.cha.append("(%s * %s)" % (x[0][ii], x[1][jj]))
                    if x[0][ii] - x[1][jj] > 0:
                        valeurs.val.append(x[0][ii] - x[1][jj])
                        valeurs.cha.append("(%s - %s)" % (x[0][ii], x[1][jj]))
                    elif x[1][jj] - x[0][ii] > 0:
                        valeurs.val.append(x[1][jj] - x[0][ii])
                        valeurs.cha.append("(%s - %s)" % (x[1][jj], x[0][ii]))
                    else:
                        valeurs.val.append([])
                        valeurs.cha.append([])
                    if not x[0][ii] % x[1][jj]:
                        valeurs.val.append(x[0][ii]//x[1][jj])
                        valeurs.cha.append("(%s / %s)" % (x[0][ii], x[1][jj]))
                    elif not x[1][jj] % x[0][ii]:
                        valeurs.val.append(x[1][jj] // x[0][ii])
                        valeurs.cha.append("(%s / %s)" % (x[0][ii], x[1][jj]))
                    else:
                        valeurs.val.append([])
                        valeurs.cha.append([])
                else:
                    valeurs.val.append([])
                    valeurs.val.append([])
                    valeurs.val.append([])
                    valeurs.val.append([])
                    valeurs.cha.append([])
                    valeurs.cha.append([])
                    valeurs.cha.append([])
                    valeurs.cha.append([])
    else:
        # obtention des partitions de x en 2 parties
        # la première partie est d'une taille inférieure ou égale à la seconde
        liste_parties = partiesliste_2(x)
        # print(liste_parties)
        for ii in range(0,(len(liste_parties))):
            w1 = liste_parties[ii][0]
            w2 = liste_parties[ii][1]
            val1 = test_solveur3(w1)
            val2 = test_solveur3(w2)
            # print('***')
            # print(w1)
            # print(w2)
            # print(val1.cha)
            # print(val1.val)
            # print(val2.cha)
            # print(val2.val)

            for kk in range(0, len(val1.val)):
                for jj in range(0, len(val2.val)):
                    if isinstance(val1.val[kk], int) and isinstance(val2.val[jj], int):
                        # print('uuu')
                        # if kk==0 and jj==43 and ii==3:
                        #     print(kk)
                        #     print(jj)
                        #     print(ii)
                        #     print(val1.cha[kk])
                        #     print(val1.val[kk])
                        #     print(val2.cha[jj])
                        #     print(val2.val[jj])
                        # print("(%s+%s)" % (val1.cha[kk], val2.cha[jj]))
                        valeurs.val.append(val1.val[kk] + val2.val[jj])
                        valeurs.cha.append("(%s + %s)" % (val1.cha[kk], val2.cha[jj]))
                        # print('000')
                        # print(valeurs.cha)
                        valeurs.val.append(val1.val[kk] * val2.val[jj])
                        valeurs.cha.append("(%s * %s)" % (val1.cha[kk], val2.cha[jj]))
                        if val1.val[kk] - val2.val[jj] > 0:
                            valeurs.val.append(val1.val[kk] - val2.val[jj])
                            valeurs.cha.append("(%s - %s)" % (val1.cha[kk], val2.cha[jj]))
                        elif val2.val[jj] - val1.val[kk] > 0:
                            valeurs.val.append(val2.val[jj] - val1.val[kk])
                            valeurs.cha.append("(%s - %s)" % (val2.cha[jj], val1.cha[kk]))
                        else:
                            valeurs.val.append([])
                            valeurs.cha.append([])
                        if val2.val[jj]>0 and val1.val[kk]>0:
                            if not val1.val[kk] % val2.val[jj]:
                                valeurs.val.append(val1.val[kk] // val2.val[jj])
                                valeurs.cha.append("(%s / %s)" % (val1.cha[kk], val2.cha[jj]))
                            elif not val2.val[jj] % val1.val[kk]:
                                valeurs.val.append(val2.val[jj] // val1.val[kk])
                                valeurs.cha.append("(%s / %s)" % (val2.cha[jj], val1.cha[kk]))
                            else:
                                valeurs.val.append([])
                                valeurs.cha.append([])
                        else:
                            valeurs.val.append([])
                            valeurs.cha.append([])
                    else:
                        valeurs.val.append([])
                        valeurs.val.append([])
                        valeurs.val.append([])
                        valeurs.val.append([])
                        valeurs.cha.append([])
                        valeurs.cha.append([])
                        valeurs.cha.append([])
                        valeurs.cha.append([])
    return valeurs

def partiesliste(seq):
    p = []
    i, imax = 0, 2**len(seq)-1
    while i <= imax:
        s = []
        j, jmax = 0, len(seq)-1
        while j <= jmax:
            if (i>>j)&1 == 1:
                s.append(seq[j])
            j += 1
        p.append(s)
        i += 1
    return p


def partiesliste_2(seq):
    liste_parties = []
    for ii in range(1,1+(len(seq))//2):
        if ii==1:
            for jj in range(0,len(seq)):
                par1 = []
                par2 = []
                par1.append(seq[jj])
                len_par2 = len(seq)-len(par1)
                if len(par1) != len_par2:
                    for kk in range(0,len(seq)):
                        if kk != jj:
                            par2.append(seq[kk])
                    par = []
                    par.append(par1)
                    par.append(par2)
                    liste_parties.append(par)
                elif jj < len(seq)-1:
                    for kk in range(jj+1,len(seq)):
                        par2.append(seq[kk])
                    par = []
                    par.append(par1)
                    par.append(par2)
                    liste_parties.append(par)
        if ii==2:
            for jj1 in range(0,len(seq)-1):
                for jj2 in range(jj1+1,len(seq)):
                    par1 = []
                    par2 = []
                    par1.append(seq[jj1])
                    par1.append(seq[jj2])
                    idxj = []
                    idxj.append(jj1)
                    idxj.append(jj2)
                    len_par2 = len(seq) - len(par1)
                    if len(par1) != len_par2:
                        for kk in range(0,len(seq)):
                            if kk not in idxj:
                                par2.append(seq[kk])
                        par = []
                        par.append(par1)
                        par.append(par2)
                        liste_parties.append(par)
                    elif jj1 < len(seq) - 1:
                        for kk in range(jj1+1,len(seq)):
                            if kk not in idxj:
                                par2.append(seq[kk])
                        par = []
                        if len(par2)==len(par1):
                            par.append(par1)
                            par.append(par2)
                            liste_parties.append(par)

        if ii==3:
            for jj1 in range(0,len(seq)-2):
                for jj2 in range(jj1+1,len(seq)-1):
                    for jj3 in range(jj2+1, len(seq)):
                        par1 = []
                        par2 = []
                        par1.append(seq[jj1])
                        par1.append(seq[jj2])
                        par1.append(seq[jj3])
                        idxj = []
                        idxj.append(jj1)
                        idxj.append(jj2)
                        idxj.append(jj3)
                        len_par2 = len(seq) - len(par1)
                        if len(par1) != len_par2:
                            for kk in range(0,len(seq)):
                                if kk not in idxj:
                                    par2.append(seq[kk])
                            par = []
                            par.append(par1)
                            par.append(par2)
                            liste_parties.append(par)
                        elif jj1 < len(seq) - 1:
                            for kk in range(jj1 + 1, len(seq)):
                                if kk not in idxj:
                                    par2.append(seq[kk])
                            par = []
                            if len(par2) == len(par1):
                                par.append(par1)
                                par.append(par2)
                                liste_parties.append(par)
    return liste_parties