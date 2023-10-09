

#Python-fil med kode som tar inn strings fra txt-fil og legger det inn i variabler og matriser.

knutepunkter_matrise=[]
elementer_matrise=[]
fordelte_laster_matrise=[]
punktlaster_matrise=[]

with open('input_fil.txt', 'r') as input_fil:
    linjer = input_fil.readlines()
    #åpner filer og leser inn linje for linje

for line in linjer:
    if line.startswith("#Antall knutepunkt"):
        antall_knutepunkt = int(linjer[linjer.index(line) + 1])
    elif line.startswith("#Antall element"):
        antall_element = int(linjer[linjer.index(line) + 1])
    elif line.startswith("#Antall fordelte laster"):
        antall_fordelte_laster = int(linjer[linjer.index(line) + 1])
    elif line.startswith("#Antall punktlaster"):
        antall_punktlaster = int(linjer[linjer.index(line) + 1])
#lagrer variabler

for line in linjer:
    if line.startswith("#Knutepunkter:"):
        index=1
        while index <= antall_knutepunkt:
            knutepunkt = [float(x.strip()) for x in linjer[linjer.index(line) + index].split(',')]
            knutepunkter_matrise.append(knutepunkt)
            index+=1
    if line.startswith("#Elementer:"):
        index=1
        while index <= antall_element:
            element = [float(x.strip()) for x in linjer[linjer.index(line) + index].split(',')]
            elementer_matrise.append(element)
            index+=1
    if line.startswith("#Fordelte laster:"):
        index=1
        while index <= antall_fordelte_laster:
            fordelt_last = [float(x.strip()) for x in linjer[linjer.index(line) + index].split(',')]
            fordelte_laster_matrise.append(fordelt_last)
            index+=1
    if line.startswith("#Punktlaster:"):
        index=1
        while index <= antall_punktlaster:
            punktlast = [float(x.strip()) for x in linjer[linjer.index(line) + index].split(',')]
            punktlaster_matrise.append(punktlast)
            index+=1
#lagrer listene med data


