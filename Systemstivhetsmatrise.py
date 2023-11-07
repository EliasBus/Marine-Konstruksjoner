import Transformasjonsmatrise   as tra
import Konnektivitetstabell     as kon
import Elementstivhetsmatrise   as elesti
import numpy                    as np

def systemstivhetsmatrise_funksjon(elementer_utvidet,antall_knutepunkt, knutepunkt):
    #definerer en funkssjon som tar inn elementer_utvidet og antall knutepunkt
    str_matrise= 3*antall_knutepunkt 
    #finner dimensjonen på systemstivhetsmatrisen
    systemstivhetsmatrise = np.zeros((str_matrise,str_matrise))
    #lager matrisen med bare 'nuller'
    for elem in elementer_utvidet:
    #iterer gjennom hvert element i konstruksjonen
        elementstivhetsmatrise = elesti.elementsivhetsmatrise_funskjon(elem)
        T = tra.transformasjonsmatrise_funksjon(elem)
        #henter transformasjonsmatrisen fra Transformasjonsmatrise.py
        T_transponert = np.transpose(T)
        #transponerer matrisen
        elementstivhetsmatrise_glob = T_transponert @ elementstivhetsmatrise @ T
        #finner global elementstivhetsmatrise (T_transp * k * T)
        konnektivitetstabell=kon.konnektivitetstabell_funksjon(elem)
        lokale_frihetsgrader=6
        for x in range(lokale_frihetsgrader):
            for y in range(lokale_frihetsgrader):
                rad=int(konnektivitetstabell[x,2])
                kol=int(konnektivitetstabell[y,2])
                #Finner koordinatet til bidraget i den globale systemstivhetsmatrisen
                systemstivhetsmatrise[rad-1][kol-1] += elementstivhetsmatrise_glob[x][y]
                #Legger til bidraget i systemstivhetsmatrisen

    for knute in knutepunkt:
        if knute[3]==1:
                #sjekker om punktet er fast innspent
                knute_indeks    =int(knute[0]-1)
                fjærstivhet     =10**8
                systemstivhetsmatrise[knute_indeks*3+0][knute_indeks*3+0] +=fjærstivhet
                systemstivhetsmatrise[knute_indeks*3+1][knute_indeks*3+1] +=fjærstivhet
                systemstivhetsmatrise[knute_indeks*3+2][knute_indeks*3+2] +=fjærstivhet
                #Legger til fjærstivhet til systemstivhetsmatrise på diagonalen hvor innspenningen er fast
    return systemstivhetsmatrise
    #returnerer matrisen