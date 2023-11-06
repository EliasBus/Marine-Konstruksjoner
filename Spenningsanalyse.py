import numpy as np

def spenningsanalyse_funksjon(elementer, elementer_utvidet,R, momenter):
    utnyttelse  =[]
    for i in range(len(elementer_utvidet)):
        prosenter=[]
        knute_1         =int(elementer[i][1])
        knute_2         =int(elementer[i][2])
        N               =R[(knute_1-1)*3 +0]
        M_midt          =momenter[i][0]
        M_1             =momenter[i][1]
        M_2             =momenter[i][2]
        A               =elementer_utvidet[i][11]
        I               =elementer_utvidet[i][12]
        tverrsnittstype =elementer_utvidet[i][10]
        
        
        if tverrsnittstype == 0:
            z=elementer[i][7]
            #ytre radius
        elif tverrsnittstype ==1:
            z=elementer[i][7] + elementer[i][8]/2
            # høyde flens       + høyde stag/2
        elif tverrsnittstype == 2:
            z=elementer[i][7]/2
            #høyde boks/2
        #finner z-verdien (høyde/2) til tverrsnittet

        sigma_midt = abs(N/A) + abs(M_midt*z/I)
        sigma_1 = abs(N/A) + abs(M_1*z/I)
        sigma_2 = abs(N/A) + abs(M_2*z/I)
        #Naviers formel

        flytespenning=elementer_utvidet[i][9]
        prosent_midt = sigma_midt/flytespenning * 100
        prosent_1 = sigma_1/flytespenning * 100
        prosent_2 = sigma_2/flytespenning * 100
        #prosent utnyttelse av f_y
        
        prosenter.append(prosent_midt)
        prosenter.append(prosent_1)
        prosenter.append(prosent_2)
        utnyttelse.append(prosenter)
    return utnyttelse