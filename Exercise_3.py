# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('Input your number N: '))
my_list = {}
total = 0
for i in range(1, n+1):
    total += round((1+1/i)**i, 2)
    my_list[i] = round((1+1/i)**i, 2)
print(f'For N = {n} {my_list}')
print(f'Summary = {total}')    