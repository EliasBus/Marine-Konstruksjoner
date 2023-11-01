import numpy as np
import matplotlib.pyplot as plt
import math

def momenter_skjaer_normal(S, fordelte_laster, punktlaster, elementer_utvidet):

    #Setter opp plots for moment-, skjær- og aksialkraftdiagram

    #Lager en tabell for diagrammene. Slik kan man ha mange diagram i et vindu
    Tot = len(elementer_utvidet)

    #-------Endre verdiene av antall kolonner dersom du ønsker det :) -----
    Cols = 5
    Rows = Tot//Cols

    if Tot % Cols != 0:
        Rows += 1

    if Rows == 0:
        Rows += 1


    mom_fig, ax = plt.subplots(Rows, Cols, squeeze=False)
    mom_fig.suptitle("Momentdiagram for bjelkene [Nm]")
    mom_fig.tight_layout(pad=1.0)

    skj_fig, bx = plt.subplots(Rows, Cols, squeeze=False)
    skj_fig.suptitle("Skjærkraftdiagram for bjelkene [N]")
    skj_fig.tight_layout(pad=1.0)

    norm_fig, cx = plt.subplots(Rows, Cols, squeeze=False)
    norm_fig.suptitle("Normalkraft for bjelkene [N] ")
    norm_fig.tight_layout(pad=1.0)

    max_moment = np.zeros(len(elementer_utvidet))
    max_skjaer = np.zeros(len(elementer_utvidet))
    max_normal = np.zeros(len(elementer_utvidet))



    #Lasttilfelle, fordelt last
    for x in range (len(fordelte_laster)):

        #Sjekker om lasten har null intensitet, dersom den har det, hopper den over beregningene
        if(fordelte_laster[x][1] == 0 and fordelte_laster[x][2] == 0):
            continue

        #Resultatarray for momenter, skjærkraft og normalkraft
        m_res = []
        s_res = []
        n_res = []

        #Henter elementlengde
        elementnummer = 0
        for i in range(len(elementer_utvidet)):
            if elementer_utvidet[i][0]==elementer_utvidet[elementnummer][0]:
                l = elementer_utvidet[i][7]
                break
            elementnummer+=1

        #Oppretter et array med x-verdier fra 0 til L med 1000 verdier
        x_arr = np.linspace(0,l,1000)

        #Henter ut inensiteten til den fordelte lasten
        q1 = fordelte_laster[x][1]
        q2 = fordelte_laster[x][2]


        #Henter ut Q1, M1 og M2 for bjelken
        N_1 = S[elementer_utvidet[x][1]-1]
        Q_1 = S[elementer_utvidet[x][1]*2-1]
        Q_2 = S[elementer_utvidet[x][2]*2-1]
        M_1 = S[elementer_utvidet[x][1]*3-1]
        M_2 = S[elementer_utvidet[x][2]*3-1]

        #Regner ut momentet langs bjelken fra knutepunkt 1 til knutepunkt 2
        for x_temp in x_arr:
            m_res.append(1/3 * q1 * x_temp**2 + 1/6 * (q1 + ((q2 - q1)/(l))*x_temp)*x_temp**2 - Q_1*x_temp - M_1)
            s_res.append(q1 *x_temp + ((q2 - q1)/(2*l))*x_temp**2 - Q_1)
            n_res.append(-N_1)


        #Finner posisjonen til diagrammet i vinduet 
        row = int(math.ceil((elementnummer + 1)/Cols)) - 1
        col = int(elementnummer + 1 - (row)* Cols) - 1

        plot_diagrams(m_res, x_arr, elementnummer, ax, col, row)
        plot_diagrams(s_res, x_arr, elementnummer, bx, col, row)
        plot_diagrams(n_res, x_arr, elementnummer, cx, col, row)
        max_moment[elementnummer] = max([M_1, M_2, max(m_res)], key=abs)  #Legger til det største momentet som virker i bjelken, uavhengig av negativ eller positivt moment
        max_skjaer[elementnummer] = max([Q_1, Q_2, max(s_res)], key=abs)  #Legger til den største skjærkraften som virker i bjelken, --||--
        max_normal[elementnummer] = max(n_res) # --||--


    #Lasttilfelle, punktlast
    for x in range (len(punktlaster)):

        #Sjekker om lasten er null, dersom den har det, hopper den over beregningene
        if(punktlaster[x][2] == 0):
            continue

        #Resultatarray for momenter
        m_res = []
        s_res = []
        n_res = []

        #Henter elementlengde
        elementnummer = 0
        for i in range(len(elementer_utvidet)):
            if elementer_utvidet[i][0]==elementer_utvidet[elementnummer][0]:
                l = elementer_utvidet[i][7]
                break
            elementnummer+=1


        #Oppretter et array med x-verdier fra 0 til L med 1000 verdier
        x_arr = np.linspace(0,l,1000)

        #Henter ut kraften P:
        P = punktlaster[x][2]

        #Henter ut lengden fra knutepunkt 1 
        a = punktlaster[x][1]


        #Henter ut Q1, M1 og M2 for bjelkene
        N_1 = S[elementer_utvidet[x][1]-1]
        Q_1 = S[elementer_utvidet[x][1]*2-1]
        Q_2 = S[elementer_utvidet[x][2]*2-1]
        M_1 = S[elementer_utvidet[x][1]*3-1]
        M_2 = S[elementer_utvidet[x][2]*3-1]


        for x_temp in x_arr:
            if (x_temp > a):
                m_res.append(P*(x_temp - a) - Q_1*x_temp - M_1)
                s_res.append(P - Q_1)
                n_res.append(-N_1)

            else:
                m_res.append(-Q_1*x_temp - M_1)
                s_res.append(-Q_1)
                n_res.append(-N_1)


        #Finner posisjonen til diagrammet i vinduet 
        row = int(math.ceil((elementnummer + 1)/Cols)) - 1
        col = int(elementnummer + 1 - (row)* Cols) - 1

        plot_diagrams(m_res, x_arr, elementnummer, ax,  col, row)
        plot_diagrams(s_res, x_arr, elementnummer, bx,  col, row)
        plot_diagrams(n_res, x_arr, elementnummer, cx,  col, row)
        max_moment[elementnummer] = max([M_1, M_2, max(m_res)], key=abs) #Legger til det største momentet som virker i bjelken, uavhengig av negativ eller positivt moment
        max_skjaer[elementnummer] = max([Q_1, Q_2, max(s_res)], key=abs) #Legger til den største skjærkraften som virker i bjelken, --||--
        max_normal[elementnummer] = max(n_res) # --||--

    
    #Ingen ytre last, bare endemomenter
    for x in range(len(elementer_utvidet)):
        #Sjekker om det allerede har blitt regnet med moment fra tidligere funksjon
        if (max_moment[x] != 0):
            continue


        #Resultatarray for momenter
        m_res = []
        s_res = []
        n_res = []


        #Henter elementnummer og lengde
        elementnummer = 0
        for i in range(len(elementer_utvidet)):
            if elementer_utvidet[i][0]==elementer_utvidet[elementnummer][0]:
                l = elementer_utvidet[i][7]
                break
            elementnummer+=1


        #Oppretter et array med x-verdier fra 0 til L med 1000 verdier
        x_arr = np.linspace(0,l,1000)


        #Henter ut N1, Q1, Q2, M1 og M2 for bjelkene
        N_1 = S[elementer_utvidet[x][1]-1]
        Q_1 = S[elementer_utvidet[x][1]*2-1]
        Q_2 = S[elementer_utvidet[x][2]*2-1]
        M_1 = S[elementer_utvidet[x][1]*3-1]
        M_2 = S[elementer_utvidet[x][2]*3-1]


        #Regner ut verdier til momentdiagramet
        for x_temp in x_arr:
            m_res.append(-M_1 - Q_1*x_temp)
            s_res.append(-Q_1)
            n_res.append(-N_1)

        #Finner posisjonen til diagrammet i vinduet 
        row = int(math.ceil((elementnummer + 1)/Cols)) - 1
        col = int(elementnummer + 1 - (row)* Cols) - 1

        plot_diagrams(m_res, x_arr, elementnummer, ax, col, row)
        plot_diagrams(s_res, x_arr, elementnummer, bx, col, row)
        plot_diagrams(n_res, x_arr, elementnummer, cx, col, row)

        max_moment[elementnummer] = max([M_1, M_2, max(m_res)], key=abs) #Legger til det største momentet som virker i bjelken, uavhengig av negativ eller positivt moment
        max_skjaer[elementnummer] = max([Q_1, Q_2, max(s_res)], key=abs) #Legger til den største skjærkraften som virker i bjelken, --||--
        max_normal[elementnummer] = max(n_res) # --||--
        

    return max_moment, max_skjaer, max_normal

def plot_diagrams(res, x_arr, elementnummer, ax, col, row):
    ax[row, col].plot(x_arr, res)
    ax[row, col].hlines(y=0, xmin=0, xmax=np.max(x_arr), colors='r', linestyles='--', lw=0.5)
    ax[row, col].set_title(str(elementnummer), fontsize=10)
    ax[row, col].set_xlabel("Meter", fontsize=8)