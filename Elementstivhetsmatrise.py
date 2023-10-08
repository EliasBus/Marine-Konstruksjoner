import Tverrsnittsdata as tve
import Innlesning as inn


str_matrise=inn.antall_knutepunkt
elementstivhetsmatrise = [[0 for i in range(str_matrise)] for i in range(str_matrise)]

print ('\n\nelementstivhetsmatrise\n')
for line in elementstivhetsmatrise:
    print(line)

for elem in tve.tverrsnittsdata_matrise:
    knutepunkt_1 = int(elem[1])
    knutepunkt_2 = int(elem[2])
    #print(f'element {elem[0]} , knute_1 {knutepunkt_1}, knute_2 {knutepunkt_2}')
    knutepunkt_1_indeks = knutepunkt_1 -1
    knutepunkt_2_indeks = knutepunkt_2 -1
    x_1 = inn.knutepunkter_matrise[knutepunkt_1_indeks][1]
    y_1 = inn.knutepunkter_matrise[knutepunkt_1_indeks][2]
    x_2 = inn.knutepunkter_matrise[knutepunkt_2_indeks][1]
    y_2 = inn.knutepunkter_matrise[knutepunkt_2_indeks][2]
    print(f'\nelement {elem[0]} , (x, y)_{knutepunkt_1}: ({x_1}, {y_1}), (x, y)_{knutepunkt_2}: ({x_2}, {y_2})')

    lengde = ((x_1-x_2)**2 + (y_1-y_2)**2)**(1/2)
    #lengde for hver av elementene
    #print(f'element: {elem[0]} , lengde: {lengde} m')
    
    k_11 = int(4*elem[5]/lengde)
    k_12 = int(4*elem[5]/lengde *1/2)
    k_21 = int(4*elem[5]/lengde *1/2)
    k_22 = int(4*elem[5]/lengde)
    print(f'knutepunkt_1_indeks: {knutepunkt_1_indeks},  knutepunkt_2_indeks: {knutepunkt_2_indeks}')
    elementstivhetsmatrise[knutepunkt_1_indeks][knutepunkt_1_indeks] += k_11
    elementstivhetsmatrise[knutepunkt_1_indeks][knutepunkt_2_indeks] += k_12
    elementstivhetsmatrise[knutepunkt_2_indeks][knutepunkt_1_indeks] += k_21
    elementstivhetsmatrise[knutepunkt_2_indeks][knutepunkt_2_indeks] += k_22

print ('\n\nelementstivhetsmatrise\n')
for line in elementstivhetsmatrise:
    print(line)