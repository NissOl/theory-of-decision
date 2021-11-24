from tabulate import tabulate

def check_all_candidat(mat):
    all_candidat = []
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            if mat[i][j] not in all_candidat and not isinstance(mat[i][j], int):
                all_candidat.append(mat[i][j])
    return sorted(all_candidat)

def method_Borda(mat, candidate):
    Sum = 0
    for i in range(0, len(mat)):    
        for j in range(1, len(mat[i])):
            if mat[i][j] == candidate:
                if mat[i].index(candidate) == 1:
                    Sum += mat[i][0] * 2
                elif mat[i].index(candidate) == 2:
                    Sum += mat[i][0] * 1
                elif mat[i].index(candidate) == 3:
                    Sum += mat[i][0] * 0
    return Sum

def method_Condorce(mat, candidate1, candidate2):
    res1 = 0
    res2 = 0
    for i in range(0, len(mat)):
        if mat[i].index(candidate1) < mat[i].index(candidate2):
            res1 += mat[i][0]
        else:
            res2 += mat[i][0]
    res = [res1, res2]
    compare = [candidate1 + " > " + candidate2, candidate2 + " > " + candidate1]
    table = []
    for i in range(0, len(res)):
        table.append([res[i], compare[i]])
    show(table)
    res_str = compare[res.index(max(res))]
    return res_str, max(res)

def show(table):
    show = tabulate(table, showindex=range(1, len(table)+1), tablefmt='fancy_grid')
    print(show)

def result_Condorce(str1, str2, str3):
    if str1[len(str1) - 1] == str2[0]:
        str1_str2 = str1 + ' > ' + str2[len(str2) - 1]
        if str1_str2[0] == str3[0] and str1_str2[len(str1_str2) - 1] == str3[len(str3) - 1]:
            print(str1_str2)
            print('Winer of Condorce method is candidat %s' %str1_str2[0])
        else:
            print('these statements is imbosible to combine')    


file = open('lab3.txt', 'r')

input_matrix = []
for line in file:
        strip = line.strip()
        split = strip.split(' ')
        for i in range(0, len(split)):
            if split[i].isdigit():
                split[i] = int(split[i])
        input_matrix.append(split)
file.close()
show(input_matrix)

candidat = check_all_candidat(input_matrix)

result_for_Borda = []
for el in candidat:
    result_for_Borda.append(method_Borda(input_matrix, el))

table_Borda = []
for i in range(0, len(candidat)):
    table_Borda.append([candidat[i], result_for_Borda[i]])
show(table_Borda)

win_Borda = max(result_for_Borda)
print("Winer of Borda method is candidat %s with %d votes"
      %(candidat[(result_for_Borda.index(win_Borda))], win_Borda))

str_A_B, A_B = method_Condorce(input_matrix, 'A', 'B')
str_B_C, B_C = method_Condorce(input_matrix, 'B', 'C')
str_A_C, A_C = method_Condorce(input_matrix, 'A', 'C')

show([[str_A_B, A_B], [str_B_C, B_C], [str_A_C, A_C]])

win_str = [str_A_B, str_B_C, str_A_C]
for i in range(0, len(win_str)):
    for j in range(0, len(win_str)):
        for k in range(0, len(win_str)):
            if win_str[i] != win_str[j] and win_str[i] != win_str[k] and win_str[j] != win_str[k]:
                result_Condorce(win_str[i], win_str[j], win_str[k])
