import numpy as np
from tabulate import tabulate
from pulp import LpVariable, LpProblem, LpMinimize, LpMaximize, value

def solve(mat, length, variable, strategy, player):
    mas_variable = []
    variable_str = variable
    F_str = "F(" + str(variable) + ")"
    for i in range(0, length):
        mas_variable.append(LpVariable(variable + str(i + 1), lowBound=0))
    if variable == "x":
        problem = LpProblem("Simple_Problem", LpMinimize)
        for i in range(0, len(mat)):
            problem += sum(mat[i] * mas_variable) >= 1
    else:
        problem = LpProblem("Simple_Problem", LpMaximize)
        for i in range(0, len(mat)):
            problem += sum(mat[i] * mas_variable) <= 1
        
    problem += sum(mas_variable)
        
    problem.solve()
    mas_result = []
    for variable in problem.variables():
        mas_result.append(variable.varValue)
    F = value(problem.objective)
    
    V = 1 / sum(mas_result)
    probability = []
    for element in mas_result:
        probability.append(element * V)
    probability.append(V)
    str_strategy = []
    for i in range(0, len(mat[0])):
        str_strategy.append(strategy + str(i + 1))
    str_strategy.append("Price of the game ")
    
    mas_variable.append(F_str)    
    mas_result.append(F)
    print("Solution for parametr %s: " %variable_str)
    show([mas_result], mas_variable)
    print()
    
    print("The price of the game and the probability of applying the strategies of player", player)
    show([probability], str_strategy)
    print()

def show(table, header):
    show = tabulate(table, headers=header, tablefmt='fancy_grid', stralign='center')
    print(show)

mat = np.loadtxt("lab 5.txt", dtype=int)
print("Pay matrix withour dominant row and column:")
show(mat, [])
print()

transpose_mat = np.transpose(mat)

solve(transpose_mat, len(transpose_mat[0]), "x", "p", "A")
solve(mat, len(mat[0]), "y", "q", "B")