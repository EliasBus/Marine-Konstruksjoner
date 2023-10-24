import numpy as np

def spenningsanalyse_funksjon(elementer, elementer_utvidet,R):
    ind=0
    for elem in elementer_utvidet:
        knute_1=elem[1]
        knute_2=elem[2]
        N=R[(knute_1-1)*3 +0]
        M=R[(knute_1-1)*3 +2]
        A=elem[11]
        I=elem[12]

        tverrsnittstype=elem[10]
        if tverrsnittstype == 0:
            z=elementer[ind][7]
            #ytre radius
        elif tverrsnittstype ==1:
            z=elementer[ind][7] + elementer[ind][8]/2
            # høyde flens       + høyde stag/2
        elif tverrsnittstype == 2:
            z=elementer[ind][7]
            #høyde boks
        #finner z-verdien (høyde/2) til tverrsnittet

        sigma = N/A + M*z/I
        #Naviers formel

        flytespenning=elem[9]
        prosent = sigma/flytespenning * 100
        #prosent utnyttelse av f_y
        print(prosent)

        ind+=1