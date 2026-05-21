import numpy as np

def my_newton(f, df, x0, tol, R=None, E=None):
    if R is None or E is None:
        R = []
        E = []
    
    R.append(float(x0))
    E.append(float(abs(f(x0))))

    if E[-1] < tol:
        return [R, E]
    
    x1 = x0 - f(x0)/df(x0)
    return my_newton(f, df, x1, tol, R, E)
    
f = lambda x: x**2 - 2
df = lambda x: 2*x

R, E = my_newton(f, df, 1, 1e-5)
print(f"R = {R}")
print(f"E = {E}")

f = lambda x: np.sin(x) - np.cos(x)
df = lambda x: np.cos(x) + np.sin(x)

R, E = my_newton(f, df, 1, 1e-5)
print(f"R = {R}")
print(f"E = {E}")
