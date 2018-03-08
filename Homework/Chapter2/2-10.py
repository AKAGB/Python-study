# lambda可以生成一个匿名函数
# map将第一个参数(函数)作用在列表中的每一个元素并返回一个map对象
# list将map对象转化为list
print(list(map(lambda x : x * x, [1, 2, 3])))
