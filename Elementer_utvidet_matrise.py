import Innlesning as inn
import Tverrsnittsdata as tve
import Systemstivhetsmatrise as sys
import Transformasjonsmatrise as tra
import math

elementer_utvidet_matrise=[]
#etablerer en matrise som skal inneholde alle data for alle elementer

for i in range(inn.antall_element):

    elementdata=[]
    #lager tom liste for hver iterasjon
    
    elementdata.append(inn.elementer_matrise[i][0])
    elementdata.append(inn.elementer_matrise[i][1])
    elementdata.append(inn.elementer_matrise[i][2])
    elementdata.append(inn.elementer_matrise[i][3])
    elementdata.append(inn.elementer_matrise[i][4])
    #Legger til alle data som allerede står i elementer_matrise

    elementdata.append(tve.tverrsnittsdata_matrise[i][4])
    elementdata.append(tve.tverrsnittsdata_matrise[i][5])
    elementdata.append(tve.tverrsnittsdata_matrise[i][6])
    #Legger til alle data som allerede står i tverrsnittsdata_matrise

    elementdata.append(sys.koordinater_lengde_matrise[i][0])
    elementdata.append(sys.koordinater_lengde_matrise[i][1])
    elementdata.append(sys.koordinater_lengde_matrise[i][2])
    elementdata.append(sys.koordinater_lengde_matrise[i][3])
    elementdata.append(sys.koordinater_lengde_matrise[i][4])
    #Legger til alle data som allerede står i koordinater_lengde_matrise

    elementdata.append(tra.elementer_vinkler_liste[i])
    #legger til vinkel til element i forhold til x_aksen

    elementer_utvidet_matrise.append(elementdata)
    #Legger til alle data for hvert element inn i den utvidede matrisen

#Matrisen er på formen: 
# [0] Element_ID, 
# [1] Første knutepunkt, 
# [2] Andre knutepunkt, 
# [3] E-modul, 
# [4] Tverrsnitts-type
# [5] Areal, 
# [6] Andre arealmoment, 
# [7] Bøyestivhet, 
# [8] x-koord første knutepunkt, 
# [9] y-koord første knutepunkt, 
# [10] x-koord andre knutepunkt, 
# [11] y-koord andre knutepunkt,   
# [12] Lengden på elementet, 
# [13] Vinkelen til elementet i forhold til x-aksen