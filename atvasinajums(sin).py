import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace

def f(x):
    return sin(x)

x = linspace(0,4,11)
print(x)
#y = sin(x)
y = f(x)
print(y)

legend=[]

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('$sin(x)$ funkcija un tas atvasinajumi')
plt.plot(x,y,'k')  #melna krāsa - k
legend.append('$sin(x) funkcija$')

plt.plot(x,y, 'go') #punktiņi zaļa krāsa
legend.append('$sin(x)$ funkcija(dazhi punkti')

deltax=x[1]-x[0]
N = len(x)
derivative = [] #atvasinajums

for i in range(N):
    temp = (f(x[i]+deltax) - f(x[i])) / deltax
    derivative.append(temp)
    print(derivative)

plt.plot(x,derivative,'y')
legend.append('atvasinajums')

plt.plot(x,derivative, 'ro') #sarkanas krāsa punkti
legend.append('atvasinajums (dazhi punkti)')

derivative_through_array = [] #atvasinājums caur masīvu
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    derivative_through_array.append(temp)

plt.plot(x[0:N-1],derivative_through_array,'m')
legend.append('atvasinajums (izmantojot vertibas no masiva)')

plt.plot(x[0:N-1],derivative_through_array, 'bo')
legend.append('atvasinajums (izmantojot vertibas no masiva; dazhi punkti)')
#print(plt.legend.__doc__)
plt.legend(legend, loc = 3) #loc = 3 - ir legendas atrašanas vieta


plt.show() #attēlot grafiku
