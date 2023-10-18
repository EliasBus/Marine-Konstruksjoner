import Elementer_utvidet_matrise as ele
import Innlesning as inn

import numpy as np


def lastvektor_funk(n_knutepunkt,n_elementer, elementer_utvidet, n_punktlaster, punktlaster, n_fordelte_laster, fordelte_laster):

    fast_innsp_mom = np.zeros((n_elementer,2))
    fast_innsp_skj = np.zeros((n_elementer,2))

    idx=0

    for elem in elementer_utvidet:
        q1=0
        q2=0

        l = elem[7]
        knute_1 = elem[1]
        knute_2 = elem[2]
        for ford in fordelte_laster:
            if ford[0]==elem[0]:
                q1 = ford[3]
                q2 = ford[4]
        

        Q1 = (7/20*q1 +3/20*q2) *l     
        Q2 = (7/20*q2 +3/20*q1) *l   
        M1 = (-1/20*q1*l**2 -1/30*q2*l**2 )
        M2 = (1/20*q2*l**2 + 1/30*q1*l**2)

        #NB!
        #Antagelse! punktlast P2 vil alltid virke i punkt 11!

        

        fast_innsp_skj[idx][0] = Q1
        fast_innsp_skj[idx][1] = Q2
        fast_innsp_mom[idx][0] = M1
        fast_innsp_mom[idx][1] = M2
        #legger til M1 og M2 til matrisen med

        idx+=1

    R=np.zeros(n_knutepunkt *3)
    for i in range(n_elementer):
        theta = elementer_utvidet[i][13]

        R[(elementer_utvidet[i][1] -1)*3 + 0] += -fast_innsp_skj[i][0] * np.sin(theta)
        R[(elementer_utvidet[i][2] -1)*3 + 0] += -fast_innsp_skj[i][1] * np.sin(theta)
        #Legger til aksialspennigsbidrag til i hver første indeks i R
        R[(elementer_utvidet[i][1] -1)*3 + 1] += -fast_innsp_skj[i][0] * np.cos(theta)
        R[(elementer_utvidet[i][2] -1)*3 + 1] += -fast_innsp_skj[i][1] * np.cos(theta)
        #Legger til skjærspenningsbidrag til i hver andre indeks i R
        R[(elementer_utvidet[i][1] -1)*3 + 2] += -fast_innsp_mom[i][0]
        R[(elementer_utvidet[i][2] -1)*3 + 2] += -fast_innsp_mom[i][1]
        #Legger til bidrag fra fast_innsp_mom til hver tredje indeks i R

    return R



'''

for punk in punktlaster:
            if punk[0]==11:
                P2 = punk[0]
                P2_ortogonal = -np.sin(punk[1]) * P2

        if elem[0] == 911:
            M1 += -P2_ortogonal *l
            #moment i punkt 9 fra P2
        elif elem[0] == 1011:
            M1 += P2_ortogonal *l
            #moment i punkt 10 fra P2

        for punk in punktlaster:
            if punk[0] == knute_1:
                p = punk[2]
                p_ortogonal = -np.sin(punk[1]) * p
                Q1 += p_ortogonal
                #definerer positiv retning opp
            elif punk[0] == knute_2:
                p = punk[2]
                p_ortogonal = -np.sin(punk[1]) * p
                Q2 += p_ortogonal

        #NB! Dette her er møkk*dritt!

'''