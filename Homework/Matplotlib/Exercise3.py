import matplotlib.pyplot as plt
import numpy as np
import numpy.random
from scipy.stats import gaussian_kde

sigma = 0.5
mu = 2
z = np.random.randn(10000)
z = sorted(z)
kernel = gaussian_kde(z)

plt.hist(z, bins=25, density=True, facecolor='blue', edgecolor='black')
plt.plot(z, kernel.pdf(z))
plt.show()