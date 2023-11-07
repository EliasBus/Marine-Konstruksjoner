import numpy                        as np

import Elementer_utvidet_matrise    as ele
import Fastinnspenningskrefter      as fast
import Systemstivhetsmatrise        as sys
import Spenningsanalyse             as spe
import Tverrsnittsdata              as tve
import Deformasjoner                as defo
import Innlesning                   as inn
import Lastvektor                   as las
import Figurer                      as fig
import Print                        as pri
import Midt_moment                  as midt_M
import Midt_skjær                   as midt_Q
import Momentdiagram                as mom

beam  ='Z.3Dbeam.txt'           #Hovedfil
bjelke  ='Z.fastbjelke.txt'     #Fast innspent bjelke
portal ='Z.Portal.txt'          #Portalramme
#Angi en fil programmet skal kjøre
fil=beam

antall_knutepunkt       =inn.innlesning_funk                (fil)[0]
antall_element          =inn.innlesning_funk                (fil)[1]
antall_fordelte_laster  =inn.innlesning_funk                (fil)[2]
antall_punktlaster      =inn.innlesning_funk                (fil)[3]
knutepunkter            =inn.innlesning_funk                (fil)[4]
elementer               =inn.innlesning_funk                (fil)[5]
fordelte_laster         =inn.innlesning_funk                (fil)[6]
punktlaster             =inn.innlesning_funk                (fil)[7]
tverrsnittsdata         =tve.tverrsnittsdata_funk           (elementer)
elementer_utvidet       =ele.elementer_utvidet_matrise_funk (antall_element, elementer, knutepunkter, tverrsnittsdata)

K               =sys.systemstivhetsmatrise_funksjon     (elementer_utvidet,antall_knutepunkt, knutepunkter)
R               =las.lastvektor_funk                    (antall_knutepunkt, elementer_utvidet,  punktlaster,  fordelte_laster)
v               =defo.deformasjoner_funk                (R, K)
S               =fast.fastinnspenningskrefter_funksjon  (elementer_utvidet, v, fordelte_laster, antall_knutepunkt)
momenter        =midt_M.midtmoment_funksjon             (elementer_utvidet, fordelte_laster, S)
skjærkrefter    =midt_Q.midtskjær_funksjon              (elementer_utvidet, fordelte_laster, S)
utnyttelse      =spe.spenningsanalyse_funksjon          (elementer, elementer_utvidet, R, momenter)

#print output i tabeller
pri.print_K                         (K)
pri.print_elementer                 (elementer_utvidet)
pri.print_tversnittsdata            (elementer_utvidet)
pri.print_R                         (R)
pri.print_r                         (v)
pri.print_fastinnspenningskrefter   (S)
pri.print_momenter                  (momenter, elementer)
pri.print_skjærkrefter              (skjærkrefter, elementer)
pri.print_utnyttelse                (elementer, utnyttelse)

skalar_deformasjon=100  #Angi en skalar som skalerer deformasjonene
skalar_linjebredde=1    #Angi en skalar som skalerer linjebredden til elementene
skalar_krefter =1       #Angi en skalar som skalerer størrelsen på kraft-pilene i figuren
#Plotter forskjellige figurer hver for seg
fig.plot_konstruksjon               (knutepunkter, elementer, elementer_utvidet,    skalar_linjebredde, 0)
fig.plot_krefter                    (knutepunkter, elementer, elementer_utvidet, skalar_linjebredde,skalar_krefter, fordelte_laster, punktlaster)
fig.plot_deformasjon                (knutepunkter, elementer, elementer_utvidet, v, skalar_deformasjon, skalar_linjebredde)
fig.plot_rotasjoner                 (knutepunkter, elementer, elementer_utvidet, v, skalar_deformasjon, skalar_linjebredde)
fig.plot_rotasjoner_og_deformasjoner(knutepunkter, elementer, elementer_utvidet, v, skalar_deformasjon, skalar_linjebredde)
mom.momentdiagram_funksjon          (momenter, elementer_utvidet, fordelte_laster)