"""
Вывести в порядке возрастания все простые числа, расположенные между n и m (включая сами числа n и m),
а также количество x этих чисел.
"""
n = int(input("Введите n: \n"))
m = int(input("Введите m: \n"))

i = 0

for item in range(n, m+1):
    print(item)
    if item % 2 == 0:
        i+=1
print("Количество X: ", i)