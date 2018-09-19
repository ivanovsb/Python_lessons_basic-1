﻿# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random
sp = int(input('введи размер списка: '))
lst = []
for i in range(sp):
    num = random.randint(0,10)
    lst.append(str(num))
new_lst = list(map(lambda a:int(a)**2,lst))
print('Исходный список: ',lst)
print('\nНовый список \nквадрат элементов исходного: ',new_lst)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

lst1 = ['яблоко', 'ананас', 'банан', 'апельсин', 'виноград', 'слива']
lst2 = ['ананас', 'абрикос', 'яблоко', 'черешня', 'арбуз', 'апельсин', 'мандарин']
temp_lst = set(lst2)
new_lst = [x for x in lst1 if x in temp_lst]
print('Список 1', lst1)
print('Список 2', lst2)
print('\nНовый список с общими фруктами:\n', new_lst)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
sp = int(input('введи размер списка: '))
lst = []
for i in range(sp):
    num = random.randint(-100,100)
    lst.append(str(num))
    
new_lst1 = [el for el in lst if ((not (int(el) % 3)) and (int(el) > 0) and (int(el) % 4))]
print('Исходный список: ',lst)
print('\nНовый список: ',new_lst1)
