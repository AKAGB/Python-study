import numpy as np
import random

if __name__ == '__main__':
    a = []
    p = 1/3
    n = 100
    for i in range(n**2):
        if random.random() < p:
            a.append(1)
        else:
            a.append(0)
        i += 1
    A = np.resize(np.array(a), (n, n))
    U, S, V = np.linalg.svd(A)
    
    # Max singular value = n * p
    print('Max singular value:', max(S))
