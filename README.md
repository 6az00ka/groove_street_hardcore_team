# Проект: <<Автоматизированное решение задач по графам» из сборника задач по дискретной математике А.А. Набебина>>

## Описание проекта
Разработка ведётся в рамках дисциплины "Технологии и методы программирования".

## Юнит-тесты по проекту
Папка tests

## Документация по модулям
Папка html

## Стратегия тестирования
https://docs.google.com/spreadsheets/d/1Lyd1x-gOIpEULhIiiwzNQhxN6o_y6Bi-/edit?usp=sharing&ouid=116518513111554135372&rtpof=true&sd=true

## Принцип работы
Запуск алгоритмов происходит через файл gsht.py.<br/>
Файлы task1.py, dijkstra.py, task3.py - подключаемые модули.<br/>
На вход программе подаётся выбранное значение в качестве выбора алгоритма, а также входные данные, передаваемые в тот или иной алгоритм.

## Участники

| Учебная группа | Имя пользователя | ФИО                      |
|----------------|------------------|--------------------------|
| 181-331        | https://github.com/6az00ka       | Белов П.Д.              |
| 181-331        | https://github.com/VanyaWrestling       | Великанов И.В.              | 
| 181-331        | https://github.com/Relatoros      | Максименко С.В.            |
| 181-331        | https://github.com/Makhmadziyoev      | Махмадзиёев А.О.              | 
 

## Личный вклад участников

### Белов П.Д.
Лидер команды, дополнительная ответственность - GIT.<br/>
Задача 2 - поиск кратчайшего пути в графе по алгоритму Дейкстры.<br/>
На вход подаётся значение N.<br/>
Производится расчёт кратчайшего пути, отрисовка в png и визуализация работы всего алгоритма с конкретным графом в gif.

### Великанов И.В.
Дополнительная ответственность - Docker.<br/>
Задача 3 - проверка, является ли граф Эйлеровым, в случае отсутствия признака - дорисовка ребёр.<br/>
Производится расчёт чётности вершин, проверка признака и отрисовка в png.

### Максименко С.В.
Дополнительная ответственность - PDoc.<br/>
Задача 4 - удаление циклических рёбер.

### Махмадзиёев А.О.
Дополнительная ответственность - Тестирование.<br/>
Задача 1 - выделение и рисование элементов графа.<br/>
Производится расчёт соответствующих элементов и отрисовка в png.
