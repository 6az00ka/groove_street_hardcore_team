# Задача №1 из темы "ГРАФЫ"

# Импорты необходимых библиотек
import numpy as np
import matplotlib as plt
from IPython.display import Image
from graphviz import Digraph
import pydot
import os
import random
import copy

def fill_array_incedent(arrayIncedent, numV, count):
    for i in range(0,numV):
        for j in range(0,numV):
            if arraySmejnost[i][j] == 1:
                arrayIncedent[i][count] = 1
                arrayIncedent[j][count] = 1
                count+=1
    return(arrayIncedent)

def fill_array_smejnost(arraySmejnost, numV):
    for i in range(0,numV):
        for j in range(0,numV):
            if arraySmejnost[i][j] == 1:
                arraySmejnost[j][i] = 1
    return(arraySmejnost)

def route_array(route, numV):
    for i in range(0,numV):
        for j in range(0,numV):
            if route[i][j] == 1:
                route[j][i] = 1        
    return(route)

def route_graph_array(route, routeGraph, count, max, numV):
    i=0
    j=0
    while count < max:
        while i< numV:
            while j < numV:
                if count == max:
                        i=numV+1
                        j=numV+1
                elif route[i][j] == 1:
                    routeGraph[0][count] = i+1
                    routeGraph[1][count] = j+1
                    i=j
                    j=random.randint(0, numV-1)
                    count+=1
                elif (i == numV-1 and j == numV-1 and route[numV-1][numV-1] == 0):
                    count = max
                else:
                    j+=1
    #                 print('j: ',i)
            i+=1
    #         print('i: ',i)
    return(routeGraph)

def chain_array(chain, numV):
    for i in range(0,numV):
        for j in range(0,numV):
            if chain[i][j] == 1:
                chain[j][i] = 1
    return(chain)

def chain_graph_array(chain, chainGraph, max, numV):
    i=0
    j=0
    count=0 # Счетчик для выполнения цикла по поиску цепи
    count1=0 # Счетчик для проверки строки массива на контрастные значения

    while count < max:

        while i < numV:

            while j < numV:

                # Проверка счетчика на максимальное значение, если соответствует - выход из цикла

                if count == max:    
                    i=numV+1
                    j=numV+1

                # Проверка на наличие ребра

                elif chain[i][j] == 1:
                    chainGraph[0][count] = i+1 # Запись начальной точки ребра в массив
                    chainGraph[1][count] = j+1 # Запись конечной точки ребра в массив
                    chain[i][j]=-1 # Заполнение используемых ребер контрастными значениями
                    chain[j][i]=-1 # Заполнение используемых ребер контрастными значениями
                    i=j # Переход к конечной точке ребра
                    j=random.randint(0, numV-1) # Генерация случайного значения j для оптимального построения цепи
                    count+=1 # Перевод счетчика на +1

                # Проверка на контрастные значения

                elif chain[i][j] == -1:
                    for z in range(0,numV-1): # Цикл для проверки всей строки массива
                        if chain[i][z] == -1 or chain[i][z] == 0: # Если значения контрастные, то к счетчику прибавляется 1, когда счетчик достигнет максимального значения, общий цикл завершится
                            count1+=1 # Перевод счетчика на +1
                            if count1 >= numV-1: # Проверка счетчика на максимальное значение
                                count = max
                    count1=0 # Обнуление счетчика в случае неудачи цикла
                    j+=1 # Перевод счетчика j на +1
                    if j>=numV-1: # Если j >= максимальному значению, он обнуляется
                        j=0 # Обнуление j

    #             elif (i == numV-1 and j == numV-1 and route[numV-1][numV-1] == 0):
    #                 count = max

                else:
                    if j>=numV-1:
                        j=0
                    else:
                        j+=1
            i+=1
        count = max
        return(chainGraph)
    
def simple_chain_array(simpleChain):
    for i in range(0,numV):
        for j in range(0,numV):
            if simpleChain[i][j] == 1:
                simpleChain[j][i] = 1       
    return(simpleChain)

def simple_chain_graph_array(simpleChain, simpleChainGraph, max, numV):
    i=0
    j=random.randint(0, numV-1)
    count=0 # Счетчик для выполнения цикла по поиску цепи
    count1=0 # Счетчик для проверки строки массива на контрастные значения

    while count < max:

        while i < numV:

            while j < numV:

                # Проверка счетчика на максимальное значение, если соответствует - выход из цикла

                if count == max:    
                    i=numV+1
                    j=numV+1

                # Проверка на наличие ребра

                elif simpleChain[i][j] == 1:
                    simpleChainGraph[0][count] = i+1 # Запись начальной точки ребра в массив
                    simpleChainGraph[1][count] = j+1 # Запись конечной точки ребра в массив
                    for z in range(0,numV-1):
                        simpleChain[i][z] = 0 # Заполнение всех остальных путей из вершины нулями, т.к. ими больше нельзя пользоваться
                        simpleChain[z][i] = 0
                    simpleChain[i][j]=-1
                    simpleChain[j][i]=-1
                    i=j # Переход к новой вершине
                    j=random.randint(0, numV-1) # Генерация случайного значения j для оптимального построения цепи
                    count+=1 # Перевод счетчика на +1

                # Проверка на контрастные значения

                elif simpleChain[i][j] == -1:
                    for z in range(0,numV-1): # Цикл для проверки всей строки массива
                        if simpleChain[i][z] == -1 or simpleChain[i][z] == 0: # Если значения контрастные, то к счетчику прибавляется 1, когда счетчик достигнет максимального значения, общий цикл завершится
                            count1+=1 # Перевод счетчика на +1
                            if count1 >= numV-1: # Проверка счетчика на максимальное значение
                                count = max
                    count1=0 # Обнуление счетчика в случае неудачи цикла
                    j+=1 # Перевод счетчика j на +1
                    if j>=numV-1: # Если j >= максимальному значению, он обнуляется
                        j=0 # Обнуление j

    #             elif (i == numV-1 and j == numV-1 and route[numV-1][numV-1] == 0):
    #                 count = max

                else:
                    if j>=numV-1:
                        j=0
                    else:
                        j+=1
            i+=1
        count = max
        return(simpleChainGraph)
    
def oriented_smejnost_array(orientedArraySmejnost):
    for i in range(0,numV):
        for j in range(0,numV):
            if orientedArraySmejnost[i][j] == 1:
                orientedArraySmejnost[j][i] = 0
    return(orientedArraySmejnost)

def oriented_incedent_array(orientedArrayIncedent):
    count=0 # Счётчик, необходимый для передвижения по столбцам матрицы
    for i in range(0,numV):
        for j in range(0,numV):
            if orientedArraySmejnost[i][j] == 1:
                orientedArrayIncedent[i][count] = 1
                orientedArrayIncedent[j][count] = 1
                count+=1
    return(orientedArrayIncedent)


def oriented_route_graph_array(orientedRoute, orientedRouteGraph, max, numV):
    i=0
    j=random.randint(0, numV-1)
    count=0 

    while count < max:
        while i< numV:
            while j < numV:
                if count == max:
                        i=numV+1
                        j=numV+1
                elif orientedRoute[i][j] == 1:
                    orientedRouteGraph[0][count] = i+1
                    orientedRouteGraph[1][count] = j+1
                    i=j
                    j=random.randint(0, numV-1)
                    count+=1
    #                 print('i: ',i)
    #                 print('j: ',i)
                elif (i == numV-1 and j == numV-1 and orientedRoute[numV-1][numV-1] == 0):
                    count = max
                else:
                    j+=1
    #                 count+=1
    #                 print('j: ',i)
            i+=1
    #         print('i: ',i)
    return(orientedRouteGraph)

def oriented_way_graph_array(orientedWay, orientedWayGraph, max, numV):
    count=0
    i=0
    j=random.randint(0, numV-1)
    while count < max:
        while i< numV:
            while j < numV:
                if count == max:
                        i=numV+1
                        j=numV+1
                elif orientedWay[i][j] == 1:
                    orientedWayGraph[0][count] = i+1
                    orientedWayGraph[1][count] = j+1
                    i=j
                    j=random.randint(0, numV-1)
                    count+=1
                elif (i == numV-1 and j == numV-1 and orientedWay[numV-1][numV-1] == 0):
                    count = max

                else:
                    j+=1

            i+=1
    return(orientedWayGraph)


def oriented_simple_way_graph_array(orientedSimpleWay, orientedSimpleWayGraph, max, numV):
    i=0
    j=random.randint(0,numV-1)
    count=0 # Счетчик для выполнения цикла по поиску простого пути
    count1=0 # Счетчик для проверки строки массива на контрастные значения

    while count < max:

        while i < numV:

            while j < numV:

                # Проверка счетчика на максимальное значение, если соответствует - выход из цикла

                if count == max:    
                    i=numV+1
                    j=numV+1

                # Проверка на наличие ребра

                elif orientedSimpleWay[i][j] == 1:
                    orientedSimpleWayGraph[0][count] = i+1 # Запись начальной точки ребра в массив
                    orientedSimpleWayGraph[1][count] = j+1 # Запись конечной точки ребра в массив
                    orientedSimpleWay[i][j]=-1 # Заполнение используемых ребер контрастными значениями
                    orientedSimpleWay[j][i]=-1 # Заполнение используемых ребер контрастными значениями
                    i=j # Переход к конечной точке ребра
                    j=random.randint(0, numV-1) # Генерация случайного значения j для оптимального построения цепи
                    count+=1 # Перевод счетчика на +1

                # Проверка на контрастные значения

                elif orientedSimpleWay[i][j] == -1:
                    for z in range(0,numV-1): # Цикл для проверки всей строки массива
                        if orientedSimpleWay[i][z] == -1 or orientedSimpleWay[i][z] == 0: # Если значения контрастные, то к счетчику прибавляется 1, когда счетчик достигнет максимального значения, общий цикл завершится
                            count1+=1 # Перевод счетчика на +1
                            if count1 >= numV-1: # Проверка счетчика на максимальное значение
                                count = max
                    count1=0 # Обнуление счетчика в случае неудачи цикла
                    j+=1 # Перевод счетчика j на +1
                    if j>=numV-1: # Если j >= максимальному значению, он обнуляется
                        j=0 # Обнуление j

    #             elif (i == numV-1 and j == numV-1 and route[numV-1][numV-1] == 0):
    #                 count = max

                else:
                    if j>=numV-1:
                        j=0
                    else:
                        j+=1
            i+=1
        count = max
    return(orientedSimpleWayGraph)

# Заполнение важных переменных для составления графа
inp=1 # Точка выхода с цикла заполнения ребрами
numE=0 # Подсчёт количества рёбер
# Ввод количества вершин для определения размерности массива
# numV=int(input('Введите количество вершин: '))
# numV

# # Заполнение матрицы ребрами, подсчёт количества рёбер.
# while inp == 1:
#     i=int(input('Введите 1 вершину: '))
#     j=int(input('Введите 2 вершину: '))
#     arraySmejnost[i-1][j-1]=1
#     inp=int(input('Хотите добавить еще ребро? 1-да, 0 - нет:  '))
#     numE+=1
# for i in range(0,numV):
#     for j in range(0,numV):
#         if arraySmejnost[i][j] == 1:
#             arraySmejnost[j][i] = 1
# arraySmejnost
# # numE

# *****ТЕСТОВЫЕ ЗНАЧЕНИЯ ВАРИАНТ 1.1*****


numV=6
numE=12
arraySmejnost=np.zeros(numV*numV, int).reshape(numV,numV)
arraySmejnost[0][1]=1
arraySmejnost[0][2]=1
arraySmejnost[0][4]=1
arraySmejnost[0][5]=1
arraySmejnost[1][2]=1
arraySmejnost[1][3]=1
arraySmejnost[1][5]=1
arraySmejnost[2][3]=1
arraySmejnost[2][4]=1
arraySmejnost[3][4]=1
arraySmejnost[3][5]=1
arraySmejnost[4][5]=1


# *****КОНЕЦ ТЕСТОВЫХ ЗНАЧЕНИЙ*****

# Создание нулевого массива для матрицы смежности
# arraySmejnost=np.zeros(numV*numV, int).reshape(numV,numV)
# print('Вывод нулевой неориентированной матрицы смежности: ')
# arraySmejnost

# Создание нулевого массива для матрицы инцедентности
arrayIncedent=np.zeros(numV*numE, int).reshape(numV,numE)
print('Вывод нулевой матрицы инцидентности: ')
print(arrayIncedent)

# Заполнение матрицы инцедентности
count=0 # Счётчик, необходимый для передвижения по столбцам матрицы

fill_array_incedent(arrayIncedent, numV, count)
print('Вывод неориентированной матрицы инцидентности: ')            
print(arrayIncedent)

# Заполнение матрицы смежности

fill_array_smejnost(arraySmejnost, numV)
print('Вывод неориентированной матрицы смежности: ')
print(arraySmejnost)

# Отрисовка неориентированного графа

nonOrientedGraph = Digraph(comment="Неориентированный граф'")

# Создание вершин графа
for i in range(0,numV):
    nonOrientedGraph.node(f'{i+1}',f'{i+1}')

# Создание массива под неориентированный граф
graphArraySmejnost=copy.deepcopy(arraySmejnost)

# Запись ребер по матрице смежности
for i in range(0,numV):
    for j in range(0,numV):
            if graphArraySmejnost[i][j] != 0:
                nonOrientedGraph.edge(f'{i+1}',f'{j+1}', arrowhead='none')
                graphArraySmejnost[j][i]=0
                
# Сохранение неориентированного графа
nonOrientedGraph.save('nonOrientedGraph.dot', None)
(nonOrientedGraph,) = pydot.graph_from_dot_file('nonOrientedGraph.dot')
nonOrientedGraph.write_png('nonOrientedGraph.png')
# display(Image(filename='nonOrientedGraph.png'))
os.remove('nonOrientedGraph.dot')


# Маршрут для неориентированного графа

route=copy.deepcopy(arraySmejnost)

route_array(route, numV)            


max=int(input('Введите размер маршрута: '))
routeGraph=np.zeros(2*max, int).reshape(2,max)
count=0

route_graph_array(route, routeGraph, count, max, numV)
print('Получившийся маршрут для неориентированного графа: ')         
print(routeGraph)

# Цепь для неориентированного графа 
# Цепь - маршрут без повторяющихся рёбер

chain=copy.deepcopy(arraySmejnost)
# print('ВЫВОД СКОПИРОВАННОЙ МАТРИЦЫ: ')
# print(chain)
chain_array(chain, numV)
# print('ВЫВОД СКОПИРОВАННОЙ МАТРИЦЫ ПОСЛЕ ПРЕОБРАЗОВАНИЯ: ')
# print(chain)
chainGraph=np.zeros(2*max, int).reshape(2,max)

chain_graph_array(chain, chainGraph, max, numV)
print('Получившаяся цепь: ')
print(chainGraph)
# print('ВЫВОД СКОПИРОВАННОЙ МАТРИЦЫ ПОСЛЕ ПРЕОБРАЗОВАНИЯ: ')
# print(chain)

# Простая цепь для неориентированного графа
# Простая цепь - цепь, в которой не повторяются вершины

simpleChain=copy.deepcopy(arraySmejnost)
simple_chain_array(simpleChain)
            

max=int(input('Введите размер простой цепи: '))
simpleChainGraph=np.zeros(2*max, int).reshape(2,max)

simple_chain_graph_array(simpleChain, simpleChainGraph, max, numV)
print('Получившаяся простая цепь: ')
print(simpleChainGraph)


# Цикл для неориентированного графа

cycle=copy.deepcopy(arrayIncedent)




# Простой цикл для неориентированного графа

simpleCycle=copy.deepcopy(arrayIncedent)


# Преобразование неориентированной матрицы смежности в ориентированную
orientedArraySmejnost=copy.deepcopy(arraySmejnost)
oriented_smejnost_array(orientedArraySmejnost)
            
print('Вывод ориентированной матрицы смежности: ')
orientedArraySmejnost

# Создание ориентированной матрицы инцедентности
orientedArrayIncedent=np.zeros(numV*numE, int).reshape(numV,numE)
oriented_incedent_array(orientedArrayIncedent)

print('Вывод ориентированной матрицы инцидентности: ')
orientedArrayIncedent

#Отрисовка ориентированного графа

orientedGraph= Digraph(comment="Ориентированный граф'")

# Создание вершин ориентированного графа
for i in range(0,numV):
    orientedGraph.node(f'{i+1}',f'{i+1}')

# Запись ребер по матрице смежности
for i in range(0,numV):
    for j in range(0,numV):
            if orientedArraySmejnost[i][j] != 0:
                orientedGraph.edge(f'{i+1}',f'{j+1}')

# Сохранение ориентированного графа
orientedGraph.save('orientedGraph.dot', None)
(orientedGraph,) = pydot.graph_from_dot_file('orientedGraph.dot')
orientedGraph.write_png('orientedGraph.png')
os.remove('orientedGraph.dot')
# display(Image(filename='orientedGraph.png'))

# Ориентированный маршрут для ориентированного графа

orientedRoute=copy.deepcopy(orientedArraySmejnost)

max=int(input('Введите размер ориентированного маршрута: '))
orientedRouteGraph=np.zeros(2*max, int).reshape(2,max)

oriented_route_graph_array(orientedRoute, orientedRouteGraph, max, numV)
print('Маршрут в ориентированном графе: ')
print (orientedRouteGraph)

# Путь для ориентированного графа

orientedWay=copy.deepcopy(orientedArraySmejnost)


max=int(input('Введите размер пути: '))
orientedWayGraph=np.zeros(2*max, int).reshape(2,max)
oriented_way_graph_array(orientedWay, orientedWayGraph, max, numV)

print('Путь в ориентированном графе: ')
print (orientedWayGraph)

# Простой путь для ориентированного графа

orientedSimpleWay=copy.deepcopy(orientedArraySmejnost)

max=int(input('Введите размер пути: '))
orientedSimpleWayGraph=np.zeros(2*max, int).reshape(2,max)
oriented_simple_way_graph_array(orientedSimpleWay, orientedSimpleWayGraph, max, numV)
    
    
print('Путь в ориентированном графе: ')
print (orientedSimpleWayGraph)

# Контур для ориентированного графа
# Контур - это путь, у которого совпадает начальная и конечная вершины
# !!!!!! СРАВНЕНИЕ КОНЕЧНОЙ ТОЧКИ С НАЧАЛЬНОЙ !!!!!!!!!



# Простой контур для ориентированного графа
# Простой контур - это простой путь, у которого совпадают начальные и конечные вершины




