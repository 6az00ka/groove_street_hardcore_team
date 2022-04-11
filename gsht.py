import sys
import task3
import task1
import dijkstra
import os

print("             .';coxO00KKKK0000Oxdl:,.             \n          .;lxO0KKKKKKKKKK000000KKK0Od:'          \n        'lxOO00000KKKKKKKK0000000KKKKKK0x:.       \n      ,okkkOOOOO000KKKKKKK000000KKKKKKKKXXOc.     \n    .cxxxkkkkkOO000KKKKKKK000000KKKKKKXXXXXXO;    \n   ,oxxxxxxkkkOOOO0KK0OOkkkO00KKKKKKKXXXXXNNNXo.  \n  ;oddddxxxxxkkkkkoc;'.......,cdOKKXXXXNNNNNNNNx. \n ,oddddddddxxxxd;.              .:kXNNNNNNNNNNNNd.\n.loooodddddddd:.                  .cKNNNNNNNNNNNXc\n;oooooooooodo,                      ;0NNNWWWWWWWWO\ncooooooooooo;                        cXWMMMMMMMMMN\nloollollllol.                        '0MMMMMMMMMMM\nlllllllllloc.                        .OMMMMMMMMMMW\nclllllllllll'                         cXMMMMMMMMM0\nclllllllllll'                         cXMMMMMMMMM0\n'clccccccccc:,.                          .;:c:,.  \n.;cccccc:::::;,.                                  \n .;c::::::;;;;,,'..                               \n  .,::::;;;;,,,''''.......   ........             \n    ';;;;;,,,,'''.....................            \n     .',,,,,,''''.......................          \n       ..','''''.........................         \n          ..'''.......................            \n             ......................               \n                 ..............                   ")
print('Программное решение по дисциплине "Технологии и методы программирования"')
print('Выполнили студенты уч.гр. 181-331 Белов Павел, Великанов Иван, Махмадзиёев Али, Максименко Степан')
print('2022')
print('\n\n 1 — Параграф 5 Задача 1 (элементы графов)')
print(' 2 — Параграф 5 Задача 2 (алгоритм Дейкстры)')
print(' 3 — Параграф 5 Задача 3 (Эйлеров граф)')
print(' А не будет 4 задачи, Максименко плюнул на предмет')
print(' 0 — Выход из программы')
number = input('\nВыберите необходимую вам задачу: ')
while number:
    if number == '1' or number == 'Makhmadziyoev':
        # sys.exit()
        task1.main()
        print('\ntask1 - Выполнен успешно\n')
    elif number == '2' or number == 'Belov':
        dijkstra.run(int(input("N = ")))
        print('\ndijkstra - Выполнен успешно\n')
    elif number == '3' or number == 'Velikanov':
        task3.run()
        print('\ntask3 - Выполнен успешно\n')
    elif number == '0' or number == 'exit' or number == 'x':
        print('\n***Burp***!')
        sys.exit()
    else:
        print('\nВведено неверное значение!\nПожалуйста, введите корректный номер для выполнения программы, или 0 - чтобы выйти из программы')
    number = input('\nВыберите необходимую вам задачу: ')
