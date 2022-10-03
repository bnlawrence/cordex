# Includes domain definitions taken from
#    https://cordex.org/wp-content/uploads/2012/11/CORDEX-domain-description_231015.pdf

definitions = '''

The primary definition is in rotated coordinates with the domain size set in terms of 
0.44 degree cells in the rotated coordinate system.

In other coordinate systems 

Coordinates of the TLC, Centre point of the Northern Boundary (CNB) and Top Right Hand Corner
(TRC) in non-rotated coordinates:
- TLC (Longitude,Latitude)
- CNB (Longitude,Latitude)
- TRC (Longitude,Latitude)

Coordinates of the Centre point of the Eastern Boundary (CEB), Centre point of the domain (CPD),
Centre point of the Western Boundary (CWB):
- CEB (Longitude,Latitude)
- CPD (Longitude,Latitude)
- CWB (Longitude,Latitude),

Coordinates of the Bottom Left Corner (BLC), Centre point of the Southern Boundary (CSB) and
Bottom Right Hand Corner (BRC) in non-rotated coordinates:
- BLC (Longitude,Latitude)
- CSB (Longitude,Latitude)
- BRC (Longitude,Latitude)
'''

rotated_delta = 0.44

regions = {
    (4,'EURO','Europe'):[
        {'RotPole': (198.0, 39.25), 'TLC': (331.79, 21.67), 'Nx':106, 'Ny':103},
        {'TLC': (315.86, 60.21),
         'CNB': (1.92, 71.84),
         'TRC': (64.4, 66.65),
         'CWB': (338.23, 42.36),
         'CPD': (9.75, 49.68),
         'CEB': (44.77, 46.72),
         'BLC': (350.01, 22.20),
         'CSB': (12.48, 27.34),
         'BRC': (36.30, 25.36) }
        ],
    (12, 'MED','Mediterranean'):[
        {'RotPole':(198.0, 39.25), 'TLC':(336.78, 5.94), 'Nx':98, 'Ny': 63},
        {'TLC': (339.79, 50.65),
         'CNB': (15.0, 56.66),
         'TRC': (50.85, 52.34),
         'CWB': (348.12, 38.35),
         'CPD': (15.75, 43.02),
         'CEB': (43.41, 39.70),
         'BLC': (353.96, 25.63),
         'CSB': (16.22, 29.39),
         'BRC': (38.33, 26.73) }
        ],
    (9,'ANZ','Australasia'):[
       {'RotPole': (321.38, -60.31), 'TLC': (142.16, 33.44), 'Nx': 200, 'Ny':129},
       {'TLC': (110.19, 8.76),
        'CNB': (146.16, 3.87),
        'TRC': (182.02, 12.21),
        'CWB': (101.41, -18.03),
        'CPD': (147.63, -24.26),
        'CEB': (199.57, -27.90),
        'BLC': (89.25, -44.28),
        'CSB': (150.03, -52.36),
        'BRC': (206.57, -39.25), }
    ],
    (11,'Arctic','Arctic'):[
        {'RotPole': (0.0, 6.55), 'TLC': (337.12, 33.88), 'Nx':116, 'Ny':133},
        {'TLC': (214.68, 55.43),
         'CNB': (175.24, 62.56),
         'TRC': (140.59, 52.53),
         'CWB': (273.09, 67.17),
         'CPD': (57.07, 86.86),
         'CEB': (87.92, 63.37),
         'BLC': (324.82, 52.0),
         'CSB': (4.70, 59.14),
         'BRC': (40.35, 46.06),
        }
    ]
}