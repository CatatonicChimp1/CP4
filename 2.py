import numpy
import random
a = int(input("Введите размерность массива A:"))
b = int(input("Введите размерность массива B:"))
A = numpy.random.random_integers(1, 20, a)
B = numpy.random.random_integers(1, 20, b)
for i in A:
    for j in B:
        if i == j:
            print(i)