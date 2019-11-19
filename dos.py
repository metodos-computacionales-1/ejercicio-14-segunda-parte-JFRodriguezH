import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("solucion.dat")

t = data[:, 0]
x = data[:, 1]
v = data[:, 2]
y = data[:, 3]
w = data[:, 4]

plt.figure()
plt.subplot(2,2,1)
plt.plot(t,x)
plt.subplot(2,2,2)
plt.plot(x,v)
plt.subplot(2,2,3)
plt.plot(t,y)
plt.subplot(2,2,4)
plt.plot(y, w)
plt.tight_layout()
plt.savefig("punto_1_a_6.png")