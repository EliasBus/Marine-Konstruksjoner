def midtskjær_funksjon(elementer_utvidet, fordelte_laster, fastinnspenningskrefter):
    skj_result=[]
    for i in range(len(elementer_utvidet)):
        skjærkrefter=[]
        knute_1=int(elementer_utvidet[i][1])
        knute_2=int(elementer_utvidet[i][2])
        L=elementer_utvidet[i][7]
        m_ende1 =fastinnspenningskrefter[(knute_1-1)*3+2]
        m_ende2 =fastinnspenningskrefter[(knute_2-1)*3+2]
        Q_ende1 =fastinnspenningskrefter[(knute_1-1)*3+1]
        Q_ende2 =fastinnspenningskrefter[(knute_2-1)*3+1]

        Q= -(m_ende1+m_ende2)/L
        #finner total skjærkraft fra to endemomenter
        skjærkrefter.append(Q)
        skjærkrefter.append(Q_ende1)
        skjærkrefter.append(Q_ende2)
        skj_result.append(skjærkrefter)
    return skj_result