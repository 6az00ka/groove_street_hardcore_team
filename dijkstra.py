import sys

import os

from PIL import Image

"""Алгоритм Дейкстры. Выполнил студент группы 181-331 Белов Павел. Модуль создан ночью 8 апреля 2022 года"""

class Vertex:
    """Класс Вершина"""
    def __init__(self):
        self.w = sys.maxsize
        """Вес пути до вершины от старта. Принимает значение maxsize до тех пор, пока непройдёт итерация в алгоритме по этой вершине."""
        self.done = False
        """Данное значение показывает, рассмотрена ли вершина в процессе работы алгоритма, для того, чтобы избежать бесконечного выполнения алгоритма."""
        self.olinks = []
        """Двумерный массив: множество массивов длиной 2, включающие в себя вершины, с которыми данная вершина связана рёбрами, а также веса ребёр до этих вершин, включены в единый массив."""

class Link:
    """Класс Ребро"""
    def __init__(self, i, j, bdir):
        self.i = i
        """Индекс первой вершины в ребре."""
        self.j = j
        """Индекс второй вершины в ребре."""
        self.bdir = bdir
        """Булевое значение направленности ребра (однонаправленное - False, двунаправленное - True)."""

class Graph:
    """Класс Граф"""
    def __init__(self, n, bias, i_start, i_finish):
        self.vertexes = []
        """Массив объектов класса "Вершина" в графе."""
        self.paths = []
        """Массив (при инициализации содержащий только пометку стартовой вершины), который в начале поиска будет заполнен нулями. В процессе поиска кратчайшего пути в ячейке вершины, входящей в кратчайший путь, записывается номер ячейки связанной вершины."""
        self.unseen = [i for i in range(n)]
        """Массив вершин, не пройденных в процессе работы алгоритма."""
        self.bias = bias
        """Значение N из условия задачи."""
        self.n = n
        """Количество вершин в графе."""
        self.i_start = i_start
        """Индекс вершины, из которой нужно найти кратчайший путь."""
        self.i_finish = i_finish
        """Индекс вершины, в которую нужно найти кратчайший путь."""
        # Заполнение массива вершин и пометка стартовой вершины
        for x in range(n):
            self.vertexes.append(Vertex())
            self.paths.append(i_start)
        self.vertexes[self.i_start].w = 0
        
    
    def min_w(self):
        """Метод, выполняющий поиск ближайшей вершины и веса пути до неё. Возвращает индекс вершины и вес пути до неё."""
        w = sys.maxsize
        x = -1
        for k in self.unseen:
            if self.vertexes[k].w < w:
                w = self.vertexes[k].w
                x = k
        return (x,w)
    
    def search(self):
        """Метод, выполняющий расчёт общего веса кратчайшего пути, который возвращается на выходе."""
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
        """Метод, выстраивающий кратчайший путь из полученных расчётов и заполненного массива paths[] и возвращающий массив индексов вершин кратчайшего пути в порядке от стартовой до конечной вершин."""
        path = []
        i = self.i_finish
        while i != self.i_start:
            path.append(i)
            i = self.paths[i]
        path.append(self.i_start)
        return path[::-1]
     
    def update_links(self, links):
        """Метод, распределяющий данные о вершинах и их связях из массива объектов класса "Ребро", подаваемого на вход, а также рассчитывающий веса рёбер."""
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
        """Метод, проверяющий, есть ли у конкретного объекта класса "Вершина", подаваемого на вход, связь с вершиной, индекс которой подаётся на вход, а также возвращающий True, если связь есть, и False, если связи нет."""
        for link in v.olinks:
            j = link[0]
            if i == j:
                return True
        return False

    def generate_frame(self, iter, current):
        """Метод, производящий рисование состояния графа при помощи модуля GraphViz и конвертации *.dot-файлов в *.png-файлы утилитой dot.exe. На вход подаются номер итерации (0 - состояние графа до работы алгоритма) и индекс вершины, рассматриваемой на данной итерации."""
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
        """Метод, производящий рисование состояния графа после работы алгоритма, аналогично generate_frame, но с выводом общего веса кратчайшего пути сверху, а также закрашиванием вершин, входящих в кратчайший путь."""
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
    """Глобальная функция, производящая множество объектов класса "Ребро" из множеств вершин и ребёр, подаваемых на вход и оформленных в стиле условия из учебника."""
    links = []
    for (vi, vj, bidir) in E:
        i = V.index(vi)
        j = V.index(vj)
        links.append(Link(i,j,True if bidir == "0" else False))
    return links      

def png_to_gif(V):
    """Глобальная функция, производящая конвертацию множества картинок формата png в один файл формата gif с задержкой между кадрами в 1 секунду"""
    frames = []
    for i in range(len(V)+2):
        new_frame = Image.open(f'Iter_{i}.png')
        frames.append(new_frame)
    frames[0].save('Graph.gif', format='GIF', append_images=frames[1:], save_all=True, duration=1000, loop=0)

def run(N):
    """Глобальная функция запуска модуля"""
    #Вершины в стиле условия в учебнике
    V=["v1","v2","v3","v4","v5","v6","v7","v8","v9"]
    #Рёбра в стиле условия в учебнике
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
    g = Graph(n=len(V), bias=N, i_start=0, i_finish=3)
    g.update_links(parser(V,E))
    sss = g.search()
    ppp = [V[x] for x in g.route()]          
    png_to_gif(V)
    #Удаление ненужных dot и png
    for i in range(len(V)+1):
        os.remove(f'Iter_{i}.png')
    for i in range(len(V)+2):
        os.remove(f'Iter_{i}.dot')
    return sss, ppp


