import Elementer_utvidet_matrise as ele
import matplotlib.pyplot as plt

for elem in ele.elementer_utvidet_matrise:
    plt.plot(elem[8],elem[9], marker='o', color='r')
    x_verdier= [elem[8],elem[10]]
    y_verdier= [elem[9], elem[11]]
    plt.plot(x_verdier, y_verdier, 'y', linestyle="-")
plt.show()    