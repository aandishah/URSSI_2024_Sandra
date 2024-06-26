from numpy import *
from matplotlib.pyplot import *\

def forcing(x,t,x0,S0,k,alpha):
    r = abs(x-x0)
    Q = zeros((N+1,M+1))
    for m in range(0,M+1):
        tau = t[m]
        Q[:,m] = S0*exp(-k*tau -alpha*r**2)
    return Q