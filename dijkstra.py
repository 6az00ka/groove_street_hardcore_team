import sys

import os

from PIL import Image

class Vertex:
    def __init__(self):
        self.w = sys.maxsize
        self.done = False
        self.olinks = []
    def __getattr__(self, attr):
        return self[attr]


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
        self.generate_frame(0, self.i_start)
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
            self.generate_frame(z+1, i)
            o = z+1
        www = self.vertexes[self.i_finish].w
        self.generate_last_frame(self.n+1,self.route(),www)
        return www

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
    
    def lookup_pair(self,v,i):
        for link in v.olinks:
            j = link[0]
            if i == j:
                return True
        return False

    def generate_frame(self, iter, current):
        m = {}
        f = open(f'Iter_{iter}.dot', 'w')
        f.write('digraph Iter'+str(iter)+' {\n')
        f.write('label="Iteration = '+str(iter)+'"\n')
        f.write('fontsize=32\n')
        f.write('subgraph'+'{\n')
        f.write('fontsize=14\n')
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
        f.write('}\n}')
        f.close()
        os.system(f'dot -Tpng Iter_{iter}.dot -o Iter_{iter}.png')
        
    def generate_last_frame(self, iter, path, final_weight):
        m = {}
        mp = {}
        j = path[0]
        for i in path[1:]:
            mp[f'{i}:{j}'] = True
            mp[f'{j}:{i}'] = True
            j = i
        f = open(f'Iter_{iter}.dot', 'w')
        search = str(final_weight)
        f.write('digraph Iter'+str(iter)+' {\n')
        f.write('label="Final Weight = '+search+'"\n')
        f.write('fontsize=32\n')
        f.write('subgraph'+'{\n')
        f.write('fontsize=14\n')
        for i, v in enumerate(self.vertexes):
            x = i+1
            wi = v.w if v.w != sys.maxsize else "+INF"
            di = "X" if v.done else "O"
            if i in path:
                bzz = path.index(i)+1
                f.write(f'v{x}[shape=circle,label="V{x}\\n{wi}\\n{di} {bzz}", style=filled, fillcolor=Salmon, color=Red];\n')
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
                    color = ""
                    if f'{i}:{j}' in mp:
                        color = ", color=Red"
                    if self.lookup_pair(self.vertexes[j],i):
                        f.write(f'v{x} -> v{y} [label="{w}", dir=both{color}]\n')
                    else:
                        f.write(f'v{x} -> v{y} [label="{w}"{color}]\n')
        f.write('}\n}')
        f.close()
        os.system(f'dot -Tpng Iter_{iter}.dot -o Iter_{iter}.png')

def parser(V,E):
    links = []
    for (vi, vj, bidir) in E:
        i = V.index(vi)
        j = V.index(vj)
        links.append(Link(i,j,True if bidir == "0" else False))
    return links      

def png_to_gif(V):
    frames = []
    for i in range(len(V)+2):
        new_frame = Image.open(f'Iter_{i}.png')
        frames.append(new_frame)
    frames[0].save('Graph.gif', format='GIF', append_images=frames[1:], save_all=True, duration=1000, loop=0)

V=["v1","v2","v3","v4","v5","v6","v7","v8","v9"]
E=[["v1","v2","0"],
   ["v1","v7","1"],
   ["v1","v8","0"],
   ["v1","v9","0"],
   ["v2","v3","0"],
   ["v2","v7","0"],
   ["v2","v9","0"],
   ["v3","v4","0"],
   ["v3","v6","0"],
   ["v3","v9","0"],
   ["v4","v5","1"],
   ["v4","v6","1"],
   ["v4","v7","0"],
   ["v5","v6","0"],
   ["v6","v7","0"],
   ["v6","v8","0"],
   ["v6","v9","0"],
   ["v7","v9","0"],
   ["v8","v9","0"]]

N = 3

g = Graph(n=9, bias=N, i_start=0, i_finish=3)
g.update_links(parser(V,E))
print(g.search())
print([V[x] for x in g.route()])           
png_to_gif(V)

for i in range(len(V)+1):
    os.remove(f'Iter_{i}.png')
for i in range(len(V)+2):
    os.remove(f'Iter_{i}.dot')
