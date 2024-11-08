import numpy as np
a = [1,5,3,6]
b = np.array([a, np.array(a)*3])
print(b)
print(b[::,1]) # взять столбец только второй