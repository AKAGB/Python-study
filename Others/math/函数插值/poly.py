def polyFunc(x, y, xt):
    """多项式插值法求函数值"""
    yt = 0
    length = len(x)
    for i in range(length):
        temp = 1
        for j in range(length):
            temp = temp * (xt - x[j]) / (x[i] - x[j])
        yt = yt + temp * y[i]