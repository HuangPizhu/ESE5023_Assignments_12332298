import random
import numpy as np
#2.1
M1 = np.random.randint(0, 50, size=(5, 10))
M2 = np.random.randint(0, 50, size=(10, 5))
#2.2
def Matrix_multip(M1,M2):
    result = [[0 for _ in range(len(M2[0]))] for _ in range(len(M1))]  
    for i in range(len(M1)):  
        for j in range(len(M2[0])):  
            for k in range(len(M2)):  
                result[i][j] += M1[i][k] * M2[k][j]  
    return result