import Transformasjonsmatrise as tra
import Konnektivitetstabell   as kon
import numpy as np

def systemstivhetsmatrise_funksjon(elementer_utvidet,antall_knutepunkt, knutepunkt):
    #definerer en funkssjon som tar inn elementer_utvidet og antall knutepunkt
    

    str_matrise= 3*(antall_knutepunkt) 
    #finner dimensjonen på systemstivhetsmatrisen
    systemstivhetsmatrise = np.zeros((str_matrise,str_matrise))
    #lager matrisen med bare 'nuller'
    

    for elem in elementer_utvidet:
    #iterer gjennom hvert element i konstruksjonen

        knutepunkt_1 = elem[1]
        knutepunkt_2 = elem[2]
        #Finner knutepunktene i elementet

        E=elem[8]
        A=elem[11]
        L=elem[7]
        I=elem[12]

        elementstivhetsmatrise=np.array([
        [E*A/L , 0             , 0            , -E*A/L, 0             , 0            ],
        [0     , 12*E*I/(L**3) , -6*E*I/(L**2), 0     , -12*E*I/(L**3), -6*E*I/(L**2)],
        [0     , -6*E*I/(L**2) , 4*E*I/L      , 0     , 6*E*I/(L**2)  , 2*E*I/L      ],
        [-E*A/L, 0             , 0            , E*A/L , 0             , 0            ],
        [0     , -12*E*I/(L**3), 6*E*I/(L**2) , 0     , 12*E*I/(L**3) , 6*E*I/(L**2) ],
        [0     , -6*E*I/(L**2) , 2*E*I/L      , 0     , 6*E*I/(L**2)  , 4*E*I/L      ],
        ])   
        #ovenfor er elementstivhetsmatrisen
        
        trans = tra.transformasjonsmatrise_funksjon(elem)
        #henter transformasjonsmatrisen fra Transformasjonsmatrise.py
        trans_transponert = np.linalg.inv(trans)
        #transponerer matrisen
        
        #elementstivhetsmatrise_glob = np.dot( np.dot(trans_transponert, elementstivhetsmatrise), trans)
        elementstivhetsmatrise_glob = trans_transponert @ elementstivhetsmatrise @ trans
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
                knute_indeks = int(knute[0]-1)

                fjærstivhet=10**8
                
                systemstivhetsmatrise[knute_indeks*3+0][knute_indeks*3+0] +=fjærstivhet
                systemstivhetsmatrise[knute_indeks*3+1][knute_indeks*3+1] +=fjærstivhet
                systemstivhetsmatrise[knute_indeks*3+2][knute_indeks*3+2] +=fjærstivhet
                #Legger til fjærstivhet til systemstivhetsmatrise på diagonalen hvor innspenningen er fast

    return systemstivhetsmatrise
    #returnerer matrisen
    

