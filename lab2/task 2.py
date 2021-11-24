from tabulate import tabulate

def calculations_1(mat, year):
    earn = year * mat[1]
    waste = year * mat[3]
    win = earn * mat[2] + waste * mat[4] - mat[0]
    result = [earn, waste, win]
    return result

def calculations_2(mat1, mat2, year):
    earn = year * mat1[1]
    waste = year * mat1[3]
    win = earn * mat2[2] + waste * mat2[3] - mat1[0]
    result = [earn, waste, win]
    return result

def show_res(mat1, mat2, year):
    mat1.insert(0, "Великий завод")
    mat2.insert(0, "Малий завод")
    header = ["План", "Дохід за " + str(year) + " Років",
                      "Витрати за " + str(year) + " Років",
                      "Виграш за " + str(year) + " Років"]
    table = [mat1, mat2]
    show = tabulate(table, headers=header, tablefmt='fancy_grid', showindex=range(1, len(table)+1))
    print(show)

file = open("lab2.txt", "r")

A = file.readline()
B = file.readline()
C = file.readline()

file.close()

A = A.split(' ')
B = B.split(' ')
C = C.split(' ')

A = [float(i) for i in A]
B = [float(i) for i in B]
C = [float(i) for i in C]

A_res_5 = calculations_1(A, 5)
B_res_5 = calculations_1(B, 5)

show_res(A_res_5, B_res_5, 5)

A_res_4 = calculations_2(A, C, 4)
B_res_4 = calculations_2(B, C, 4)

show_res(A_res_4, B_res_4, 4)

win_AB_4 = max([A_res_4[-1], B_res_4[-1]])

win_C1_4 = C[0] * win_AB_4
win_C2_4 = C[1] * 0
win_C_5 = max([win_C1_4, win_C2_4])

data = [[A_res_5[-1], B_res_5[-1], win_C_5]]
res_head = ["Виграш стратегії А", "Виграш стратегії Б", "Виграш стратегії В"]
prnt = tabulate(data, headers=res_head, tablefmt='fancy_grid')
print(prnt)

win_strategy = max(data[0])

if win_strategy == A_res_5[-1]:
    print('Стратегія A є виграшна:', win_strategy)
    print('Бужуєм великый завод!')
elif win_strategy == B_res_5[-1]:
    print('Стратегія Б є виграшна:', win_strategy)
    print('Будуєм малий завод!')
elif win_strategy == win_C_5:
    print('Стратегія В є виграшна::', win_strategy)
    print('Відладаєм будівництво')