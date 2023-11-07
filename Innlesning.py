#Python-fil med kode som tar inn strings fra txt-fil og legger det inn i variabler og matriser.
rød     ='\033[1;31m'
reset   = '\033[m'
feilmelding     =rød+'FEILMELDING: '+reset

def innlesning_funk(fil):
    knutepunkter_matrise    =[]
    elementer_matrise       =[]
    fordelte_laster_matrise =[]
    punktlaster_matrise     =[]

    with open(fil, 'r') as input_fil:
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
                if len(knutepunkt)!=4:
                    print(feilmelding+f'Knutepunkt nr {index} i input-filen mangler data')
                    #feilmeldig
                knutepunkter_matrise.append(knutepunkt)
                index+=1
        if line.startswith("#Elementer:"):
            index=1
            while index <= antall_element:
                element = [float(x.strip()) for x in linjer[linjer.index(line) + index].split(',')]
                if len(element)!=10:
                    print(feilmelding+f'Element nr {index} i input-filen mangler data, sjekk om tverrsnittet har fire dimensjoner')
                    #feilmeldig
                elementer_matrise.append(element)
                index+=1
        if line.startswith("#Fordelte laster:"):
            index=1
            while index <= antall_fordelte_laster:
                fordelt_last = [float(x.strip()) for x in linjer[linjer.index(line) + index].split(',')]
                if len(fordelt_last)!=5:
                    print(feilmelding+f'Fordelt last nr {index} i input-filen mangler data')
                    #feilmeldig
                fordelte_laster_matrise.append(fordelt_last)
                index+=1
        if line.startswith("#Punktlaster:"):
            index=1
            while index <= antall_punktlaster:
                punktlast = [float(x.strip()) for x in linjer[linjer.index(line) + index].split(',')]
                if len(punktlast)!=3:
                    print(feilmelding+f'Punktlast nr {index} i input-filen mangler data')
                    #feilmeldig
                punktlaster_matrise.append(punktlast)
                index+=1
    #lagrer matrisene med data

    return antall_knutepunkt, antall_element, antall_fordelte_laster, antall_punktlaster, knutepunkter_matrise, elementer_matrise, fordelte_laster_matrise, punktlaster_matrise