import numpy as np
from tabulate import tabulate
from statistics import mode

def Wald(matrix):
    minimum = []
    for el in matrix:
        minimum.append(min(el))    
    return minimum

def Max(matrix):
    maximum = []
    for el in matrix:
        maximum.append(max(el))    
    return maximum

def Laplace(matrix):
    result = []
    for el in matrix:
        result.append(sum(el) / 3)
    return result

def Hurwitz(matrix):
    y = 0.25
    result = []
    for el in matrix:
        result.append(y * min(el) + (1 - y) * max(el))
    return result

def Bayes_Laplace(matrix):
    p = np.array([0.5, 0.35, 0.15])
    result = []
    for el in matrix:
        result.append(sum(el * p))
    return result

def print_res(method, matrix, add_col):
    headers = []
    for i in range(1, len(matrix)+1):
        headers.append("A" + str(i))
    headers.append(method)
    result = matrix.astype(float)
    result = np.insert(result, len(matrix), add_col, axis=1)
    show = tabulate(result, headers=headers, tablefmt='fancy_grid')
    print(show)
    max_val = max(add_col)
    print("Для цього методу максимальне значення:", max_val)
    index_max_val = add_col.index(max_val) + 1
    print("Це стратегія під номером:", index_max_val)
    most_repeatуed.append(index_max_val)
    print()

input_matrix = np.loadtxt("lab1.txt", dtype=int)
most_repeatуed = []

Wald_val = Wald(input_matrix)
print_res("Метод Вальда", input_matrix, Wald_val)

Max_val = Max(input_matrix)
print_res("Метод Максимуму", input_matrix, Max_val)

Laplace_val = Laplace(input_matrix)
print_res("Метод Лапласа", input_matrix, Laplace_val)

Hurwitz_val = Hurwitz(input_matrix)
print_res("Метод Гурвіца", input_matrix, Hurwitz_val)

Bayes_Laplace_val = Bayes_Laplace(input_matrix)
print_res("Метод Баєса-Лапласа", input_matrix, Bayes_Laplace_val)

print("В результаті найчастіше зустрічаєть стратегія:", mode(most_repeatуed))