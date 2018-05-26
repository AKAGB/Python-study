import matplotlib.pyplot as plt
import numpy as np
import math

# 从[0, 2]中等距取50个数作为x的取值
x = np.linspace(-1, 1, 50)
y = list(map(lambda x : pow(math.sin(x-2), 2)*pow(math.e, -(x**2)), x))

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('f(x)')

plt.title('f(x) = ((sin(x - 2))^2)*e^-(x^2) graph')

plt.show()