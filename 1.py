opa = []
for n in range(4):
    n = float(input("Введите элемент массива:"))
    opa.append(n)
start = opa.index(max(opa)) + 1
opa[start:] = [0] * (len(opa) - start)
print(opa)