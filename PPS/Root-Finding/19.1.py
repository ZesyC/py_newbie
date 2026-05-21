import numpy as np
from scipy import optimize

f = lambda x: np.cos(x) - x
r = optimize.fsolve(f, -2)
print(f'r = {r}')

result = f(r)
print(f'result = {result}')