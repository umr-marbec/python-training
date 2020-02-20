import numpy as np
x = np.empty((5, 10))
for i in range(5):  # inner loop: 1st dim
    for j in range(10):  # outer loop: last dim
        print(x[i, j])
