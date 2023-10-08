import Innlesning as inn
import math
#importerer data fra Innlesning.py som 'inn'
#importerer math for å bruke math.pi

tverrsnittsdata_matrise=[]
#etablerer en matrise som skal inneholde tversnittsdata for alle elementer


for i in inn.elementer_matrise:
    tverrsnittsdata=[]
    #Nuller listen for hver iterasjon
    if i[4]==0:
    #hvis rør
        areal=            math.pi * (i[6]**2 - i[5]**2)
        #                 pi      * (ytre_radius^2 - indre_radius^2)
        andrearealmoment= math.pi * (i[6]**4 - i[5]**4) / 4
        #                 pi      * (ytre_radius^4 - indre_radius^4) / 4
        bøyestivhet=      i[3] * andrearealmoment
        #                 andrearealmoment * E-modul
    elif i[4]==1:
    #hvis I-profil
        areal=            2 * i[5]*i[6]   + i[7]*i[8] 
        #                 2 * areal flens + areal stag
        andrearealmoment= 2 * (i[5]*i[6]**(3) /12 + (i[7]/2+i[6]/2)**2 * (i[5]*i[6])) + i[7]**(3) *i[8] /12
        #                 2 * (I_flens         + steinerbidrag_flens)                  + I_stag
        bøyestivhet=      i[3] * andrearealmoment
        #                 andrearealmoment * E-modul
    elif i[4]==2:
    #hvis boks-profil
        areal=            i[5]*i[6]       - (i[5]-2*i[7])*(i[6]-2*i[8])
        #                 areal_ytre_boks - areal_indre_boks
        andrearealmoment= 2 * (i[5]*i[8]**(3) /12 + ((i[6]/2-i[8]/2)**2 * i[5]*i[8])) + 2 * (i[7]*(i[6]-2*i[8])**(3) /12)
        #                 2 * (I_flens            + steinerbidrag_flens)              + 2 * (I_stag)
        bøyestivhet=      i[3]    * andrearealmoment
        #                 E-modul * andrearealmoment
    else:
    #hvis vi har ugyldig verdi i input_fil
        areal='input feil'
        andrearealmoment='input feil'
        bøyestivhet='input feil'

    tverrsnittsdata.append(i[0])
    tverrsnittsdata.append(i[1])
    tverrsnittsdata.append(i[2])
    tverrsnittsdata.append(i[3])
    tverrsnittsdata.append(areal)
    tverrsnittsdata.append(andrearealmoment)
    tverrsnittsdata.append(bøyestivhet)
    #Legger inn element_ID, startpunkt, sluttpunkt, E-modul
    #Legger inn hver av verdiene inn i en liste for hver av elementene

    tverrsnittsdata_matrise.append(tverrsnittsdata)
    #Legger til hver liste i en matrise for alle elementer


print ('\n\nTversnittsdata_matrise:  [ID, Knutepunkt 1, Knutepunkt 2, E-modul, Areal, Andrearealmoment, Bøyestivhet]\n')
for line in tverrsnittsdata_matrise:
    print(line)


