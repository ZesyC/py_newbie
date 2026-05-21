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
    
