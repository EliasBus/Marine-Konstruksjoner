import numpy                  as np
import Transformasjonsmatrise as tra
import Elementstivhetsmatrise as elesti
import Konnektivitetstabell   as kon
import Lastvektor_lokal       as R_l

def fastinnspenningskrefter_funksjon(elementer_utvidet, v, fordelte_laster, n_knutepunkt):
    S=np.zeros(n_knutepunkt *3)
    #oppretter S
    for elem in elementer_utvidet:
        deformasjonsvektor_element  =np.zeros(6)
        knutepunkt_1                =elem[1]
        knutepunkt_2                =elem[2]
        konnektivitetstabell        =kon.konnektivitetstabell_funksjon(elem)
        for i in range(6):
            if i<3:
                deformasjonsvektor_element[i] = v[3*(knutepunkt_1-1)+i]
            elif i>=3: 
                deformasjonsvektor_element[i] = v[3*(knutepunkt_1-1)+i -3]
 
        T                       = tra.transformasjonsmatrise_funksjon(elem)
        k                       = elesti.elementsivhetsmatrise_funskjon(elem)
        v_lok                   = np.transpose(T) @ deformasjonsvektor_element
        R_lok                   = R_l.R_lok_funksjon(elem, fordelte_laster)
        S_lok                   = np.add(k @ v_lok , R_lok)
        S_glob                  = T @ S_lok
        
        S[int(konnektivitetstabell[0][2]-1)] += S_glob[0]
        S[int(konnektivitetstabell[1][2]-1)] += S_glob[1]
        S[int(konnektivitetstabell[2][2]-1)] += S_glob[2]
        S[int(konnektivitetstabell[3][2]-1)] += S_glob[3]
        S[int(konnektivitetstabell[4][2]-1)] += S_glob[4]
        S[int(konnektivitetstabell[5][2]-1)] += S_glob[5]
        #legger inn i global fastinnspenningsvektor
    return S