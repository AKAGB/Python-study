import numpy as np
import numpy.random
import numpy.linalg
from scipy.linalg import toeplitz

if __name__ == '__main__':
    n = 200
    m = 500

    vec = np.array(range(m))
    A = np.random.randn(n, m)
    B = toeplitz(vec)
    b = np.random.randn(m)
    x = np.linalg.solve(B, b)
    print('Calcute Bx=b, and x =')
    print(x)