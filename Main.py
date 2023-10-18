import Innlesning as inn
import Tverrsnittsdata as tve
import Systemstivhetsmatrise as sys
import Elementer_utvidet_matrise as ele
import Transformasjonsmatrise as tra
import Figurer as fig
import Lastvektor as las
import Enderotasjoner as end

import numpy as np



#Data fra Innlesning.py:
'''

print(f"\n\nAntall knutepunkt: {inn.antall_knutepunkt}\n")
for line in inn.knutepunkter_matrise:
    print(line)
print(f"\n\nAntall element: {inn.antall_element}\n")
for line in inn.elementer_matrise:
    print(line)
print(f"\n\nAntall fordelte laster: {inn.antall_fordelte_laster}\n")
for line in inn.fordelte_laster_matrise:
    print(line)
print(f"\n\nAntall punktlaster: {inn.antall_punktlaster}\n")
for line in inn.punktlaster_matrise:
    print(line)

'''

#Data fra Tverrsnittsdata.py:
'''

print ('\n\nTversnittsdata_matrise:  [ID, Knutepunkt 1, Knutepunkt 2, E-modul, Areal, Andrearealmoment, Bøyestivhet]\n')
for line in tve.tverrsnittsdata_matrise:
    print(line)

'''


#Data fra Systemstivhetsmatrise.py
'''
systemstivhetsmatrise = sys.systemstivhetsmatrise_funksjon(ele.elementer_utvidet_matrise, inn.antall_knutepunkt, inn.knutepunkter_matrise)
for line in systemstivhetsmatrise:
    print(line)

syst = sys.systemstivhetsmatrise_funksjon(ele.elementer_utvidet_matrise, inn.antall_knutepunkt, inn.knutepunkter_matrise)
for line in syst:
    print(line)

'''



#Data fra Elementer_utvidet_matrise:
'''
for elem in ele.elementer_utvidet_matrise:  
    print(f'Element {round(elem[0])}: {round(elem[13]*180/math.pi)}')

print(ele.elementer_utvidet_matrise[18][13]*180/math.pi)  

'''
print ('\n\nElementer utvidet matrise:  \n')
for line in ele.elementer_utvidet_matrise:
    print(line)




#Data fra Transformasjonsmatrise.py:
'''

for i in range(inn.antall_element):
    print(f'Element {round(ele.elementer_utvidet_matrise[i][0])}: {round(tra.elementer_vinkler_liste[i]*180/math.pi)} grader')

'''


#Data fra Figurer.py:


fig.plot_elements(ele.elementer_utvidet_matrise, inn.knutepunkter_matrise)


#Data fra lastvektor.py

R=las.lastvektor_funk(inn.antall_knutepunkt, inn.antall_element, ele.elementer_utvidet_matrise, inn.antall_punktlaster, inn.punktlaster_matrise, inn.antall_fordelte_laster, inn.fordelte_laster_matrise)

#Data fra enderotasjoner.py

K = sys.systemstivhetsmatrise_funksjon(ele.elementer_utvidet_matrise, inn.antall_knutepunkt, inn.knutepunkter_matrise)
n_knuter = inn.antall_knutepunkt

r= end.enderotasjoner_funk(R, K, n_knuter)
