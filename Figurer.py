import matplotlib.pyplot    as plt
import numpy                as np
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
    plt.xlim(min_x -margin , max_x +margin*2)
    plt.ylim(min_y -margin , max_y +margin*5)
    #setter sammen og plotter figuren



def plot_konstruksjon(knutepunkter, elementer, elementer_utvidet, skalar_linjebredde, bakgrunn):
#Definerer en funksjon som kan kalles for å tegne konsktruksjonen
    plot_vindu(knutepunkter)
    if bakgrunn==0:
    #Funskjonen skal plotte konstruksjonen tydelig
        gjennomsiktighet=1
    elif bakgrunn==1:
    #Funksjonen skal plotte konstruksjonen i bakgrunnen
        gjennomsiktighet=0.5
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
            plt.plot(knute[1],knute[2], 'mo', alpha=gjennomsiktighet)
            plt.text(knute[1]+0.5,knute[2]-2,int(knute[0]), fontsize=14, alpha=gjennomsiktighet)
        #plotter knutepunktene samt label til knutepunktet
    plt.title('Konstruksjon')
    plt.plot([], [], 'mo',              label='Knutepunkter',   alpha=gjennomsiktighet)
    plt.plot([], [], 'y-', linewidth=6, label='O-Profil',       alpha=gjennomsiktighet)
    plt.plot([], [], 'c-', linewidth=6, label='I-Profil',       alpha=gjennomsiktighet)
    plt.plot([], [], 'g-', linewidth=6, label='\uF790-Profil',  alpha=gjennomsiktighet)
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
    knutepunkter=np.array(      knutepunkter[:, 1:3],   copy =1, dtype=float)
    elementer   =np.array(      elementer[:, 1:3],      copy =1, dtype=int)
    nod_dof     =np.arange(1,   knutepunkter.shape[0]+1, 1,      dtype=int)
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
    rotasjoner=[]
    knutepunkter = np.array(knutepunkter[:, 1:3])
    for i in range(len(knutepunkter)):
        x       =knutepunkter[i][0]
        y       =knutepunkter[i][1]
        x_def   =deformasjoner[i*3]
        y_def   =deformasjoner[i*3+1]
        rot     =deformasjoner[i*3+2]
        rotasjoner.append(rot*skalar_deformasjon)
        knutepunkter[i]= [knutepunkter[i][0]+deformasjoner[i*3]*skalar_deformasjon,knutepunkter[i][1]+deformasjoner[i*3+1]*skalar_deformasjon]
        #legger til deformasjoner til koordinatene, fra r
        #skalerer deformasjonene som skal plottes
    elementer = np.array(elementer[:, 1:3], copy =1, dtype=int)
    nod_dof = np.arange(1, knutepunkter.shape[0] + 1, 1, dtype=int)
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
        xx= np.arange(0, 1.01, 0.01)*L
        cs= CubicSpline(x, z, bc_type = ((1, -phi[0, 0]), (1, -phi[1, 0])))
        zz= cs(xx)
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


def plot_krefter(knutepunkter, elementer, elementer_utvidet, skalar_linjebredde,skalar_krefter, fordelte_laster, punktlaster):
    plot_konstruksjon(knutepunkter, elementer, elementer_utvidet, skalar_linjebredde, 1)
    plt.title('Punktlaster og fordelte laster')
    for i in range(len(punktlaster)):
        punkt=int(punktlaster[i][0])
        x=knutepunkter[punkt-1][1]
        y=knutepunkter[punkt-1][2]
        kraft = punktlaster[i][2]
        vinkel=punktlaster[i][1]/180*np.pi
        lengde=(10000 + kraft/300)*skalar_krefter
        dx=np.cos(vinkel)*lengde
        dy=np.sin(vinkel)*lengde
        plt.arrow(x-dx, y-dy, dx, dy, head_width = 1000*skalar_krefter ,width = 500*skalar_krefter,fc ='red', alpha =1)
        plt.text(x-dx, y-dy, f'{int(kraft/1000)} kN')
        #Plotter røde piler hvor punktlastene virker
    
    for i in range(len(fordelte_laster)):
        elem =int(fordelte_laster[i][0])
        punkt1=int(fordelte_laster[i][1])
        punkt2=int(fordelte_laster[i][2])
        x1=knutepunkter[punkt1-1][1]
        y1=knutepunkter[punkt1-1][2]
        x2=knutepunkter[punkt2-1][1]
        y2=knutepunkter[punkt2-1][2]
        q1 = fordelte_laster[i][3]
        q2 = fordelte_laster[i][4]
        for i in range(len(elementer_utvidet)):
            if elementer_utvidet[i][0]==elem:
                elem_ind = i
        vinkel=elementer_utvidet[elem_ind][14]-np.pi/2
        lengde1=q1*20*skalar_krefter
        lengde2=q2*20*skalar_krefter
        dx1=np.cos(vinkel)*lengde1
        dy1=np.sin(vinkel)*lengde1
        dx2=np.cos(vinkel)*lengde2
        dy2=np.sin(vinkel)*lengde2
        if q1!=0:
            plt.arrow(x1-dx1, y1-dy1, dx1, dy1, head_width = 1000*skalar_krefter,width = 500*skalar_krefter,fc ='blue', alpha=1)
        if q2!=0:
            plt.arrow(x2-dx2, y2-dy2, dx2, dy2, head_width = 1000*skalar_krefter,width = 500*skalar_krefter,fc ='blue', alpha=1)
        #plotter en pil for fordelt last ved ende, hvis den er ulik 0
        x=[x1-dx1,  x2-dx2]
        y=[y1-dy1, y2-dy2]
        plt.plot(x,y, 'b-', linewidth=1)
        #tegner en strek som markerer fordelt last
        plt.text(x1-dx1, y1-dy1, f'{q1} kN/m')
        plt.text(x2-dx2, y2-dy2, f'{q2} kN/m')
        #Plotter blå piler hvor fordelte laster virker
    plt.plot([], [], 'r->', linewidth=2, label='Punktlaster', alpha=1)
    plt.plot([], [], 'b->', linewidth=1, label='Fordelte laster', alpha=1)
    plt.legend(loc='upper right')
    #plotter legend
    plt.show()
