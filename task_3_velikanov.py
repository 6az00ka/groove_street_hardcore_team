from turtle import circle
import numpy as np
import itertools as itoo

def e_indices(E, value):
    arr = []
    for x in range(len(E)):
        if E[x][0] == value:
            arr.append(x)
    return arr

def count_ones(arr):
    i = 0
    for x in arr:
        if x == 1:
            i += 1
    I2 = i%2
    return I2

# def zeros_indices(arr, ind):
#     arr1 = []
#     for i, x in enumerate(arr):
#         if x == 0 and i!=ind:
#             arr1.append(i)
#     return arr1

def check_ayler(M, V):
    p = 0
    errors = []
    for m, x in enumerate(M):
        ones = count_ones(x)
        if ones == 0:
            p += 1
        else:
            errors.append(m)
    return p==len(V), errors

def adjacency_matrix(V, E):
    M = []
    for x in range(len(V)):
        arr=[]
        for y in range(len(V)):
            arr.append(0)
        M.append(arr)
    for m in range(len(M)):
        arr = e_indices(E, V[m])
        if arr != []:
            for j in arr:
                ind = V.index(E[j][1])
                if ind != m:
                    M[m][ind], M[ind][m] = 1, 1
    return M


def additional_ones(M, errors):
    for x in itoo.permutations(errors, 2):
        M[x[0]][x[1]] = 1
    return M

def get_path_points(M, ind):
    arr = []
    for x in range(len(M[ind])):
        if M[ind][x] > 0:
            arr.append(x)
    return arr

def ayler_cycle(M, V):
    i = 0
    j = 0
    k = 0
    cycle = []
    cycle.append(V[i])
    while k != len(V):
        arr = get_path_points(M, i)
        for x in arr:
            if V[x] not in cycle:
                z = x
                cycle.append(V[x])
                break
        k += 1
        i = z
    return cycle

# print('Hello Ivan')

V = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8"]

E = [["V1", "V6"], ["V1", "V8"], ["V2", "V6"], ["V2", "V7"], ["V3", "V4"], ["V3", "V5"], ["V3", "V6"], ["V3", "V8"], ["V4", "V5"], ["V4", "V6"], ["V4", "V8"], ["V7", "V8"]]

# E={(1,6),(1,8), (2,6),(2,7),(3,4),(3,5), (3,6),(3,8),(4,5),(4,6),(4,8),(7,8)}


# V=["v1","v2","v3","v4","v5","v6","v7","v8","v9"]
# E=[["v1","v2"],["v1","v7"],["v1","v8"],["v1","v9"],["v2","v3"],["v2","v7"],["v2","v9"],["v3","v4"],["v3","v6"],["v3","v9"],["v4","v5"],["v4","v6"],["v4","v7"],["v5","v6"],["v6","v7"],["v6","v8"],["v6","v9"],["v7","v9"],["v8","v9"]]


M1 = adjacency_matrix(V, E)
for k in M1:
    print(k)
# quit()
bool_ayler, errors = check_ayler(M1, V)
print(bool_ayler)


new_M1 = additional_ones(M1, errors)
for k in new_M1:
    print(k)
bool_ayler1, errors1 = check_ayler(new_M1, V)
print(bool_ayler1)

print(ayler_cycle(new_M1, V))