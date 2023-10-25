import Innlesning                   as inn
import Tverrsnittsdata              as tve
import Systemstivhetsmatrise        as sys
import Elementer_utvidet_matrise    as ele
import Transformasjonsmatrise       as tra
import Figurer                      as fig
import Lastvektor                   as las
import Deformasjoner                as defo
import Spenningsanalyse             as spe
import Konnektivitetstabell         as kon
import Print                        as pri

import numpy                        as np
import matplotlib.pyplot            as plt

jacket='input_fil.txt'
beam  ='input_fil_3Dbeam.txt'
test  ='test_fil.txt'

#Data fra Innlesning.py:
fil=beam

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

#Data fra Konnektivitetstabell.py:


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
    # [9] Flytespenning, 
    # [10] Tverrsnitts-type,
    # [11] Areal, 
    # [12] Andre arealmoment, 
    # [13] Bøyestivhet, 
    # [14] Vinkelen til elementet i forhold til x-aksen

#Data fra Systemstivhetsmatrise.py:
K = sys.systemstivhetsmatrise_funksjon(elementer_utvidet,antall_knutepunkt, knutepunkter)


#Data fra Transformasjonsmatrise.py:

#Data fra lastvektor.py:
R=las.lastvektor_funk(antall_knutepunkt, antall_element, elementer_utvidet, antall_punktlaster, punktlaster, antall_fordelte_laster, fordelte_laster)


#Data fra deformasjoner.py:
r= defo.deformasjoner_funk(R, K, antall_knutepunkt)


#Data fra Spenningsanalyse.py:
utnyttelse=spe.spenningsanalyse_funksjon(elementer, elementer_utvidet, R)



#Data fra Figurer.py:
skalar=100


#Data fra Print.py:
pri.print_K(K)
pri.print_elementer(elementer_utvidet)
pri.print_R(R)
pri.print_r(r)
pri.print_utnyttelse(elementer, utnyttelse)
pri.print_figurer(knutepunkter, elementer, elementer_utvidet,r,skalar)
