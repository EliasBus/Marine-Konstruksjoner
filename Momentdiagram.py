import matplotlib.pyplot as plt
import numpy as np

def momentdiagram_funksjon(momenter, elementer_utvidet, fordelte_laster):
    num_plots = len(elementer_utvidet)
    fig, axes = plt.subplots(2, num_plots, figsize=(16, 6))  # Create subplots
    
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
        x=np.linspace(0,100)
        x=L/x
        M_x_q1  =q1*x/(6*L)*(2*L**2-3*L*x+x**2)
        M_x_q2  =q2*x/(6*L)*(2*L**2-3*L*x+x**2)
        #Momentdiagram fra fordelte laster
        M_x_m1  =m_ende1-m_ende1/L*x
        M_x_m2  =m_ende2/L*x
        #Momentdiagram fra endemomenter
        M_x     =M_x_q1+M_x_q2+M_x_m1+M_x_m2

        if i < len(elementer_utvidet)/2:
            row=0
            col=i
        else:
            row=1
            col=i-int(len(elementer_utvidet)/2)
        axes[row, col].plot(x, M_x)
        axes[row, col].set_title(f'Element {int(elementer_utvidet[i][0])}')
        axes[row, col].axis('off')
    plt.tight_layout(rect=[0, 0, 2, 0.9])  # Adjust subplot parameters
    
    plt.show()
