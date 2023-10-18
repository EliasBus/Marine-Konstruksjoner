import numpy as np


def transformasjonsmatrise_funksjon(element):
    #definerer en funksjon som tar inn et element
    #setter theta lik vinkelen til elementet
    theta=element[13]
    #Oppretter transformasjonsmatrisen
    transformasjon_matrise=np.array([ 
        [np.cos(theta) ,np.sin(theta),0,0             ,0            ,0],
        [-np.sin(theta),np.cos(theta),0,0             ,0            ,0],
        [0             ,0            ,1,0             ,0            ,0],
        [0             ,0            ,0,np.cos(theta) ,np.sin(theta),0],
        [0             ,0            ,0,-np.sin(theta),np.cos(theta),0],
        [0             ,0            ,0,0             ,0            ,1]
        ])
        
    return transformasjon_matrise


