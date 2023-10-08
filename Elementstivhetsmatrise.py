import Tverrsnittsdata as tve
import Innlesning as inn

elementstivhetsmatrise=[]
liste=[]
for i in range(inn.antall_knutepunkt):
    liste.append(0)
for i in range(inn.antall_knutepunkt):
    elementstivhetsmatrise.append(liste)

for elem in tve.tverrsnittsdata_matrise:
    knutepunkt_1 = elem[1]
    knutepunkt_2 = elem[2]
    x_1 = inn.knutepunkter_matrise[int(knutepunkt_1)-1][1]
    y_1 = inn.knutepunkter_matrise[int(knutepunkt_1)-1][2]
    x_2 = inn.knutepunkter_matrise[int(knutepunkt_2)-1][1]
    y_2 = inn.knutepunkter_matrise[int(knutepunkt_2)-1][2]
    lengde = ((x_1-x_2)**2 + (y_1-y_2)**2)**(1/2)
    print(f'element: {elem[0]} , lengde = {lengde}')
    for i in range(4):
        k_11 = 4

print ('elementstivhetsmatrise\n\n')
for line in elementstivhetsmatrise:
    print(line)