import Elementer_utvidet_matrise as ele
import Innlesning as inn

import numpy as np


def moment(n_elementer, elementer, n_punktlaster, punktlaster, n_fordelte_laster, fordelte_laster):

    fast_innsp_mom = np.zeros(n_elementer,2)
    fast_innsp_skj = np.zeros(n_elementer,2)

    idx=0

    for elem in elementer:
        idx+=1
        l = elem[7]
        knute_1 = elem[1]
        knute_2 = elem[2]
        for ford in fordelte_laster:
            if ford[1]==knute_1 and ford[2]==knute_2:
                q1 = ford[3]
                q2 = ford[4]
        
                

        
        
        M1 = (-1/30*q2*l**2 - 1/20*q1*l**2)
        M2 = (1/20*q2*l**2 + 1/30*q1*l**2)

        #NB!
        #Antagelse! punktlast P2 vil alltid virke i punkt 11!

        for punk in punktlaster:
            if punk[0]==11:
                P2 = punk[0]
                P2_ortogonal = -np.sin(punk[1]) * P2

        if elem[0] == 911:
            M1 += -P2_ortogonal *l/2
            #moment i punkt 9 fra P2
        elif elem[0] == 1011:
            M1 += P2_ortogonal *l/2 
            #moment i punkt 10 fra P2

        fast_innsp_mom[idx][0] = M1
        fast_innsp_mom[idx][1] = M2
        #legger til M1 og M2 til matrisen med 


    return fast_innsp_mom, fast_innsp_skj

'''
if punk[0]==knute_1 and punk[0]==11:
                p1 = punk[2]
                p1_ortogonal = -np.sin(punk[1]) * p1
            elif punk[0]==knute_2 and punk[0]==11:
                p2 = punk[2]
                p2_ortogonal = -np.sin(punk[1]) * p2
'''