# 4. Получаем от пользователя 2 числа, это длинна и ширина матрицы.

# На вывод даем таблицу из чисел, например при вводе 3 и 5
#### 0 1 2 3 #### 1 1 2 3 #### 2 2 4 6 #### 3 3 6 9 #### 4 4 8 12 ####5 5 10

import numpy

length = int(input('Please enter length of the matrix: '))
width = int(input('Please enter width of the matrix: '))

first = [i for i in range(0, length + 1)]


def gen(x=1, y=1):
    p = 0
    z = 0
    while p <= length:
        yield x
        p += 1
        z += 1
        if z > 1:
            x = x + y


def f():
    x, y = 1, 1
    lst = []
    for i in range(width):
        for j in gen(x, y):
            lst.append(j)
        x += 1
        y += 1
    return lst


split = numpy.array_split(f(), width)
print(first)
for array in split:
    print(list(array))
