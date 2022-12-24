#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
#  Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = int(input("Input ypur number N: "))

my_list = []
for i in range(n):
    my_list.append(randint(-n, n))
print(f'my_list = {my_list}')

path = 'file.txt'
data = open(path, 'r')
mult = 1
for i in data:
    mult *= my_list[int(i)]
print(mult)                
        