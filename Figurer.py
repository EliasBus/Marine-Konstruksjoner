import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

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

    plt.figure(figsize=(7,7))
    plt.xlabel('x-koordinater')
    plt.ylabel('y-koordinater')
    plt.title('Konstruksjon')
    margin = max_x *0.2
    plt.xlim(min_x -margin , max_x *2.5)
    plt.ylim(min_y -margin , max_y +margin)
    #setter sammen og plotter figuren



def plot_elementer(elementer, elementer_utvidet, knutepunkter):
#Definerer en funksjon som kan kalles for å tegne konsktruksjonen

    for i in range(len(elementer)):

        x_verdier= [elementer_utvidet[i][3],elementer_utvidet[i][5]]
        y_verdier= [elementer_utvidet[i][4], elementer_utvidet[i][6]]
        #finner x/y-koordinatene til hvert av knutepunktene i elemntet
        
        tverrsnittstype=elementer[i][5]

        if tverrsnittstype == 0:
            farge='y-'
            tykkelse=   elementer[i][7] *2
            #           ytre radius *2
        elif tverrsnittstype ==1:
            farge='c-'
            tykkelse=   elementer[i][7]*2 + elementer[i][8]
            #           høyde flens *2    + høyde stag
        elif tverrsnittstype == 2:
            farge='g-'
            tykkelse=   elementer[i][7]
            #           høyde boks
        tykkelse/=(2*10**2)
        #finner fargen og tykkelsen/høyden til tverrsnittet


        plt.plot(x_verdier, y_verdier, farge, linewidth=tykkelse, alpha =1)
        #plotter elementet som en linje med tykkelse proposjanalt med bøyestivheten til elementet

        if elementer_utvidet[i][3]<elementer_utvidet[i][5]:
            x_koord=elementer_utvidet[i][3]+ abs(elementer_utvidet[i][3]-elementer_utvidet[i][5])/2
        elif elementer_utvidet[i][3]>elementer_utvidet[i][5]:
            x_koord=elementer_utvidet[i][3]- abs(elementer_utvidet[i][3]-elementer_utvidet[i][5])/2
        else:
            x_koord=elementer_utvidet[i][3]
        if elementer_utvidet[i][4]<elementer_utvidet[i][6]:
            y_koord=elementer_utvidet[i][4]+ abs(elementer_utvidet[i][4]-elementer_utvidet[i][6])/2
        elif elementer_utvidet[i][4]>elementer_utvidet[i][6]:
            y_koord=elementer_utvidet[i][4]- abs(elementer_utvidet[i][4]-elementer_utvidet[i][6])/2
        else:
            y_koord=elementer_utvidet[i][4]
        #finner koordinatene hvor label til element-ID skal plottes
    
        plt.text(x_koord, y_koord, f'{int(elementer_utvidet[i][0])}', fontsize=8)
        #plotter label til hvert av elementene

        for knute in knutepunkter:
            plt.plot(knute[1],knute[2], 'ro')
            plt.text(knute[1]+0.5,knute[2]-2,int(knute[0]), fontsize=14)
        #plotter knutepunktene samt label til knutepunktet



    plt.plot([], [], 'ro', label='Knutepunkter')
    plt.plot([], [], 'y-', linewidth=6, label='\u3007-Profil')
    plt.plot([], [], 'c-', linewidth=6, label='I-Profil')
    plt.plot([], [], 'g-', linewidth=6, label='\uF790-Profil')
    plt.legend(loc='lower right')
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
        
        
        plt.plot(x_verdier, y_verdier, 'r-', linewidth=1.5, alpha=0.3)
        #plotter element
    plt.plot([], [], 'r-', label='Deformasjonsskisse', alpha=0.5)
    plt.legend(loc='upper right')
    #plotter legend
        
       
