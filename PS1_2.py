import random
#2.1
M1 = [[random.randint(0, 50) for _ in range(10)] for _ in range(5)] 
M2 = [[random.randint(0, 50) for _ in range(5)] for _ in range(10)]
#2.2
def Matrix_multip(M1,M2):
    result = [[0 for _ in range(len(M2[0]))] for _ in range(len(M1))]  
    for i in range(len(M1)):  
        for j in range(len(M2[0])):  
            for k in range(len(M2)):  
                result[i][j] += M1[i][k] * M2[k][j]  
    return result