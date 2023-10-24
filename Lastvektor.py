import Transformasjonsmatrise as tra
import numpy as np


def lastvektor_funk(n_knutepunkt,n_elementer, elementer_utvidet, n_punktlaster, punktlaster, n_fordelte_laster, fordelte_laster):

    R=np.zeros(n_knutepunkt *3)
    #oppretter lastvektor

    for elem in elementer_utvidet:
        q1=0
        q2=0

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
        V2 = ( 7/20*q2  + 3/20*q1) *l   
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

        T = tra.transformasjonsmatrise_funksjon(elem)
        R_tra = T @ R_lok
        #transformerer lokal lastvektor

        R[(knute_1 -1)*3 + 0] += R_tra[0]
        R[(knute_1 -1)*3 + 1] += R_tra[1]
        R[(knute_1 -1)*3 + 2] += R_tra[2]
        R[(knute_2 -1)*3 + 0] += R_tra[3]
        R[(knute_2 -1)*3 + 1] += R_tra[4]
        R[(knute_2 -1)*3 + 2] += R_tra[5]
        #legger inn i global lastvektor

    for kraft in punktlaster:
        knute_p = int(kraft[0])
        R[(knute_p -1)*3 + 1] += kraft[2] * np.sin(kraft[1] *np.pi /180)
        
        print(f'punkt {knute_p}, kraft {kraft[2]}, retning {np.sin(kraft[1]*np.pi/180)}')
        #legger til aksialkraft fra punktlaster på konstruksjonen i retning den virker i

    return R



