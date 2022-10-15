array = []
c = 0
for n in range(4):
    n = int(input("Введите массив array:"))
    array.append(n)
delta = int(input("Введите значение Delta:"))
min_array = min(array)
c = 0
for i in array:
    if (i - delta) == min_array:
        c += 1
print(c)