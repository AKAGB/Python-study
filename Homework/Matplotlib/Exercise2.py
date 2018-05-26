import matplotlib.pyplot as plt
import numpy as np
import numpy.random
from numpy import linalg as LA

# 生成数据
X = np.random.rand(20, 10)
b = np.random.rand(10)
z = np.random.randn(20)
y = np.dot(X, b) - z

b_ = LA.lstsq(X, y, rcond=None)[0]

# 生成图像
index = list(range(10))
plt.scatter(index, b, label='True coefficients', color='r', marker='x')
plt.scatter(index, b_, label='Estimated coefficients', color='blue', marker='o')

plt.xlabel('index')
plt.ylabel('value')
plt.title('Parameter plot')
plt.legend()
plt.show()