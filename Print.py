import Figurer              as fig
import numpy                as np
import matplotlib.pyplot    as plt  

#tekstfarger:
rød_u   ='\033[4;31m'
rød   ='\033[1;31m'
gul     ='\033[1;33m'
magenta ='\033[1;35m'
blå     ='\033[1;34m'
grønn   ='\033[1;32m'
cyan    ='\033[1;36m'
#Bakgrunnsfarger:
gul_b   ='\033[;;43m'
grønn_b ='\033[;;42m'
cyan_b  ='\033[;;46m'
#reset:
reset = '\033[m'
  

def print_elementer(elementer_utvidet):
    print(f'{gul}{'\n\n\n------------------------------------------ELEMENTOVERSIKT----------------------------------------------'}{reset}')
    print(f'{rød_u+'Element \031':<21}{'(k1-k2):':<13}{'Koordinater':<12}{'-- Koordinater':<20}{'Lengde:':<9}{'E-modul:':<11}{'Flyt:':<11}{'Vinkel:'}{reset}{gul}{'|':>7}{reset}')
    for elem in elementer_utvidet:
        print(f'{f'{int(elem[0])} \u2192':<12}{f'| ({int(elem[1])} - {int(elem[2])}):':<15}{f'({round(elem[3]/1000,1)}, {round(elem[4]/1000,1)})':<12}{f'-- ({round(elem[5]/1000,2)}, {round(elem[6]/1000,2)})':<20}{f'{round(elem[7]/1000,1)}m':<9}{f'{int(elem[8]/1000)} GPa':<11}{f'{int(elem[9])} MPa':<11}{f'\u03B8: {round(elem[14]*180/np.pi,3)}\u00B0':<13}{gul}{'|'}{reset}')
    print(f'{gul}{'|':>104}{reset}')
    print(f'{gul}{'------------------------------------------ELEMENTOVERSIKT----------------------------------------------'}{reset}')

def print_tversnittsdata(elementer_utvidet):
    print(f'{magenta}{'\n\n\n---------------------------------------TVERRSNITTSDATA------------------------------------'}{reset}')
    print(f'{rød_u+'Element \031':<21}{'Type:':<13}{'Areal:':<18}{'I\u1d67:':<22}{'Bøyestivhet (EI):':<11}{reset}{magenta}{'|':>7}{reset}')
    for elem in elementer_utvidet:
        if elem[10]==0:
            type='Rør'
            farge_b=cyan_b
        elif elem[10]==1:
            type='IPE'
            farge_b=gul_b
        elif elem[10]==2:
            type='Boks'
            farge_b=grønn_b
        print(f'{f'{int(elem[0])} \u2192':<12}{f'| {farge_b}{type}{reset}':<25}{f'{int(elem[11])} mm\u00b2':<18}{f'{int(elem[12])}':<14}{f'mm\u2074':<8}{f'{int(elem[13]/(10**9))}':<10}{f'\u22c510\u2079 Nmm\u00b2':<13}{magenta}{'|'}{reset}')
    print(f'{magenta}{'|':>91}{reset}')
    print(f'{magenta}{'---------------------------------------TVERRSNITTSDATA------------------------------------'}{reset}')


def print_K(K):
    print(rød+'\n\n\n----------------------------------------------------------SYSTEMSTIVHETSMATRISE---------------------------------------------'+reset)
    for x in range(len(K)):
        print(f'\n---------------------|Linje {x+1} \031|------------------------------------------------------------------------------------------')
        for y in range(len(K)):
            print(f'{round(K[x][y])}, ', end=" ")
        print('\n-----------------------------------------------------------------------------------------------------------------------------')
    print(rød+'----------------------------------------------------------SYSTEMSTIVHETSMATRISE---------------------------------------------'+reset)


def print_R(R):
    print(f'{blå}{'\n\n\n----------------------------LASTVEKTOR--------------------------------'}{reset}')
    print(f'{rød_u+'Knutepunkt \031':<24}{'Aksial:':<17}{'Skjær:':<17}{'Moment:':<15}{reset}{blå}{'|':>5}{reset}')
    for i in range(0,len(R),3):
        print(f'{f'{int(i/3+1)} \u2192':<16}{f'|{int(R[i]/1000)}':<10}{f' kN|':<7}{f'|{(int(R[i+1]/1000))}':<10}{f' kN|':<7}{f'|{int((R[i+2]*180/np.pi)/(10**6))}':<13}{f' kNm|':<7}{blå}{'|'}{reset}')
    print(f'{blå}{'|':>71}{reset}')
    print(f'{blå}{'----------------------------LASTVEKTOR--------------------------------'}{reset}')


def print_r(r):
    print(f'{grønn}{'\n\n\n----------------------------DEFORMASJONER--------------------------------'}{reset}')
    print(f'{rød_u+'Knutepunkt \031':<25}{'Forskyvning \u2192':<18}{'Forskyvning \u2191:':<20}{'Rotasjon \u21ba':<13}{reset}{grønn}{'|':>5}{reset}')
    for i in range(0,len(r),3):
        print(f'{f'{int(i/3+1)} \u2192':<16}{f'| x: {int(r[i])} mm,':<20}{f'y: {int(r[i+1])} mm,':<20}{f'\u03B8: {round(r[i+2]*180/np.pi,3)}\u00B0':<17}{grønn}{'|'}{reset}')
    print(f'{grønn}{'|':>74}{reset}')
    print(f'{grønn}{'----------------------------DEFORMASJONER--------------------------------'}{reset}')


def print_utnyttelse(elementer, utnyttelse):
    print(f'{cyan}{'\n\n\n--------UTNYTTELSE---------'}{reset}')
    print(f'{rød_u+'Element \031':<23}{'\u03c3/f\u1d67\u22c5100%':<11}{reset}{cyan}{'|'}{reset}')
    for i in range(len(elementer)):
        utnyttelsesgrad=utnyttelse[i]
        if utnyttelsesgrad >= 80:
            print(f'{f'{int(elementer[i][0])} \u2192':<14}{f'| '}{rød}{f'{round(utnyttelsesgrad,2)} %':<11}{reset}{cyan}{'|'}{reset}')
        else:
            print(f'{f'{int(elementer[i][0])} \u2192':<14}{f'| {round(utnyttelsesgrad,2)} %':<13}{cyan}{'|'}{reset}')
        #printes i rødt om utnyttelsesgrad er større enn 80%
    print(f'{cyan}{'|':>28}{reset}')
    print(f'{cyan}{'--------UTNYTTELSE---------'}{reset}')


def print_figurer(knutepunkter, elementer, elementer_utvidet, r, skalar):
    fig.plot_vindu(knutepunkter)
    fig.plot_elementer(elementer, elementer_utvidet, knutepunkter)
    fig.plot_deformasjon(elementer_utvidet, knutepunkter, r, skalar)

    plt.show()

