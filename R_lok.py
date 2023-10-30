import Konnektivitetstabell as kon
import numpy                as np


def R_lok_funksjon(elem, fordelte_laster):
    q1=0
    q2=0
    
    konnektivitetstabell=kon.konnektivitetstabell_funksjon(elem)

    l = elem[7] #lengde
    knute_1 = elem[1]
    knute_2 = elem[2]

    for ford in fordelte_laster:
        if int(ford[0])==int(elem[0]):
        #sjekker om elementet har fordelt last
            if int(ford[1])==int(knute_1):
                q1 = ford[3]
                q2 = ford[4]
            elif int(ford[1])==int(knute_2):
                q2 = ford[3]
                q1 = ford[4]
            #finner lastintensitet i knutepunktpunkt 1 og 2
    
    N1 = 0
    V1 = ( 7/20*q1  + 3/20*q2) *l 
    M1 = (-1/20*q1  - 1/30*q2) *l**2
    N2 = 0
    V2 = (-7/20*q2  - 3/20*q1) *l   
    M2 = ( 1/20*q2  + 1/30*q1) *l**2
    #V fra momentlikevekt
    #M fra tabell for fastinnspenningmomenter

    R_lok = np.array([
        N1,
        V1,
        M1,
        N2,
        V2,
        M2
    ])
    #lokal lastvektor
    
    return R_lok