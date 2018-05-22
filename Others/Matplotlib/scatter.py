import matplotlib.pyplot as plt

# 产生数据
x = list(range(0, 60, 5))
y = [0, 1.27, 2.16, 2.86, 3.44, 3.87, 4.15, 4.37, 4.51, 4.58, 4.62, 4.64]

# x = [1, 1.25, 1.50, 1.75, 2]
# y = [5.1, 5.79, 6.53, 7.45, 8.46]

fig = plt.figure(1, dpi=100)
plt.scatter(x, y, c='r', marker='o')
plt.show()