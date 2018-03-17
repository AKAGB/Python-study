import time

lst = [i + 1 for i in range(1000000)]
print('Min:', min(lst))
print('Max:', max(lst))

# sum计时
start = time.time()
total = sum(lst)
end = time.time()
print('Sum is %d. Use %0.3fms.' % (total,
        (end - start) * 1000))