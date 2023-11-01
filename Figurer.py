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
    plt.figure(figsize=(7,7))
    plt.xlabel('x-koordinater')
    plt.ylabel('y-koordinater')
    plt.title('Konstruksjon')
    margin = max_x *0.2
    plt.xlim(min_x -margin , max_x +margin*4)
    plt.ylim(min_y -margin , max_y +margin)
    #setter sammen og plotter figuren




def plot_konstruksjon(elementer, elementer_utvidet, knutepunkter):
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
    plt.plot([], [], 'y-', linewidth=6, label='O-Profil')
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
        
        plt.plot(x_verdier, y_verdier, 'r-', linewidth=1.5, alpha=0.5)
        #plotter element
    plt.plot([], [], 'r-', label='Deformasjonsskisse', alpha=0.5)
    plt.legend(loc='upper right')
    #plotter legend

from scipy.interpolate import CubicSpline

def plot_rotasjoner(punkt, elem, numbers, index_start, r):
    # This is a translation of the original function written by Josef Kiendl in Matlab
    # This function plots the deformed beam structure defined by nodes and elements
    # The bool (0 or 1) 'numbers' decides if node and element numbers are plotted or not
 
    # Change input to the correct format
    nodes = np.array(punkt[:, 1:3], copy =1, dtype=int)
    el_nod = np.array(elem[:, 1:3], copy =1, dtype=int)
    nod_dof = np.arange(1, nodes.shape[0] + 1, 1, dtype=int)
    print(elem)
    print(el_nod)
 
    if numbers == 1:
        # Plot node number
        for inod in range(0, nodes.shape[0]):
            plt.text(nodes[inod, 0], nodes[inod, 1], str(inod + index_start), color = 'red', fontsize = 16)
 
    for iel in range(0, el_nod.shape[0]):
        delta_x = nodes[el_nod[iel, 1] - 1, 0] - nodes[el_nod[iel, 0] - 1, 0]
        delta_z = nodes[el_nod[iel, 1] - 1, 1] - nodes[el_nod[iel, 0] - 1, 1]
        L = np.sqrt(delta_x ** 2 + delta_z ** 2)
        if delta_z >= 0:
            psi = np.arccos(delta_x / L)
        else:
            psi = -np.arccos(delta_x / L)
 
        phi = np.zeros((2, 1))
        for inod in range(0, 2):
            if nod_dof[el_nod[iel, inod] - 1] > 0:
                phi[inod] = r[nod_dof[el_nod[iel, inod] - 1] - 1]
        x = np.array([0, L])
        z = np.array([0, 0])
        xx = np.arange(0, 1.01, 0.01)*L
        cs = CubicSpline(x, z, bc_type = ((1, -phi[0, 0]), (1, -phi[1, 0])))
        zz = cs(xx)
 
        # Rotate
        xxzz = np.array([[np.cos(psi), -np.sin(psi)], [np.sin(psi), np.cos(psi)]]) @ np.vstack([xx, zz])
 
        # Displace
        xx2 = xxzz[0, :] + nodes[el_nod[iel, 0] - 1, 0]
        zz2 = xxzz[1, :] + nodes[el_nod[iel, 0] - 1, 1]
        plt.plot(xx2, zz2, 'r-', linewidth = 1.5, alpha=0.5)
 
        if numbers == 1:
            # Plot element numbers. These are not plotted in the midpoint to
            # avoid number superposition when elements cross in the middle
            plt.text(xx2[round(xx2.size / 2.5)], zz2[round(xx2.size / 2.5)], str(iel + index_start), color = 'blue', fontsize = 16)
        
        
    
    plt.plot([], [], 'r-', label='Deformasjonsskisse', alpha=0.5)
    plt.legend(loc='upper right')
    #plotter legend