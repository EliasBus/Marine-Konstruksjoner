import Transformasjonsmatrise   as tra
import Konnektivitetstabell     as kon
import Lastvektor_lokal         as R_l
import numpy                    as np

def lastvektor_funk(n_knutepunkt, elementer_utvidet,punktlaster, fordelte_laster):
    R=np.zeros(n_knutepunkt *3)
    #oppretter lastvektor
    for elem in elementer_utvidet:
        R_lok               = R_l.R_lok_funksjon(elem, fordelte_laster)
        konnektivitetstabell= kon.konnektivitetstabell_funksjon(elem)
        T                   = tra.transformasjonsmatrise_funksjon(elem)
        R_glob              = T @ R_lok
        #transformerer lokal lastvektor
        R[int(konnektivitetstabell[0][2]-1)] -= R_glob[0]
        R[int(konnektivitetstabell[1][2]-1)] -= R_glob[1]
        R[int(konnektivitetstabell[2][2]-1)] -= R_glob[2]
        R[int(konnektivitetstabell[3][2]-1)] -= R_glob[3]
        R[int(konnektivitetstabell[4][2]-1)] -= R_glob[4]
        R[int(konnektivitetstabell[5][2]-1)] -= R_glob[5]
        #legger inn i global lastvektor

    for kraft in punktlaster:
        knute_p = int(kraft[0])
        theta=kraft[1]*np.pi/180
        x_komp= kraft[2] * np.cos(theta)
        y_komp= kraft[2] * np.sin(theta)
        #x og y komponent til punktlasten
        R[(knute_p -1)*3 + 0] += x_komp
        R[(knute_p -1)*3 + 1] += y_komp
        #legger til aksialkraft og skjærkraft fra punktlaster på konstruksjonen i retningen den virker i
    return R