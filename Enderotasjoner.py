import numpy as np

def enderotasjoner_funk(lastvektor, systemstivhetsmatrise, n_knutepunkter):
    
    enderotasjoner_vektor = np.linalg.inv(systemstivhetsmatrise) @ lastvektor
    #vektor for enderotasjoner defineres ved r = K^-1 * R
    
    
    return enderotasjoner_vektor