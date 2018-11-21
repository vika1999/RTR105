import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace

def f(x):
    return sin(x)

x = linspace(0, 7, 71)
y = f(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcijas $sin(x)$')
plt.plot(x,y, color = "#FF0000")
plt.legend(['$sin(x)$'])
#plt.legend(['¢sin(x)$'])
#plt.show()

delta_x = x[1] - x[0]

y_first_derivative = (f(x+delta_x) - f(x)) / delta_x
plt.plot(x, y_first_derivative, color = "#00FF00")

#plt.legend(['$sin(x)$','$sin\'(x)$'])
#plt.show()

N = len(x)

y_first_derivative_build_from_array = []
for i in range(N-1):
    temp = ( y[i+1] - y[i] ) / (delta_x)
    #temp = ( y[i+1] - y[i]) / (x[i+1] - x[i] )
    y_first_derivative_build_from_array.append(temp)
    print(i,x[i],x[i+1],y[i],y[i+1],temp,y_first_derivative_build_from_array)

plt.plot(x[0:N-1], y_first_derivative_build_from_array, color = "#0000FF")
plt.legend(['$sin(x)$','$sin\'(x)$','$sin\'(x)$ - build from array'])
plt.show()
