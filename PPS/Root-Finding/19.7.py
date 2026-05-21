import numpy as np

def my_bisection(f, a, b, tol, R=None, E=None):
    if R is None or E is None:
        if a >= b:
            raise Exception("a must be less than b")
        
        if tol <= 0:
            raise Exception("tol must be strictly positive")
        
        if np.sign(f(a)) == np.sign(f(b)):
            raise Exception("The scalars a and b do not bound a root")
        
        R = []
        E = []
    
    m = (a + b)/ 2
    R.append(m)
    E.append(abs(f(m)))

    if E[-1] < tol:
        return [R, E]
    elif np.sign(f(a)) == np.sign(f(m)):
        return my_bisection(f, m, b, tol, R, E)
    elif np.sign(f(b)) == np.sign(f(m)):
        return my_bisection(f, a, m, tol, R, E)
    else:
        return [R, E]
        
f = lambda x: x**2 - 2

R, E = my_bisection(f, 0, 2, 1e-1)
print(f"R = {R}")
print(f"E = {E}")
