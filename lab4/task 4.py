from random import randint
import numpy as np
import os
from tabulate import tabulate

def randomize_raiting(i, j):
    x = [[randint(1,10) for i in range(i)] for j in range(j)]
    return x

parameters = []
file_par = open('parameters.txt', 'r', encoding="utf-8")
for line in file_par:
    parameters.append(line[:-1])
file_par.close()

planes = []
file_pla = open('plane.txt', 'r', encoding="utf-8")
for line in file_pla:
    planes.append(line[:-1])
file_pla.close()

importance = []
file_imp = open('importances.txt', 'r', encoding="utf-8")
for line in file_imp:
    importance.append(float(line[:-1]))
file_imp.close()

file_raiting = []
if os.stat("rating.txt").st_size == 0:
    with open("rating.txt", "w+") as file_raiting:
        raiting = randomize_raiting(len(planes), len(parameters))
        r = np.array(raiting)
        np.savetxt(file_raiting, r, fmt="%4d", delimiter="", newline="\n")
else:
    file_raiting = np.loadtxt("rating.txt", dtype=int)

importance = np.reshape(importance, (len(importance), 1))
imp_on_rait = file_raiting * importance
imp_on_rait = np.round(imp_on_rait, 3)
sum_imp_on_rait = np.sum(imp_on_rait, axis=0)
max_sum = max(sum_imp_on_rait)
index = sum_imp_on_rait.tolist().index(max_sum)
best_plane = planes[index]
planes.insert(0, "Ваги")
planes.insert(0, "Параметри")
imp_on_rait = imp_on_rait.tolist()
ctr = 0
for el in imp_on_rait:
    el.insert(0, importance[ctr])
    el.insert(0, parameters[ctr])
    ctr +=1
sum_imp_on_rait = sum_imp_on_rait.tolist()
sum_imp_on_rait.insert(0,sum(importance))
sum_imp_on_rait.insert(0, "Сума")
imp_on_rait.append(sum_imp_on_rait)

show = tabulate(imp_on_rait, headers=planes, tablefmt='plain', 
                numalign='center', showindex=range(1,len(imp_on_rait)+1))
print(show)

print()
print("В результаті експертної оцінки було вибрано літак - %s з оцінкою %.2f"
      %(best_plane , max_sum))
