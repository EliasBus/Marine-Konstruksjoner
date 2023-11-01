import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

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
    plt.figure(figsize=(9,7))
    plt.xlabel('x-koordinater')
    plt.ylabel('y-koordinater')
    margin = max_x *0.2
    plt.xlim(min_x -margin , max_x +margin*4)
    plt.ylim(min_y -margin , max_y +margin)
    #setter sammen og plotter figuren



def plot_konstruksjon(knutepunkter, elementer, elementer_utvidet, skalar_linjebredde, bakgrunn):
#Definerer en funksjon som kan kalles for å tegne konsktruksjonen
    plot_vindu(knutepunkter)
    if bakgrunn==0:
    #Funskjonen skal plotte konstruksjonen tydelig
        gjennomsiktighet=1
    elif bakgrunn==1:
    #Funksjonen skal plotte konstruksjonen i bakgrunnen
        gjennomsiktighet=0.3
    else:
        print('bakgrunn skal ha verdi 1 for å brukes som bagrunn, 0 for å plotte som konstruksjon')
    for i in range(len(elementer)):
        x_verdier= [elementer_utvidet[i][3], elementer_utvidet[i][5]]
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
        tykkelse*=(skalar_linjebredde/(2*10**2)) #skalerer tykkelsen
        #finner fargen og tykkelsen/høyden til tverrsnittet
        plt.plot(x_verdier, y_verdier, farge, linewidth=tykkelse, alpha =gjennomsiktighet)
        #plotter elementet som en linje med tykkelse proposjanalt med høyden til elementet

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

        plt.text(x_koord, y_koord, f'{int(elementer_utvidet[i][0])}', fontsize=8, alpha=gjennomsiktighet)
        #plotter label til hvert av elementene
        for knute in knutepunkter:
            plt.plot(knute[1],knute[2], 'ro', alpha=gjennomsiktighet)
            plt.text(knute[1]+0.5,knute[2]-2,int(knute[0]), fontsize=14, alpha=gjennomsiktighet)
        #plotter knutepunktene samt label til knutepunktet
    plt.title('Konstruksjon')
    plt.plot([], [], 'ro',                     label='Knutepunkter',   alpha=gjennomsiktighet)
    plt.plot([], [], 'y-', linewidth=tykkelse, label='O-Profil',       alpha=gjennomsiktighet)
    plt.plot([], [], 'c-', linewidth=tykkelse, label='I-Profil',       alpha=gjennomsiktighet)
    plt.plot([], [], 'g-', linewidth=tykkelse, label='\uF790-Profil',  alpha=gjennomsiktighet)
    plt.legend(loc='upper right')
    #Plotter legend
    if bakgrunn==0:
        plt.show()
    #Plotter konstruskjonen hvis den ikke er ment som bakgrunn



def plot_deformasjon(knutepunkter, elementer, elementer_utvidet, deformasjoner, skalar_deformasjon, skalar_linjebredde):
#Definerer en funksjon som kan kalles for å tegne figur med deformasjoner i x- og y-retning
    plot_konstruksjon(knutepunkter, elementer, elementer_utvidet, skalar_linjebredde, 1)
    plt.title('Deformasjoner (kun x- og y-retning)')
    linjebredde=3
    for elem in elementer:
        knute_1 = int(elem[1])
        knute_2 = int(elem[2])

        x_verdi_1= knutepunkter[knute_1-1][1] + deformasjoner[(knute_1-1)*3]   *skalar_deformasjon
        y_verdi_1= knutepunkter[knute_1-1][2] + deformasjoner[(knute_1-1)*3 +1]*skalar_deformasjon
        x_verdi_2= knutepunkter[knute_2-1][1] + deformasjoner[(knute_2-1)*3]   *skalar_deformasjon
        y_verdi_2= knutepunkter[knute_2-1][2] + deformasjoner[(knute_2-1)*3 +1]*skalar_deformasjon
        x_verdier=np.array([x_verdi_1,x_verdi_2])
        y_verdier=np.array([y_verdi_1,y_verdi_2])
        #finner x/y-koordinatene til hvert av knutepunktene i elemntet
        plt.plot(x_verdier, y_verdier, 'r-', linewidth=linjebredde, alpha=1)
        #plotter element
    plt.plot([], [], 'r-', linewidth=linjebredde, label='Deformasjonsskisse', alpha=1)
    plt.legend(loc='upper right')
    #plotter legend
    plt.show()



def plot_rotasjoner(knutepunkter, elementer, elementer_utvidet, deformasjoner, skalar_deformasjon, skalar_linjebredde):
#funksjon for å plotte bøyninger i elementene (rotasjoner)
    plot_konstruksjon(knutepunkter, elementer, elementer_utvidet, skalar_linjebredde, 1)
    plt.title('Deformasjoner (bøyning i elementene)')
    linjebredde=3
    knutepunkter = np.array(knutepunkter[:, 1:3], copy =1, dtype=int)
    elementer = np.array(elementer[:, 1:3], copy =1, dtype=int)
    nod_dof = np.arange(1, knutepunkter.shape[0] + 1, 1, dtype=int)
    rotasjoner=[]
    for i in range(0, len(deformasjoner), 3):
        rotasjoner.append(deformasjoner[i+2]*skalar_deformasjon)
        #henter kun ut rotasjoner fra r
    for iel in range(0, elementer.shape[0]):
        delta_x = knutepunkter[elementer[iel, 1] - 1, 0] - knutepunkter[elementer[iel, 0] - 1, 0]
        delta_z = knutepunkter[elementer[iel, 1] - 1, 1] - knutepunkter[elementer[iel, 0] - 1, 1]
        L = np.sqrt(delta_x ** 2 + delta_z ** 2)
        if delta_z >= 0:
            psi = np.arccos(delta_x / L)
        else:
            psi = -np.arccos(delta_x / L)
        phi = np.zeros((2, 1))
        for inod in range(0, 2):
            if nod_dof[elementer[iel, inod] - 1] > 0:
                phi[inod] = rotasjoner[nod_dof[elementer[iel, inod] - 1] - 1]
        x = np.array([0, L])
        z = np.array([0, 0])
        xx = np.arange(0, 1.01, 0.01)*L
        cs = CubicSpline(x, z, bc_type = ((1, -phi[0, 0]), (1, -phi[1, 0])))
        zz = cs(xx)
        # Rotate
        xxzz = np.array([[np.cos(psi), -np.sin(psi)], [np.sin(psi), np.cos(psi)]]) @ np.vstack([xx, zz])
        # Displace
        xx2 = xxzz[0, :] + knutepunkter[elementer[iel, 0] - 1, 0]
        zz2 = xxzz[1, :] + knutepunkter[elementer[iel, 0] - 1, 1]
        plt.plot(xx2, zz2, 'r-', linewidth = linjebredde, alpha=1)
    plt.plot([], [], 'r-', linewidth=linjebredde, label='Deformasjonsskisse', alpha=1)
    plt.legend(loc='upper right')
    #plotter legend
    plt.show()



def plot_rotasjoner_og_deformasjoner(knutepunkter, elementer, elementer_utvidet, deformasjoner, skalar_deformasjon, skalar_linjebredde):
#funksjon for å plotte alle deformasjoner
    plot_konstruksjon(knutepunkter, elementer, elementer_utvidet, skalar_linjebredde, 1)
    plt.title('Deformasjoner (både x-retning, y-retning og rotasjoner)')
    linjebredde=3
    knutepunkter = np.array(knutepunkter[:, 1:3])
    for i in range(len(knutepunkter)):
        knutepunkter[i]= [knutepunkter[i][0]+deformasjoner[i*3]*skalar_deformasjon,knutepunkter[i][1]+deformasjoner[i*3+1]*skalar_deformasjon]
    #legger til deformasjoner til koordinatene fra r
    elementer = np.array(elementer[:, 1:3], copy =1, dtype=int)
    nod_dof = np.arange(1, knutepunkter.shape[0] + 1, 1, dtype=int)
    rotasjoner=[]
    for i in range(0, len(deformasjoner), 3):
        rotasjoner.append(deformasjoner[i+2]*skalar_deformasjon)
    #henter kun ut rotasjoner fra r
    for iel in range(0, elementer.shape[0]):
        delta_x = knutepunkter[elementer[iel, 1] - 1, 0] - knutepunkter[elementer[iel, 0] - 1, 0]
        delta_z = knutepunkter[elementer[iel, 1] - 1, 1] - knutepunkter[elementer[iel, 0] - 1, 1]
        L = np.sqrt(delta_x ** 2 + delta_z ** 2)
        if delta_z >= 0:
            psi = np.arccos(delta_x / L)
        else:
            psi = -np.arccos(delta_x / L)
        phi = np.zeros((2, 1))
        for inod in range(0, 2):
            if nod_dof[elementer[iel, inod] - 1] > 0:
                phi[inod] = rotasjoner[nod_dof[elementer[iel, inod] - 1] - 1]
        x = np.array([0, L])
        z = np.array([0, 0])
        xx = np.arange(0, 1.01, 0.01)*L
        cs = CubicSpline(x, z, bc_type = ((1, -phi[0, 0]), (1, -phi[1, 0])))
        zz = cs(xx)
        # Rotate
        xxzz = np.array([[np.cos(psi), -np.sin(psi)], [np.sin(psi), np.cos(psi)]]) @ np.vstack([xx, zz])
        # Displace
        xx2 = xxzz[0, :] + knutepunkter[elementer[iel, 0] - 1, 0]
        zz2 = xxzz[1, :] + knutepunkter[elementer[iel, 0] - 1, 1]
        plt.plot(xx2, zz2, 'r-', linewidth = linjebredde, alpha=1)
    plt.plot([], [], 'r-', linewidth=linjebredde, label='Deformasjonsskisse', alpha=1)
    plt.legend(loc='upper right')
    #plotter legend
    plt.show()