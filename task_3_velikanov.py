"""
# **Задание \"Автоматическая документация кода\" Великанов Иван 181-331** 
"""

from turtle import circle, color
import numpy as np
import itertools as itoo
import networkx as nx
import matplotlib.pyplot as plt

# from pdoc.html_helpers import extract_toc
# extract_toc("Задание \"Автоматическая документация кода\" Великанов Иван 181-331 ")


# Функция, которая запоминает индексы вершин по необходимой вершине
def e_indices(E, value):
    """
    # Функция, которая запоминает индексы вершин по необходимой вершине
    ## Принимает на вход 2 параметра:
       - 1 - E(Множество ребер)
       - 2 - value (Вершина из которой ищутся ребра)
    ## Функция возвращает массив индексов вершин с которыми есть ребра
    """
    arr = []
    for x in range(len(E)):
        if E[x][0] == value:
            arr.append(x)
    return arr

# Функция, которая считает количество едениц в строке в матрице смежности


def count_ones(arr):
    """
    # Функция, которая считает количество едениц в строке в матрице смежности
    ## Принимает на вход 1 параметр:
       - arr - строка матрицы
    ## Функция возвращает остаток от деления на 2 количества единиц в строке матрицы
    """
    i = 0
    for x in arr:
        if x == 1:
            i += 1
    I2 = i % 2
    return I2

# def zeros_indices(arr, ind):
#     arr1 = []
#     for i, x in enumerate(arr):
#         if x == 0 and i!=ind:
#             arr1.append(i)
#     return arr1

# Функция, которая проверяет является ли граф эйлеровым


def check_ayler(M, V):
    """
    # Функция, которая проверяет является ли граф эйлеровым
    ## Функция принимает на вход 2 аргумента:
       - 1 - M (Матрица смежности)
       - 2 - V (МНожество вершин)
    ## Функция возвращает значения:
       - 1 - Bool значение является ли граф эйлеровым
       - 2 - Массив в который записываются индексы вершин с нечетным количеством ребер, если граф эйлеровый то массив вернется пустым
    """
    p = 0
    errors = []
    for m, x in enumerate(M):
        ones = count_ones(x)
        if ones == 0:
            p += 1
        else:
            errors.append(m)
    return p == len(V), errors

# Функция, которая строит матрицу смежности


def adjacency_matrix(V, E):
    """
    # Функция, которая строит матрицу смежности
    ## Функия принимает на вход 2 аргумента:
       - 1 - V (Множество вершин)
       - 2 - E (Множество ребер)
    ## Функция возвращает матрицу смежности
    """
    M = []
    for x in range(len(V)):
        arr = []
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


# Функция, которая достраивает граф до эйлерового
def additional_ones(M, errors):
    """
    # Функция, которая достраивает граф до эйлерового
    ## Функция принимает на вход 2 агрумента:
       - 1 - M (Матрица смежности)
       - 2 - errors (Массив в который записаны индексы вершин с нечетным количеством ребер)
    ## Функция возвращает:
       - Матрицу смежности достроенного графа
    """
    for x in itoo.permutations(errors, 2):
        M[x[0]][x[1]] = 1
    return M

# Функция, которая возвращает индексы вершин в которые можно попасть из вершины индекс которой подается на вход


def get_path_points(M, ind):
    """
    # Функция, которая возвращает индексы вершин в которые можно попасть из вершины индекс которой подается на вход
    ## Функция принимает на вход 2 аргумента:
       - 1 - M (Матрица смежности)
       - 2 - ind (Индекс вершины из которой рассматривается наличие ребер)
    ## Функция возвращает:
       - Массив индексов вершин с которыми есть связь
    """
    arr = []
    for x in range(len(M[ind])):
        if M[ind][x] > 0:
            arr.append(x)
    return arr

# Функция, которая находит эйлеров цикл


def ayler_cycle(M, V):
    """
    # Функция, которая находит эйлеров цикл
    ## Функция принимает на вход 2 аргумента:
       - 1 - M (Матрица смежности)
       - 2 - V (Множество вершин)
    ## Функция возвращает:
       - Массив в котором перечислины вершины в нужном порядке
    """
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


######

# python3 -m pdoc --html . --output-dir html_pdoc/ --force

############

def func_for_draw_ayler_cycle(V):
    """
    # Функция которая прнимает массив вершин, и возвращает двухмерный массив эйлерового цикла [(откуда-куда), (откуда-куда)] (Нужно для рисования)
    """
    ayler_links = []
    for x in range(len(V)-1):
        ayler_links.append((V[x], V[x+1]))

    return ayler_links


def run():

    V = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8"]

    E = [["V1", "V6"], ["V1", "V8"], ["V2", "V6"], ["V2", "V7"], ["V3", "V4"], ["V3", "V5"], [
        "V3", "V6"], ["V3", "V8"], ["V4", "V5"], ["V4", "V6"], ["V4", "V8"], ["V7", "V8"]]

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

    # print(ayler_cycle(new_M1, V))

    ayler_cycle_temp = ayler_cycle(new_M1, V)
    print(ayler_cycle_temp)

    temp = func_for_draw_ayler_cycle(ayler_cycle_temp)
    print(temp)

    # G1 = nx.Graph()
    # G1.add_edges_from(E)
    # nx.draw(G1, with_labels=True)
    # # plt.show()
    # plt.savefig('data/graph.jpg')

    G = nx.Graph()
    G.add_node(temp[0][0], color='g')

    G.add_edges_from(E, color='b')
    # G.remove_edges_from(temp)
    G.add_edges_from(temp, color='r')
    edges = G.edges()

    # массив цветов ребер
    colors = [G[u][v]['color'] for u, v in edges]

    # массив цветов вершин
    color_map = []
    for node in G.nodes():
        if node == temp[0][0]:
            color_map.append('green')
        elif node == temp[len(temp) - 1][1]:
            color_map.append('green')
        else:
            color_map.append('blue')

    # строим граф
    nx.draw(G, with_labels=True, edge_color=colors, node_color=color_map)
    # plt.show()
    plt.savefig('data/ayler_cicle.jpg')

    print("It's OKEY!")

    print("Чтобы скопировать картинку из докера введите эту команду в терминале основной машины")
    print("docker cp container_name:/app/data/ayler_cicle.jpg path_kyda_zakinut")
