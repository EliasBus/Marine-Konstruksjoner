import numpy as np

def elementsivhetsmatrise_funskjon(elem):
    E=elem[8]
    A=elem[11]
    L=elem[7]
    I=elem[12]

    elementstivhetsmatrise=np.array([
    [E*A/L , 0             , 0            , -E*A/L, 0             , 0            ],
    [0     , 12*E*I/(L**3) , -6*E*I/(L**2), 0     , -12*E*I/(L**3), -6*E*I/(L**2)],
    [0     , -6*E*I/(L**2) , 4*E*I/L      , 0     , 6*E*I/(L**2)  , 2*E*I/L      ],
    [-E*A/L, 0             , 0            , E*A/L , 0             , 0            ],
    [0     , -12*E*I/(L**3), 6*E*I/(L**2) , 0     , 12*E*I/(L**3) , 6*E*I/(L**2) ],
    [0     , -6*E*I/(L**2) , 2*E*I/L      , 0     , 6*E*I/(L**2)  , 4*E*I/L      ],
    ])   
    #ovenfor er elementstivhetsmatrisen
    return elementstivhetsmatrise