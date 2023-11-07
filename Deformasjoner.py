import numpy as np

def deformasjoner_funk(R, systemstivhetsmatrise):
    deformasjoner_vektor = np.linalg.inv(systemstivhetsmatrise) @ R
    #vektor for deformasjoner defineres ved r = K^-1 * R
    return deformasjoner_vektor