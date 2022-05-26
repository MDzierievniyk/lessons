"""
Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
"""
import random
i = True
while i == True:
    random_number = random.randint(1,10)
    if random_number != 7:
        print(random_number)
    else:
        print("Выпала 7")
        break




