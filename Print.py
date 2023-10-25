import Figurer              as fig
import numpy                as np
import matplotlib.pyplot    as plt      

def print_elementer(elementer_utvidet):
    print('\n\n\n------------------------------------------------------ELEMENTOVERSIKT------------------------------------------------------')
    for elem in elementer_utvidet:
        print(f'{f'Element {int(elem[0])}-->':<17}{f'Koord:  ({round(elem[3]/1000,2)}, {round(elem[4]/1000,2)})':<21}{f'---({round(elem[5]/1000,2)}, {round(elem[6]/1000,2)})':<20}{f'L: {round(elem[7]/1000,1)}m,':<15}{f'E: {int(elem[8]/1000)} GPa,':<15}{f'Flytspenning: {int(elem[8]/1000)} GPa'}')
    print('------------------------------------------------------ELEMENTOVERSIKT------------------------------------------------------')

def print_tversnittsdata(elementer_utvidet):
    print('\n\n\n------------------------------------------------------TVERRSNITTSDATA------------------------------------------------------')
    for elem in elementer_utvidet:
        if elem[10]==0:
            type='Rør'
        elif elem[10]==1:
            type='IPE'
        elif elem[10]==2:
            type='Boks'
        print(f'{f'Element {int(elem[0])}-->':<17}{type:<7}{f'Areal: {int(elem[11])} mm^2':<25}{f'I_z: {int(elem[12])}':<18}{f'mm^4':<10}{f'EI: {int(elem[13]/(10**9))}':<13}{f'*10^9 mm^4':<15}{f'Vinkel: {round(elem[14],3)}*'}')
    print('------------------------------------------------------TVERRSNITTSDATA------------------------------------------------------')



def print_K(K):
    print('\n\n\n---------------------------------------------------SYSTEMSTIVHETSMATRISE-----------------------------------------------------')
    linje=0
    for line in K:
        linje+=1
        print(f'\n--linje {linje} under-------------------------------------------------------------------------------------------------------------')
        for punkt in line:
            print(f'{round(punkt)}, ', end=" ")
        print('\n-----------------------------------------------------------------------------------------------------------------------------')
    print('---------------------------------------------------SYSTEMSTIVHETSMATRISE-----------------------------------------------------')


def print_R(R):
    print('\n\n\n-------------------------------------------------LASTVEKTOR-------------------------------------------------------------')
    for i in range(0,len(R),3):
        print(f'{f'Knutepunkt {int(i/3+1)}-->':<30}{f'N: {int(R[i])/1000} kN,':<30}{f'V: {(int(R[i+1])/1000)} kN,':<30}{f'M: {int((R[i+2]*180/np.pi)/(10**6))} kNm':<30}')
    print('-------------------------------------------------LASTVEKTOR-------------------------------------------------------------')


def print_r(r):
    print('\n\n\n---------------------------------DEFORMASJONER--------------------------------')
    for i in range(0,len(r),3):
        print(f'{f'Knutepunkt {int(i/3+1)}-->':<20}{f'x: {int(r[i])} mm,':<20}{f'y: {int(r[i+1])} mm,':<20}{f'theta: {round(r[i+2]*180/np.pi,3)}*':<30}')
    print('---------------------------------DEFORMASJONER--------------------------------')


def print_utnyttelse(elementer, utnyttelse):
    print('\n\n\n---------UTNYTTELSE----------')
    for i in range(len(elementer)):
        print(f'{f'Element {int(elementer[i][0])}-->':<20}{f'{round(utnyttelse[i],2)}%'}')
    print('--------UTNYTTELSE----------')


def print_figurer(knutepunkter, elementer, elementer_utvidet, r, skalar):
    fig.plot_vindu(knutepunkter)
    fig.plot_elementer(elementer, elementer_utvidet, knutepunkter)
    fig.plot_deformasjon(elementer_utvidet, knutepunkter, r, skalar)

    plt.show()

