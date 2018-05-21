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
    print('||A||F =', np.linalg.norm(A))
    print('||B||inf =', np.linalg.norm(B, np.inf))

    # svd分解
    U, S, V = np.linalg.svd(B)
    print('The largest singular values of B =', S[0])
    print('The smallest singular values of B =', S[len(S) - 1])