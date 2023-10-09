import Systemstivhetsmatrise as sys
import math

elementer_vinkler_liste=[]
#lager tom liste

for i in sys.koordinater_lengde_matrise:
    #iterer gjennom alle elementer
    hosliggende = (i[2]-i[0])
    #finner lengde på hosliggende katet
    lengde = i[4]
    #finner lengde på hypotenus
    
    theta= math.acos(hosliggende / lengde)
    #regner vinkelen med cosinus
    if i[2]>i[0] and i[3]<i[1] and theta<(math.pi/2):
        theta+=math.pi/2
    #korrigerer for fortegnsfeil
    
    elementer_vinkler_liste.append(theta)
    #legger til vinkelen i lista

    
