import numpy as np

def back_into(U, b):
    """解上三角方程组的回代过程"""
    n = U.shape[0]
    x = np.zeros(n)
    if b.dtype != np.float64:
        b = b.astype(np.float64)
    for i in range(n-1, -1, -1):
        if U[i, i] == 0:
            break
        x[i] = b[i]
        for j in range(n-1, i, -1):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]
    return x

def front_into(L, b):
    """解下三角方程组的前代过程"""
    n = L.shape[0]
    x = np.zeros(n)
    if b.dtype != np.float64:
        b = b.astype(np.float64)
    for i in range(n):
        if L[i, i] == 0:
            break
        x[i] = b[i]
        for j in range(i):
            x[i] = x[i] - L[i, j] * x[j]
        x[i] /= L[i, i]
    return x

def cholesky(A):
    """输入矩阵A，输出Cholesky分解结果中的L(下三角)"""
    A = A.copy()
    if A.dtype != np.float64:
        A = A.astype(np.float64)
    n = A.shape[0]
    for j in range(n):
        for k in range(j):
            A[j, j] = A[j, j] - A[j, k]**2
        A[j, j] = A[j, j]**0.5
        for i in range(j+1, n):
            for k in range(j):
                A[i, j] = A[i, j] - A[i, k] * A[j, k]
            A[i, j] = A[i, j] / A[j, j]
    
    return A*np.tri(n)

def cho_solute(A, b):
    """利用Cholesky分解算法求解方程Ax=b"""
    L = cholesky(A)
    y = front_into(L, b)
    x = back_into(L.transpose(), y)
    return x

def Hilbert(n):
    """生成n阶 Hilbert 矩阵"""
    h = np.zeros([n, n])
    for i in range(n):
        for j in range(i + 1):
            h[i, j] = h[j, i] = (1 / (i + j + 1))
    return h

def generateB(H):
    """H是Hilbert矩阵，生成 b=Hx (x是全1向量)"""
    n = H.shape[0]
    x = np.ones(n)
    return np.dot(H, x)

def infinite_norm(x):
    """求向量无穷范数"""
    result = abs(x[0])
    n = x.shape[0]
    for i in range(1, n):
        if result < abs(x[i]):
            result = abs(x[i])
    return result

