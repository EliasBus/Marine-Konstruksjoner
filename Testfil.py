print("Fjerner og tester på nytt")

print("OKei gutta:")
print("CTRL + SHIFT + P og så Git: sync for å oppdatere desktop vsCode")

print("Fn + F5 for å oppdatere selve github-siden")
#Man kan også endre kode direkte i GIThub
#Når noen andre endrer kode må man starte med å synce så man har den mest oppdaterte koden

#For å teste hele koden CTRL + SHIFT + P så skriv git clone, velg riktig prosjekt
#lag så ny mappe, deretter så har du en klone av hele prosjektet
#Send melding hvis noe er uklart, ses på søndag tommel opp

import numpy as np
theta = np.pi/4

transformasjon_matrise=np.array(
        [[np.cos(theta),np.sin(theta),0,0,0,0],
        [-np.sin(theta),np.cos(theta),0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,np.cos(theta),np.sin(theta),0],
        [0,0,0,-np.sin(theta),np.cos(theta),0],
        [0,0,0,0,0,1]])
print(transformasjon_matrise)
print('\n\n')

K_trans = np.linalg.inv(transformasjon_matrise)

print(K_trans)