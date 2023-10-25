import Figurer              as fig
import numpy                as np
import matplotlib.pyplot    as plt      

def print_elementer(elementer_utvidet):
    print('\n\n----SYSTEMSTIVHETSMATRISE-----------------')
    for elem in elementer_utvidet:
        print(f'--Element {int(elem[0])} under-----------------------------------------------------------------------------------')
        print(f'Koordinater: ({int(elem[3])},{int(elem[5])})-({int(elem[4])},{int(elem[6])}) , Lengde: {round(elem[7]/1000)}m, E-modul og flytgrense: {int(elem[8]/1000)} GPa, {int(elem[9])} MPa, \nAreal: {int(elem[11])} mm^2, I: {int(elem[13])} mm^4, Vinkel: {int(elem[14]*180/np.pi)}*\n')

def print_K(K):
    print('\n\n----SYSTEMSTIVHETSMATRISE-----------------')
    linje=0
    for line in K:
        linje+=1
        print(f'\n--linje {linje} under-------------------------------------------------------------------------------------------------------------')
        for punkt in line:
            print(f'{round(punkt)}, ', end=" ")
        print('\n-----------------------------------------------------------------------------------------------------------------------------')


def print_R(R):
    print('\n\n----LASTVEKTOR-----------------')
    for i in range(0,len(R),3):
        print(f'Knutepunkt {int(i/3+1)}: x {int(R[i])/1000} kN,  y {(int(R[i+1])/1000)} kN,  Moment {int((R[i+2]*180/np.pi)/(10**6))} kNm\n')

def print_r(r):
    print('\n\n----DEFORMASJONER--------------------------------')
    for i in range(0,len(r),3):
        print(f'Knutepunkt {int(i/3+1)}: x {int(r[i])} mm,  y {int(r[i+1])} mm,  theta {round(r[i+2]*180/np.pi,3)}*')

def print_utnyttelse(elementer, utnyttelse):
    print('\n\n----UTNYTTELSE--------------')
    for i in range(len(elementer)):
        print(f'Element {int(elementer[i][0])}: {round(utnyttelse[i],2)}%')


def print_figurer(knutepunkter, elementer, elementer_utvidet, r, skalar):
    fig.plot_vindu(knutepunkter)
    fig.plot_elementer(elementer, elementer_utvidet, knutepunkter)
    fig.plot_deformasjon(elementer_utvidet, knutepunkter, r, skalar)

    plt.show()

