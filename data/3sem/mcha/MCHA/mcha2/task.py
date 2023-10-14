import numpy as np

k = 3
E = 0.000000100000000

C = np.array([
    [0.0100000000000, 0, -0.0200000000000, 0, 0],
    [0.0100000000000, 0.0100000000000, -0.0200000000000, 0, 0],
    [0, 0.0100000000000, 0.0100000000000, 0, -0.0200000000000],
    [0, 0, 0.0100000000000, 0.0100000000000, 0],
    [0, 0, 0, 0.0100000000000, 0.0100000000000]
])

D = np.array([
    [1.3300000000000, 0.2100000000000, 0.1700000000000, 0.1200000000000, -0.1300000000000],
    [-0.1300000000000, -1.3300000000000, 0.1100000000000, 0.1700000000000, 0.1200000000000],
    [0.1200000000000, -0.1300000000000, -1.3300000000000, 0.1100000000000, 0.1700000000000],
    [0.1700000000000, 0.1200000000000, -0.1300000000000, -1.3300000000000, 0.1100000000000],
    [0.1100000000000, 0.6700000000000, 0.1200000000000, -0.1300000000000, -1.3300000000000]
])

b = np.array(
    [1.200000000000, 2.200000000000, 4.000000000000, 0, -1.200000000000]
)

A = k * C + D