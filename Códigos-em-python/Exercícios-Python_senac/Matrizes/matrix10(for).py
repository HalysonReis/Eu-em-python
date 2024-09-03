matriz = [
    [3, 4, 5, 6],
    [7, 6, 5, 4],
    [9, 3, 2, 1],
    [1, 2, 3, 4]
]

mult = 1

j = 0

for lin in matriz:
    mult *= lin[j]
    j += 1

print('a multiplicação é ', mult)
