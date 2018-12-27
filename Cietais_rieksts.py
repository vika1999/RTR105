Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
# -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))

while k < 3:
        k = k + 1
        R = (-1)*x*x/((2*k)*(2*k+1))
        a = a * R
        S = S + a
        print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
print("Izdruka no liet.f. Beigas!")
return S
x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = sin(x)
print("standarta sin(%.2f) = %6.2f"%(x,y))
yy = mans_sinuss(x)
print("mans sin(%.2f) = %6.2f"%(x,yy))
