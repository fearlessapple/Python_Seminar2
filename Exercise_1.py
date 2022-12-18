# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = float(input("Input your number: "))
total = 0
if n < 0:
    n = (-1)*n
while n != int(n):
    n = round(n*10, 5)
while n != 0:
    total += n % 10
    n = n // 10
print(total)    