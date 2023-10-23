#5.1
import itertools
import matplotlib.pyplot as plt
import numpy as np

def find_expressions(target):
    num, ope, expressions = "123456789", ["+", "-", ""], []
    for i in itertools.product(ope, repeat=len(num) - 1):
        expression = "".join(j + k for j, k in zip(num, i)) + num[-1]
        if eval(expression) == target:
            print(f"{expression} = {target}")
    return expressions

#5.2
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

#plot
x = range(1, 101)
plt.figure(figsize=(18, 5))
plt.plot(x, Total_solutions, marker='o', linestyle='-' , label='Number of Expressions')
plt.xticks(np.arange(1, 102,2))
plt.yticks(np.arange(int(min(Total_solutions)), int(max(Total_solutions)) + 1))
plt.xlabel('Target Value')
plt.ylabel('Number of Expressions')
plt.title('Number of Expressions for Targets 1-100')
plt.legend()
plt.show()

#find the max and min
max_value = max(Total_solutions)
min_value = min(Total_solutions)

max_indices = [index + 1 for index, value in enumerate(Total_solutions) if value == max_value]
min_indices = [index + 1 for index, value in enumerate(Total_solutions) if value == min_value]

print(f"maximum: {max_value}，number: {max_indices}")
print(f"minimum: {min_value}，number: {min_indices}")