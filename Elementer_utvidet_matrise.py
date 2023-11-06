import numpy as np

def elementer_utvidet_matrise_funk(antall_element, elementer_matrise, knutepunkter_matrise, tverrsnittsdata_matrise):
    
    elementer_utvidet_matrise=[]
    #etablerer en matrise som skal inneholde alle data for alle elementer


    for i in range(antall_element):

        elementdata=[]
        #lager tom liste for hver iterasjon
        
        elementdata.append(elementer_matrise[i][0])
        #legger til ID

        knutepunkt_1 = int(elementer_matrise[i][1])
        knutepunkt_2 = int(elementer_matrise[i][2])
        #finner 1. og 2. knutepunkt til elementet
        elementdata.append(knutepunkt_1)
        elementdata.append(knutepunkt_2)
        #legger til knutepunkt 1, knutepunkt 2

        
        
        x_1 = knutepunkter_matrise[knutepunkt_1-1][1]
        y_1 = knutepunkter_matrise[knutepunkt_1-1][2]
        x_2 = knutepunkter_matrise[knutepunkt_2-1][1]
        y_2 = knutepunkter_matrise[knutepunkt_2-1][2]
        #finner koordinatene til 1. og 2. knutepunkt i elemntet
        

        elementdata.append(x_1)
        elementdata.append(y_1)
        elementdata.append(x_2)
        elementdata.append(y_2)
        #legger til koordinater
        
        lengde = ((x_1-x_2)**2 + (y_1-y_2)**2)**(1/2)
        #finner lengde for hvert av elementene ved Pythagoras

        elementdata.append(lengde)
        #legger til lengden i listen

        elementdata.append(elementer_matrise[i][3])
        elementdata.append(elementer_matrise[i][4])
        elementdata.append(elementer_matrise[i][5])
        #Legger til E-Modul, flytespenning og tverrsnittstype

        elementdata.append(tverrsnittsdata_matrise[i][0])
        elementdata.append(tverrsnittsdata_matrise[i][1])
        elementdata.append(tverrsnittsdata_matrise[i][2])
        #Legger til alle data som allerede står i tverrsnittsdata_matrise

        hosliggende_katet = (x_2-x_1)
        #finner lengde på hosliggende katet
        hypotenus = lengde
        #finner lengde på hypotenus
        
        theta= np.arccos(hosliggende_katet / hypotenus)
        #regner vinkelen med cosinus
        if x_2>x_1 and y_2<y_1 and theta<(np.pi/2):
            theta+=np.pi/2
        #korrigerer for fortegnsfeil
        
        elementdata.append(theta)
        #legger til vinkel til element i forhold til x_aksen

        elementer_utvidet_matrise.append(elementdata)
        #Legger til alle data for hvert element inn i den utvidede matrisen

    return elementer_utvidet_matrise

    #Matrisen er på formen: 
    # [0] Element_ID, 
    # [1] Første knutepunkt, 
    # [2] Andre knutepunkt, 
    # [3] x-koord første knutepunkt, 
    # [4] y-koord første knutepunkt, 
    # [5] x-koord andre knutepunkt, 
    # [6] y-koord andre knutepunkt,
    # [7] Lengden,
    # [8] E-modul,
    # [9] Flytespenning, 
    # [10] Tverrsnitts-type,
    # [11] Areal, 
    # [12] Andre arealmoment, 
    # [13] Bøyestivhet, 
    # [14] Vinkelen til elementet i forhold til x-aksen