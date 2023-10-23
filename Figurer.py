import matplotlib.pyplot as plt
import numpy as np

def plot_vindu(knutepunkter):
#Definerer en funksjon som kan kalles for å tegne tomt vindu med riktige dimensjoner

    min_x=0
    max_x=0
    min_y=0
    max_y=0
    #Definerer min/max-verdier for koordinatene til knutepunktene

    for knute in knutepunkter:
        if knute[1] < min_x:
            min_x = knute[1]
        if knute[1] > max_x:
            max_x = knute[1]
        if knute[2] < min_y:
            min_y = knute[2]
        if knute[2] > max_y:
            max_y = knute[2]
        #eventuelt oppdaterer min/max-verdier til koordinatene

    plt.xlabel('x-koordinater')
    plt.ylabel('y-koordinater')
    plt.title('Konstruksjon')
    margin = max_x *0.2
    plt.xlim(min_x -margin , max_x +margin)
    plt.ylim(min_y -margin , max_y *1.5)
    #setter sammen og plotter figuren



def plot_elementer(elementer_utvidet, knutepunkter):
#Definerer en funksjon som kan kalles for å tegne konsktruksjonen

    for elem in elementer_utvidet:

        x_verdier= [elem[3],elem[5]]
        y_verdier= [elem[4], elem[6]]
        #finner x/y-koordinatene til hvert av knutepunktene i elemntet
        
        linjebredde=elem[12]
        while linjebredde >20:
            linjebredde /=10
        #finner en linjebredde som er proposjonal med EI, men som ser bra ut i plottet


        plt.plot(x_verdier, y_verdier, 'y-', linewidth=linjebredde)
        #plotter elementet som en linje med tykkelse proposjanalt med bøyestivheten til elementet

        if elem[3]<elem[5]:
            x_koord=elem[3]+ abs(elem[3]-elem[5])/2
        elif elem[3]>elem[5]:
            x_koord=elem[3]- abs(elem[3]-elem[5])/2
        else:
            x_koord=elem[3]
        if elem[4]<elem[6]:
            y_koord=elem[4]+ abs(elem[4]-elem[6])/2
        elif elem[4]>elem[6]:
            y_koord=elem[4]- abs(elem[4]-elem[6])/2
        else:
            y_koord=elem[4]
        #finner koordinatene hvor label til element-ID skal plottes
    
        plt.text(x_koord, y_koord, f'{int(elem[0])}', fontsize=8)
        #plotter label til hvert av elementene

        for knute in knutepunkter:
            plt.plot(knute[1],knute[2], 'ro')
            plt.text(knute[1]+0.5,knute[2]-2,int(knute[0]), fontsize=14)
        #plotter knutepunktene samt label til knutepunktet

    plt.plot([], [], 'ro', label='Knutepunkter')
    plt.plot([], [], 'y-', linewidth=6, label='Elementer')
    plt.legend(loc='upper right')
    #Plotter legend


def plot_deformasjon(elementer, knutepunkter, deformasjoner, skalar):
    #Definerer en funksjon som kan kalles for å tegne figur med deformasjoner

    for elem in elementer:
        knute_1 = elem[1]
        knute_2 = elem[2]

        

        x_verdi_1= knutepunkter[knute_1-1][1] + deformasjoner[(knute_1-1)*3]   *skalar
        y_verdi_1= knutepunkter[knute_1-1][2] + deformasjoner[(knute_1-1)*3 +1]*skalar
        x_verdi_2= knutepunkter[knute_2-1][1] + deformasjoner[(knute_2-1)*3]   *skalar
        y_verdi_2= knutepunkter[knute_2-1][2] + deformasjoner[(knute_2-1)*3 +1]*skalar

        x_verdier=np.array([x_verdi_1,x_verdi_2])
        y_verdier=np.array([y_verdi_1,y_verdi_2])
        #finner x/y-koordinatene til hvert av knutepunktene i elemntet
        
        
        plt.plot(x_verdier, y_verdier, 'r--', linewidth=1.5)
        #plotter element
    plt.plot([], [], 'r--', label='Deformasjonsskisse')
    plt.legend(loc='upper right')
    #plotter legend
        
       
