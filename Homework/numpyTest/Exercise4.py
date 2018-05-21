import numpy as np
import numpy.random
import numpy.linalg
from scipy.linalg import toeplitz
import time

def power_iteration(A, ep):
    # power iteration from wikipedia
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector
    b_k = np.random.rand(A.shape[1])
    b_k1 = np.dot(A, b_k)
    b_k1_norm = np.linalg.norm(b_k1, np.inf)
    last = b_k1_norm + ep + 1
    cnt = 0
    while True:
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)

        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1, np.inf)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm
        
        cnt += 1
        if cnt > 10000000:
            print('Too much times!')
            break
        if abs(b_k1_norm - last) < ep:
            break
        last = b_k1_norm
    return b_k, b_k1_norm, cnt

if __name__ == '__main__':
    n = 20
    Z = np.random.randn(n, n)
    t = time.time()
    result = power_iteration(Z, 1e-5)
    t = time.time() - t
    print('Using %dus.' % int(t*1e6))
    print('Iteration %d times.' % result[2])
    print('The largest eigenvalue =', result[1])
    print('Corresponding eigenvector =', result[0])