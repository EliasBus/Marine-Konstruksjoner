import Elementer_utvidet_matrise as ele
import Innlesning as inn
import matplotlib.pyplot as plt



for elem in ele.elementer_utvidet_matrise:
    
    x_verdier= [elem[8],elem[10]]
    y_verdier= [elem[9], elem[11]]
    plt.plot(x_verdier, y_verdier, 'y', linestyle="-")
#plotter hvert av elementene

    for knute in inn.knutepunkter_matrise:
        plt.plot(knute[1],knute[2], 'ro')
        plt.text(knute[1],knute[2],int(knute[0]), fontsize=12, ha='right', va='bottom')
    #plotter første knutepunkt i hvert element



for elem in ele.elementer_utvidet_matrise:
    print(f'{elem[1]}')

plt.legend()
plt.xlabel('x-koordinater')
plt.ylabel('y-koordinater')
plt.title('Konstruksjon')
plt.show()    