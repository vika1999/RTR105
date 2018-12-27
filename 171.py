# Fails : 171.py
# Autors : Yulia Semchenkova
# Apliecibas numurs: 181REB329
# Datums: 14.11.2018.
# Sagatave funkcijas saknes mekleeshanai ar dihatomijas metodi

# -*- coding: utf-8 -*-
from math import asin, fabs
from time import sleep

def f(x):
    return asin(x)

# Definejam argumenta x robezhas:
a = -1
b = 1

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

# Paarbaudam, vai dotajaa intervaalaa ir saknes:
if ( funa * funb > 0.0):
    print("Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b))
    sleep(1); exit()   # Zinjo uz ekraana, gaida 1 sec. un darbu pabeidz
else:
    print("Dotajaa intervaalaa sakne(s) ir!")

#Defineejam precizitaati, ar kaadu mekleesim sakni:
deltax = 0.01

# Sashaurinam saknes mekleeshanas robezhas:
while ( fabs(b-a) > deltax ):
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else:
        a = x

print("Sakne ir: ", x)
