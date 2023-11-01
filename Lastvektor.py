import Transformasjonsmatrise as tra
import Konnektivitetstabell   as kon
import Lastvektor_lokal                 as R_l
import numpy as np


def lastvektor_funk(n_knutepunkt,n_elementer, elementer_utvidet, n_punktlaster, punktlaster, n_fordelte_laster, fordelte_laster):

    R=np.zeros(n_knutepunkt *3)
    #oppretter lastvektor
    

    for elem in elementer_utvidet:
        R_lok = R_l.R_lok_funksjon(elem, fordelte_laster)
        konnektivitetstabell=kon.konnektivitetstabell_funksjon(elem)
        T = tra.transformasjonsmatrise_funksjon(elem)
        R_tra = np.transpose(T) @ R_lok
        #transformerer lokal lastvektor

        R[int(konnektivitetstabell[0][2]-1)] += R_tra[0]
        R[int(konnektivitetstabell[1][2]-1)] += R_tra[1]
        R[int(konnektivitetstabell[2][2]-1)] += R_tra[2]
        R[int(konnektivitetstabell[3][2]-1)] += R_tra[3]
        R[int(konnektivitetstabell[4][2]-1)] += R_tra[4]
        R[int(konnektivitetstabell[5][2]-1)] += R_tra[5]
        #legger inn i global lastvektor

    for kraft in punktlaster:
        knute_p = int(kraft[0])
        theta=kraft[1]
        x_komp= kraft[2] * np.cos(theta *np.pi /180)
        y_komp= kraft[2] * np.sin(theta *np.pi /180)
        #x og y komponent til punktlasten

        R[(knute_p -1)*3 + 0] += x_komp
        R[(knute_p -1)*3 + 1] += y_komp
        #legger til aksialkraft fra punktlaster på konstruksjonen i retning den virker i

    return R