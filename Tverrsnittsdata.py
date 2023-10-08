import Innlesning as inn
import math

tverrsnittsdata_matrise=[]
tverrsnittsdata=[]
areal=0
andrearealmoment=0
bøyestivhet=0
for i in inn.elementer_matrise:
    if i[4]==0:
        # data for rør
        areal=            math.pi * (i[5]**2 - i[5]**2)
        andrearealmoment= math.pi * (i[5]**4 - i[5]**4) / 4
        bøyestivhet=      i[3] * andrearealmoment
    elif i[4]==1:
        # data for I-profil
        areal=            2 * i[6]*i[7]   + i[8]*i[9] 
        #                 2 * areal flens + areal stag
        andrearealmoment= 2 * i[6]*i[7]**3/12 + (i[8]/2+i[7]/2)**2 * (2 * i[6]*i[7]) + i[8]**3*i[9]/12
        #                 2 * I_flens         + steinerbidrag_flens                  + I_stag
        bøyestivhet=      i[3] * andrearealmoment
    tverrsnittsdata.append(areal)
    tverrsnittsdata.append(andrearealmoment)
    tverrsnittsdata.append(bøyestivhet)
    tverrsnittsdata_matrise.append(tverrsnittsdata)


for line in tverrsnittsdata_matrise:
    print(line)


