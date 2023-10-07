

#Knutepunkter:
#Format: 
# 1. knutepunktsnummer
# 2. x-koordinat
# 3. y-koordinat
# 4. Fast innspent(1), ikke fast innspent(0)

with open('input_fil.txt', 'r') as input_fil:
    linjer = input_fil.readlines()


for line in linjer:
    if line[:2].isdigit():
        antall_pkt=int(line[:2])
        break

ind= -1
for line in linjer:
    ind+=1
    if line[0]=='0':
        forste_pkt_ind = ind
        break

pkt = []

for ind, line in enumerate(linjer):
    if forste_pkt_ind <= ind < (forste_pkt_ind + antall_pkt):
        pkt.append(line)

print(f'Første punkt har indeks {forste_pkt_ind}, og vi har {antall_pkt} knutepunkter.\n')
for line in pkt:
    print(line)



