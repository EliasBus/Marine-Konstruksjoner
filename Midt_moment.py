def midtmoment_funksjon(elementer_utvidet, fordelte_laster, fastinnspenningskrefter):
    mom_result=[]
    for i in range(len(elementer_utvidet)):
        knute_1=int(elementer_utvidet[i][1])
        knute_2=int(elementer_utvidet[i][2])
        L=elementer_utvidet[i][7]
        m_midt=0
        momenter=[]
        for ford in fordelte_laster:
            if int(ford[0])==int(elementer_utvidet[i][0]):
            #sjekker om elementet har fordelt_last last
                if int(ford[1])==int(knute_1):
                    q1 = ford[3]
                    q2 = ford[4]
                elif int(ford[1])==int(knute_2):
                    q2 = ford[3]
                    q1 = ford[4]
                #finner lastintensitet i knutepunktpunkt 1 og 2
                m_midt=1/24*L**2*(q1+q2)/2
                #midtmoment pga fordelt last (parabel)
        m_ende1 =fastinnspenningskrefter[(knute_1-1)*3+2]
        m_ende2 =fastinnspenningskrefter[(knute_2-1)*3+2]
        m_midt +=m_ende1/2
        m_midt +=m_ende2/2
        #midmtmoment pga innspenningsmomenter
        momenter.append(m_midt)
        momenter.append(m_ende1)
        momenter.append(m_ende2)
        mom_result.append(momenter)
    return mom_result