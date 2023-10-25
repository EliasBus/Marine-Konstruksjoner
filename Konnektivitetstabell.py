import numpy as np

def konnektivitetstabell_funksjon(element):
    knutepunkt_1 = element[1]
    knutepunkt_2 = element[2]
    #Finner knutepunktene i elemententet
    lokale_frihetsgrader=6

    konnektivitetstabell =np.zeros((lokale_frihetsgrader,3))
    #oppretter tom tabell
    
    for i in range(1,lokale_frihetsgrader+1):
        rad = np.array([])
        if i <= 3:
            rad = np.append(rad, i)
            rad = np.append(rad, knutepunkt_1)
            rad = np.append(rad, 3*(knutepunkt_1-1) + (i))
        elif i >= 4:
            rad = np.append(rad, i)
            rad = np.append(rad, knutepunkt_2)
            rad = np.append(rad, 3*(knutepunkt_2-1) + (i - 3))

        konnektivitetstabell[i-1] = rad
    
    return konnektivitetstabell