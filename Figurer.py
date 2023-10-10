import matplotlib.pyplot as plt

def plot_elements(elementer, knutepunkter):
#Definere en funksjon som kan kalles for å tegne figur

    min_x=0
    max_x=0
    min_y=0
    max_y=0
    #Definerer min/max-verdier for koordinatene til knutepunktene

    for elem in elementer:

        x_verdier= [elem[8],elem[10]]
        y_verdier= [elem[9], elem[11]]
        #finner x/y-koordinatene til hvert av knutepunktene i elemntet
        
        plt.plot(x_verdier, y_verdier, 'y', linewidth=elem[7]/(10**12), linestyle="-")
        #plotter elementet som en linje med tykkelse proposjanalt med bøyestivheten til elementet

        if elem[8]<elem[10]:
            x_koord=elem[8]+ abs(elem[8]-elem[10])/2
        elif elem[8]>elem[10]:
            x_koord=elem[8]- abs(elem[8]-elem[10])/2
        else:
            x_koord=elem[8]
        if elem[9]<elem[11]:
            y_koord=elem[9]+ abs(elem[9]-elem[11])/2
        elif elem[9]>elem[11]:
            y_koord=elem[9]- abs(elem[9]-elem[11])/2
        else:
            y_koord=elem[9]
        #finner koordinatene hvor label til element-ID skal plottes
    
        plt.text(x_koord, y_koord, f'{int(elem[0])}', fontsize=8)
        #plotter label til hvert av elementene

        for knute in knutepunkter:
            plt.plot(knute[1],knute[2], 'ro')
            plt.text(knute[1]+0.5,knute[2]-2,int(knute[0]), fontsize=14)
        #plotter første knutepunkt i hvert element samt label til knutepunktet
    
            if knute[1] < min_x:
                min_x = knute[1]
            if knute[1] > max_x:
                max_x = knute[1]
            if knute[2] < min_y:
                min_y = knute[2]
            if knute[2] > max_y:
                max_y = knute[2]
            #eventuelt oppdaterer min/max-verdier til koordinatene


    plt.legend()
    plt.xlabel('x-koordinater')
    plt.ylabel('y-koordinater')
    plt.title('Konstruksjon')
    plt.xlim(min_x -10 , max_x +10)
    plt.ylim(min_y -30 , max_y +30)
    plt.show()    
    #setter sammen og plotter figuren