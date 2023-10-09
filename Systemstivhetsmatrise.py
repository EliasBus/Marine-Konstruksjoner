import Tverrsnittsdata as tve
import Innlesning as inn
#importerer data fra Tversnittsdata.py som 'tve'
#importerer data fra Innlesning.py som 'inn'


str_matrise=inn.antall_knutepunkt
#finner dimensjonen på systemstivhetsmatrisen
systemstivhetsmatrise = [[0 for i in range(str_matrise)] for i in range(str_matrise)]
#lager matrisen med bare 'nuller'

koordinater_lengde_matrise=[]



for elem in tve.tverrsnittsdata_matrise:
    #iterer gjennom hvert element i konstruksjonen

    koordinater_lengde_liste=[]

    knutepunkt_1 = int(elem[1])
    knutepunkt_2 = int(elem[2])
    #finner 1. og 2. knutepunkt til elementet

    knutepunkt_1_indeks = knutepunkt_1 -1
    knutepunkt_2_indeks = knutepunkt_2 -1
    #finner indeksen knutepunktet skal ha i systemstivhetsmatrisen

    x_1 = inn.knutepunkter_matrise[knutepunkt_1_indeks][1]
    y_1 = inn.knutepunkter_matrise[knutepunkt_1_indeks][2]
    x_2 = inn.knutepunkter_matrise[knutepunkt_2_indeks][1]
    y_2 = inn.knutepunkter_matrise[knutepunkt_2_indeks][2]
    #finner koordinatene til 1. og 2. knutepunkt i elemntet
    

    koordinater_lengde_liste.append(x_1)
    koordinater_lengde_liste.append(y_1)
    koordinater_lengde_liste.append(x_2)
    koordinater_lengde_liste.append(y_2)

    #print(f'element {elem[0]} --> (x, y)_{knutepunkt_1}: ({x_1}, {y_1}), (x, y)_{knutepunkt_2}: ({x_2}, {y_2})')


    lengde = ((x_1-x_2)**2 + (y_1-y_2)**2)**(1/2)
    #finner lengde for hvert av elementene

    koordinater_lengde_liste.append(lengde)

    '''
    print(f'\n{int(elem[0])}:               ({int(elem[1])}, {int(elem[2])})')
    print(f'lengde:           {round(lengde,2)}      [m]')
    print(f'E-modul:          {elem[3]}      [kN/mm^2]')
    print(f'Andrearealmoment: {round(elem[5]/(10**9),2)}*10^9 [mm^4]')
    '''
    
    
    k_11 = int((4*elem[6]/lengde)        /(10**9))
    k_12 = int((4*elem[6]/lengde *1/2)   /(10**9))
    k_21 = int((4*elem[6]/lengde *1/2)   /(10**9))
    k_22 = int((4*elem[6]/lengde)        /(10**9))
    #regner stivhetsbidraget til elementstivhetsmatrisen
      
    #print(f'knutepunkt_1_indeks: {knutepunkt_1_indeks},  knutepunkt_2_indeks: {knutepunkt_2_indeks}')
    
    systemstivhetsmatrise[knutepunkt_1_indeks][knutepunkt_1_indeks] += k_11
    systemstivhetsmatrise[knutepunkt_1_indeks][knutepunkt_2_indeks] += k_12
    systemstivhetsmatrise[knutepunkt_2_indeks][knutepunkt_1_indeks] += k_21
    systemstivhetsmatrise[knutepunkt_2_indeks][knutepunkt_2_indeks] += k_22
    #legger til stivhetsbidraget fra elementstivhetsmatrisen til systemstivhetsmatrisen på riktig indeks



    koordinater_lengde_matrise.append(koordinater_lengde_liste)

'''
print ('\n\nSystemstivhetsmatrise:  [(kN/mm^2 * mm^4)/m = N*mm] * 10^9\n')
for line in systemstivhetsmatrise:
    print(line)
'''