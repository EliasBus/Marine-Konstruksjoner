import Elementer_utvidet_matrise as ele
import math

for i in ele.elementer_utvidet_matrise:
    #iterer gjennom alle elementer
    hosliggende = (i[10]-i[8])
    motstående = (i[11]-i[9])
    #finner lengde på hosliggende og motstående katet
    if hosliggende == 0:
        theta = math.pi/2
        #for å ikke dele på 0
    else:
        theta= math.atan(motstående / hosliggende)
        #regner ellers vinkelen med tangens
    
    print(f'Element {i[0]}: {round(theta*180/math.pi)}')
