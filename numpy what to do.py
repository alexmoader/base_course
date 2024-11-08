import numpy as np
a = [1,2,4]
b = np.array(a) # создание массива из списка
print(type(a))
print(type(b))
print(b + b)
print(b/b)
print(b-b)
#b[0] = 'GOOD' не сработает 
b = np.append(b,'good')
print(b)