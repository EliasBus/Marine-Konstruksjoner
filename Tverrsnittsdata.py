import numpy as np
#importerer data fra Innlesning.py som 'inn'
#importerer np for å bruke np.pi

tverrsnittsdata_matrise=[]
#etablerer en matrise som skal inneholde tversnittsdata for alle elementer

def tverrsnittsdata_funk(elementer_matrise):
    for i in elementer_matrise:
        tverrsnittsdata =[]
        #Nuller listen for hver iterasjon
        tverrsnittstype =i[5]
        E               =i[3]

        if tverrsnittstype==0:
        #hvis rør
            r_ytre=i[7]
            r_indre=i[6]
            areal              =np.pi * (r_ytre**2 - r_indre**2)
            #                   pi    * (ytre_radius^2 - indre_radius^2)
            andrearealmoment   =np.pi * (r_ytre**4 - r_indre**4) / 4
            #                   pi    * (ytre_radius^4 - indre_radius^4) / 4
            bøyestivhet        =E * andrearealmoment
            #                   andrearealmoment * E-modul
        elif tverrsnittstype==1:
        #hvis I-profil
            b_flens=i[6]
            h_flens=i[7]
            h_stag=i[8]
            b_stag=i[9]
            areal              =2 * b_flens*h_flens   + h_stag*b_stag
            #                   2 * areal flens       + areal stag
            andrearealmoment   =2 * (b_flens*h_flens**(3) /12 + (h_stag/2+h_flens/2)**2 * (b_flens*h_flens)) + h_stag**(3) *b_stag/12
            #                   2 * (I_flens            + (steinerbidrag_flens            ) + I_stag
            bøyestivhet        =E * andrearealmoment
            #                   andrearealmoment * E-modul
        elif tverrsnittstype==2:
        #hvis boks-profil
            b_boks=i[6]
            h_boks=i[7]
            b_stag=i[8]
            h_flens=i[9]
            areal              =b_boks*h_boks       - (b_boks-2*b_stag)*(h_boks-2*h_flens)
            #                   areal_ytre_boks - areal_indre_boks
            andrearealmoment   =2 * (b_boks*h_flens**(3) /12 + ((h_boks/2-h_flens/2)**2 * b_boks*h_flens)) + 2 * (b_stag*(h_boks-2*h_flens)**(3) /12)
            #                   2 * (I_flens            + (steinerbidrag_flens            ) + 2 * (I_stag)
            bøyestivhet        =E * andrearealmoment
            #                   E-modul * andrearealmoment
        else:
        #hvis vi har ugyldig verdi i input_fil
            areal='input feil'
            andrearealmoment='input feil'
            bøyestivhet='input feil'
        
        tverrsnittsdata.append(areal)
        tverrsnittsdata.append(andrearealmoment)
        tverrsnittsdata.append(bøyestivhet)
        #Legger inn element_ID, startpunkt, sluttpunkt, E-modul
        #Legger inn hver av verdiene inn i en liste for hver av elementene
        tverrsnittsdata_matrise.append(tverrsnittsdata)
        #Legger til hver liste i en matrise for alle elementer
    return tverrsnittsdata_matrise