n = int(input())
i = 1
a = []

while i*i <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1

"""
НОД
"""

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
while b > 0:
    c = a%b
    a = b
    b = c
print(f'Нод={a}')