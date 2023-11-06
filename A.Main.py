import matplotlib.pyplot            as plt
import numpy                        as np

import Elementer_utvidet_matrise    as ele
import Fastinnspenningskrefter      as fast
import Transformasjonsmatrise       as tra
import Systemstivhetsmatrise        as sys
import Konnektivitetstabell         as kon
import Spenningsanalyse             as spe
import Tverrsnittsdata              as tve
import Deformasjoner                as defo
import Innlesning                   as inn
import Lastvektor                   as las
import Figurer                      as fig
import Print                        as pri
import Midt_moment                  as midt
import Momentdiagram                as mom

jacket='Z.Input_fil.txt'
beam  ='Z.3Dbeam.txt'
bjelke  ='Z.fastbjelke.txt'
portal ='Z.Portal.txt'
#Angi en fil programmet skal kjøre
fil=beam

antall_knutepunkt       =inn.innlesning_funk(fil)[0]
antall_element          =inn.innlesning_funk(fil)[1]
antall_fordelte_laster  =inn.innlesning_funk(fil)[2]
antall_punktlaster      =inn.innlesning_funk(fil)[3]
knutepunkter            =np.array(inn.innlesning_funk(fil)[4])
elementer               =np.array(inn.innlesning_funk(fil)[5])
fordelte_laster         =inn.innlesning_funk(fil)[6]
punktlaster             =inn.innlesning_funk(fil)[7]
tverrsnittsdata         =tve.tverrsnittsdata_funk(elementer)
elementer_utvidet       =ele.elementer_utvidet_matrise_funk(antall_element, elementer, knutepunkter, tverrsnittsdata)

#Matrisen 'elementer_utvidet' er på formen: 
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

K                       =sys.systemstivhetsmatrise_funksjon(elementer_utvidet,antall_knutepunkt, knutepunkter)
R                       =las.lastvektor_funk(antall_knutepunkt, elementer_utvidet,  punktlaster,  fordelte_laster)
v                       =defo.deformasjoner_funk(R, K)
S                       =fast.fastinnspenningskrefter_funksjon(elementer_utvidet, v, fordelte_laster, antall_knutepunkt)
momenter                =midt.midtmoment_funksjon(elementer_utvidet, fordelte_laster, S)
utnyttelse              =spe.spenningsanalyse_funksjon(elementer, elementer_utvidet, R, momenter)


#print programmet
pri.print_K(K)
pri.print_elementer(elementer_utvidet)
pri.print_tversnittsdata(elementer_utvidet)
pri.print_R(R)
pri.print_r(v)
pri.print_fastinnspenningskrefter(S)
pri.print_momenter(momenter, elementer)
pri.print_utnyttelse(elementer, utnyttelse)


#Angi en skalar som skalerer deformasjonene, linjebredden til elementene og størrelsen på kraft-pilene i figuren
skalar_deformasjon=100
skalar_linjebredde=1
skalar_krefter =1
#fig.plot_konstruksjon               (knutepunkter, elementer, elementer_utvidet,    skalar_linjebredde, 0)
#fig.plot_deformasjon               (knutepunkter, elementer, elementer_utvidet, v, skalar_deformasjon, skalar_linjebredde)
#fig.plot_rotasjoner                (knutepunkter, elementer, elementer_utvidet, v, skalar_deformasjon, skalar_linjebredde)
#fig.plot_krefter                    (knutepunkter, elementer, elementer_utvidet, skalar_linjebredde,skalar_krefter, fordelte_laster, punktlaster)
fig.plot_rotasjoner_og_deformasjoner(knutepunkter, elementer, elementer_utvidet, v, skalar_deformasjon, skalar_linjebredde)

#Plotter forskjellige figurer hver for seg

mom.momentdiagram_funksjon(momenter, elementer_utvidet, fordelte_laster)
