import Innlesning as inn
import math

tverrsnittsdata_matrise=[]

areal=0
andrearealmoment=0
bøyestivhet=0
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
        bøyestivhet=      i[3] * andrearealmoment
        #                 andrearealmoment * E-modul
    

    tverrsnittsdata.append(i[0])
    tverrsnittsdata.append(areal)
    tverrsnittsdata.append(andrearealmoment)
    tverrsnittsdata.append(bøyestivhet)
    #Legger inn hver av verdiene inn i en liste for hver av elementene

    tverrsnittsdata_matrise.append(tverrsnittsdata)
    #Legger til hver liste i en matrise for alle elementer

print ('Tversnittsda\n\n')
for line in tverrsnittsdata_matrise:
    print(line)


