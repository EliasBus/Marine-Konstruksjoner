import numpy as np

def deformasjoner_funk(lastvektor, systemstivhetsmatrise, n_knutepunkter):
    
    deformasjoner_vektor = np.linalg.inv(systemstivhetsmatrise) @ lastvektor
    #vektor for deformasjoner defineres ved r = K^-1 * R
    
    
    return deformasjoner_vektor