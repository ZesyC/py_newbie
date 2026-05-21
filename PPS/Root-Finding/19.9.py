import numpy as np

def my_bisection(F, a, b, tol, max_iter):
    if max_iter == 0:
        return []
    
    m = (a + b)/2

    if np.abs(F(m)) < tol:
        return m
    elif np.sign(F(a)) == np.sign(F(m)):
        return my_bisection(F, m, b, tol, max_iter - 1)
    elif np.sign(F(b)) == np.sign(F(m)):
        return my_bisection(F, a, m, tol, max_iter - 1)
    else:
        return m
    
def my_pipe_builder(C_ocean, C_land, L, H):
    if C_ocean <= 0 or C_land <= 0 or L <= 0 or H <= 0:
        raise Exception("C_ocean, C_land, L, and H must be strictly positive")
    
    if C_ocean <= C_land:
        return L
    
    F = lambda x: C_ocean*x/np.sqrt(H**2 + x**2) - C_land

    if F(L) <= 0:
        return L
    
    return my_bisection(F, 0, L, 1e-6, 100)

r = my_pipe_builder(30, 10, 100, 20)
print(f"r = {r}")
