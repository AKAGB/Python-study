import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA
from numpy.polynomial.legendre import Legendre

from math import e
from math import log
from ex1 import *

def Lrd(y):
    """返回Py(x)"""
    coef = (0,) * y + (1,)
    return Legendre(coef, [-1, 1])


def ln_cond(x, f, n):
    fs = [f(x) for x in range(n+1)]
    A = getA(x, fs)
    return log(LA.cond(A))

def ep(x, y, f, n):
    fs = [f(x) for x in range(n+1)]
    coms = leastSq(x, y, fs)
    # 用于计算残差
    y_1 = [getS(coms, fs, i) for i in x]
    return epsi(y_1, y)

if __name__ == '__main__':
    
    # 生成数据
    x = np.linspace(-1, 1, 20)
    y = np.array(list(map(lambda x : e**x, x)))

    ns = [3, 5, 7, 9]
    ls1 = [ln_cond(x, p, i) for i in ns]
    ls2 = [ln_cond(x, Lrd, i) for i in ns]
    eps1 = [ep(x, y, p, i) for i in ns]
    eps2 = [ep(x, y, Lrd, i) for i in ns]
    print('x^n:')
    for i in range(len(eps1)):
        print('σ(%d) = %g' % (ns[i], eps1[i]))
    print('Pn(x):')
    for i in range(len(eps2)):
        print('σ(%d) = %g' % (ns[i], eps2[i]))
    # plt.scatter(x, y)
    plt.plot(ns, ls1, label='x^n', color='r')
    plt.plot(ns, ls2, label='Pn(x)', color='b')
    plt.xlabel('n')
    plt.ylabel('ln(cond(A))')
    plt.legend()
    plt.show()