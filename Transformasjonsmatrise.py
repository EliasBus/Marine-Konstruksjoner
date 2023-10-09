import Elementer_utvidet_matrise as ele
import math

for i in ele.elementer_utvidet_matrise:
    hosliggende = (i[10]-i[8])
    motstående = (i[11]-i[9])
    if hosliggende == 0:
        theta = math.pi/2
    else:
        theta= math.atan(motstående / hosliggende)
    
    print(f'Element {i[0]}: {round(theta*180/math.pi)}')
