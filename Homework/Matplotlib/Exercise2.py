import matplotlib.pyplot as plt
import numpy as np
import numpy.random
from numpy import linalg as LA

X = np.random.rand(20, 10)
b = np.random.rand(10)
z = np.random.randn(10)
tmp = np.dot(X, b)
y = tmp + z
