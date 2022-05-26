"""
Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры.
"""
n = int(input("Введите n: \n"))
m = int(input("Введите m: \n"))
result = 0
i = 1

for item in range(n, m+1):
    result += item**3
    i += 1
    if i == m:
        print(result)


