#  Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
#  Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Input ypur number N: "))

my_list = {}
for i in range(-n, n+1):
    my_list[i] = i
print(f'my_list = {my_list}')

data = [1, 2, 3]

# Пробовал вывести позиции из файла, на выходе у меня получился список списков. 
# Переводил его в список чисел, а он всё равно не запихивается в  my_list[data[j]], пишет TypeError: unhashable type: 'list'
# data = []
# with open("file.txt") as f:
#     for line in f:
#         data.append([int(x) for x in line.split()])
# flat_1 = [x for l in data for x in l]      
# print(f'data = {flat_1}')

total = 1
for j in range(len(data)):
    total *= my_list[data[j]]
print(f'total = {total}')             
        