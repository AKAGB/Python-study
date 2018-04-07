import numpy as np

def infinite_norm(x):
    """求向量无穷范数"""
    result = abs(x[0])
    n = x.shape[0]
    for i in range(1, n):
        if result < abs(x[i]):
            result = abs(x[i])
    return result

def jacobi(x, A, b, e):
    """Jacobi迭代法，判停条件为无穷范数小于e"""
    n = A.shape[0]
    y = x - 1 - e
    if x.dtype != np.float64:
        x = x.astype(np.float64)
    cnt = 0
    while infinite_norm(x - y) >= e:
        cnt += 1
        y = x.copy()
        for i in range(n):
            x[i] = b[i]
            for j in range(i):
                x[i] = x[i] - A[i, j]*y[j]
            for j in range(i+1, n):
                x[i] = x[i] - A[i, j]*y[j]
            x[i] /= A[i, i]
        
    return x, cnt

def g_s(x, A, b, e):
    """G-S迭代法，判停条件为无穷范数小于e"""
    n = A.shape[0]
    x = x.copy()
    y = x - 1 - e
    if x.dtype != np.float64:
        x = x.astype(np.float64)
    cnt = 0
    while infinite_norm(x - y) >= e:
        cnt += 1
        y = x.copy()
        for i in range(n):
            x[i] = b[i]
            for j in range(i):
                x[i] = x[i] - A[i, j]*x[j]
            for j in range(i+1, n):
                x[i] = x[i] - A[i, j]*x[j]
            x[i] /= A[i, i]
        print('x[%d] =' % cnt, x)
    return x, cnt

def SOR(x, A, b, w, e):
    """SOR迭代法，判停条件为无穷范数小于e"""
    n = A.shape[0]
    x = x.copy()
    y = x - 1 - e
    if x.dtype != np.float64:
        x = x.astype(np.float64)
    cnt = 0
    while infinite_norm(x - y) >= e:
        cnt += 1
        y = x.copy()
        for i in range(n):
            x[i] = b[i]
            for j in range(i):
                x[i] = x[i] - A[i, j]*x[j]
            for j in range(i+1, n):
                x[i] = x[i] - A[i, j]*x[j]
            x[i] /= A[i, i]
            x[i] = (1 - w) * y[i] + w * x[i]
    return x, cnt

if __name__ == '__main__':
    A = np.array([
        [5, 2, 1], 
        [-1, 4, 2],
        [2, -3, 10]
    ], np.float64)

    x = np.zeros(3)
    b = np.array([-12, 20, 3], np.float64)
    e = 1e-2
    w = 0.9

    result = g_s(x, A, b, e)
    print(result[0], 'n =', result[1])