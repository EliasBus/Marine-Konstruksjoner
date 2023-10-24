import Innlesning                   as inn
import Tverrsnittsdata              as tve
import Systemstivhetsmatrise        as sys
import Elementer_utvidet_matrise    as ele
import Transformasjonsmatrise       as tra
import Figurer                      as fig
import Lastvektor                   as las
import Deformasjoner                as defo

import numpy                        as np
import matplotlib.pyplot            as plt


#Data fra Innlesning.py:
fil='input_fil.txt'

antall_knutepunkt       = inn.innlesning_funk(fil)[0]
antall_element          = inn.innlesning_funk(fil)[1]
antall_fordelte_laster  = inn.innlesning_funk(fil)[2]
antall_punktlaster      = inn.innlesning_funk(fil)[3]
knutepunkter            = inn.innlesning_funk(fil)[4]
elementer               = inn.innlesning_funk(fil)[5]
fordelte_laster         = inn.innlesning_funk(fil)[6]
punktlaster             = inn.innlesning_funk(fil)[7]

#Data fra Tverrsnittsdata.py:
tverrsnittsdata = tve.tverrsnittsdata_funk(elementer)

#Data fra Elementer_utvidet_matrise:
elementer_utvidet=ele.elementer_utvidet_matrise_funk(antall_element, elementer, knutepunkter, tverrsnittsdata)

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
    # [9] Tverrsnitts-type,
    # [10] Areal, 
    # [11] Andre arealmoment, 
    # [12] Bøyestivhet, 
    # [13] Vinkelen til elementet i forhold til x-aksen


#Data fra Systemstivhetsmatrise.py:
K = sys.systemstivhetsmatrise_funksjon(elementer_utvidet,antall_knutepunkt, knutepunkter)
for line in K:
    print (line)

#Data fra Transformasjonsmatrise.py:

#Data fra lastvektor.py:
R=las.lastvektor_funk(antall_knutepunkt, antall_element, elementer_utvidet, antall_punktlaster, punktlaster, antall_fordelte_laster, fordelte_laster)
print('\nlastvektor:')
print(R)

#Data fra deformasjoner.py:
r= defo.deformasjoner_funk(R, K, antall_knutepunkt)
print('\nDeformasjoner: \n')
for i in range(0,len(r),3):
    print(f'KNUTEPUNKT {int(i/3+1)}: x {int(r[i])} mm,  y {int(r[i+1])} mm,  theta {round(r[i+2]*180/np.pi,3)} grader\n')

#Data fra Figurer.py:
fig.plot_vindu(knutepunkter)
fig.plot_elementer(elementer_utvidet, knutepunkter)
skalar=1
fig.plot_deformasjon(elementer_utvidet, knutepunkter, r, skalar)

plt.show()

