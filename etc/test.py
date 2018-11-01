import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)

plt.plot(x, x, label='y=x')
plt.plot(x, x-1, label='y=x+b')
plt.plot(x, x**2, label='y=x2')
plt.plot(x, x**2 + x*1.5 + 1, label='y=a*x2+b*x+c')
plt.plot(x, x**3, label='y=x3')
#plt.plot(x, np.linalg.matrix_power(x, 1/2), label='y=sqrt(x)')
plt.plot(x, 1/x, label='y=k/x')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('Simple plot')

plt.legend()
plt.show()