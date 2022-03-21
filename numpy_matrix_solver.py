import numpy as np

# https://github.com/numpy/numpy
# To be more precise: https://github.com/numpy/numpy/blob/main/numpy/linalg/linalg.py (Row 320)

a = np.array([[0.457, 0.330], [0.913, 0.659]])
b = np.array([0.127, 0.254])

x = np.linalg.solve(a, b)
print(x)
