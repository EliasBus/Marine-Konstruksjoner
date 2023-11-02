import numpy as np
import Transformasjonsmatrise as tra
import Elementstivhetsmatrise as elesti
import Konnektivitetstabell   as kon
import Lastvektor_lokal               as R_l

def fastinnspenningskrefter_funksjon(elementer_utvidet, r, fordelte_laster, n_knutepunkt):
    S=np.zeros(n_knutepunkt *3)
    #oppretter S
    
    for elem in elementer_utvidet:
        deformasjonsvektor_element  =np.zeros(6)
        knutepunkt_1                =elem[1]
        knutepunkt_2                =elem[2]
        konnektivitetstabell        =kon.konnektivitetstabell_funksjon(elem)


        for i in range(6):
            if i<3:
                deformasjonsvektor_element[i] = r[3*(knutepunkt_1-1)+i]
            elif i>=3: 
                deformasjonsvektor_element[i] = r[3*(knutepunkt_1-1)+i -3]

        T                       = tra.transformasjonsmatrise_funksjon(elem)
        k                       = elesti.elementsivhetsmatrise_funskjon(elem)
        R_lok                   = R_l.R_lok_funksjon(elem, fordelte_laster)
        S_lok                   = np.add(k @ deformasjonsvektor_element , R_lok)
        S_lok = k @ deformasjonsvektor_element@T

        S[int(konnektivitetstabell[0][2]-1)] += S_lok[0]
        S[int(konnektivitetstabell[1][2]-1)] += S_lok[1]
        S[int(konnektivitetstabell[2][2]-1)] += S_lok[2]
        S[int(konnektivitetstabell[3][2]-1)] += S_lok[3]
        S[int(konnektivitetstabell[4][2]-1)] += S_lok[4]
        S[int(konnektivitetstabell[5][2]-1)] += S_lok[5]
        #legger inn i global fastinnspenningsvektor
    return S