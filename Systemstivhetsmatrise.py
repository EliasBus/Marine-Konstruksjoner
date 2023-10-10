

def systemstivhetsmatrise_funksjon(elementer,antall_knutepunkt):
    #definerer en funkssjon som tar inn elementer og antall knutepunkt
    str_matrise=antall_knutepunkt
    #finner dimensjonen på systemstivhetsmatrisen
    systemstivhetsmatrise = [[0 for i in range(str_matrise)] for i in range(str_matrise)]
    #lager matrisen med bare 'nuller'


    for elem in elementer:
    #iterer gjennom hvert element i konstruksjonen

        k_11 = int((4*elem[12]/elem[7])        /(10**9))
        k_12 = int((4*elem[12]/elem[7] *1/2)   /(10**9))
        k_21 = int((4*elem[12]/elem[7] *1/2)   /(10**9))
        k_22 = int((4*elem[12]/elem[7])        /(10**9))
        #regner stivhetsbidraget til elementstivhetsmatrisen

        knutepunkt_1_indeks = elem[1]-1
        knutepunkt_2_indeks = elem[2]-1
      
        systemstivhetsmatrise[knutepunkt_1_indeks][knutepunkt_1_indeks] += k_11
        systemstivhetsmatrise[knutepunkt_1_indeks][knutepunkt_2_indeks] += k_12
        systemstivhetsmatrise[knutepunkt_2_indeks][knutepunkt_1_indeks] += k_21
        systemstivhetsmatrise[knutepunkt_2_indeks][knutepunkt_2_indeks] += k_22
        #legger til stivhetsbidraget fra elementstivhetsmatrisen til systemstivhetsmatrisen på riktig indeks
    return systemstivhetsmatrise
    

