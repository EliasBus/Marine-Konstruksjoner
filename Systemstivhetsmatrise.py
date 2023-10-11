import numpy as np

def systemstivhetsmatrise_funksjon(elementer,antall_knutepunkt):
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
        knutepunkt_1_indeks = elem[1]-1
        knutepunkt_2_indeks = elem[2]-1
        #Finner knutepunktene
        

        konnektivitetstabell =np.zeros((lokale_frihetsgrader,3))
        
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
            #lager konnektivitetstabell    
        
            

        E=elem[8]
        A=elem[10]
        L=elem[7]
        I=elem[11]
        Stivhetsmatrise=np.array([
        [E*A/L , 0             , 0            , -E*A/L, 0             , 0            ],
        [0     , 12*E*I/(L**3) , -6*E*I/(L**2), 0     , -12*E*I/(L**3), -6*E*I/(L**2)],
        [0     , -6*E*I/(L**2) , 4*E*I/L      , 0     , 6*E*I/(L**2)  , 2*E*I/L      ],
        [-E*A/L, 0             , 0            , E*A/L , 0             , 0            ],
        [0     , -12*E*I/(L**3), 6*E*I/(L**2) , 0     , 12*E*I/(L**3) , 6*E*I/(L**2) ],
        [0     , -6*E*I/(L**2) , 2*E*I/L      , 0     , 6*E*I/(L**2)  , 4*E*I/L      ],
        ])   

        

        

        
        

        for x in range(lokale_frihetsgrader):
            for y in range(lokale_frihetsgrader):
                rad=int(konnektivitetstabell[x,2])
                kol=int(konnektivitetstabell[y,2])
                systemstivhetsmatrise[rad-1,kol-1] += Stivhetsmatrise[x][y]

    for rad in systemstivhetsmatrise:
        print(np.round(rad/(10**9)))
        
      
        
    return systemstivhetsmatrise
    

