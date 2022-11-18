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
    (11,'Arc','Arctic'):[
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

global_south = {
    (1,'S-Ame','South America'):[
        {'RotPole':(123.94, -70.6),'TLC':(143.92, 34.76), 'Nx':146, 'Ny':167},
        {'TLC': (273.26, 18.50),
         'CNB': (300.56, 15.40),
         'TRC': (327.52, 17.23),
         'CWB': (265.88, -17.30),
         'CPD': (299.70, -21.11),
         'CEB': (333.36, -18.84),
         'BLC': (254.28, -52.66),
         'CSB': (298.13, -57.61),
         'BRC': (343.02, -54.6),
        }
    ],
    (2,'C-Ame', 'Central America'): [
        {'RotPole': (113.98, 75.74), 'TLC': (307.20, 20.68), 'Nx':210, 'Ny':113},
        {'TLC': (235.74, 28.79),
         'CNB': (286.45, 34.83),
         'TRC': (337.78, 31.40),
         'CWB': (241.11, 4.68),
         'CPD': (287.29, 10.20),
         'CEB': (333.40, 7.10),
         'BLC': (246.10, -19.46),
         'CSB': (288.0, -14.42),
         'BRC': (329.46, -17.23)
        }
    ],
    (5, 'Africa','Africa'): [
        {'RotPole': (180.0, 90.0), 'TLC': (335.36, 42.24), 'Nx':194, 'Ny':201},
        {'TLC': (335.36, 42.24),
         'CNB': (17.60, 42.24),
         'TRC': (60.28, 42.24),
         'CWB': (335.36, -1.32),
         'CPD': (17.60, -1.32),
         'CEB': (60.28, -1.32),
         'BLC': (335.36, -45.76),
         'CSB': (17.60, -45.76),
         'BRC': (60.28, -45.76),
        }
    ],
    ('6','S-Asia','South Asia'):[
       {'RotPole': (236.66, 79.95), 'TLC': (327.88, 35.20), 'Nx':193, 'Ny':130},
       {'TLC': (19.88, 43.5),
        'CNB': (68.41, 45.07),
        'TRC': (115.55, 41.0),
        'CWB': (23.48, 15.51),
        'CPD': (67.18, 16.93),
        'CEB': (110.47, 13.09),
        'BLC': (26.19, -12.97),
        'CSB': (66.29, -11.66),
        'BRC': (106.43, -15.23),
       } 
    ],
    ('7','E-Asia','East Asia'):[
        {'RotPole': (296.3, 61.0), 'TLC': (316.77, 32.90), 'Nx':203, 'Ny':167},
        {'TLC': (51.59, 50.50),
         'CNB': (116.70, 61.90),
         'TRC': (181.50, 50.31),
         'CWB': (67.11, 25.72),
         'CPD': (116.57, 34.40),
         'CEB': (165.94, 25.56),
         'BLC': (76.91, -0.10),
         'CSB': (116.51, 6.90),
         'BRC': (156.08, -0.24),
        }
    ],
    (13,'MENA','Middle East North Africa'): [
        {'RotPole': (180.0, 90.0), 'TLC': (333.6, 44.88), 'Nx':232,  'Ny': 118},
        {'TLC': (333., 45.0),
         'CNB': (24.5, 45.0),
         'TRC': (76.0, 45),
         'CWB': (333.0, 19.0),
         'CPD': (24.5, 19.0),
         'CEB': (333.0, 19.0),
         'BLC': (333.0, -7),
         'CSB': (24.5, -7),
         'BRC': (76.0, -7)},
    ],
    (14,'SEA','South East Asia'):[
        {'RotPole': (180.0, 90.0), 'TLC': (89.26, 27.28), 'Nx':264,  'Ny':194},
        {'TLC':(27.26, 89.26),
         'CNB':(27.26, 118.04),
         'TRC':(27.26, 146.96),
         'CWB':(6.5, 89.26),
         'CPD':(6.5,118.04),
         'CEB':(6.5, 146.96),
         'BLC':(-15.14,89.26),
         'CSB':(-15.14, 118.04),
         'BRC':(-14.81, 146.96)}
    ],
    
}