import sys

import os

# def e_indices(E, value):
#     arr = []
#     for x in range(len(E)):
#         if E[x][0] == value:
#             arr.append(x)
#     return arr

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
        k0 = x[0] + 1
        k1 = x[1] + 1
        M[x[0]][x[1]] = (N * ((k0**2)+(k1**2)) + k0 + k1) % 10
    return M

class Vertex:
    def __init__(self):
        self.w = sys.maxsize
        self.done = False
        self.olinks = []
    def __getattr__(self, attr):
        return self[attr]
    def __pp__(self):
        print(self.__dict__)


class Link:
    def __init__(self, i, j, bdir):
        self.i = i
        self.j = j
        self.bdir = bdir
    
class Graph:
    def __init__(self, n, bias, i_start, i_finish):
        self.vertexes = []
        self.paths = []
        self.unseen = [i for i in range(n)]
        self.bias = bias
        self.n = n
        self.i_start = i_start
        self.i_finish = i_finish
        for x in range(n):
            self.vertexes.append(Vertex())
            self.paths.append(i_start)
        self.vertexes[self.i_start].w = 0
    def min_w(self):
        w = sys.maxsize
        x = -1
        for k in self.unseen:
            if self.vertexes[k].w < w:
                w = self.vertexes[k].w
                x = k
        return (x,w)
    def search(self):
        self.generate_dot(0, self.i_start)
        # (dtp,) = pydot.graph_from_dot_file('Iter_0.dot')
        # dtp.write_png('Iter_0.dot')
        for z in range(self.n):
            (i,wi) = self.min_w()
            if i<0:
                print("\nNot enough Links\n")
                quit()
            for link in self.vertexes[i].olinks:
                j = link[0]
                if self.vertexes[j].done:
                    continue
                w = link[1]
                new_w = wi+w
                wj = self.vertexes[j].w
                if new_w < wj:
                    self.vertexes[j].w = new_w
                    self.paths[j] = i
            self.vertexes[i].done = True
            self.unseen.remove(i)
            self.generate_dot(z+1, i)
            o = z+1
            # (dtpz,) = pydot.graph_from_dot_file(f'Iter_{o}.dot')
            # dtpz.write_png(f'Iter_{o}.dot')
            # print("\n z = ", z)
            # self.__pp__()
        # print("\n paths = ", self.paths)
        return self.vertexes[self.i_finish].w

    def route(self):
        path = []
        i = self.i_finish
        while i != self.i_start:
            path.append(i)
            i = self.paths[i]
        path.append(self.i_start)
        return path[::-1]
            
    def update_links(self, links):
        for link in links:
            k0 = link.i + 1
            k1 = link.j + 1
            w = (self.bias * ((k0**2)+(k1**2)) + k0 + k1) % 10
            v = self.vertexes[link.i]
            v.olinks.append((link.j, w))
            if link.bdir == True:
                v = self.vertexes[link.j]
                v.olinks.append((link.i, w))
    def __pp__(self):
        print(self.unseen)
        for v in self.vertexes:
            v.__pp__()
    
    def lookup_pair(self,v,i):
        for link in v.olinks:
            j = link[0]
            if i == j:
                return True
        return False

    def generate_dot(self, iter, current):
        m = {}
        f = open(f'Iter_{iter}.dot', 'w')
        f.write('digraph Iter'+str(iter)+' {\n')
        if 
        for i, v in enumerate(self.vertexes):
            x = i+1
            wi = v.w if v.w != sys.maxsize else "+INF"
            di = "X" if v.done else "O"
            if i == current:
                f.write(f'v{x}[shape=circle,label="V{x}\\n{wi}\\n{di}", color=Red];\n')
            else:
                f.write(f'v{x}[shape=circle,label="V{x}\\n{wi}\\n{di}"];\n')
        for i, v in enumerate(self.vertexes):
            x = i+1
            for link in v.olinks:
                j = link[0]
                w = link[1]
                y = j+1
                if f'{i}:{j}' not in m:
                    m[f'{i}:{j}'] = True
                    m[f'{j}:{i}'] = True
                    if self.lookup_pair(self.vertexes[j],i):
                        f.write(f'v{x} -> v{y} [label="{w}", dir=both]\n')
                    else:
                        f.write(f'v{x} -> v{y} [label="{w}"]\n')
        f.write('}')
        f.close()
        os.system(f'dot.exe -Tpng Iter_{iter}.dot -o Iter_{iter}.png')

def pretty_print(clas, indent=0):
    print(' ' * indent +  type(clas).__name__ +  ':')
    indent += 4
    for k,v in clas.__dict__.items():
        if '__dict__' in dir(v):
            pretty_print(v,indent)
        else:
            print(' ' * indent +  k + ': ' + str(v))

V=["v1","v2","v3","v4","v5","v6","v7","v8","v9"]
E=[["v1","v2","0"],["v1","v7","1"],["v1","v8","0"],["v1","v9","0"],["v2","v3","0"],["v2","v7","0"],["v2","v9","0"],["v3","v4","0"],["v3","v6","0"],["v3","v9","0"],["v4","v5","1"],["v4","v6","1"],["v4","v7","0"],["v5","v6","0"],["v6","v7","0"],["v6","v8","0"],["v6","v9","0"],["v7","v9","0"],["v8","v9","0"]]
N = 3
# dijkstra_map={}
# I1 = indices_for_matrix(V, E)
# M1 = adjacency_matrix(V, E, I1)
# M2 = fill_the_paths(M1, V, I1, N)
# for k in M2:
#     print(k)

def parser(V,E):
    links = []
    for (vi, vj, bidir) in E:
        i = V.index(vi)
        j = V.index(vj)
        links.append(Link(i,j,True if bidir == "0" else False))
    return links      


g = Graph(n=9, bias=N, i_start=0, i_finish=3)
# g.update_links([Link(0,1,True),Link(1,7,False)])
g.update_links(parser(V,E))
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(g.vertexes)
print(g.search())
print([V[x] for x in g.route()])                
        
        
        





