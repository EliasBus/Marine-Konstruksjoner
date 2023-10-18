import Transformasjonsmatrise as tra
import numpy as np

def systemstivhetsmatrise_funksjon(elementer,antall_knutepunkt, knutepunkt):
    #definerer en funkssjon som tar inn elementer og antall knutepunkt
    

    
    lokale_frihetsgrader=6

    str_matrise= 3*(antall_knutepunkt) 
    #finner dimensjonen på systemstivhetsmatrisen
    systemstivhetsmatrise = np.zeros((str_matrise,str_matrise))
    #lager matrisen med bare 'nuller'
    

    for elem in elementer:
    #iterer gjennom hvert element i konstruksjonen

        knutepunkt_1 = elem[1]
        knutepunkt_2 = elem[2]
        #Finner knutepunktene i elementet
        

        konnektivitetstabell =np.zeros((lokale_frihetsgrader,3))
        #oppretter tom tabell
        
        for i in range(1, lokale_frihetsgrader+1):
            rad = np.array([])
            if i <= 3:
                rad = np.append(rad, i)
                rad = np.append(rad, knutepunkt_1)
                rad = np.append(rad, 3*(knutepunkt_1 - 1) + i)
            elif i >= 4:
                rad = np.append(rad, i)
                rad = np.append(rad, knutepunkt_2)
                rad = np.append(rad, 3*(knutepunkt_2 - 1) + (i - 3))

            konnektivitetstabell[i-1] = rad
            #legger til rad for rad i konnektivitetstabellen    
        
            

        E=elem[8]
        A=elem[10]
        L=elem[7]
        I=elem[11]

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
        

        for x in range(lokale_frihetsgrader):
            for y in range(lokale_frihetsgrader):

                rad=int(konnektivitetstabell[x,2])-1
                kol=int(konnektivitetstabell[y,2])-1
                #Finner koordinatet til bidraget i den globale systemstivhetsmatrisen

                systemstivhetsmatrise[rad][kol] += elementstivhetsmatrise_glob[x][y]
                #Legger til bidraget i systemstivhetsmatrisen
        
       
        if knutepunkt[knutepunkt_1-1][3]==1:
                systemstivhetsmatrise[(knutepunkt_1-1)*3][(knutepunkt_1-1)*3] +=10^8
                systemstivhetsmatrise[(knutepunkt_1-1)*3+1][(knutepunkt_1-1)*3+1] +=10^8
                systemstivhetsmatrise[(knutepunkt_1-1)*3+2][(knutepunkt_1-1)*3+2] +=10^8

        #Legger til fjærstivhet til systemstivhetsmatrise på diagonalen hvor innspenningen er fast

    return systemstivhetsmatrise
    #returnerer matrisen
    

