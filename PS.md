# <center> Report of ESE5023_Assignments_#1
<b><p align="right">Name: HUANG Pizhu</p></b>
<b><p align="right">SID:12332298</p></b>
<b><p align="right">Date:Otc 25, 2023</p></b>


## 1.Flowchart 
Write a function  `Print_values() ` with arguments a, b, and c accoding to the flowchart with conditional statement.
```python
def Print_values(a,b,c):
    if a>b:
        if b>c:
            return a,b,c
        else:
            if a>c:
                return a,c,b
            else:
                return c,a,b
    else:
        if b>c:
            return None
        else:
            return c,b,a
```  
Report the output with a,b and c that can express code logic.
<div class="center">

| a | b | c | output |
| :---: | :---: | :---: | :---: |
| 5 | 3 | 1 | (5,3,1) |
| 5 | 1 | 3 | (5,3,1)  |
| 3 | 1 | 5 | (5,3,1)  |
| 1 | 5 | 1 | None |
| 1 | 3 | 5 | (5,3,1)  |

</div>

## 2.Matrix multiplication
### 2.1 
Use `random.randint()` to generate the random numbers.  
loop `for i in range()` to fill out rows and comlums.  
```python
import random
import numpy as np
M1 = np.random.randint(0, 50, size=(5, 10))
M2 = np.random.randint(0, 50, size=(10, 5))
```
### 2.2
Initialize the shape of the result matrix based on the two matrices being mulplied. Use nested loops to teaverse and fill each position with value in the result maxtrix.
```python
def Matrix_multip(M1,M2):
    result = [[0 for _ in range(len(M2[0]))] for _ in range(len(M1))]  
    for i in range(len(M1)):  
        for j in range(len(M2[0])):  
            for k in range(len(M2)):  
                result[i][j] += M1[i][k] * M2[k][j]  
    return result
```

## 3.Pascal triangle
The ith number in the kth row is sum of the (i-1)th and ith numbers in the (k-1)th row.*I got the mathematical version of Pascal triangle by reading "https://www.mathsisfun.com/pascals-triangle.html"*  
*I learned about the **recursion** of thought from this passage accessed online at https://blog.csdn.net/dreamispossible/article/details/90552557*, and I use recursion in problem 3 and 4.  
The function Pascal triangle(k), when k>1, for kth row, the ith number is sum of the (i-1)th and ith numbers in the (k-1)th row. Recurve (k-1)th row and append 0 in the end to conveniently calculate the kth row.  
Pascal triangle(100) and Pascal triangle(200) has output as annotation in PS1_3.py
```python
def Pascal_triangle(k):
    if k == 1:
        return [1]
    else:
        row = Pascal_triangle(k-1)
        row.append(0)
        new_row = []
        for i in range(len(row)-1):
            new_row.append(row[i]+row[i+1])
        new_row.insert(0,1)
    return new_row
```
## 4.Add or double
Condsidering path form number x to 1, double operation is more than add 1 operation in case of number more than 1. If x is even, one step of double and recursively call the function with x//2. If x is odd, one step that x-1 and recursively call the function with x-1. The function will recursively calculate the minimum number of steps reducing x to 1.
```python
def Least_moves(x):
    if x == 1:
        return 0
    elif x % 2 == 0:
        return 1 + Least_moves(x // 2)
    else:
        return 1 + Least_moves(x - 1)
```

## 5.Dynamic programming
### 5.1 
In the function `find_expressions(target)`, firstly define numbers' string and three state("+", "-", and " ") and initialize a list to save valid expressions. For number '12345678', per number has three state behind, so there are total 3**8 state in 8 positions between '123456789', using `itertools.product()` from itertools package to creat all arrange of operators(states). In loop, concatenate numbers '12345678' and states by `zip()` and number 9 is appended in the end; use `eval()` to decide the string expression and target. (*I got information of some python function to solve this problem, its java code accessed online at https://blog.csdn.net/tao617/article/details/107547933*)
```python
import itertools
def find_expressions(target):
    num, ope, expressions = "123456789", ["+", "-", ""], []
    for i in itertools.product(ope, repeat=len(num) - 1):
        expression = "".join(j + k for j, k in zip(num, i)) + num[-1]
        if eval(expression) == target:
            expressions.append(f"{expression} = {target}")
    return expressions
```
### 5.2
Rewrite the function in 5.1 to return the lenth of different targets, which is number of expression.
```python
def Total_solutions():
    def new_find_expressions(target):
        num, ope, expressions= "123456789", ["+", "-", ""], []
        for i in itertools.product(ope, repeat=len(num) - 1):
            expression = "".join(j + k for j, k in zip(num, i)) + num[-1]
            if eval(expression) == target:
                expressions.append(f"{expression} = {target}")
        return len(expressions)
    results = []
    for target in range(1, 101):
        num_of_expressions = new_find_expressions(target)
        results.append(num_of_expressions)
    return results
Total_solutions = Total_solutions()
```
Plot a bar chart of numbers and their valid expressions.
```python
import matplotlib.pyplot as plt
import numpy as np
x = range(1, 101)
plt.figure(figsize=(18, 5))
plt.bar(x, Total_solutions, color='forestgreen', alpha=0.7, label='Number of Expressions')
plt.xticks(np.arange(1, 102,2))
plt.yticks(np.arange(int(min(Total_solutions)), int(max(Total_solutions)) + 1))
plt.xlabel('Target Value',fontsize=16)
plt.ylabel('Number of Expressions',fontsize=16)
plt.title('Number of Expressions for Targets 1-100',fontsize=16)
plt.legend()
plt.show()
```
Find the max and min in the list saving number of expressions:  
*maximum is 26 for target numbers 1 and 45*  
*minimun is 6 for target number 88*
```python
max_value = max(Total_solutions)
min_value = min(Total_solutions)

max_indices = [index + 1 for index, value in enumerate(Total_solutions) if value == max_value]
min_indices = [index + 1 for index, value in enumerate(Total_solutions) if value == min_value]

print(f"maximum: {max_value}，number: {max_indices}")
print(f"minimum: {min_value}，number: {min_indices}")
```