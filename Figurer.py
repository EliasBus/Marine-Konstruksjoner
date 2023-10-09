import Elementer_utvidet_matrise as ele
import Innlesning as inn
import matplotlib.pyplot as plt


min_x=0
max_x=0
min_y=0
max_y=0

for elem in ele.elementer_utvidet_matrise:

    
    
    
    x_verdier= [elem[8],elem[10]]
    y_verdier= [elem[9], elem[11]]
    plt.plot(x_verdier, y_verdier, 'y', linewidth=elem[7]/(10**12), linestyle="-")

    if elem[8]<elem[10]:
        x_koord=elem[8]+ abs(elem[8]-elem[10])/2
    elif elem[8]>elem[10]:
        x_koord=elem[8]- abs(elem[8]-elem[10])/2
    else:
        x_koord=elem[8]
    if elem[9]<elem[11]:
        y_koord=elem[9]+ abs(elem[9]-elem[11])/2
    elif elem[9]>elem[11]:
        y_koord=elem[9]- abs(elem[9]-elem[11])/2
    else:
        y_koord=elem[9]
    
    
    plt.text(x_koord, y_koord, f'{int(elem[0])}', fontsize=10)
#plotter hvert av elementene

    for knute in inn.knutepunkter_matrise:
        plt.plot(knute[1],knute[2], 'ro')
        plt.text(knute[1],knute[2],int(knute[0]), fontsize=16)
    #plotter første knutepunkt i hvert element
    
        if knute[1] < min_x:
            min_x = knute[1]
        if knute[1] > max_x:
            max_x = knute[1]
        if knute[2] < min_y:
            min_y = knute[2]
        if knute[2] > max_y:
            max_y = knute[2]




plt.legend()
plt.xlabel('x-koordinater')
plt.ylabel('y-koordinater')
plt.title('Konstruksjon')
plt.xlim(min_x -10 , max_x +10)
plt.ylim(min_y -10 , max_y +30)
plt.show()    