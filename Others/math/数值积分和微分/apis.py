import numpy as np
import math

def fuhe_tixing(h, y):
    """复合梯形公式，h为步长，y为函数值"""
    n = len(y)
    result = y[0] + y[n-1]
    for i in range(1, n-1):
        result += 2 * y[i]
    return result * h / 2

def fuhe_xinpusen(h, y):
    """复合辛普森公式"""
    n = len(y)
    result = 0
    for i in range(0, n-1, 2):
        result += y[i] + 4 * y[i+1] + y[i+2]
    return result * h / 6

def t2n(n, a, b, f, Tn):
    """折半法递推公式"""
    h = (b - a) / n
    xs = [a+h/2]
    while xs[-1] + h <= b:
        xs.append(xs[-1]+h)
    ys = [f(x) for x in xs]
    return Tn / 2 + sum(ys) * h / 2
    

def romberg(a, b, f):
    """龙贝格求积算法"""
    h = b - a
    n = 0
    T = [[]]
    T[0].append((f(a) + f(b)) * h / 2)
    while True:
        T.append([])
        T[0].append(t2n(n+1, a, b, f, T[0][-1]))
        # 理查德外推
        for i in range(1, n+2):
            T[i].append((4**i * T[i-1][-1] - T[i-1][-2]) / (4**i - 1))
        n += 1
        if abs(T[-1][0] - T[-2][0]) < 1e-5:
            break
    print(len(T))
    return T[-1][-1]
        

if __name__ == '__main__':
    f = lambda x : math.e**(-x)
    a = 0
    b = 1
    print(romberg(a, b, f)*2/(math.pi**0.5))
    