import matplotlib.pyplot as plt
import numpy as np

def momentdiagram_funksjon(momenter, elementer_utvidet, fordelte_laster):
    num_plots = int(len(elementer_utvidet))
    fig, axes = plt.subplots(4, 5, figsize=(15, 7), gridspec_kw={'wspace': 0.4, 'hspace': 1})  
    fig.align_ylabels
    fig.align_xlabels
    for i in range(num_plots):
        L=elementer_utvidet[i][7]
        knute_1=int(elementer_utvidet[i][1])
        knute_2=int(elementer_utvidet[i][2])
        q1=0
        q2=0
        for ford in fordelte_laster:
            if int(ford[0])==int(elementer_utvidet[i][0]):
                if int(ford[1])==int(knute_1):
                    q1 = ford[3]
                    q2 = ford[4]
                elif int(ford[1])==int(knute_2):
                    q2 = ford[3]
                    q1 = ford[4]
        m_ende1=momenter[i][1]
        m_ende2=momenter[i][2]
        inkrement=1000
        x=np.linspace(1,inkrement)
        x=L*x/inkrement
        M_x_q1  =q1*x/(6*L)*(2*L**2-3*L*x+x**2)
        M_x_q2  =q2*x/(6*L)*(2*L**2-3*L*x+x**2)
        #Momentdiagram fra fordelte laster
        M_x_m1  =m_ende1-m_ende1/L*x
        M_x_m2  =m_ende2/L*x
        #Momentdiagram fra endemomenter
        M_x     =M_x_q1 +M_x_q2 +M_x_m1 +M_x_m2
        #Legger til bidrag fra q1, q2, endemoment 1 og endemoment 2
        if i < len(elementer_utvidet)*1/4:
            row=0
            col=i
        elif i< len(elementer_utvidet)*2/4:
            row=1
            col=i-int(len(elementer_utvidet)*1/4)
        elif i< len(elementer_utvidet)*3/4:
            row=2
            col=i-int(len(elementer_utvidet)*2/4)
        else:
            row=3
            col=i-int(len(elementer_utvidet)*3/4)
        #deler opp diagrammene i et 4x5-grid
        axes[row, col].plot(x, M_x)
        axes[row, col].set_title(f'Element {int(elementer_utvidet[i][0])}')
        axes[row, col].set_ylim([-max(abs(M_x)), max(abs(M_x))])  # x-akse i midten
        axes[row, col].spines['top'].set_position('zero')
        #alle verdiene er i mm (x-akse) og i Nmm (y-akse)
        axes[row, col].set_xlabel('x [mm]')  
        axes[row, col].set_ylabel('M(x) [Nmm]')          
    plt.show()
