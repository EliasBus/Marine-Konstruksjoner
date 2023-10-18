import numpy as np


def lastvektor_funk(n_knutepunkt,n_elementer, elementer_utvidet, n_punktlaster, punktlaster, n_fordelte_laster, fordelte_laster):


    R=np.zeros(n_knutepunkt *3)
    #oppretter lastvektor

    for elem in elementer_utvidet:
        q1=0
        q2=0

        l = elem[7]
        knute_1 = elem[1]
        knute_2 = elem[2]

        for ford in fordelte_laster:
            if int(ford[0])==int(elem[0]):
                if int(ford[1])==int(knute_1):
                    q1 = ford[3]
                    q2 = ford[4]
                elif int(ford[1])==int(knute_2):
                    q2 = ford[3]
                    q1 = ford[4]
        #finner lastintensitet i knutepunktpunkt 1 og 2
        

        V1 = ( 7/20*q1  + 3/20*q2) *l     
        V2 = ( 7/20*q2  + 3/20*q1) *l   
        M1 = (-1/20*q1  - 1/30*q2) *l**2
        M2 = ( 1/20*q2  + 1/30*q1) *l**2

        
        #print(f'Element: {elem[0]}\nV1: {V1} \nV2: {V2} \nM1: {M1} \nM2: {M2} \n')


        theta = elem[13]
    

        R[(knute_1 -1)*3 + 0] += 0
        R[(knute_2 -1)*3 + 0] += 0
        #Legger til aksialspennigsbidrag til i hver første indeks i R
        R[(knute_1 -1)*3 + 1] += -V1 
        R[(knute_2 -1)*3 + 1] += -V2 
        #Legger til skjærspenningsbidrag til i hver andre indeks i R
        R[(knute_1 -1)*3 + 2] += -M1
        R[(knute_2 -1)*3 + 2] += -M2
        #Legger til bidrag fra fas2_innsp_mom til hver tredje indeks i R

    for kraft in punktlaster:
        punkt = int(kraft[0])
        R[(punkt-1)*3 + 0] += kraft[2] * np.sin(kraft[1]*np.pi / 180)
        #legger til aksialkraft fra punktlaster på konstruksjonen i retning den virker i

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