#zad4
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
x =np.linspace(0, 5, 201)
x= np.delete(x, 0)
y =np.log(x)
noise = y+rd.randn(np.size(y))*0.2

def redukcja(n):
    srednia=[]
    s = int((n-1)/2)
    for i in range(1+s,np.size(noise)+1-s):
        srednia.append(np.sum(noise[i-s:i+s+1])/n)
    return srednia


def splot(x_1, x_2):
    x_2 = np.flip(x_2)
    x_wy = []
#    if x_2<x_1:

    for i in range((len(x_2)-1)/2, len(x_1) - (len(x_2)-1),int(lenx_1)/step):
        lp = i - (len(x_2)-1)/2
        x_wy.append(sum())

    return x_wy

print(len(redukcja(3)))

plt.figure(figsize =(20,5))
plt.subplot(1,3,1)
plt.plot(x,y, "-", color = 'red', lw=0.6, label = "ln x")
plt.plot(x,noise,"-", color = 'blue', lw=0.6, label = 'noise')
plt.plot(x[1:np.size(x)-1],redukcja(3), "-", color = 'green', lw=0.6, label = "Aweraged n=3")
plt.xlim(0,5)
plt.grid()
plt.legend()
plt.subplot(1,3,2)
plt.plot(x,y, color = 'red', lw=0.6, label = "ln x")
plt.plot(x,noise,"-", color = 'blue', lw=0.6, label = 'noise')
plt.plot(x[3:np.size(x)-3],redukcja(7), "-", color = 'green', lw=0.6, label = "Aweraged n=3")
plt.xlim(0,5)
plt.grid()
plt.legend()
plt.subplot(1,3,3)
plt.plot(x,y, color = 'red', lw=0.6, label = "ln x")
plt.plot(x,noise,"-", color = 'blue', lw=0.6, label = 'noise')
plt.plot(x[6:np.size(x)-6],redukcja(13), "-", color = 'green', lw=0.6, label = "Aweraged n=3")
plt.xlim(0,5)
plt.grid()
plt.legend()
plt.show()
#funkcja nie jest liniowa, więc średnia nie będzie środkiem rozkładu zmiennych