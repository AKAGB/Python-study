import numpy as np

def cloeset_element(A, z):
    tmp = np.array(A)-z
    return min(min(tmp[tmp>0]), -max(tmp[tmp<=0])) + z

if __name__ == '__main__':
    a = [1,5,2,4,6,3,2,56,89,36,2]
    print(cloeset_element(a, 32))