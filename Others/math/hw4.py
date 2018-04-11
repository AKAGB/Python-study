import numpy as np
import math

def infinite_norm(x):
    """求向量无穷范数"""
    result = abs(x[0])
    n = x.shape[0]
    for i in range(1, n):
        if result < abs(x[i]):
            result = abs(x[i])
    return result

def generateA(S, B):
    """生成系数矩阵A"""
    n = S.shape[0]
    Z = np.zeros([n, n])
    result = None
    for i in range(n):
        line = None
        for j in range(n):
            if j == 0:
                if i == 0:
                    line = S.copy()
                elif i == 1:
                    line = B.copy()
                else:
                    line = Z.copy()
            else:
                if abs(i-j) == 1:
                    line = np.hstack((line, B))
                elif i == j:
                    line = np.hstack((line, S))
                else:
                    line = np.hstack((line, Z))
        if i == 0:
            result = line.copy()
        else:
            result = np.vstack((result, line))
    return result

def generateS(a, b, n):
    """a为对角元，b为次对角元，n为阶数"""
    S = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            if i == j:
                S[i, j] = a
            elif abs(i - j) == 1:
                S[i, j] = b
    return S

def generateb(f, g, n):
    """向量b"""
    matrix_result = np.zeros(n-1)
    for i in range(1,n):
    	matrix = np.zeros(n-1)
    	for j in range(1,n):
    		matrix[j-1] = h*h/4*f(i,j)
    		if i==1:
    			matrix[j-1] += 1/4*g(0,j)
    		if i==n-1:
    			matrix[j-1] += 1/4*g(n,j)
    		if j==1:
    			matrix[j-1] += 1/4*g(i,0)
    		if j == n-1:
    			matrix[j-1] += 1/4*g(i,n)
    	if i==1:
    		matrix_result = matrix
    		#print(matrix)
    	else:
    		matrix_result = np.hstack((matrix_result,matrix))
    return matrix_result

def gonge(x, A, b):
    """共轭梯度法"""
    x = x.copy()
    r = b - np.dot(A, x)
    p = r
    y = x + 1
    while infinite_norm(y-x) > 1e-5:
        t = np.dot(np.dot(p.transpose(), A), p)
        if abs(t) < 1e-10:
            return x
        a = np.dot(r.transpose(), p) / np.dot(np.dot(p.transpose(), A), p)
        x = x + a * p
        r = r - a * np.dot(A, p)
        bt = - np.dot(np.dot(r.transpose(), A), p) / np.dot(np.dot(p.transpose(), A), p)
        p = r + bt * p
        #print('x%d = ' % (i+1), x)
    return x

if __name__ == '__main__':
    n = 20
    h = 1 / n
    S = generateS(1+(h**2)/4, -0.25, n-1)
    B = generateS(-0.25, 0, n-1)
    A = generateA(S, B)
    f = lambda x, y: math.sin(x*h*y*h)
    g = lambda x, y: (x*h)**2 + (y*h)**2
    b = generateb(f, g, n)
    x = np.zeros((n-1)*(n-1))
    x = gonge(x, A, b)
    print(x)