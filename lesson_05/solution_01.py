def three_args(a):
    if a is not None:
        print(a)



vars = []
for item in range(3):
    vars = input("Введите число: \n")
    three_args(vars)
