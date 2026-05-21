import numpy as np

def my_newton(f, df, x0, tol):
    if np.abs(f(x0)) < tol:
        return x0
    
    if df(x0) == 0:
        raise Exception("Derivative is zero")
    
    x1 = x0 - f(x0)/df(x0)

    if np.abs(f(x1)) < tol:
        return x1
    else:
        return my_newton(f, df, x1, tol)
    
f = lambda x: x**3 - 100*x**2 - x + 100
df = lambda x: 3*x**2 - 200*x - 1

r1 = my_newton(f, df, 0, 0.01)
print(f"r1 = {r1}")
print(f'f(r1) = {f(r1)}')
