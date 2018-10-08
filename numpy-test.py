import matplotlib.pyplot as plt
import numpy as np

data1, data2, data3, data4 = np.random.randn(4, 10)
fig, (ax1, ax2) = plt.subplots(1, 2)
param = {'marker': 'x'}
ax1.plot(data1, data2, **param)
ax2.plot(data3, data4, **param)
plt.show()