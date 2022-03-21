from sympy import *

# https://github.com/sympy/sympy
# To be more precise: https://github.com/sympysympy/polys/matrices/linsolve.py (Row 45)

x, y = symbols('x y')
print(linsolve(Matrix(([0.457, 0.330, 0.127], [0.913, 0.659, 0.254])), (x, y)))
