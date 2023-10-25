import Figurer              as fig
import numpy                as np
import matplotlib.pyplot    as plt      

def print_elementer(elementer_utvidet):
    print('\n\n\n--------------------------------------------------------------ELEMENTOVERSIKT-------------------------------------------------------------')
    print(f'{'|':>140}')
    for elem in elementer_utvidet:
        print(f'{f'Element {int(elem[0])}-->':<17}{f'| Koord ({int(elem[1])} - {int(elem[2])}):':<20}{f'({round(elem[3]/1000,2)}, {round(elem[4]/1000,2)})':<14}{f'-- ({round(elem[5]/1000,2)}, {round(elem[6]/1000,2)})':<25}{f'L: {round(elem[7]/1000,1)}m,':<15}{f'E: {int(elem[8]/1000)} GPa,':<15}{f'Fy: {int(elem[8]/1000)} MPa':<15}{f'Vinkel: {round(elem[14],3)}*':<18}{'|'}')
    print(f'{'|':>140}')
    print('--------------------------------------------------------------ELEMENTOVERSIKT-------------------------------------------------------------')

def print_tversnittsdata(elementer_utvidet):
    print('\n\n\n------------------------------------------------------TVERRSNITTSDATA--------------------------------------------------')
    print(f'{'|':>121}')
    for elem in elementer_utvidet:
        if elem[10]==0:
            type='Rør'
        elif elem[10]==1:
            type='IPE'
        elif elem[10]==2:
            type='Boks'
        print(f'{f'Element {int(elem[0])}-->':<17}{f'| {type}':<10}{f'Areal: {int(elem[11])} mm^2':<30}{f'I_z: {int(elem[12])}':<18}{f'mm^4':<15}{f'EI: {int(elem[13]/(10**9))}':<13}{f'*10^9 mm^4':<17}{'|'}')
    print(f'{'|':>121}')
    print('------------------------------------------------------TVERRSNITTSDATA--------------------------------------------------')


def print_K(K):
    print('\n\n\n----------------------------------------------------------SYSTEMSTIVHETSMATRISE-------------------------------------------------------------')
    for x in range(len(K)):
        print(f'\n---------------------|Linje {x+1} under|-------------------------------------------------------------------------------------------------------------')
        for y in range(len(K)):
            print(f'{round(K[x][y])}, ', end=" ")
        print('\n-----------------------------------------------------------------------------------------------------------------------------')
    print('-------------------------------------------------------------SYSTEMSTIVHETSMATRISE-----------------------------------------------------------------')


def print_R(R):
    print('\n\n\n-------------------------------------------------LASTVEKTOR--------------------------------------------------')
    print(f'{'|':>111}')
    for i in range(0,len(R),3):
        print(f'{f'Knutepunkt {int(i/3+1)}-->':<17}{f'|':<10}{f' N: {int(R[i])/1000} kN,':<30}{f'V: {(int(R[i+1])/1000)} kN,':<30}{f'M: {int((R[i+2]*180/np.pi)/(10**6))} kNm':<23}{'|'}')
    print(f'{'|':>111}')
    print('-------------------------------------------------LASTVEKTOR---------------------------------------------------')


def print_r(r):
    print('\n\n\n---------------------------------DEFORMASJONER--------------------------------')
    print(f'{'|':>79}')
    for i in range(0,len(r),3):
        print(f'{f'Knutepunkt {int(i/3+1)}-->':<17}{f'| x: {int(r[i])} mm,':<20}{f'y: {int(r[i+1])} mm,':<20}{f'theta: {round(r[i+2]*180/np.pi,3)}*':<21}{'|'}')
    print(f'{'|':>79}')
    print('---------------------------------DEFORMASJONER--------------------------------')


def print_utnyttelse(elementer, utnyttelse):
    print('\n\n\n---------UTNYTTELSE----------')
    print(f'{'|':>29}')
    for i in range(len(elementer)):
        print(f'{f'Element {int(elementer[i][0])}-->':<17}{f'| {round(utnyttelse[i],2)}%':<11}{'|'}')
    print(f'{'|':>29}')
    print('--------UTNYTTELSE----------')


def print_figurer(knutepunkter, elementer, elementer_utvidet, r, skalar):
    fig.plot_vindu(knutepunkter)
    fig.plot_elementer(elementer, elementer_utvidet, knutepunkter)
    fig.plot_deformasjon(elementer_utvidet, knutepunkter, r, skalar)

    plt.show()

