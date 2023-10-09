import Innlesning as inn
import Tverrsnittsdata as tve
import Systemstivhetsmatrise as sys
import Elementer_utvidet_matrise as ele
import Transformasjonsmatrise as tra
import Figurer as fig

import math



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

for elem in sys.systemstivhetsmatrise:
    print(f'\n{int(elem[0])}:               ({int(elem[1])}, {int(elem[2])})')
    print(f'lengde:           {round(lengde,2)}      [m]')
    print(f'E-modul:          {elem[3]}      [kN/mm^2]')
    print(f'Andrearealmoment: {round(elem[5]/(10**9),2)}*10^9 [mm^4]')

    
print ('\n\nSystemstivhetsmatrise:  [(kN/mm^2 * mm^4)/m = N*mm] * 10^9\n')
for line in sys.systemstivhetsmatrise:
    print(line)


'''

#Data fra Elementer_utvidet_matrise:
'''

for elem in ele.elementer_utvidet_matrise:  
    print(f'Element {round(elem[0])}: {round(elem[13]*180/math.pi)}')

print(ele.elementer_utvidet_matrise[18][13]*180/math.pi)    

print ('\n\nElementer utvidet matrise:  \n')
for line in ele.elementer_utvidet_matrise:
    print(line)

'''

#Data fra Transformasjonsmatrise.py:
'''

for i in range(inn.antall_element):
    print(f'Element {round(ele.elementer_utvidet_matrise[i][0])}: {round(tra.elementer_vinkler_liste[i]*180/math.pi)} grader')

'''

#Data fra Figurer.py:

fig.plot_elements(ele.elementer_utvidet_matrise, inn.knutepunkter_matrise)