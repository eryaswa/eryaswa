import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,11,1)
y=2*x + 3
print(x)
print(y)


jari2 = 5

sudut = np.arange(0,2*np.pi,0.1)
x2=jari2*np.cos(sudut)
y2=jari2*np.sin(sudut)

plt.plot(x2,y2)
plt.show()