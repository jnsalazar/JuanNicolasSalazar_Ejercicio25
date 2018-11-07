import numpy as np
import maplotlib.pyplot as plt

data = np.genfromtxt('sample.dat')
plt.hist(data, density = True)
plt.savefig('sample.pdf')