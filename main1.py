import numpy as np
import matplotlib.pyplot as plt
m=1
hbar=1

xmin=-6.5
xmax=6.5

N=1000
x=np.linspace(xmin,xmax,N+1)
dx = x[1]-x[0]
print(dx)
p=40
v0=p**2/(2*m)
sig=0.15
x0=2
V=0*x
#print(len(V))
for i in range(len(V)):
    if x[i]>0 and x[i]<0.5:
        V[i]=v0
plt.plot(x,V)

Psi0=np.exp(-(x[1:-1]+x0)**2/sig**2)*np.exp(1j*p*(x[1:-1]+x0))
A=np.sum(np.abs(Psi0)**2*dx)
Psi0=Psi0/np.sqrt(A)
plt.plot(x[1:-1],np.abs(Psi0))





