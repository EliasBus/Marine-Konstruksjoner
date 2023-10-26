import numpy as np
import Transformasjonsmatrise as tra

def innspenninger_funksjon(elementer_utvidet, r):
    
    for elem in elementer_utvidet:
        T = tra.transformasjonsmatrise_funksjon(elem)
        nedbøyningvektor_element=np.zeros(6)
        knutepunkt_1=elem[1]
        knutepunkt_2=elem[2]

        for i in range(len(nedbøyningvektor_element)):
            if i<3:
                nedbøyningvektor_element[i] = r[3*(knutepunkt_1-1)+i]
            elif i>=3: 
                nedbøyningvektor_element[i] = r[3*(knutepunkt_1-1)+i -3]

        T_transp =  np.transpose(T)
        T_transp @ nedbøyningvektor_element 

        