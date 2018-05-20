import numpy as np
import numpy.random
from scipy.linalg import toeplitz

def func(mA, mB, l):
    """Calculate A(B − lI)"""
    return np.dot(mA, mB - l * np.eye(mB.shape[0]))

if __name__ == '__main__':
    n = 200
    m = 500

    vec = np.array(range(m))
    A = np.random.randn(n, m)
    B = toeplitz(vec)
    print('A + A =')
    print(A + A)
    print('A(A.transpose()) =')
    print(np.dot(A, A.transpose()))
    print('(A.transpose())A =')
    print(np.dot(A.transpose(), A))
    print('AB = ')
    print(np.dot(A, B))
    l = int(input('Please input λ: '))
    print('A(B − %dI) = ' % l)
    print(func(A, B, l))
