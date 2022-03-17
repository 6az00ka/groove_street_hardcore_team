def e_indices(E, value):
    arr = []
    for x in range(len(E)):
        if E[x][0] == value:
            arr.append(x)
    return arr

def get_path_points(M, ind):
    arr = []
    for x in range(len(M[ind])):
        if M[ind][x] > 0:
            arr.append(x)
    return arr  

def adjacency_matrix(V, E, I):
    M = []
    for x in range(len(V)):
        arr=[]
        for y in range(len(V)):
            arr.append(0)
        M.append(arr)
    for x in I:
        M[x[0]][x[1]] = 1
    return M                  


def indices_for_matrix(V, E):
    I = []
    for x in E:
        ind1 = V.index(x[0])
        ind2 = V.index(x[1])
        arr1 = [ind1, ind2]
        arr2 = [ind2, ind1]
        if x[2] == "0":
            I.append(arr1)
            I.append(arr2)
        else:
            I.append(arr1)
    return I


def fill_the_paths(M, V, I, N):
    for x in I:
        M[x[0]][x[1]] = (N * ((x[0]**2)+(x[1]**2)) + x[0] + x[1]) % 10
    return M
   

V=["v1","v2","v3","v4","v5","v6","v7","v8","v9"]
E=[["v1","v2","0"],["v1","v7","1"],["v1","v8","0"],["v1","v9","0"],["v2","v3","0"],["v2","v7","0"],["v2","v9","0"],["v3","v4","0"],["v3","v6","0"],["v3","v9","0"],["v4","v5","1"],["v4","v6","1"],["v4","v7","0"],["v5","v6","0"],["v6","v7","0"],["v6","v8","0"],["v6","v9","0"],["v7","v9","0"],["v8","v9","0"]]
N = 3
I1 = indices_for_matrix(V, E)
M1 = adjacency_matrix(V, E, I1)
M2 = fill_the_paths(M1, V, I1, N)
for k in M2:
    print(k)



                
        
        
        





